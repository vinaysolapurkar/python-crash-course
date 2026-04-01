"""
=============================================================
  PROJECT 10: AI-POWERED STUDY BUDDY - SOLUTION
=============================================================
  A CLI chatbot that loads study materials and answers
  questions about them. Works with OpenAI API or in mock
  mode using keyword matching.

  Dependencies (optional):
    pip install openai

  The app works WITHOUT any API key using mock mode!

  Run:  python solution.py

  For AI mode, set your API key first:
    export OPENAI_API_KEY="your-key-here"   (Mac/Linux)
    set OPENAI_API_KEY=your-key-here        (Windows)

  Create a sample study file:
    python -c "
    with open('sample_notes.txt', 'w') as f:
        f.write('''Python Basics Study Notes

Variables and Data Types
A variable is a name that refers to a value stored in memory.
In Python, you create a variable by assigning a value with the = operator.
Python has several data types: int, float, str, bool, list, dict, tuple, and set.
Integers are whole numbers like 1, 42, or -7.
Floats are decimal numbers like 3.14 or -0.5.
Strings are sequences of characters enclosed in quotes.
Booleans are either True or False.

Lists and Collections
A list is an ordered, mutable collection created with square brackets.
You can add items to a list with the append() method.
Lists support indexing, slicing, and iteration.
A dictionary maps keys to values and is created with curly braces.
Tuples are like lists but immutable - they cannot be changed after creation.
Sets contain only unique elements and support mathematical set operations.

Functions
A function is a reusable block of code defined with the def keyword.
Functions can accept parameters and return values.
The print() function displays output to the console.
The len() function returns the number of items in a collection.
The range() function generates a sequence of numbers.
Lambda functions are small anonymous functions defined in one line.

Control Flow
The if statement executes code based on a condition.
The for loop iterates over a sequence of items.
The while loop repeats as long as a condition is true.
Break exits a loop early, and continue skips to the next iteration.
Try and except blocks handle errors and exceptions gracefully.
''')
    print('Created sample_notes.txt')
    "
=============================================================
"""

import os
import re
import random
import math
from datetime import datetime
from collections import Counter

# Try to import OpenAI (optional)
try:
    from openai import OpenAI
    HAS_OPENAI = True
except ImportError:
    HAS_OPENAI = False


# ── Study Buddy Class ──────────────────────────────────────

