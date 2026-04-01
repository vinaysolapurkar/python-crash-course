"""
Chapter 30: AI APIs — SOLUTION
================================

Your very own Python tutor chatbot! It remembers the entire
conversation, so you can ask follow-up questions like
"Can you explain that more simply?" and it knows what "that" is.

This is essentially how ChatGPT works under the hood:
  - Maintain a conversation history
  - Send the FULL history with each new message
  - Append each response to the history

Run this with: python solution.py
Make sure OPENAI_API_KEY is set in your environment!
"""

import os
import sys

# --- Setup ---
try:
    from openai import OpenAI
except ImportError:
    print("Please install openai: pip install openai")
    sys.exit(1)

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("=" * 50)
    print("OPENAI_API_KEY not set!")
    print()
    print("To set it:")
    print("  Windows:   set OPENAI_API_KEY=sk-your-key-here")
    print("  Mac/Linux: export OPENAI_API_KEY=sk-your-key-here")
    print()
    print("Running in DEMO MODE (simulated responses).")
    print("=" * 50)
    print()
    DEMO_MODE = True
else:
    DEMO_MODE = False
    client = OpenAI(api_key=api_key)

# --- System message ---
# This defines the chatbot's personality and expertise.
system_message = {
    "role": "system",
    "content": (
        "You are a friendly, encouraging Python tutor. "
        "Your name is PyBot. You explain concepts clearly with analogies "
        "and short code examples. Keep responses concise (under 200 words) "
        "unless the user asks for more detail. "
        "If someone asks a non-Python question, gently redirect them. "
        "Use casual, fun language. Celebrate when they understand something!"
    )
}

# --- Conversation history ---
# This list grows with each exchange. The AI sees ALL of it each time.
conversation_history = [system_message]

# Demo responses for when API key isn't available
DEMO_RESPONSES = [
    "A list is like a backpack - you can toss anything in, take stuff out, "
    "and rearrange things. `my_list = [1, 'hello', True]`. "
    "Lists use square brackets and can hold any type of data!",

    "Great follow-up! A tuple is like a sealed envelope - once you put stuff "
    "in, you can't change it. `my_tuple = (1, 'hello', True)`. "
    "Use tuples when data shouldn't change, like coordinates (x, y)!",

    "You're doing awesome! A dictionary is like a real dictionary - "
    "you look up a KEY to find a VALUE. `my_dict = {'name': 'Alice', 'age': 25}`. "
    "Access with `my_dict['name']` to get 'Alice'!",
]
demo_index = 0


def get_ai_response(messages):
    """Send messages to OpenAI and return the response."""
    global demo_index

    if DEMO_MODE:
        # Simulate a response when no API key is available
        response = DEMO_RESPONSES[demo_index % len(DEMO_RESPONSES)]
        demo_index += 1
        return response

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.7,
            max_tokens=300,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Oops! Something went wrong: {e}"


# --- Main chat loop ---
def main():
    print("=" * 50)
    print("  PyBot - Your Python Tutor")
    print("=" * 50)
    print("Ask me anything about Python!")
    print("Type 'quit' to exit, 'clear' to reset history.")
    if DEMO_MODE:
        print("(Running in demo mode - responses are simulated)")
    print()

    while True:
        # Get user input
        try:
            user_input = input("You: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\n\nGoodbye! Happy coding!")
            break

        # Handle special commands
        if not user_input:
            print("(Please type a question, or 'quit' to exit)\n")
            continue

        if user_input.lower() in ("quit", "exit", "bye", "q"):
            print("\nPyBot: Goodbye! Remember: every expert was once a "
                  "beginner. Keep coding!")
            break

        if user_input.lower() == "clear":
            conversation_history.clear()
            conversation_history.append(system_message)
            print("(Conversation history cleared!)\n")
            continue

        if user_input.lower() == "history":
            print(f"\n(Conversation has {len(conversation_history)} messages)")
            for msg in conversation_history:
                role = msg["role"].upper()
                content = msg["content"][:80] + "..." if len(msg["content"]) > 80 else msg["content"]
                print(f"  [{role}] {content}")
            print()
            continue

        # Add user message to history
        conversation_history.append({
            "role": "user",
            "content": user_input
        })

        # Get AI response
        print("PyBot: ", end="", flush=True)
        response = get_ai_response(conversation_history)
        print(response)
        print()

        # Add assistant response to history
        conversation_history.append({
            "role": "assistant",
            "content": response
        })

        # Warn if history is getting long (costs more tokens!)
        if len(conversation_history) > 20:
            print("(Tip: Type 'clear' to reset the conversation "
                  "if it's getting long. Long histories use more tokens!)\n")


if __name__ == "__main__":
    main()
