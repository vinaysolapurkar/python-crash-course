"""
Chapter 30: AI APIs — YOUR TURN!
==================================

Build an "Ask Me Anything About Python" chatbot!

This chatbot will:
1. Take user questions in a loop
2. Send them to OpenAI's API
3. Print the AI's response
4. Maintain conversation history (so it remembers context!)

The conversation history part is key — without it, the AI forgets
everything after each question. We keep a list of messages and
append each new exchange.

Type 'quit' or 'exit' to stop the chatbot.

REQUIREMENTS:
  pip install openai
  Set OPENAI_API_KEY environment variable

TASKS:
1. Set up the OpenAI client
2. Define the system message (personality)
3. Create the conversation loop
4. Maintain message history
5. Handle errors gracefully
"""

import os

# TODO 1: Import OpenAI and set up the client
# Hint: from openai import OpenAI
#        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


# TODO 2: Define the system message
# This sets the AI's personality and expertise.
# Make it a Python expert that's friendly and encouraging!
system_message = {
    "role": "system",
    "content": "???"  # Fill this in!
}

# TODO 3: Initialize conversation history with the system message
# conversation_history = [system_message]


# TODO 4: Create the chat loop
# Pseudocode:
#   while True:
#       Get user input
#       If user types 'quit' or 'exit', break
#       Add user message to conversation_history
#       Send conversation_history to OpenAI
#       Get the response
#       Add assistant response to conversation_history
#       Print the response
#
# Don't forget to handle errors! What if:
#   - The API key is missing?
#   - The API call fails (network error)?
#   - The user enters an empty message?


print("Python Tutor Chatbot")
print("=" * 40)
print("Ask me anything about Python!")
print("Type 'quit' to exit.\n")

# Your chat loop here...
