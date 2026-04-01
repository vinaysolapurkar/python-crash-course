"""
Chapter 31: LangChain & AI Agents — Building Smarter AI Apps
==============================================================

LangChain is like LEGO for AI applications. Instead of writing
everything from scratch, you snap together pre-built components:
  - LLMs (the brain)
  - Prompts (the instructions)
  - Memory (the conversation history)
  - Tools (the hands — web search, databases, etc.)
  - Retrieval (reading your documents)

The killer feature? RAG (Retrieval Augmented Generation):
  Instead of the AI making stuff up, it READS YOUR DOCUMENTS first,
  then answers based on what it found. Like giving the AI a cheat sheet!

REQUIREMENTS:
  pip install langchain langchain-openai chromadb
  Set OPENAI_API_KEY environment variable

NOTE: LangChain evolves fast. If something breaks, check their docs
      at python.langchain.com for the latest syntax.
"""

import os
import sys

# ============================================================
# 1. WHAT IS LANGCHAIN?
# ============================================================
print("=" * 60)
print("WHAT IS LANGCHAIN?")
print("=" * 60)
print("""
LangChain helps you build AI apps by providing:

  1. Model wrappers: Talk to OpenAI, Anthropic, Google, etc.
     with the SAME code (swap models without rewriting!)

  2. Prompt templates: Reusable prompt formats with variables

  3. Chains: Connect multiple steps together
     (prompt -> LLM -> parse output -> next step)

  4. Memory: Remember previous conversations automatically

  5. RAG: Read your documents, find relevant parts, answer questions

Think of it as Flask/Django but for AI applications.
""")

# Check for required packages
try:
    from langchain_openai import ChatOpenAI
    from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
    from langchain_core.output_parsers import StrOutputParser
    from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
    HAS_LANGCHAIN = True
except ImportError:
    HAS_LANGCHAIN = False
    print("LangChain not installed. Run:")
    print("  pip install langchain langchain-openai langchain-core")
    print("Showing code examples in demo mode.\n")

api_key = os.getenv("OPENAI_API_KEY")
DEMO_MODE = not (HAS_LANGCHAIN and api_key)

if not api_key:
    print("OPENAI_API_KEY not set. Running in demo mode.")
    print("Set it with: export OPENAI_API_KEY=sk-your-key-here\n")


# ============================================================
# 2. CHATOPENAI — The LLM Wrapper
# ============================================================
print("=" * 60)
print("CHATOPENAI SETUP")
print("=" * 60)

if not DEMO_MODE:
    # Create the LLM wrapper
    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0.7,
        api_key=api_key,
    )

    # Simple invocation
    response = llm.invoke("What is Python in one sentence?")
    print(f"LLM says: {response.content}")
    print()
else:
    print("""
DEMO: ChatOpenAI setup:

    from langchain_openai import ChatOpenAI

    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0.7,
        api_key=os.getenv("OPENAI_API_KEY"),
    )

    response = llm.invoke("What is Python in one sentence?")
    print(response.content)
""")


# ============================================================
# 3. PROMPT TEMPLATES — Reusable Prompts
# ============================================================
# Instead of building prompts with f-strings every time,
# use templates. They're cleaner and reusable!

print("=" * 60)
print("PROMPT TEMPLATES")
print("=" * 60)

if not DEMO_MODE:
    # ChatPromptTemplate — for chat models
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are an expert in {topic}. Explain concepts simply."),
        ("user", "{question}"),
    ])

    # Fill in the variables
    messages = prompt.invoke({
        "topic": "Python programming",
        "question": "What is a decorator?"
    })
    print(f"Formatted prompt: {messages}")
    print()

    # Send to LLM
    response = llm.invoke(messages)
    print(f"Response: {response.content[:200]}...")
    print()
else:
    print("""
DEMO: Prompt templates:

    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are an expert in {topic}. Explain simply."),
        ("user", "{question}"),
    ])

    # Fill in variables and send to LLM
    messages = prompt.invoke({
        "topic": "Python",
        "question": "What is a decorator?"
    })
    response = llm.invoke(messages)
    print(response.content)
""")


