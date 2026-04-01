# Project 10: AI-Powered Study Buddy

> **Difficulty:** 5/5 | **Time:** ~4 hours | **Skills:** OpenAI API, LangChain, RAG, conversation memory
> **Code:** https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/final-projects/project-10-study-buddy/

## What You'll Build

An intelligent study assistant that loads your study materials (text files, notes, PDFs), lets you ask questions about them using AI, generates quizzes based on the content, and maintains conversation history so it remembers context. This is a real-world application of Retrieval-Augmented Generation (RAG) -- the same pattern used in enterprise AI tools.

Here's what it looks like:

```
=== AI STUDY BUDDY ===

Loaded 3 study files (12,450 words total)
Model: gpt-3.5-turbo

Commands: /quiz, /summary, /history, /load, /clear, /help, /quit

You: What are the main causes of World War I?

Study Buddy: Based on your study materials, the main causes of WWI
were: (1) the alliance system that divided Europe into two blocs,
(2) militarism and the arms race, (3) imperial competition for
colonies, and (4) nationalism, particularly in the Balkans. Your
notes specifically highlight the assassination of Archduke Franz
Ferdinand as the immediate trigger.

You: /quiz

Generating quiz from your materials...

Q1: What event is considered the immediate trigger of World War I?
  a) The sinking of the Lusitania
  b) The assassination of Archduke Franz Ferdinand
  c) The invasion of Belgium
  d) The Treaty of Versailles

Your answer:
```

## Skills You'll Use

- OpenAI API (learned in Chapter 18)
- File I/O for loading documents (learned in Chapter 7)
- JSON for conversation persistence (learned in Chapter 7)
- String processing and text chunking (learned in Chapter 2)
- Functions and OOP (learned in Chapters 5 and 9)
- Error handling (learned in Chapter 8)

## Step-by-Step Build Guide

### Step 1: Install Dependencies and Set Up

```bash
pip install openai
```

You'll need an OpenAI API key. Set it as an environment variable:

```bash
# Linux/Mac
export OPENAI_API_KEY="your-key-here"

# Windows (Command Prompt)
set OPENAI_API_KEY=your-key-here

# Windows (PowerShell)
$env:OPENAI_API_KEY="your-key-here"
```

Now create the project file:

```python
# study_buddy.py

import os
import json
import glob
from datetime import datetime

try:
    from openai import OpenAI
except ImportError:
    print("Please install openai: pip install openai")
    exit(1)

# Configuration
HISTORY_FILE = "conversation_history.json"
MATERIALS_DIR = "study_materials"
MODEL = "gpt-3.5-turbo"
MAX_CONTEXT_CHARS = 6000  # Limit context sent to the API
```

### Step 2: Build the Document Loader

This component loads study materials from text files, splits them into manageable chunks, and prepares them for use as context in AI queries.

