"""
Chapter 31: LangChain — SOLUTION
==================================

You just built a document Q&A bot with RAG! This is the same
technology behind enterprise AI assistants that can answer
questions about company documents, codebases, and knowledge bases.

You're officially building production-level AI stuff!
"""

import os
import sys

# --- Check requirements ---
MISSING = []
try:
    from langchain.text_splitter import RecursiveCharacterTextSplitter
except ImportError:
    MISSING.append("langchain")

try:
    from langchain_openai import ChatOpenAI, OpenAIEmbeddings
except ImportError:
    MISSING.append("langchain-openai")

try:
    from langchain_community.vectorstores import Chroma
except ImportError:
    try:
        from langchain.vectorstores import Chroma
    except ImportError:
        MISSING.append("chromadb langchain-community")

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

if MISSING:
    print(f"Missing packages: {', '.join(MISSING)}")
    print(f"Run: pip install {' '.join(MISSING)}")
    sys.exit(1)

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    print("OPENAI_API_KEY not set!")
    print("Set it with: export OPENAI_API_KEY=sk-your-key-here")
    print("\nRunning in demo mode with simulated answers.\n")
    DEMO_MODE = True
else:
    DEMO_MODE = False

# --- SAMPLE DOCUMENT ---
DOCUMENT = """
TechCorp Employee Handbook (2024 Edition)

Section 1: Working Hours
All employees are expected to work 40 hours per week. Core hours are
9:00 AM to 3:00 PM, Monday through Friday. Outside of core hours,
employees may choose their own schedule (flex time). Remote work is
allowed up to 3 days per week with manager approval.

Section 2: Paid Time Off (PTO)
New employees receive 15 days of PTO per year. After 3 years, this
increases to 20 days. After 7 years, employees receive 25 days.
PTO requests must be submitted at least 2 weeks in advance.
Unused PTO can be carried over (up to 5 days) to the next year.

Section 3: Benefits
All full-time employees receive health insurance (medical, dental,
and vision), a 401(k) with 4% company match, and a $500 annual
wellness stipend. Part-time employees receive prorated benefits.
The company also offers a $2,000 annual education reimbursement
for job-related courses and certifications.

Section 4: Code of Conduct
Employees must maintain professional behavior at all times. This
includes respectful communication, appropriate dress code (business
casual in office, casual on Fridays), and maintaining confidentiality
of company information. Violations may result in disciplinary action.

Section 5: Performance Reviews
Performance reviews are conducted twice a year (January and July).
Reviews include self-assessment, peer feedback, and manager evaluation.
Promotions are based on performance, not tenure. Bonus eligibility
is determined by individual and team performance metrics.

Section 6: Parental Leave
Primary caregivers receive 16 weeks of paid parental leave.
Secondary caregivers receive 6 weeks of paid parental leave.
Leave must be taken within 12 months of the birth or adoption.
Employees may request additional unpaid leave up to 6 months.

Section 7: Technology Policy
Employees receive a company laptop and phone. Personal use of
company devices is allowed within reason. All company data must
be stored on approved cloud services (not personal devices).
Two-factor authentication is required for all company accounts.
"""


print("=" * 60)
print("  TechCorp Handbook Q&A Bot (RAG)")
print("=" * 60)
print()


# STEP 1: Split the document into chunks
print("Step 1: Splitting document into chunks...")
splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,       # ~300 chars per chunk
    chunk_overlap=50,     # 50 char overlap for context continuity
    separators=["\n\n", "\n", ". ", " "]
)
chunks = splitter.split_text(DOCUMENT)
print(f"  Created {len(chunks)} chunks from the document.")
print()


if not DEMO_MODE:
    # STEP 2: Create embeddings and store in Chroma
    print("Step 2: Creating embeddings and storing in vector DB...")
    embeddings = OpenAIEmbeddings(api_key=api_key)
    vectorstore = Chroma.from_texts(texts=chunks, embedding=embeddings)
    retriever = vectorstore.as_retriever(search_kwargs={"k": 2})
    print("  Vector database ready!")
    print()

    # STEP 3: Create the LLM and RAG chain
    print("Step 3: Setting up RAG chain...")
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.2, api_key=api_key)

    rag_prompt = ChatPromptTemplate.from_messages([
        ("system",
         "You are an HR assistant for TechCorp. Answer questions based ONLY "
         "on the following context from the employee handbook. Be helpful, "
         "specific, and quote relevant details. If the context doesn't contain "
         "the answer, say 'I couldn't find that in the handbook.'\n\n"
         "Context:\n{context}"),
        ("user", "{question}"),
    ])

    chain = rag_prompt | llm | StrOutputParser()
    print("  RAG chain ready!")
    print()

    def ask(question):
        """Ask a question about the handbook."""
        relevant_docs = retriever.invoke(question)
        context = "\n\n".join(doc.page_content for doc in relevant_docs)
        answer = chain.invoke({"context": context, "question": question})
        return answer, relevant_docs

else:
    # Demo mode — simulated answers
    DEMO_ANSWERS = {
        "How many PTO days do new employees get?":
            "New employees receive 15 days of PTO per year. After 3 years it "
            "increases to 20 days, and after 7 years to 25 days.",
        "What is the dress code policy?":
            "The dress code is business casual in the office, with casual "
            "dress allowed on Fridays.",
        "How long is parental leave for primary caregivers?":
            "Primary caregivers receive 16 weeks of paid parental leave. "
            "Leave must be taken within 12 months of birth or adoption.",
        "What's the 401k match?":
            "The company offers a 401(k) with a 4% company match.",
        "Can I work from home?":
            "Remote work is allowed up to 3 days per week with manager approval.",
    }

    def ask(question):
        for key, answer in DEMO_ANSWERS.items():
            if any(word in question.lower() for word in key.lower().split()):
                return answer, []
        return "I couldn't find that in the handbook.", []


# STEP 4: Ask questions!
print("=" * 60)
print("ASKING QUESTIONS")
print("=" * 60)

questions = [
    "How many PTO days do new employees get?",
    "What is the dress code policy?",
    "How long is parental leave for primary caregivers?",
    "What's the 401k match?",
    "Can I work from home?",
]

for question in questions:
    answer, docs = ask(question)
    print(f"\nQ: {question}")
    print(f"A: {answer}")
    if docs:
        print(f"   (Based on {len(docs)} relevant chunks)")

print()


# STEP 5 (BONUS): Interactive mode
print("=" * 60)
print("INTERACTIVE MODE")
print("=" * 60)
print("Ask your own questions! Type 'quit' to exit.")
print()

while True:
    try:
        user_question = input("Your question: ").strip()
    except (KeyboardInterrupt, EOFError):
        print("\nGoodbye!")
        break

    if not user_question:
        continue
    if user_question.lower() in ("quit", "exit", "q"):
        print("Goodbye! Check the handbook for more details!")
        break

    answer, docs = ask(user_question)
    print(f"\nAnswer: {answer}\n")

# Cleanup
if not DEMO_MODE:
    vectorstore.delete_collection()
    print("(Vector database cleaned up.)")