# ============================================================
# 4. CHAINS — Connecting Components with |
# ============================================================
# Chains connect components together using the | operator.
# prompt | llm | output_parser
# Data flows through each step: prompt → LLM → parser

print("=" * 60)
print("CHAINS (prompt | llm | parser)")
print("=" * 60)

if not DEMO_MODE:
    # Create a chain: prompt -> LLM -> string output
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a {style} comedian."),
        ("user", "Tell me a short joke about {topic}."),
    ])

    # The | operator connects components into a chain
    chain = prompt | llm | StrOutputParser()

    # Run the chain
    joke = chain.invoke({
        "style": "dad joke",
        "topic": "programming"
    })
    print(f"Joke: {joke}")
    print()

    # Another chain — code explainer
    explainer_prompt = ChatPromptTemplate.from_messages([
        ("system", "You explain code in plain English. Be brief."),
        ("user", "Explain this code: {code}"),
    ])

    explainer_chain = explainer_prompt | llm | StrOutputParser()
    explanation = explainer_chain.invoke({
        "code": "[x**2 for x in range(10) if x % 2 == 0]"
    })
    print(f"Code explanation: {explanation}")
    print()
else:
    print("""
DEMO: Chains with the | operator:

    from langchain_core.output_parsers import StrOutputParser

    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a {style} comedian."),
        ("user", "Tell me a joke about {topic}."),
    ])

    # Chain: prompt -> LLM -> parse to string
    chain = prompt | llm | StrOutputParser()

    joke = chain.invoke({"style": "dad joke", "topic": "programming"})
    print(joke)  # "Why do programmers prefer dark mode? ..."
""")


# ============================================================
# 5. MEMORY — Remembering Conversations
# ============================================================
# Without memory, each call to the LLM is independent.
# Memory keeps track of the conversation so the AI has context.

print("=" * 60)
print("MEMORY — Conversation History")
print("=" * 60)

if not DEMO_MODE:
    from langchain_core.chat_history import InMemoryChatMessageHistory
    from langchain_core.runnables.history import RunnableWithMessageHistory

    # Simple approach: manually manage message history
    history = [
        SystemMessage(content="You are a helpful Python tutor. Be brief."),
    ]

    # First question
    history.append(HumanMessage(content="What is a list?"))
    response = llm.invoke(history)
    history.append(response)
    print(f"Q: What is a list?")
    print(f"A: {response.content[:150]}...\n")

    # Follow-up (the AI remembers!)
    history.append(HumanMessage(content="How do I add items to one?"))
    response = llm.invoke(history)
    history.append(response)
    print(f"Q: How do I add items to one?")
    print(f"A: {response.content[:150]}...")
    print(f"\n(The AI knew 'one' means 'a list' because of conversation history!)")
    print()
else:
    print("""
DEMO: Managing conversation memory:

    from langchain_core.messages import HumanMessage, SystemMessage

    history = [
        SystemMessage(content="You are a helpful Python tutor."),
    ]

    # First question
    history.append(HumanMessage(content="What is a list?"))
    response = llm.invoke(history)
    history.append(response)

    # Follow-up — AI remembers context!
    history.append(HumanMessage(content="How do I add items to one?"))
    response = llm.invoke(history)
    # The AI knows "one" refers to "a list" from the previous exchange!
""")


# ============================================================
# 6. RAG CONCEPT — Retrieval Augmented Generation
# ============================================================
# This is the BIG one. RAG lets you give the AI YOUR data.
#
# Problem: LLMs only know what they were trained on.
#   They don't know about YOUR company's docs, YOUR codebase, etc.
#
# Solution: RAG = Find relevant docs FIRST, then include them in the prompt.
#
# It's like open-book exam: instead of relying on memory alone,
# the AI gets to look things up in YOUR documents!

