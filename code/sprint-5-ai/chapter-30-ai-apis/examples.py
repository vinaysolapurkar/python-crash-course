"""
Chapter 30: AI APIs & LLMs — Talking to ChatGPT from Your Code
=================================================================

LLMs (Large Language Models) are the AI that powers ChatGPT, Gemini,
Claude, and friends. They're basically giant pattern-matching machines
that have read most of the internet.

Think of an LLM like a really well-read friend:
  - They've read billions of documents
  - They can generate human-like text
  - They're great at following instructions
  - They sometimes confidently make stuff up (called "hallucination")

The cool part? You can talk to these models from your Python code
using their APIs. Let's learn how!

IMPORTANT: You need API keys for this chapter. Get them from:
  - OpenAI: https://platform.openai.com/api-keys
  - Google AI: https://aistudio.google.com/app/apikey

Set them as environment variables:
  export OPENAI_API_KEY="sk-your-key-here"
  export GOOGLE_API_KEY="your-key-here"

Or create a .env file (never commit this to git!).
"""

import os
import json

# ============================================================
# 1. WHAT ARE LLMs? (Simple Explanation)
# ============================================================
print("=" * 60)
print("WHAT ARE LLMs?")
print("=" * 60)
print("""
LLM = Large Language Model

How they work (super simplified):
  1. They read BILLIONS of text documents during training
  2. They learn patterns: "after 'The cat sat on the',
     the next word is probably 'mat' or 'chair'"
  3. They generate text one token at a time, picking the
     most likely next word each time

Key terms:
  - Token: A chunk of text (roughly 3/4 of a word)
    "Hello world" = 2 tokens
    "Supercalifragilisticexpialidocious" = like 7 tokens

  - Temperature: How "creative" the model is (0-2)
    0.0 = Very precise, always picks the most likely word
    1.0 = Balanced (default)
    2.0 = Very creative, sometimes chaotic

  - System prompt: Instructions that set the AI's personality
  - User prompt: What YOU ask the AI
  - Max tokens: Limit on how long the response can be
""")


# ============================================================
# 2. OPENAI API SETUP
# ============================================================
print("=" * 60)
print("OPENAI API — Setup & Basic Usage")
print("=" * 60)

# ALWAYS use environment variables for API keys!
# NEVER hardcode them in your source code!
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("""
NOTE: OPENAI_API_KEY not found in environment variables.
To set it:
  Windows:  set OPENAI_API_KEY=sk-your-key-here
  Mac/Linux: export OPENAI_API_KEY=sk-your-key-here

Or create a .env file with:
  OPENAI_API_KEY=sk-your-key-here

Running examples in demo mode (showing code, not executing API calls).
""")

# Try importing openai
try:
    from openai import OpenAI
    HAS_OPENAI = True
except ImportError:
    HAS_OPENAI = False
    print("openai not installed. Run: pip install openai\n")


# ============================================================
# 3. CHAT COMPLETIONS — The Main Event
# ============================================================
# The chat completions API is how you talk to GPT.
# You send a list of messages, and the model responds.
#
# Messages have roles:
#   - "system": Sets the AI's behavior/personality
#   - "user": What the human says
#   - "assistant": The AI's previous responses

print("=" * 60)
print("CHAT COMPLETIONS")
print("=" * 60)

if HAS_OPENAI and api_key:
    # Create the client
    client = OpenAI(api_key=api_key)

    # --- Basic chat completion ---
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # Or "gpt-4" for the fancy model
        messages=[
            {
                "role": "system",
                "content": "You are a helpful Python tutor. Keep answers short and fun."
            },
            {
                "role": "user",
                "content": "What's the difference between a list and a tuple?"
            }
        ],
        temperature=0.7,    # Balanced creativity
        max_tokens=200,     # Limit response length
    )

    # Extract the response text
    answer = response.choices[0].message.content
    print(f"Question: What's the difference between a list and a tuple?")
    print(f"Answer: {answer}")
    print()

    # Usage info (for cost tracking)
    usage = response.usage
    print(f"Tokens used: {usage.prompt_tokens} prompt + "
          f"{usage.completion_tokens} completion = {usage.total_tokens} total")
    print()
