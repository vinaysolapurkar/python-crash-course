# Chapter 31: LangChain & AI Agents: The Next Level

> **Sprint 5, Chapter 31** | **12 min read** | **Code: [github link](https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/sprint-5-ai/chapter-31-langchain/)**

If the OpenAI API is a smart employee, LangChain is the project manager that organizes their work, gives them memory, and lets them use tools. In Chapter 30, you learned to have a conversation with an AI. In this chapter, you'll learn to give that AI access to your own data, remember past conversations, and chain multiple steps together. This is what companies are building RIGHT NOW.

## What You'll Learn
- What LangChain is and why it exists
- ChatOpenAI setup
- PromptTemplates -- reusable instructions
- Chains -- connecting the dots
- Memory -- AI that remembers
- RAG: letting AI read YOUR documents
- Embeddings, vector stores, and retrieval chains

## Why Should I Care?

Open ChatGPT right now and ask it about your company's internal docs. It can't answer. Ask it about a PDF you downloaded yesterday. It can't read it. Ask it what you talked about last Tuesday. It doesn't remember.

RAG (Retrieval-Augmented Generation) fixes all of this. It lets AI read your documents and answer questions about them. AI agents can use tools, browse the web, and take actions. Chatbots with memory can have real conversations across sessions.

This is the bleeding edge, and it's shockingly accessible. Let's dive in.

## Installing LangChain

```bash
pip install langchain langchain-openai langchain-community chromadb
```

That's a few packages:
- `langchain` -- the core framework
- `langchain-openai` -- OpenAI integration
- `langchain-community` -- community integrations (document loaders, etc.)
- `chromadb` -- a vector database (more on this soon)

## ChatOpenAI: LangChain's Way of Talking to OpenAI

```python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

response = llm.invoke("What's the capital of France?")
print(response.content)
# "The capital of France is Paris."
```

Looks similar to the raw OpenAI API, right? The magic comes when you start combining things.

## PromptTemplates: Reusable Instructions

Instead of writing the same prompt structure over and over, templates let you create reusable patterns:

```python
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

# Create a template with variables
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert {role}. Explain concepts for a {audience} audience."),
    ("user", "{question}")
])

# Use it with different inputs
chain = prompt | llm  # The | operator connects prompt to LLM

# Python tutor mode
response = chain.invoke({
    "role": "Python tutor",
    "audience": "beginner",
    "question": "What are list comprehensions?"
})
print(response.content)

# Data scientist mode (same template, different variables)
response = chain.invoke({
    "role": "data scientist",
    "audience": "technical",
    "question": "What are list comprehensions?"
})
print(response.content)
```

One template, multiple uses. The `|` operator (called "pipe") connects components together. Prompt goes in, gets filled with your variables, gets sent to the LLM, and the response comes out. Like a pipeline. Like piping water through connected pipes.

### More Template Examples

```python
# Email writer
email_prompt = ChatPromptTemplate.from_messages([
    ("system", "You write professional but friendly emails. Keep them under 100 words."),
    ("user", "Write an email to {recipient} about {topic}. Tone: {tone}.")
])

email_chain = email_prompt | llm

response = email_chain.invoke({
    "recipient": "my manager",
    "topic": "requesting a day off next Friday",
    "tone": "polite and brief"
})
print(response.content)

# Code reviewer
review_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a senior Python developer doing code review. "
               "Be constructive and specific. Rate the code 1-10."),
    ("user", "Review this code:\n\n```python\n{code}\n```")
])

review_chain = review_prompt | llm

response = review_chain.invoke({
    "code": "def add(a,b): return a+b"
})
print(response.content)
```

## Chains: Connecting the Dots

Chains are sequences of operations. The output of one step becomes the input of the next. Like an assembly line.

```python
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

# Step 1: Generate a topic
topic_prompt = ChatPromptTemplate.from_messages([
    ("user", "Give me one interesting Python topic for beginners. "
             "Just the topic name, nothing else.")
])

# Step 2: Explain that topic
explain_prompt = ChatPromptTemplate.from_messages([
    ("user", "Explain '{topic}' in Python to a beginner in 3 sentences. "
             "Include a code example.")
])

# Chain them together
topic_chain = topic_prompt | llm | StrOutputParser()
explain_chain = explain_prompt | llm | StrOutputParser()

# Run step 1
topic = topic_chain.invoke({})
print(f"Topic: {topic}\n")

# Feed result into step 2
explanation = explain_chain.invoke({"topic": topic})
print(f"Explanation:\n{explanation}")
```

`StrOutputParser()` extracts just the text content from the AI's response. Without it, you'd get the full message object.

### A More Practical Chain: Summarize Then Quiz

