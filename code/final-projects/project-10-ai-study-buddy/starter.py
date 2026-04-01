"""
=============================================================
  PROJECT 10: AI-POWERED STUDY BUDDY
=============================================================

Build an AI-powered study assistant! This is the capstone
project - it brings together everything you've learned.

The study buddy loads text files as study material, lets you
ask questions about them, and can even generate practice
quizzes. It works with an AI API (OpenAI/Gemini) or in a
mock mode using keyword matching if no API key is available.

WHAT YOU'LL PRACTICE:
  - Working with AI/LLM APIs
  - Text processing and search
  - Conversation memory
  - Command parsing
  - File I/O
  - Error handling
  - OOP design patterns

DEPENDENCIES:
  pip install openai   (optional - mock mode works without it)

REQUIREMENTS:
  1. CLI chatbot interface
  2. Load study material from .txt files
  3. Answer questions about the loaded material
  4. Maintain conversation history
  5. Support commands:
     /load <file>  - Load a study material file
     /clear        - Clear conversation history
     /history      - Show conversation history
     /quiz         - Generate practice questions
     /help         - Show available commands
     /quit         - Exit the app
  6. Graceful fallback to mock mode if no API key

MOCK MODE:
  When no API key is available, the app should still work
  using keyword matching:
  - Search loaded documents for relevant sentences
  - Return the most relevant passages
  - Generate simple quiz questions from the material

EXAMPLE OUTPUT:
  ========================================
    AI STUDY BUDDY
  ========================================
  Mode: Mock (no API key - using keyword matching)
  Type /help for commands or ask a question!

  You: /load python_basics.txt
  Loaded 'python_basics.txt' (45 lines)

  You: What is a variable in Python?
  Study Buddy: Based on your study material:
  "A variable is a name that refers to a value stored in
  memory. In Python, you create a variable by assigning
  a value with the = operator."

  You: /quiz
  Generated 3 practice questions:

  1. What is a variable in Python?
  2. What does the print() function do?
  3. How do you create a list in Python?

HINTS:
  - Use os.environ.get("OPENAI_API_KEY") for the key
  - Split text into sentences for better searching
  - Use simple TF-IDF-like scoring for keyword matching
  - Keep conversation history in a list of dicts

Good luck with your capstone project!
=============================================================
"""

import os
import re
from datetime import datetime


class StudyBuddy:
    """AI-powered study assistant."""

    def __init__(self):
        self.documents = {}         # {filename: content}
        self.conversation_history = []
        self.api_mode = False       # True if API key available
        # TODO: Check for API key and set mode

    def load_document(self, filepath):
        """Load a text file as study material."""
        # TODO: Read the file
        # TODO: Store in self.documents
        # TODO: Handle file not found
        pass

    def ask_question(self, question):
        """Answer a question about the loaded material."""
        # TODO: If API mode, use the AI API
        # TODO: If mock mode, use keyword matching
        # TODO: Add to conversation history
        pass

    def keyword_search(self, query):
        """Search loaded documents using keyword matching."""
        # TODO: Split query into keywords
        # TODO: Search through document sentences
        # TODO: Score and rank matches
        # TODO: Return best matches
        pass

    def generate_quiz(self):
        """Generate practice questions from loaded material."""
        # TODO: Extract key sentences from documents
        # TODO: Convert to question format
        # TODO: Return list of questions
        pass

    def show_history(self):
        """Display the conversation history."""
        # TODO: Print all Q&A pairs
        pass

    def clear_history(self):
        """Clear the conversation history."""
        # TODO: Reset the history list
        pass

    def process_command(self, user_input):
        """Parse and execute a slash command."""
        # TODO: Parse the command
        # TODO: Route to the right method
        # TODO: Return the result
        pass


def show_help():
    """Display available commands."""
    # TODO: Print command list
    pass


def main():
    """Main chat loop."""
    # TODO: Create StudyBuddy instance
    # TODO: Show welcome message
    # TODO: Loop: get input, process, respond
    # TODO: Handle commands vs questions
    pass


if __name__ == "__main__":
    main()