```python
class DocumentLoader:
    """Loads and manages study materials."""

    def __init__(self, materials_dir=MATERIALS_DIR):
        self.materials_dir = materials_dir
        self.documents = []    # List of {"filename": ..., "content": ...}
        self.chunks = []       # Smaller text chunks for context

    def load_all(self):
        """Load all .txt files from the materials directory."""
        if not os.path.exists(self.materials_dir):
            os.makedirs(self.materials_dir)
            self._create_sample_files()

        patterns = [
            os.path.join(self.materials_dir, "*.txt"),
            os.path.join(self.materials_dir, "*.md"),
        ]

        files_loaded = 0
        total_words = 0

        for pattern in patterns:
            for filepath in glob.glob(pattern):
                try:
                    with open(filepath, "r", encoding="utf-8") as f:
                        content = f.read()

                    filename = os.path.basename(filepath)
                    self.documents.append({
                        "filename": filename,
                        "content": content
                    })

                    # Split into chunks of ~500 words for better retrieval
                    chunks = self._chunk_text(content, filename)
                    self.chunks.extend(chunks)

                    word_count = len(content.split())
                    total_words += word_count
                    files_loaded += 1

                except (IOError, UnicodeDecodeError) as e:
                    print(f"  Warning: Could not load {filepath}: {e}")

        print(f"Loaded {files_loaded} study file(s) "
              f"({total_words:,} words total)")
        return files_loaded

    def _chunk_text(self, text, filename, chunk_size=500):
        """Split text into chunks of approximately chunk_size words."""
        words = text.split()
        chunks = []

        for i in range(0, len(words), chunk_size):
            chunk_words = words[i:i + chunk_size]
            chunk_text = " ".join(chunk_words)
            chunks.append({
                "source": filename,
                "content": chunk_text
            })

        return chunks

    def find_relevant_chunks(self, query, max_chunks=3):
        """Find the most relevant chunks for a query (simple keyword matching).
        A production system would use embeddings and vector search."""
        query_words = set(query.lower().split())

        scored_chunks = []
        for chunk in self.chunks:
            chunk_lower = chunk["content"].lower()
            # Score by number of query words found in the chunk
            score = sum(1 for word in query_words
                        if word in chunk_lower and len(word) > 3)
            scored_chunks.append((score, chunk))

        # Sort by score (highest first) and return top chunks
        scored_chunks.sort(key=lambda x: x[0], reverse=True)
        relevant = [chunk for score, chunk in scored_chunks[:max_chunks]
                     if score > 0]

        # If no matches found, return the first few chunks as general context
        if not relevant and self.chunks:
            relevant = self.chunks[:max_chunks]

        return relevant

    def get_context(self, query):
        """Build a context string from relevant document chunks."""
        chunks = self.find_relevant_chunks(query)

        if not chunks:
            return "No study materials loaded."

        context_parts = []
        total_chars = 0

        for chunk in chunks:
            if total_chars + len(chunk["content"]) > MAX_CONTEXT_CHARS:
                break
            context_parts.append(
                f"[From: {chunk['source']}]\n{chunk['content']}"
            )
            total_chars += len(chunk["content"])

        return "\n\n---\n\n".join(context_parts)

    def _create_sample_files(self):
        """Create sample study materials for demonstration."""
        sample = {
            "python_basics.txt": (
                "Python Basics - Study Notes\n\n"
                "Variables and Data Types:\n"
                "Python has several built-in data types: integers (int), "
                "floating-point numbers (float), strings (str), and "
                "booleans (bool). Variables don't need type declarations. "
                "Python uses dynamic typing, meaning the type is determined "
                "at runtime.\n\n"
                "Control Flow:\n"
                "Python uses if/elif/else for conditional execution. "
                "For loops iterate over sequences (lists, strings, ranges). "
                "While loops repeat as long as a condition is True. "
                "Break exits a loop early, continue skips to the next "
                "iteration.\n\n"
                "Functions:\n"
                "Functions are defined with the def keyword. They can "
                "accept parameters and return values. Python supports "
                "default parameter values, *args for variable positional "
                "arguments, and **kwargs for variable keyword arguments.\n"
            ),
        }

        for filename, content in sample.items():
            filepath = os.path.join(self.materials_dir, filename)
            with open(filepath, "w") as f:
                f.write(content)

        print(f"  Created sample study materials in {self.materials_dir}/")
        print("  Add your own .txt files there for better results!")
```

### Step 3: Build Conversation Memory

Track conversation history so the AI remembers previous questions and answers.

```python
class ConversationMemory:
    """Manages conversation history with persistence."""

    def __init__(self, history_file=HISTORY_FILE, max_history=20):
        self.history_file = history_file
        self.max_history = max_history
        self.messages = []  # List of {"role": ..., "content": ...}
        self.load_history()

    def add_message(self, role, content):
        """Add a message to the conversation history."""
        self.messages.append({
            "role": role,
            "content": content,
            "timestamp": datetime.now().isoformat()
        })

        # Keep history bounded
        if len(self.messages) > self.max_history * 2:
            # Keep the system message and the most recent messages
            self.messages = self.messages[-self.max_history * 2:]

        self.save_history()

    def get_messages_for_api(self):
        """Return messages formatted for the OpenAI API."""
        return [{"role": m["role"], "content": m["content"]}
                for m in self.messages]

    def clear(self):
        """Clear conversation history."""
        self.messages = []
        self.save_history()

    def save_history(self):
        """Save conversation history to JSON."""
        try:
            with open(self.history_file, "w") as f:
                json.dump(self.messages, f, indent=2)
        except IOError:
            pass

    def load_history(self):
        """Load conversation history from JSON."""
        if not os.path.exists(self.history_file):
            return

        try:
            with open(self.history_file, "r") as f:
                self.messages = json.load(f)
        except (json.JSONDecodeError, IOError):
            self.messages = []

    def display_history(self):
        """Show recent conversation history."""
        if not self.messages:
            print("\n  No conversation history yet.")
            return

        print(f"\n--- Conversation History ({len(self.messages)} messages) ---")
        for msg in self.messages[-10:]:  # Show last 10
            role = "You" if msg["role"] == "user" else "Study Buddy"
            content = msg["content"][:100]
            if len(msg["content"]) > 100:
                content += "..."
            timestamp = msg.get("timestamp", "")[:16]
            print(f"\n  [{timestamp}] {role}:")
            print(f"  {content}")
```