```python
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

article = """
Python decorators are functions that modify the behavior of other functions.
They use the @symbol syntax. A decorator takes a function as input, adds
some functionality, and returns a modified function. Common uses include
logging, timing functions, authentication checks, and caching results.
The @property decorator is a built-in example that turns a method into
an attribute-like access pattern.
"""

# Step 1: Summarize
summary_prompt = ChatPromptTemplate.from_messages([
    ("user", "Summarize this in 2 sentences:\n\n{text}")
])
summary_chain = summary_prompt | llm | StrOutputParser()
summary = summary_chain.invoke({"text": article})
print(f"Summary: {summary}\n")

# Step 2: Generate quiz from summary
quiz_prompt = ChatPromptTemplate.from_messages([
    ("user", "Based on this summary, create 2 multiple-choice questions "
             "with 4 options each. Mark the correct answer.\n\n{summary}")
])
quiz_chain = quiz_prompt | llm | StrOutputParser()
quiz = quiz_chain.invoke({"summary": summary})
print(f"Quiz:\n{quiz}")
```

## Memory: AI That Remembers

In Chapter 30, we manually tracked conversation history by appending messages to a list. LangChain gives you memory classes that handle this automatically:

```python
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

# Create a prompt that includes conversation history
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful Python tutor named PyBot. Keep answers concise."),
    MessagesPlaceholder(variable_name="history"),
    ("user", "{input}")
])

chain = prompt | llm

# Store for conversation histories
store = {}

def get_session_history(session_id: str):
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]

# Wrap with message history
with_memory = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="history"
)

# Conversation -- the AI remembers!
config = {"configurable": {"session_id": "user_123"}}

response = with_memory.invoke(
    {"input": "My name is Alex and I'm learning Python."},
    config=config
)
print(f"Bot: {response.content}\n")

response = with_memory.invoke(
    {"input": "What's my name?"},
    config=config
)
print(f"Bot: {response.content}\n")
# The AI knows your name is Alex because it remembers the conversation!

response = with_memory.invoke(
    {"input": "What am I learning?"},
    config=config
)
print(f"Bot: {response.content}")
# It remembers you're learning Python!
```

Different session IDs mean different conversation memories. User A's conversation is separate from User B's. This is exactly how real chatbot products work.

## RAG: What If AI Could Read YOUR Documents?

RAG stands for **Retrieval-Augmented Generation**. Here's the idea in plain English:

1. You have documents (PDFs, text files, web pages, whatever)
2. You chop them into small chunks
3. You convert those chunks into numbers (embeddings) that capture their meaning
4. When a user asks a question, you find the most relevant chunks
5. You send those chunks + the question to the LLM
6. The LLM answers based on YOUR data

It's like giving the AI a cheat sheet before an exam. "Here are the relevant pages. Now answer the question."

> **Don't Panic:** RAG sounds complex but it's really just: load documents, chop them up, let AI search through them. Three steps. The code is straightforward. Let's walk through it.

### Step 1: Load Documents

```python
from langchain_community.document_loaders import TextLoader, PyPDFLoader

# Load a text file
loader = TextLoader("company_handbook.txt")
docs = loader.load()
print(f"Loaded {len(docs)} document(s)")
print(f"Content preview: {docs[0].page_content[:200]}...")

# Load a PDF
# pip install pypdf
loader = PyPDFLoader("annual_report.pdf")
docs = loader.load()
print(f"Loaded {len(docs)} pages")
```

LangChain has loaders for everything: PDFs, Word docs, web pages, CSVs, YouTube transcripts, Wikipedia articles. If data exists, LangChain can probably load it.

### Step 2: Split Into Chunks

Documents can be huge. LLMs have token limits. So we split documents into smaller, overlapping chunks:

```python
from langchain.text_splitter import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,       # Each chunk is ~500 characters
    chunk_overlap=50      # Chunks overlap by 50 characters (for context)
)

chunks = splitter.split_documents(docs)
print(f"Split into {len(chunks)} chunks")
print(f"First chunk: {chunks[0].page_content[:200]}...")
```

Why overlap? Because if a sentence gets cut in half, the overlap ensures both chunks contain the complete thought. It's like how book pages overlap topics -- you don't want to lose context at the break point.

### Step 3: Create Embeddings and Store in a Vector Database

**Embeddings** are how we turn text into numbers that capture meaning. "The cat sat on the mat" and "A feline rested on a rug" would have similar embeddings because they mean similar things, even though they use different words.

```python
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

# Create embeddings
embeddings = OpenAIEmbeddings()

# Store in Chroma (a vector database)
vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="./my_vectorstore"
)

print("Vector store created!")
```

A **vector store** is like a search engine for meaning. Instead of searching for exact words (like Google), it searches for similar meanings. "What's the refund policy?" would find chunks about "returns," "money back," and "cancellation" even if they don't contain the word "refund."

### Step 4: Build the Retrieval Chain

Now connect everything -- user asks a question, relevant chunks are retrieved, and the LLM answers:

```python
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# Create a prompt that includes retrieved context
prompt = ChatPromptTemplate.from_messages([
    ("system", "Answer questions based ONLY on the following context. "
               "If you can't find the answer in the context, say "
               "'I don't have that information in my documents.'\n\n"
               "Context: {context}"),
    ("user", "{input}")
])

# Create the chain
document_chain = create_stuff_documents_chain(llm, prompt)
retrieval_chain = create_retrieval_chain(
    vectorstore.as_retriever(),
    document_chain
)

# Ask a question!
response = retrieval_chain.invoke({"input": "What is the vacation policy?"})
print(response["answer"])
```