class StudyBuddy:
    """
    AI-powered study assistant with document loading,
    question answering, and quiz generation.
    """

    def __init__(self):
        self.documents = {}           # {filename: content_string}
        self.document_sentences = {}  # {filename: [sentences]}
        self.conversation_history = []
        self.api_client = None
        self.api_mode = False

        # Check for API key
        api_key = os.environ.get("OPENAI_API_KEY", "").strip()
        if api_key and HAS_OPENAI:
            try:
                self.api_client = OpenAI(api_key=api_key)
                self.api_mode = True
            except Exception as e:
                print(f"  Warning: Could not initialize OpenAI: {e}")
                self.api_mode = False

    @property
    def mode_name(self):
        return "AI (OpenAI)" if self.api_mode else "Mock (keyword matching)"

    @property
    def has_documents(self):
        return len(self.documents) > 0

    # ── Document Management ─────────────────────────────────

    def load_document(self, filepath):
        """Load a text file as study material."""
        # Handle relative and absolute paths
        if not os.path.isabs(filepath):
            filepath = os.path.join(os.getcwd(), filepath)

        if not os.path.exists(filepath):
            return f"File not found: {filepath}"

        try:
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
        except IOError as e:
            return f"Error reading file: {e}"

        filename = os.path.basename(filepath)
        self.documents[filename] = content

        # Pre-process: split into sentences for searching
        sentences = self._split_sentences(content)
        self.document_sentences[filename] = sentences

        line_count = content.count("\n") + 1
        return f"Loaded '{filename}' ({line_count} lines, {len(sentences)} sentences)"

    def _split_sentences(self, text):
        """Split text into meaningful sentences."""
        # Split on sentence boundaries and newlines
        raw = re.split(r'[.!?\n]+', text)

        # Clean up: strip whitespace, remove empties and very short fragments
        sentences = []
        for s in raw:
            s = s.strip()
            if len(s) > 10:  # Skip very short fragments
                sentences.append(s)

        return sentences

    def get_all_sentences(self):
        """Get all sentences from all loaded documents."""
        all_sentences = []
        for filename, sentences in self.document_sentences.items():
            all_sentences.extend(sentences)
        return all_sentences

    # ── Question Answering ──────────────────────────────────

    def ask_question(self, question):
        """Answer a question about the loaded material."""
        if not self.has_documents:
            return ("No study material loaded yet! "
                    "Use /load <filename> to load a text file.")

        if self.api_mode:
            answer = self._ask_with_api(question)
        else:
            answer = self._ask_with_keywords(question)

        # Save to conversation history
        self.conversation_history.append({
            "timestamp": datetime.now().strftime("%H:%M:%S"),
            "question": question,
            "answer": answer,
        })

        return answer

    def _ask_with_api(self, question):
        """Use OpenAI API to answer the question."""
        # Build context from loaded documents
        context = "\n\n".join(
            f"--- {name} ---\n{content}"
            for name, content in self.documents.items()
        )

        # Limit context to avoid token limits
        if len(context) > 8000:
            context = context[:8000] + "\n...(truncated)"

        try:
            response = self.api_client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are a helpful study buddy. Answer questions "
                            "based on the following study material. Be concise "
                            "and helpful. If the answer isn't in the material, "
                            "say so but try to help anyway.\n\n"
                            f"Study Material:\n{context}"
                        ),
                    },
                    {"role": "user", "content": question},
                ],
                max_tokens=500,
                temperature=0.7,
            )
            return response.choices[0].message.content.strip()

        except Exception as e:
            # Fall back to keyword mode on API error
            return (f"(API error: {e})\n"
                    f"Falling back to keyword search:\n\n"
                    f"{self._ask_with_keywords(question)}")

    def _ask_with_keywords(self, question):
        """Answer using keyword matching (mock mode)."""
        relevant = self.keyword_search(question, top_n=3)

        if not relevant:
            return ("I couldn't find anything related to your question "
                    "in the loaded materials. Try rephrasing or loading "
                    "more study material.")

        # Build a helpful response from matched sentences
        response = "Based on your study material:\n\n"
        for i, (sentence, score) in enumerate(relevant, 1):
            response += f'  "{sentence}."\n\n'

        return response.strip()

    def keyword_search(self, query, top_n=3):
        """
        Search loaded documents using TF-IDF-like keyword matching.
        Returns a list of (sentence, score) tuples.
        """
        all_sentences = self.get_all_sentences()
        if not all_sentences:
            return []

        # Extract keywords from the query (remove common stop words)
        stop_words = {
            "a", "an", "the", "is", "are", "was", "were", "be", "been",
            "being", "have", "has", "had", "do", "does", "did", "will",
            "would", "could", "should", "may", "might", "can", "shall",
            "in", "on", "at", "to", "for", "of", "with", "by", "from",
            "and", "or", "not", "but", "if", "then", "than", "that",
            "this", "what", "which", "who", "how", "when", "where", "why",
            "it", "its", "i", "me", "my", "you", "your", "we", "they",
        }

        query_words = set(
            word.lower() for word in re.findall(r'\w+', query)
            if word.lower() not in stop_words and len(word) > 1
        )

        if not query_words:
            # If all words are stop words, just use all words
            query_words = set(
                word.lower() for word in re.findall(r'\w+', query)
                if len(word) > 1
            )

        # Score each sentence by keyword overlap
        scored = []
        for sentence in all_sentences:
            sentence_words = set(
                word.lower() for word in re.findall(r'\w+', sentence)
            )

            # Count matching keywords
            matches = query_words & sentence_words
            if matches:
                # Score: number of matches, boosted by match ratio
                score = len(matches) / len(query_words) if query_words else 0
                scored.append((sentence, score))

        # Sort by score (highest first) and return top N
        scored.sort(key=lambda x: x[1], reverse=True)
        return scored[:top_n]

    # ── Quiz Generation ─────────────────────────────────────

    def generate_quiz(self, num_questions=5):
        """Generate practice questions from the loaded material."""
        all_sentences = self.get_all_sentences()

        if not all_sentences:
            return "No study material loaded! Use /load <file> first."

        if self.api_mode:
            return self._generate_quiz_api(num_questions)
        else:
            return self._generate_quiz_mock(all_sentences, num_questions)

    def _generate_quiz_api(self, num_questions):
        """Generate quiz using OpenAI."""
        context = "\n".join(
            f"{content}" for content in self.documents.values()
        )
        if len(context) > 6000:
            context = context[:6000]

        try:
            response = self.api_client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "Generate practice quiz questions based on the "
                            "following study material. Create clear, specific "
                            "questions that test understanding. Number them."
                        ),
                    },
                    {
                        "role": "user",
                        "content": (
                            f"Generate {num_questions} practice questions "
                            f"from this material:\n\n{context}"
                        ),
                    },
                ],
                max_tokens=500,
                temperature=0.8,
            )
            return response.choices[0].message.content.strip()

        except Exception as e:
            all_sentences = self.get_all_sentences()
            return (f"(API error, using mock quiz)\n\n"
                    f"{self._generate_quiz_mock(all_sentences, num_questions)}")

    def _generate_quiz_mock(self, sentences, num_questions):
        """Generate simple quiz questions from sentences (mock mode)."""
        # Pick sentences that look like they contain facts/definitions
        # (sentences with "is", "are", "means", "called", etc.)
        fact_patterns = [
            r'\bis\b', r'\bare\b', r'\bmeans\b', r'\bcalled\b',
            r'\bdefined\b', r'\bcreated?\b', r'\bused?\b',
            r'\bfunction\b', r'\breturn', r'\bcontain',
        ]

        good_sentences = []
        for sentence in sentences:
            score = sum(1 for p in fact_patterns
                        if re.search(p, sentence, re.IGNORECASE))
            if score > 0:
                good_sentences.append((sentence, score))

        # Sort by how "factual" they seem
        good_sentences.sort(key=lambda x: x[1], reverse=True)

        # Take the best ones (up to num_questions)
        selected = good_sentences[:num_questions]
        if not selected:
            selected = [(s, 0) for s in random.sample(
                sentences, min(num_questions, len(sentences))
            )]

        # Convert statements to questions
        question_starters = [
            "What", "How would you explain that", "Can you describe how",
            "What do you know about the concept that",
            "Explain the following:",
        ]

        quiz = f"Practice Quiz ({len(selected)} questions):\n"
        quiz += "=" * 40 + "\n\n"

        for i, (sentence, _) in enumerate(selected, 1):
            # Try to make it look like a question
            starter = random.choice(question_starters)
            quiz += f"  {i}. {starter}: {sentence}?\n\n"

        quiz += "=" * 40
        quiz += "\n(Review your study material for the answers!)"

        return quiz

    # ── Conversation History ────────────────────────────────

    def show_history(self):
        """Return formatted conversation history."""
        if not self.conversation_history:
            return "No conversation history yet."

        output = "Conversation History:\n"
        output += "=" * 40 + "\n\n"

        for entry in self.conversation_history:
            output += f"  [{entry['timestamp']}] You: {entry['question']}\n"
            # Truncate long answers in history view
            answer = entry['answer']
            if len(answer) > 100:
                answer = answer[:100] + "..."
            output += f"  Study Buddy: {answer}\n\n"

        output += f"Total exchanges: {len(self.conversation_history)}"
        return output

    def clear_history(self):
        """Clear conversation history."""
        count = len(self.conversation_history)
        self.conversation_history.clear()
        return f"Cleared {count} conversation(s) from history."

    # ── Command Processing ──────────────────────────────────

    def process_command(self, user_input):
        """
        Parse and execute a slash command.
        Returns (response_text, should_quit).
        """
        parts = user_input.strip().split(maxsplit=1)
        command = parts[0].lower()
        args = parts[1] if len(parts) > 1 else ""

        if command == "/load":
            if not args:
                return "Usage: /load <filename>", False
            return self.load_document(args), False

        elif command == "/clear":
            return self.clear_history(), False

        elif command == "/history":
            return self.show_history(), False

        elif command == "/quiz":
            try:
                num = int(args) if args else 5
            except ValueError:
                num = 5
            return self.generate_quiz(num), False

        elif command == "/help":
            return get_help_text(), False

        elif command == "/docs":
            return self._list_documents(), False

        elif command in ("/quit", "/exit", "/q"):
            return "Goodbye! Happy studying!", True

        else:
            return f"Unknown command: {command}. Type /help for help.", False

    def _list_documents(self):
        """List all loaded documents."""
        if not self.documents:
            return "No documents loaded. Use /load <filename> to load one."

        output = "Loaded Documents:\n"
        for name, content in self.documents.items():
            lines = content.count("\n") + 1
            sentences = len(self.document_sentences.get(name, []))
            output += f"  - {name} ({lines} lines, {sentences} sentences)\n"
        return output


