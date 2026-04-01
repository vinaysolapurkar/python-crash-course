# Chapter 30: AI APIs & LLMs: Building with OpenAI, Gemini & More

> **Sprint 5, Chapter 30** | **12 min read** | **Code: [github link](https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/sprint-5-ai/chapter-30-ai-apis/)**

LLMs are like having a very smart intern. They can write, summarize, translate, and answer questions -- but they need clear instructions and sometimes make stuff up with total confidence. Sound like anyone you know from college group projects? The key difference: this intern works 24/7, never complains, and you can build an entire product around them.

You're about to build apps that use the same technology behind ChatGPT. Take a moment. This is genuinely cool.

## What You'll Learn
- What LLMs are (simple, no PhD required)
- OpenAI API setup and your first API call
- Chat completions -- the core of everything
- System, user, and assistant messages
- Temperature -- the creativity dial
- Tokens -- how AI measures text
- Streaming responses
- Google Gemini API basics
- Prompt engineering fundamentals

## Why Should I Care?

ChatGPT, Gemini, Claude -- you've used them. Now you're going to build with them. This is the most in-demand skill in tech right now. Job postings that mention "LLM" or "AI integration" have exploded. Companies are building AI features into everything: customer support bots, content generators, code assistants, data analyzers. And the developers building these features? They're using the exact APIs you're about to learn.

The barrier to entry has never been lower. You don't need to train a model. You don't need a GPU. You just need an API key and Python. You have both.

## What LLMs Are (Simple Version)

LLM stands for Large Language Model. Here's what it actually is:

1. Someone fed the model billions of pages of text (books, websites, code, conversations)
2. The model learned patterns: what words tend to follow other words, how ideas connect, how questions get answered
3. When you give it a prompt, it generates the most likely next words based on everything it learned

That's it. It's a very sophisticated text predictor. It's not thinking. It's not conscious. It's just incredibly good at producing text that looks like a human wrote it. The "large" part means it has billions of parameters (settings) that were tuned during training.

Think of it like autocomplete on your phone, but trained on the entire internet and a thousand times more sophisticated.

## OpenAI API Setup

### Step 1: Get an API Key