### Step 4: Build the AI Study Buddy Core

This is the main class that ties everything together -- document context, conversation memory, and AI responses.

```python
class StudyBuddy:
    """AI-powered study assistant."""

    def __init__(self):
        api_key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
            print("ERROR: Set your OPENAI_API_KEY environment variable.")
            print("  export OPENAI_API_KEY='your-key-here'")
            exit(1)

        self.client = OpenAI(api_key=api_key)
        self.docs = DocumentLoader()
        self.memory = ConversationMemory()
        self.model = MODEL

    def setup(self):
        """Load materials and prepare the buddy."""
        print(f"Model: {self.model}")
        files_loaded = self.docs.load_all()
        if files_loaded == 0:
            print("Warning: No study materials found.")
            print(f"Add .txt files to the '{MATERIALS_DIR}/' directory.")
        return files_loaded

    def ask(self, question):
        """Ask the study buddy a question about your materials."""
        # Find relevant context from study materials
        context = self.docs.get_context(question)

        # Build the system prompt with context
        system_prompt = (
            "You are a helpful study assistant. Answer questions based on "
            "the student's study materials provided below. If the answer "
            "is in the materials, reference them specifically. If not, "
            "provide a helpful answer but note that it's from your general "
            "knowledge, not their notes. Be encouraging and clear.\n\n"
            f"STUDY MATERIALS:\n{context}"
        )

        # Build the message list
        messages = [{"role": "system", "content": system_prompt}]

        # Add recent conversation history for context
        recent = self.memory.get_messages_for_api()[-6:]
        messages.extend(recent)

        # Add the current question
        messages.append({"role": "user", "content": question})

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                max_tokens=500,
                temperature=0.7
            )

            answer = response.choices[0].message.content

            # Save to memory
            self.memory.add_message("user", question)
            self.memory.add_message("assistant", answer)

            return answer

        except Exception as e:
            return f"Error getting response: {e}"

    def generate_quiz(self, num_questions=3):
        """Generate a quiz based on the study materials."""
        if not self.docs.chunks:
            return "No study materials loaded. Add files first."

        # Use a random selection of content for the quiz
        import random
        sample_chunks = random.sample(
            self.docs.chunks,
            min(3, len(self.docs.chunks))
        )
        context = "\n\n".join(c["content"] for c in sample_chunks)

        prompt = (
            f"Based on the following study material, generate a quiz with "
            f"{num_questions} multiple-choice questions. For each question:\n"
            f"- Write the question\n"
            f"- Provide 4 options (a, b, c, d)\n"
            f"- Mark the correct answer\n"
            f"- Add a brief explanation\n\n"
            f"Format each question clearly with blank lines between them.\n\n"
            f"MATERIAL:\n{context[:3000]}"
        )

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system",
                     "content": "You are a quiz generator. Create clear, "
                                "educational multiple-choice questions."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=800,
                temperature=0.8
            )

            return response.choices[0].message.content

        except Exception as e:
            return f"Error generating quiz: {e}"

    def generate_summary(self):
        """Generate a summary of all loaded study materials."""
        if not self.docs.documents:
            return "No study materials loaded."

        # Combine content (limited for API)
        all_content = "\n\n".join(
            d["content"][:2000] for d in self.docs.documents
        )[:5000]

        prompt = (
            "Summarize the following study materials into key points. "
            "Organize by topic and highlight the most important concepts "
            "a student should remember.\n\n"
            f"MATERIALS:\n{all_content}"
        )

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system",
                     "content": "You are a study assistant that creates "
                                "clear, concise summaries."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=600,
                temperature=0.5
            )

            return response.choices[0].message.content

        except Exception as e:
            return f"Error generating summary: {e}"
```