print("=" * 60)
print("RAG — Retrieval Augmented Generation")
print("=" * 60)
print("""
How RAG works (step by step):

  1. LOAD: Read your documents (PDFs, text files, web pages)

  2. SPLIT: Break documents into small chunks
     (LLMs have token limits — you can't feed a 500-page PDF at once!)

  3. EMBED: Convert each chunk into a vector (list of numbers)
     Similar text → similar vectors (math magic!)

  4. STORE: Save vectors in a vector database (like Chroma)

  5. QUERY: When user asks a question:
     a. Convert the question to a vector
     b. Find the most SIMILAR document chunks
     c. Include those chunks in the prompt
     d. LLM answers based on YOUR data!

  Think of it like this:
    Without RAG: "Hey AI, what's our refund policy?" → "I don't know"
    With RAG:    "Hey AI, here's our policy doc. What's our refund policy?"
                 → "Based on your policy, refunds are available within 30 days..."
""")


# ============================================================
# 7. RAG IN PRACTICE — Document Loading & Splitting
# ============================================================
print("=" * 60)
print("RAG STEP 1-2: Load & Split Documents")
print("=" * 60)

try:
    from langchain.text_splitter import RecursiveCharacterTextSplitter
    HAS_SPLITTER = True
except ImportError:
    HAS_SPLITTER = False

if HAS_SPLITTER:
    # Simulate a document (in real life, you'd load from a file)
    sample_document = """
    Python Programming Guide

    Chapter 1: Variables
    Variables in Python are like labeled boxes. You put a value in a box
    and give it a name. Unlike some languages, you don't need to declare
    the type. Python figures it out automatically. For example:
    name = "Alice" creates a string variable, and age = 25 creates an
    integer variable.

    Chapter 2: Functions
    Functions are reusable blocks of code. Think of them as recipes.
    You define them once with 'def', and call them whenever you need them.
    Functions can take parameters (ingredients) and return values
    (the finished dish). Example: def greet(name): return f"Hello, {name}!"

    Chapter 3: Classes
    Classes are blueprints for creating objects. If a function is a recipe,
    a class is an entire cookbook. It bundles data (attributes) and behavior
    (methods) together. For example, a Dog class might have attributes like
    name and breed, and methods like bark() and fetch().
    """

    # Text splitter — breaks documents into chunks
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=200,       # Max characters per chunk
        chunk_overlap=50,     # Overlap between chunks (prevents cutting mid-sentence)
        separators=["\n\n", "\n", ". ", " "]  # Where to preferably split
    )

    chunks = splitter.split_text(sample_document)
    print(f"Original document: {len(sample_document)} characters")
    print(f"Split into {len(chunks)} chunks\n")
    for i, chunk in enumerate(chunks):
        print(f"Chunk {i+1} ({len(chunk)} chars):")
        print(f"  {chunk[:80]}...")
        print()
else:
    print("""
DEMO: Text splitting:

    from langchain.text_splitter import RecursiveCharacterTextSplitter

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=200,       # Max chars per chunk
        chunk_overlap=50,     # Overlap to keep context
    )

    chunks = splitter.split_text(document_text)
    # Result: List of text chunks, each ~200 characters
""")


# ============================================================
# 8. RAG IN PRACTICE — Embeddings & Vector Store
# ============================================================
print("=" * 60)
print("RAG STEP 3-4: Embed & Store in Vector Database")
print("=" * 60)

try:
    from langchain_openai import OpenAIEmbeddings
    HAS_EMBEDDINGS = True
except ImportError:
    HAS_EMBEDDINGS = False

try:
    from langchain_community.vectorstores import Chroma
    HAS_CHROMA = True
except ImportError:
    try:
        from langchain.vectorstores import Chroma
        HAS_CHROMA = True
    except ImportError:
        HAS_CHROMA = False

if HAS_EMBEDDINGS and HAS_CHROMA and HAS_SPLITTER and not DEMO_MODE:
    # Create embeddings (converts text to vectors)
    embeddings = OpenAIEmbeddings(api_key=api_key)

    # Store chunks in Chroma (vector database)
    vectorstore = Chroma.from_texts(
        texts=chunks,
        embedding=embeddings,
    )
    print(f"Stored {len(chunks)} chunks in Chroma vector database!")

    # Search for relevant chunks
    query = "How do functions work?"
    relevant_docs = vectorstore.similarity_search(query, k=2)
    print(f"\nQuery: '{query}'")
    print(f"Found {len(relevant_docs)} relevant chunks:")
    for i, doc in enumerate(relevant_docs):
        print(f"\n  Match {i+1}: {doc.page_content[:100]}...")
    print()

    # Clean up
    vectorstore.delete_collection()