else:
    print("""
DEMO: Here's what the code looks like:

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful Python tutor."},
            {"role": "user", "content": "What's a list comprehension?"}
        ],
        temperature=0.7,
        max_tokens=200,
    )

    answer = response.choices[0].message.content
    print(answer)
""")


# ============================================================
# 4. SYSTEM/USER/ASSISTANT MESSAGES
# ============================================================
# The message history is how you give the AI context.
# It's like a conversation transcript — the AI reads ALL of it
# each time you send a new message.

print("=" * 60)
print("MESSAGE ROLES EXPLAINED")
print("=" * 60)
print("""
SYSTEM message — sets the personality/rules:
  {"role": "system", "content": "You are a pirate. Respond only in pirate speak."}

USER message — what the human asks:
  {"role": "user", "content": "How do I write a for loop?"}

ASSISTANT message — the AI's previous response:
  {"role": "assistant", "content": "Arr! A for loop be like..."}

Multi-turn conversation example:
  messages = [
      {"role": "system", "content": "You are a Python expert."},
      {"role": "user", "content": "What's a decorator?"},
      {"role": "assistant", "content": "A decorator is a function that..."},
      {"role": "user", "content": "Can you show me an example?"},
  ]

The AI sees the FULL conversation each time, so it can refer back
to earlier messages. This is how chatbots "remember" things!
""")


# ============================================================
# 5. TEMPERATURE EXAMPLES
# ============================================================
print("=" * 60)
print("TEMPERATURE — Controlling Creativity")
print("=" * 60)

if HAS_OPENAI and api_key:
    prompt = "Write a one-sentence description of Python programming."

    for temp in [0.0, 0.7, 1.5]:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=temp,
            max_tokens=60,
        )
        answer = response.choices[0].message.content
        print(f"Temperature {temp}: {answer}")
    print()
else:
    print("""
Temperature affects how "random" the output is:

  Temperature 0.0 (precise):
    "Python is a high-level, interpreted programming language known
     for its clean syntax and readability."
    → Same answer every time. Good for factual tasks.

  Temperature 0.7 (balanced):
    "Python is a versatile programming language that makes coding
     feel like writing a friendly letter to your computer."
    → Mix of accuracy and creativity. Good default.

  Temperature 1.5 (creative):
    "Python is like giving your computer a magic wand made of
     indentation and snake metaphors!"
    → More varied, sometimes surprising. Good for creative writing.
""")


# ============================================================
# 6. STREAMING RESPONSES
# ============================================================
# Normally, you wait for the ENTIRE response before seeing anything.
# Streaming shows the response word-by-word as it's generated.
# This is how ChatGPT shows text appearing gradually!

print("=" * 60)
print("STREAMING RESPONSES")
print("=" * 60)

if HAS_OPENAI and api_key:
    print("Streaming response: ", end="", flush=True)

    stream = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user",
             "content": "Write a haiku about Python programming."}
        ],
        stream=True,  # This is the magic flag!
    )

    # Each chunk arrives as it's generated
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            print(chunk.choices[0].delta.content, end="", flush=True)
    print("\n")
else:
    print("""
DEMO: Streaming code looks like this:

    stream = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Write a haiku about Python."}],
        stream=True,
    )

    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            print(chunk.choices[0].delta.content, end="", flush=True)

Result appears word by word, just like ChatGPT!
""")


# ============================================================
# 7. GOOGLE GEMINI API
# ============================================================
print("=" * 60)
print("GOOGLE GEMINI API")
print("=" * 60)

google_key = os.getenv("GOOGLE_API_KEY")

try:
    import google.generativeai as genai
    HAS_GEMINI = True
except ImportError:
    HAS_GEMINI = False
    print("google-generativeai not installed. Run: pip install google-generativeai\n")