1. Go to [platform.openai.com](https://platform.openai.com)
2. Sign up or log in
3. Go to API Keys (in the left sidebar or settings)
4. Click "Create new secret key"
5. Copy it immediately -- you won't see it again

> **Warning:** Your API key is like a password. Never put it in your code. Never commit it to GitHub. Never share it. People scan GitHub for leaked keys and will run up your bill.

### Step 2: Install the Package

```bash
pip install openai
```

### Step 3: Set Up Your Environment Variable

The safe way to use your API key:

**Windows (Command Prompt):**
```bash
set OPENAI_API_KEY=sk-your-key-here
```

**Mac/Linux (Terminal):**
```bash
export OPENAI_API_KEY=sk-your-key-here
```

Or create a `.env` file (never commit this file):

```
OPENAI_API_KEY=sk-your-key-here
```

And use it with `python-dotenv`:

```bash
pip install python-dotenv
```

```python
from dotenv import load_dotenv
import os

load_dotenv()  # Reads .env file
api_key = os.getenv("OPENAI_API_KEY")
```

## Your First API Call

Here it is. Your first conversation with an AI, in code:

```python
from openai import OpenAI

client = OpenAI()  # Reads OPENAI_API_KEY from environment

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": "Explain Python lists in one sentence."}
    ]
)

print(response.choices[0].message.content)
# "Python lists are ordered, mutable collections that can hold
#  items of any data type, accessed by index position."
```

That's it. You just called the same AI that powers ChatGPT. From your own Python code. Five lines (not counting the import).

> **Don't Panic:** The API is literally just sending text and getting text back. If you've used the `requests` library (Chapter 21), this is the same concept -- you send data to a server, it sends data back. The OpenAI library just wraps that into a clean interface.

## Chat Completions: The Core API

Every ChatGPT-style interaction is a **chat completion**. You send a list of messages, and the API sends back a response. The messages have roles:

### System, User, Assistant

```python
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "system",
            "content": "You are a helpful Python tutor. Explain concepts simply, "
                       "use analogies, and always include a code example."
        },
        {
            "role": "user",
            "content": "What are decorators?"
        }
    ]
)

print(response.choices[0].message.content)
```

The three roles:
- **system**: Sets the AI's personality and rules. "You are a pirate. Only respond in pirate speak." The AI will follow this for the entire conversation.
- **user**: That's you (or your user). The question or instruction.
- **assistant**: The AI's previous responses. Used to give the AI memory of the conversation.

### Multi-Turn Conversations

To have a back-and-forth conversation, include the history:

```python
messages = [
    {"role": "system", "content": "You are a friendly Python tutor."},
    {"role": "user", "content": "What's a list?"},
    {"role": "assistant", "content": "A list is an ordered collection of items. "
                                      "Think of it like a shopping list!"},
    {"role": "user", "content": "How do I add items to it?"}
]

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages
)

print(response.choices[0].message.content)
# The AI knows we're talking about lists because it can see the conversation history
```

The AI doesn't have memory between API calls. Every call is independent. You create the illusion of memory by sending the entire conversation each time. More on this in Chapter 31.

## Temperature: The Creativity Dial

Temperature controls how creative (or random) the AI's responses are:

```python
# Temperature 0: Focused, deterministic, predictable
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Write a one-line Python function to add two numbers."}],
    temperature=0
)
print(response.choices[0].message.content)
# def add(a, b): return a + b
# (Same answer every time)

# Temperature 1: Creative, varied, sometimes surprising
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Write a poem about Python programming."}],
    temperature=1
)
print(response.choices[0].message.content)
# (Different poem every time you run it)
```

Rules of thumb:
- **Temperature 0**: Code generation, factual answers, data extraction. You want consistency.
- **Temperature 0.3-0.7**: General conversation, explanations. Balanced.
- **Temperature 0.7-1.0**: Creative writing, brainstorming, poetry. You want variety.

## Tokens: How AI Measures Text

LLMs don't read words -- they read **tokens**. A token is roughly 3/4 of a word. "Hello, world!" is about 3 tokens. A page of text is around 500-700 tokens.

Why do you care? Because you're **billed per token**. Both the tokens you send (input) and the tokens the AI generates (output).

```python
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Explain Python in 50 words."}],
    max_tokens=100  # Limit the response length
)

# Check token usage
print(f"Input tokens: {response.usage.prompt_tokens}")
print(f"Output tokens: {response.usage.completion_tokens}")
print(f"Total tokens: {response.usage.total_tokens}")
# Input tokens: 14
# Output tokens: 62
# Total tokens: 76
```

> **Pro Tip:** `gpt-4o-mini` is cheap and fast -- perfect for learning and most applications. `gpt-4o` is more capable but costs more. Start with mini, upgrade only if you need better quality.

## Streaming Responses

Instead of waiting for the entire response, you can stream it word by word -- just like ChatGPT does:

```python
stream = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Tell me a short joke about Python."}],
    stream=True
)

for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)

print()  # New line at the end
```

This prints the response as it's generated, creating that satisfying "typing" effect. For chatbots and interactive apps, streaming makes the experience feel much faster because the user starts seeing words immediately.

## Practical Examples

### Example 1: Code Explainer

```python
def explain_code(code_snippet):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are a Python expert. Explain code simply, "
                           "line by line. Use plain English. Assume the reader "
                           "is a beginner."
            },
            {
                "role": "user",
                "content": f"Explain this code:\n\n```python\n{code_snippet}\n```"
            }
        ],
        temperature=0.3
    )
    return response.choices[0].message.content

code = """
result = [x**2 for x in range(10) if x % 2 == 0]
"""

print(explain_code(code))
```

### Example 2: Text Summarizer

```python
def summarize(text, max_sentences=3):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": f"Summarize the following text in {max_sentences} sentences "
                           f"or fewer. Be concise and capture the key points."
            },
            {
                "role": "user",
                "content": text
            }
        ],
        temperature=0.3
    )
    return response.choices[0].message.content

article = """
Python is a high-level, general-purpose programming language. Its design philosophy
emphasizes code readability with the use of significant indentation. Python is
dynamically typed and garbage-collected. It supports multiple programming paradigms,
including structured, object-oriented, and functional programming. It was created
by Guido van Rossum and first released in 1991. Python consistently ranks as one
of the most popular programming languages.
"""

print(summarize(article))
```

### Example 3: JSON Generator

```python
import json

def generate_quiz(topic, num_questions=3):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "Generate quiz questions. Respond ONLY with valid JSON. "
                           "Format: [{\"question\": \"...\", \"options\": [\"A\", \"B\", \"C\", \"D\"], "
                           "\"answer\": \"A\"}]"
            },
            {
                "role": "user",
                "content": f"Create {num_questions} multiple choice questions about {topic}."
            }
        ],
        temperature=0.7
    )

    quiz = json.loads(response.choices[0].message.content)
    return quiz

questions = generate_quiz("Python lists")
for i, q in enumerate(questions, 1):
    print(f"\n{i}. {q['question']}")
    for opt in q["options"]:
        print(f"   {opt}")
    print(f"   Answer: {q['answer']}")
```

## Google Gemini API

Google's Gemini is another powerful LLM. The API works similarly:

```bash
pip install google-generativeai
```

```python
import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-2.0-flash")

response = model.generate_content("Explain Python decorators in simple terms.")
print(response.text)
```

Multi-turn conversation with Gemini:

```python
chat = model.start_chat()

response = chat.send_message("What's a Python list?")
print(response.text)

response = chat.send_message("How do I sort one?")
print(response.text)  # Knows we're talking about lists
```

Gemini has a generous free tier, which makes it great for learning and prototyping. The API is slightly simpler than OpenAI's, and the models are competitive in quality.

> **Pro Tip:** You don't have to pick one. Many production apps use multiple LLMs -- OpenAI for some tasks, Gemini for others, Claude for yet others. The APIs are similar enough that switching is easy.

## Prompt Engineering: 5 Practical Tips

The quality of the AI's output depends hugely on the quality of your prompt. Here are five tips that make a massive difference:

### 1. Be Specific

```python
# Bad
messages = [{"role": "user", "content": "Write about Python."}]

# Good
messages = [{"role": "user", "content": "Write a 200-word beginner-friendly explanation "
             "of Python list comprehensions, with 2 code examples."}]
```

### 2. Give It a Role

```python
# The system message is your secret weapon
messages = [
    {"role": "system", "content": "You are a senior Python developer with 15 years "
                                   "of experience. You write clean, well-commented code "
                                   "and explain your reasoning."},
    {"role": "user", "content": "Write a function to validate email addresses."}
]
```

### 3. Show Examples (Few-Shot Prompting)

```python
messages = [
    {"role": "system", "content": "Convert natural language to Python code."},
    {"role": "user", "content": "Add up all numbers from 1 to 100"},
    {"role": "assistant", "content": "total = sum(range(1, 101))"},
    {"role": "user", "content": "Find the longest word in a sentence"},
    {"role": "assistant", "content": "longest = max(sentence.split(), key=len)"},
    {"role": "user", "content": "Count how many times 'a' appears in a string"}
]
# The AI now understands the format: natural language in, one-liner out
```

### 4. Specify the Output Format

```python
messages = [
    {"role": "system", "content": "Always respond in this exact format:\n"
                                   "ANSWER: [your answer]\n"
                                   "CONFIDENCE: [high/medium/low]\n"
                                   "EXPLANATION: [one sentence]"},
    {"role": "user", "content": "What is the time complexity of Python's sort()?"}
]
```

### 5. Use Chain of Thought

```python
messages = [
    {"role": "user", "content": "A store sells notebooks for $4 each and pens for $1.50 each. "
                                 "Sarah buys 3 notebooks and 5 pens. How much does she spend? "
                                 "Think step by step."}
]
# Adding "Think step by step" dramatically improves accuracy on reasoning tasks
```

## Building a Simple Chatbot

Let's put it all together -- a command-line chatbot:

```python
from openai import OpenAI

client = OpenAI()

messages = [
    {
        "role": "system",
        "content": "You are a friendly Python tutor named PyBot. You explain "
                   "concepts simply, use analogies, and always include short "
                   "code examples. Keep responses under 150 words."
    }
]

print("PyBot: Hi! I'm PyBot, your Python tutor. Ask me anything! (type 'quit' to exit)\n")

while True:
    user_input = input("You: ").strip()

    if user_input.lower() in ["quit", "exit", "bye"]:
        print("PyBot: Happy coding! Remember: the best way to learn is to build stuff. Bye!")
        break

    if not user_input:
        continue

    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        temperature=0.7
    )

    assistant_message = response.choices[0].message.content
    messages.append({"role": "assistant", "content": assistant_message})

    print(f"\nPyBot: {assistant_message}\n")
```

Run it. You just built a chatbot. It remembers context (because we keep appending to `messages`), it has a personality (because of the system message), and it's genuinely useful.

## Your Turn: Python Q&A Chatbot

Create `python_chatbot.py` and build an enhanced chatbot:

```python
from openai import OpenAI

client = OpenAI()

# 1. Create a system message that makes the AI:
#    - A Python expert
#    - Always includes code examples
#    - Asks follow-up questions to check understanding
#    - Keeps answers concise

# 2. Add a conversation history (list of messages)

# 3. Build the chat loop:
#    - Get user input
#    - Send to API with full conversation history
#    - Print the response
#    - Handle 'quit' to exit

# 4. BONUS: Add a "clear" command that resets the conversation

# 5. BONUS: Add error handling for API failures
#    (What if the API is down or the key is wrong?)

# 6. BONUS: Save the conversation to a text file when the user quits
```

Ideas to try:
- Ask it to explain decorators
- Ask it to write a function, then ask it to improve it
- Ask it to create a quiz about lists
- Ask it to debug a piece of broken code

## TL;DR

- LLMs are sophisticated text predictors trained on massive amounts of data -- not magic, not thinking
- **OpenAI API**: `pip install openai`, set `OPENAI_API_KEY`, call `client.chat.completions.create()`
- Messages have roles: **system** (personality), **user** (you), **assistant** (AI's responses)
- **Temperature**: 0 = focused/consistent, 1 = creative/varied
- **Tokens**: how AI measures text (~4 characters per token); you're billed per token
- **Streaming**: `stream=True` gives you the typing effect
- **Gemini** works similarly: `pip install google-generativeai`, same concepts
- **Prompt engineering** matters: be specific, give roles, show examples, specify format
- The API is just sending text and getting text back -- you already know how to do this
- You're building AI-powered applications now. This is not a drill.