else:
    print("""
DEMO: Embeddings + Vector Store:

    from langchain_openai import OpenAIEmbeddings
    from langchain_community.vectorstores import Chroma

    # Convert text to vectors
    embeddings = OpenAIEmbeddings(api_key=os.getenv("OPENAI_API_KEY"))

    # Store in Chroma (a lightweight vector database)
    vectorstore = Chroma.from_texts(
        texts=chunks,          # Your document chunks
        embedding=embeddings,  # The embedding model
    )

    # Search! Find chunks similar to a query
    results = vectorstore.similarity_search("How do functions work?", k=2)
    # Returns the 2 most relevant chunks from your documents
""")


# ============================================================
# 9. RAG IN PRACTICE — Full Retrieval Chain
# ============================================================
print("=" * 60)
print("RAG STEP 5: The Full Retrieval Chain")
print("=" * 60)

if HAS_EMBEDDINGS and HAS_CHROMA and HAS_SPLITTER and not DEMO_MODE:
    # Recreate the vector store
    vectorstore = Chroma.from_texts(texts=chunks, embedding=embeddings)
    retriever = vectorstore.as_retriever(search_kwargs={"k": 2})

    # Build the RAG chain
    rag_prompt = ChatPromptTemplate.from_messages([
        ("system", "Answer the question based ONLY on the following context. "
                   "If the context doesn't contain the answer, say 'I don't "
                   "have enough information to answer that.'\n\n"
                   "Context: {context}"),
        ("user", "{question}"),
    ])

    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    # Manual RAG chain
    question = "What are classes in Python?"
    relevant_docs = retriever.invoke(question)
    context = format_docs(relevant_docs)

    chain = rag_prompt | llm | StrOutputParser()
    answer = chain.invoke({"context": context, "question": question})

    print(f"Question: {question}")
    print(f"Answer: {answer}")
    print()

    # Try a question NOT in the documents
    question2 = "What is machine learning?"
    relevant_docs2 = retriever.invoke(question2)
    context2 = format_docs(relevant_docs2)
    answer2 = chain.invoke({"context": context2, "question": question2})
    print(f"Question: {question2}")
    print(f"Answer: {answer2}")
    print("(It correctly says it doesn't know, because it's not in the docs!)")
    print()

    vectorstore.delete_collection()
else:
    print("""
DEMO: Full RAG chain:

    # Create retriever from vector store
    retriever = vectorstore.as_retriever(search_kwargs={"k": 2})

    # RAG prompt — includes context from your documents
    rag_prompt = ChatPromptTemplate.from_messages([
        ("system", "Answer based ONLY on this context: {context}"),
        ("user", "{question}"),
    ])

    # Build the chain
    relevant_docs = retriever.invoke("What are classes?")
    context = "\\n".join(doc.page_content for doc in relevant_docs)

    chain = rag_prompt | llm | StrOutputParser()
    answer = chain.invoke({"context": context, "question": "What are classes?"})
    # Answer is based on YOUR documents, not the LLM's training data!
""")


# ============================================================
# RECAP
# ============================================================
print("=" * 60)
print("CHAPTER 31 RECAP")
print("=" * 60)
print("""
LangChain is your AI application framework:

1. ChatOpenAI: Wrapper for OpenAI (swap models easily!)
2. PromptTemplate: Reusable prompts with variables
3. Chains (|): Connect prompt -> LLM -> parser
4. Memory: Keep conversation history for context
5. RAG: Give the AI YOUR documents to answer from!
   - Load documents
   - Split into chunks
   - Embed as vectors
   - Store in vector database (Chroma)
   - Retrieve relevant chunks for each question

The RAG workflow:
  Load -> Split -> Embed -> Store -> Query -> Answer

Key packages:
  pip install langchain langchain-openai chromadb

Next up: Automation — making Python do your boring tasks!
""")
