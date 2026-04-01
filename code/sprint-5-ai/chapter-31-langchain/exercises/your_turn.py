"""
Chapter 31: LangChain — YOUR TURN!
=====================================

Build a PDF Q&A Bot! (Well, text file Q&A bot — same concept.)

The idea: You have a document. You want to ask questions about it
and get answers based ONLY on what's in the document.

This is RAG (Retrieval Augmented Generation) in action:
  1. Load the document
  2. Split it into chunks
  3. Embed the chunks into vectors
  4. Store in a vector database
  5. Query: find relevant chunks, send to LLM with context

REQUIREMENTS:
  pip install langchain langchain-openai chromadb
  Set OPENAI_API_KEY environment variable

TASKS:
1. Load the sample document (provided below as a string)
2. Split it into chunks using RecursiveCharacterTextSplitter
3. Create embeddings and store in Chroma
4. Build a RAG chain
5. Ask questions and get answers from the document!
"""

import os

# --- SAMPLE DOCUMENT ---
# In real life, you'd load this from a PDF or text file.
# We're using a string for simplicity.
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

# TODO 1: Import required LangChain components
# from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain_openai import ChatOpenAI, OpenAIEmbeddings
# from langchain_community.vectorstores import Chroma
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.output_parsers import StrOutputParser


# TODO 2: Split the document into chunks
# Hint: RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=50)
# chunks = splitter.split_text(DOCUMENT)


# TODO 3: Create embeddings and store in Chroma
# Hint: embeddings = OpenAIEmbeddings(api_key=os.getenv("OPENAI_API_KEY"))
#        vectorstore = Chroma.from_texts(texts=chunks, embedding=embeddings)


# TODO 4: Create the RAG chain
# Steps:
#   a. Create a retriever: vectorstore.as_retriever(search_kwargs={"k": 2})
#   b. Create a prompt that includes context + question
#   c. Create a chain: prompt | llm | StrOutputParser()


# TODO 5: Ask questions!
questions = [
    "How many PTO days do new employees get?",
    "What is the dress code policy?",
    "How long is parental leave for primary caregivers?",
    "What's the 401k match?",
    "Can I work from home?",
]

# For each question:
#   1. Retrieve relevant chunks
#   2. Format them as context
#   3. Run the chain
#   4. Print the answer


# TODO 6 (BONUS): Add a loop where the user can ask their own questions
# while True:
#     question = input("Ask about the handbook: ")
#     if question.lower() in ("quit", "exit"): break
#     ...