### Step 5: Build the Interactive Interface

```python
def print_help():
    """Print available commands."""
    print("\n--- Commands ---")
    print("  /quiz      - Generate a quiz from your materials")
    print("  /summary   - Summarize your study materials")
    print("  /history   - View conversation history")
    print("  /load      - Reload study materials")
    print("  /clear     - Clear conversation history")
    print("  /help      - Show this help message")
    print("  /quit      - Exit the study buddy")
    print("\n  Or just type a question about your study materials!")


def main():
    """Main application loop."""
    print("=" * 35)
    print("    AI STUDY BUDDY")
    print("=" * 35)
    print()

    buddy = StudyBuddy()
    buddy.setup()

    print(f"\nCommands: /quiz, /summary, /history, /load, /clear, "
          f"/help, /quit")
    print()

    while True:
        try:
            user_input = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye! Keep studying!")
            break

        if not user_input:
            continue

        # Handle commands
        if user_input.startswith("/"):
            command = user_input.lower().split()[0]

            if command == "/quit":
                print("\nGoodbye! Keep studying!")
                break

            elif command == "/quiz":
                print("\nGenerating quiz from your materials...")
                quiz = buddy.generate_quiz()
                print(f"\n{quiz}")

            elif command == "/summary":
                print("\nGenerating summary...")
                summary = buddy.generate_summary()
                print(f"\n{summary}")

            elif command == "/history":
                buddy.memory.display_history()

            elif command == "/load":
                buddy.docs = DocumentLoader()
                buddy.docs.load_all()

            elif command == "/clear":
                buddy.memory.clear()
                print("  Conversation history cleared.")

            elif command == "/help":
                print_help()

            else:
                print(f"  Unknown command: {command}")
                print("  Type /help for available commands.")

        else:
            # It's a question -- ask the study buddy
            print()
            answer = buddy.ask(user_input)
            print(f"Study Buddy: {answer}\n")


if __name__ == "__main__":
    main()
```

### Step 6: Prepare Study Materials and Test

Create a `study_materials` folder and add some text files:

```bash
mkdir study_materials
```

Add any `.txt` files you want to study from. Then run:

```bash
python study_buddy.py
```

Try asking questions, generating quizzes, and getting summaries. The more material you add, the better the responses will be.

## Challenges (Level Up!)

1. **Embedding-based retrieval:** Replace the simple keyword matching in `find_relevant_chunks` with OpenAI's embedding API. Generate embeddings for each chunk when materials are loaded, store them, and use cosine similarity to find the most relevant chunks for each query. This is real RAG.

2. **PDF support:** Add the ability to load PDF files using the `PyPDF2` library. Extract text from each page and chunk it the same way you handle text files.

3. **Spaced repetition:** Track which quiz questions the user got right or wrong. Use a spaced repetition algorithm to re-ask missed questions more frequently, and correctly answered questions less often. Save progress to a JSON file.

## Portfolio Tips

This is your capstone project -- the one that makes hiring managers sit up. AI-powered applications are the hottest thing in tech right now. When presenting this:

- **GitHub:** Write an excellent README with screenshots, architecture explanation (document loading, chunking, retrieval, generation), and clear setup instructions. Include sample study materials.
- **Resume:** "Built an AI-powered study assistant using OpenAI's API with RAG (Retrieval-Augmented Generation), document chunking, context-aware Q&A, quiz generation, and persistent conversation memory."
- **Interview talking point:** Explain what RAG is and why it matters (the AI answers from YOUR documents, not just its training data). Discuss the chunking strategy and why you limit context size (token costs, relevance). Talk about how you'd improve retrieval with embeddings and vector databases (Pinecone, ChromaDB). This demonstrates that you understand the architecture behind tools like ChatGPT plugins, Copilot, and enterprise AI assistants.