# ── Help Text ──────────────────────────────────────────────

def get_help_text():
    """Return the help text for available commands."""
    return """
Available Commands:
  /load <file>   Load a text file as study material
  /docs          List loaded documents
  /quiz [n]      Generate n practice questions (default: 5)
  /history       Show conversation history
  /clear         Clear conversation history
  /help          Show this help message
  /quit          Exit the app

Just type a question to ask about your study material!
Example: "What is a variable in Python?"
""".strip()


# ── Main Loop ──────────────────────────────────────────────

def main():
    """Main chat loop for the Study Buddy."""
    buddy = StudyBuddy()

    print()
    print("=" * 45)
    print("       AI STUDY BUDDY")
    print("=" * 45)
    print(f"  Mode: {buddy.mode_name}")
    if not buddy.api_mode:
        print("  (Set OPENAI_API_KEY env var for AI mode)")
    print()
    print("  Load study material with /load <file>")
    print("  Then ask questions about it!")
    print("  Type /help for all commands.")
    print("=" * 45)
    print()

    while True:
        try:
            user_input = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n\nGoodbye! Happy studying!")
            break

        if not user_input:
            continue

        # Check if it's a command (starts with /)
        if user_input.startswith("/"):
            response, should_quit = buddy.process_command(user_input)
            print(f"\n{response}\n")
            if should_quit:
                break
        else:
            # It's a question - ask the study buddy
            response = buddy.ask_question(user_input)
            print(f"\nStudy Buddy: {response}\n")


if __name__ == "__main__":
    main()