That's RAG. The retriever finds relevant chunks from your documents, stuffs them into the prompt's context, and the LLM answers based on that context. The AI is now answering questions about YOUR data.

## Full RAG Example: Q&A Over a Text File

Here's a complete, runnable example:

```python
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain

# Step 1: Create sample data (in real life, you'd load a real file)
sample_text = """
Company PTO Policy:
All full-time employees receive 20 days of paid time off per year.
PTO accrues at 1.67 days per month. Unused PTO carries over up to 5 days.
Employees must request PTO at least 2 weeks in advance for vacations
longer than 3 days. Manager approval is required for all PTO requests.

Remote Work Policy:
Employees may work remotely up to 3 days per week. Core hours are
10 AM to 3 PM in the employee's local time zone. A stable internet
connection is required. Remote work from international locations
requires HR approval at least 30 days in advance.

Benefits:
Health insurance is provided through BlueCross BlueShield. The company
covers 80% of premiums for employees and 50% for dependents. Dental
and vision are optional add-ons. 401(k) matching is 4% of salary.
Open enrollment is in November each year.
"""

# Save to a file for demonstration
with open("company_handbook.txt", "w") as f:
    f.write(sample_text)

# Step 2: Load and split
from langchain_community.document_loaders import TextLoader

loader = TextLoader("company_handbook.txt")
docs = loader.load()

splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=50)
chunks = splitter.split_documents(docs)
print(f"Created {len(chunks)} chunks")

# Step 3: Embed and store
embeddings = OpenAIEmbeddings()
vectorstore = Chroma.from_documents(chunks, embeddings)

# Step 4: Build QA chain
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an HR assistant. Answer questions based ONLY on "
               "the provided context. Be specific and cite the policy.\n\n"
               "Context: {context}"),
    ("user", "{input}")
])

document_chain = create_stuff_documents_chain(llm, prompt)
qa_chain = create_retrieval_chain(vectorstore.as_retriever(), document_chain)

# Step 5: Ask questions!
questions = [
    "How many PTO days do employees get?",
    "Can I work remotely from another country?",
    "What's the 401(k) match?",
    "What's the company's policy on bringing pets to the office?"
]

for q in questions:
    response = qa_chain.invoke({"input": q})
    print(f"\nQ: {q}")
    print(f"A: {response['answer']}")
```

Output:

```
Q: How many PTO days do employees get?
A: Full-time employees receive 20 days of paid time off per year, accruing at 1.67 days per month.

Q: Can I work remotely from another country?
A: Yes, but remote work from international locations requires HR approval at least 30 days in advance.

Q: What's the 401(k) match?
A: The company matches 401(k) contributions at 4% of salary.

Q: What's the company's policy on bringing pets to the office?
A: I don't have that information in my documents.
```

Notice that last answer. The AI correctly says it doesn't know because the information isn't in the documents. That's the power of RAG -- the AI stays grounded in your data instead of making things up.

## Your Turn: PDF Q&A Bot

Create `pdf_qa_bot.py`. Build an interactive Q&A bot over a document:

```python
# 1. Create a sample text file with information about a topic you care about
#    (or use the company handbook from above)

# 2. Load it with TextLoader

# 3. Split into chunks with RecursiveCharacterTextSplitter

# 4. Create embeddings and a Chroma vector store

# 5. Build a retrieval chain

# 6. Create an interactive loop:
#    while True:
#        question = input("Ask a question: ")
#        if question == "quit": break
#        response = qa_chain.invoke({"input": question})
#        print(response["answer"])

# BONUS: Add memory so the bot remembers previous questions in the session

# BONUS: Try loading a real PDF with PyPDFLoader instead of a text file
#        pip install pypdf
```

Ideas for documents to try:
- Your resume (ask "What skills does this person have?")
- A recipe collection (ask "How do I make pasta?")
- Course notes (ask "What are the key concepts in Chapter 3?")
- A product manual (ask "How do I reset the device?")

## TL;DR

- **LangChain** is a framework that organizes LLM workflows: prompts, chains, memory, and document retrieval
- **PromptTemplates** create reusable prompts with variables: `ChatPromptTemplate.from_messages()`
- **Chains** connect components with `|`: `prompt | llm | parser`
- **Memory** gives AI conversation history so it remembers past messages
- **RAG** = load documents, split into chunks, embed as vectors, retrieve relevant chunks, let LLM answer
- **Embeddings** turn text into numbers that capture meaning -- similar meanings get similar numbers
- **Vector stores** (Chroma) are search engines for meaning, not just keywords
- The RAG workflow: `TextLoader` -> `TextSplitter` -> `Embeddings` -> `Chroma` -> `RetrievalChain`
- RAG keeps AI grounded -- it answers from YOUR data and says "I don't know" when the answer isn't there
- This is what companies are building right now: chatbots with memory, document Q&A, AI agents with tools
- You just learned the hottest technology in tech. Seriously. Go update your resume.