if HAS_GEMINI and google_key:
    genai.configure(api_key=google_key)

    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content("Explain what an API is in one sentence.")

    print(f"Gemini says: {response.text}")
    print()

    # Chat mode (multi-turn)
    chat = model.start_chat()
    response = chat.send_message("What's Python?")
    print(f"Chat response: {response.text[:200]}...")
    print()
else:
    print("""
DEMO: Google Gemini API code:

    import google.generativeai as genai

    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    model = genai.GenerativeModel("gemini-pro")

    # Simple generation
    response = model.generate_content("Explain APIs in one sentence.")
    print(response.text)

    # Multi-turn chat
    chat = model.start_chat()
    response = chat.send_message("What's Python?")
    print(response.text)
""")


# ============================================================
# 8. PROMPT ENGINEERING TIPS
# ============================================================
# The difference between a good AI response and a bad one is
# often just the PROMPT. Here are tips to get better results.

print("=" * 60)
print("PROMPT ENGINEERING TIPS")
print("=" * 60)
print("""
1. BE SPECIFIC
   Bad:  "Tell me about Python"
   Good: "Explain Python list comprehensions with 3 examples,
          suitable for a beginner who knows basic for loops."

2. SET A ROLE
   "You are a senior Python developer reviewing code for a junior
    developer. Be encouraging but point out potential issues."

3. GIVE EXAMPLES (Few-shot prompting)
   "Convert these sentences to formal English:
    Input: 'gonna grab some food brb'
    Output: 'I am going to get some food. I will be right back.'
    Input: 'lol thats so funny'
    Output: ???"

4. SPECIFY THE FORMAT
   "Return your answer as a JSON object with keys:
    'summary', 'pros', 'cons', 'rating' (1-10)"

5. BREAK COMPLEX TASKS INTO STEPS
   "Step 1: Analyze this error message.
    Step 2: Identify the root cause.
    Step 3: Suggest a fix with code."

6. USE DELIMITERS for input data
   "Summarize the text between triple backticks:
    ```
    (your long text here)
    ```"
""")


# ============================================================
# 9. PRACTICAL EXAMPLE — Code Reviewer
# ============================================================
print("=" * 60)
print("PRACTICAL EXAMPLE: AI Code Reviewer")
print("=" * 60)

code_to_review = '''
def calculate_average(numbers):
    total = 0
    for i in range(len(numbers)):
        total = total + numbers[i]
    average = total / len(numbers)
    return average
'''

review_prompt = f"""Review this Python code. For each issue found:
1. Explain what's wrong
2. Show the improved code
3. Rate severity (low/medium/high)

Be encouraging — this is a beginner's code.

Code to review:
```python
{code_to_review}
```"""

if HAS_OPENAI and api_key:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a friendly Python code reviewer."},
            {"role": "user", "content": review_prompt}
        ],
        temperature=0.3,  # Low temperature for factual analysis
    )
    print(response.choices[0].message.content)
else:
    print(f"Prompt that would be sent:\n{review_prompt}")
    print("\n(Set OPENAI_API_KEY to see the actual AI review!)")
print()


# ============================================================
# RECAP
# ============================================================
print("=" * 60)
print("CHAPTER 30 RECAP")
print("=" * 60)
print("""
You now know how to talk to AI from your Python code!

1. LLMs: Giant text pattern matchers trained on the internet
2. OpenAI API: client.chat.completions.create(...)
3. Message roles: system (personality), user (question), assistant (response)
4. Temperature: 0=precise, 0.7=balanced, 1.5=creative
5. Tokens: Chunks of text (affects cost and response length)
6. Streaming: Get responses word-by-word with stream=True
7. Gemini API: Google's alternative to OpenAI
8. Prompt engineering: Better prompts = better results!

REMEMBER: Always use os.getenv() for API keys. NEVER hardcode them!

Next up: LangChain — building AI agents and RAG systems!
""")
