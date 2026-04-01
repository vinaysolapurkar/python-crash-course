# Python Crash Course: From Zero to AI

## The Fun, Step-by-Step Guide to Python Programming

### Learn Python with Humor, Hands-On Projects, and Real-World AI Applications

---

*"The programming book that doesn't put you to sleep."*


---

# Copyright

**Python Crash Course: From Zero to AI**

Copyright (c) 2026. All rights reserved.

No part of this publication may be reproduced, distributed, or transmitted in any form or by any means, including photocopying, recording, or other electronic or mechanical methods, without the prior written permission of the author, except in the case of brief quotations embodied in critical reviews and certain other noncommercial uses permitted by copyright law.

**First Edition: 2026**

While every precaution has been taken in the preparation of this book, the author assumes no responsibility for errors or omissions, or for damages resulting from the use of the information contained herein. Python and the Python logos are trademarks of the Python Software Foundation.

All code examples in this book are available at the companion GitHub repository and are provided under the MIT License for educational use.

ISBN: [To be assigned by KDP]

---

# Dedication

*To every person who's ever Googled "how to learn coding" at 2 AM, convinced that programming isn't for them.*

*It is. This book will prove it.*

*And to coffee - the real MVP behind every line of code ever written.*

---

# How to Use This Book

Welcome, future Python developer! Before we dive in, let me explain how this book works so you can get the most out of it.

## The Sprint Model

This book is organized into **5 Sprints** - think of them like levels in a video game. Each Sprint is a collection of short chapters that build on each other, and each Sprint ends with a checkpoint project that ties everything together.

| Sprint | Theme | Chapters | You'll Build |
|----|----|-----|-------|
| 1 | Python Basics | 1-8 | Mad Libs Generator |
| 2 | Intermediate Python | 9-14 | Expense Tracker |
| 3 | Object-Oriented Programming | 15-18 | Library Management System |
| 4 | Pro Python | 19-25 | Job Listing Scraper |
| 5 | Python x AI | 26-32 | AI Resume Analyzer |

After all 5 Sprints, there's a **Final Zone** with 10 progressive projects you can add to your portfolio. Each one builds on skills from the previous project.

## The Rhythm: Read, Do, Come Back

Each chapter is designed as a **10-15 minute read**. That's it. No hour-long marathons required.

Here's the rhythm:

1. **Read** a short chapter (10-15 minutes)
2. **Do** the "Your Turn" exercise at the end (2-5 minutes)
3. **Take a break** - grab a snack, scroll TikTok, pet your dog
4. **Come back** for the next chapter when you're ready

This book is built for how your brain actually works. Short bursts. Immediate practice. No guilt if you take a day off between chapters.

## The Companion GitHub Repository

Every code example, exercise, and project in this book lives in a GitHub repository:

**https://github.com/vinaysolapurkar/python-crash-course**

Each chapter folder contains:
- `examples.py` - All the code examples from the chapter
- `exercises/your_turn.py` - The exercise starter (try this first!)
- `exercises/solution.py` - The complete solution (no peeking... okay, maybe a little)

You don't *need* the repo to follow along - all the code is right here in the book. But the repo is helpful if you want to run the examples without typing everything out.

## Callout Boxes

Throughout the book, you'll see special boxes that highlight important information:

**Your Turn** - The hands-on exercise at the end of each chapter. Don't skip these! Doing > reading.

**TL;DR** - A 3-5 bullet summary of the chapter. Great for quick review or when you come back after a break.

**Pro Tip** - Shortcuts and insights for readers who already know another programming language. If you're a complete beginner, feel free to skip these.

**Wait, What?** - Preemptive answers to the questions I know you're about to ask. "But wait, why does...?" - I got you.

**Don't Panic** - You'll see these before harder topics. They're a reminder that the concept looks scarier than it is, and you already know most of what you need.

**Remember When?** - Callbacks to earlier chapters. "Remember lists? Generators are just lazy lists." These help connect new concepts to things you already understand.

**Why Should I Care?** - Real-world motivation for a concept. Before I explain *how* something works, I'll show you *why* it matters.

**Fun Fact** - Interesting trivia about Python, programming, or tech. Because learning should be entertaining.

**Portfolio Tip** - Advice on how to present your projects to employers. Because this book isn't just about learning - it's about building a career.

## One Last Thing

This book has exactly one rule: **No shame in looking at the solution.**

Seriously. If you're stuck on an exercise for more than 10 minutes, look at the solution, understand it, then close it and try again from scratch. That's not cheating - that's learning.

The only way to fail at this book is to not start it.

So let's start it.

---

# What You'll Need

Before we write our first line of Python, let's make sure you've got everything set up. Don't worry - it's all free.

## 1. Python 3.12 or Later

Python is the language we're learning. You need to install it on your computer.

**Windows:**
1. Go to python.org/downloads
2. Click the big yellow "Download Python 3.12" button
3. Run the installer
4. **IMPORTANT:** Check the box that says "Add Python to PATH" - this is the one thing everyone forgets, and it causes 90% of setup headaches
5. Click "Install Now"

**Mac:**
1. Go to python.org/downloads
2. Download the macOS installer
3. Run it and follow the prompts
4. That's it. Macs are easier here.

**Linux:**
You probably already have Python installed. You're running Linux, after all. But just in case:
```
sudo apt update
sudo apt install python3 python3-pip
```

**Verify it works:** Open a terminal (Command Prompt on Windows, Terminal on Mac/Linux) and type:
```
python -version
```
You should see something like `Python 3.12.x`. If you see `Python 2.x`, try `python3 -version` instead.

## 2. VS Code (Visual Studio Code)

VS Code is the code editor we'll use. It's free, powerful, and used by millions of developers.

1. Go to code.visualstudio.com
2. Download and install it
3. Open VS Code and install the **Python extension** (click the Extensions icon on the left sidebar, search "Python", install the one by Microsoft)

That's your coding setup done. Fancy IDEs are nice, but VS Code is all you need.

## 3. A GitHub Account

We'll use GitHub to access the companion code repository, and later you'll use it to showcase your projects to employers.

1. Go to github.com
2. Sign up for a free account
3. That's it for now - we'll use it more in later chapters

## 4. An Internet Connection

You need this for:
- Downloading packages (starting from Sprint 4)
- Working with APIs (Sprint 4-5)
- AI features (Sprint 5)

Sprints 1-3 work completely offline once you've installed Python.

## 5. A Sense of Humor

Mandatory. If you can't laugh at a bad programming joke, this might not be the book for you.

Just kidding. But the jokes are staying.

---

**That's the full setup.** Five things. You probably already have most of them.

Now let's write some Python.

---

# Welcome to Sprint 1: The Basics

> **Chapters 1-8** | **Estimated Time: 2-3 hours** | **Difficulty: Absolute Beginner**

Hey, you made it! Whether you're here because you want to break into tech, automate the boring stuff at work, or you just saw one too many "learn to code" TikToks at 2 AM - welcome. You're in the right place.

Sprint 1 is where we build your foundation. Think of it like the tutorial level in a video game. Yeah, you have to learn how to move and jump before you fight the boss. But I promise we'll make it fun, and you'll be writing real code from the very first chapter.

## What You'll Learn

Over the next eight chapters, you're going to go from "what is a variable?" to confidently working with data, making decisions in code, and looping through stuff like a pro. Here's the lineup:

- **Chapter 1:** Why Python rocks and writing your first program
- **Chapter 2:** Variables - giving names to stuff
- **Chapter 3:** Numbers, math, and getting input from users
- **Chapter 4:** Strings - slicing, dicing, and formatting text
- **Chapter 5:** Making decisions with if/elif/else
- **Chapter 6:** Lists - your first data superpower
- **Chapter 7:** Loops - doing things on repeat without losing your mind
- **Chapter 8:** Tuples and sets - lists' lesser-known cousins

## The Sprint 1 Project: Mad Libs Generator

By the end of this sprint, you'll build a **Mad Libs Generator** from scratch. It takes user input, stores it, manipulates text, makes decisions, and loops - basically everything you'll learn, wrapped up in one goofy project. You won't even realize how much Python you've learned until you look at what you built.

No prior experience needed. No CS degree. No "math brain." Just you, your computer, and a willingness to type stuff and see what happens.

Let's go.

---

# Chapter 1: Why Python? (And Why You Won't Regret This)

> **Sprint 1** | **10 min read** | **Code: [github link](https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/sprint-1-basics/chapter-01-why-python/)**

If programming languages were Avengers, Python would be Iron Man. Not because it's the flashiest (that's JavaScript with its fancy websites), but because it's ridiculously versatile, it's everywhere, and it makes you feel like a genius even when you're just getting started. Also, much like Tony Stark, Python has a witty response for everything - its error messages actually make sense.

## What You'll Learn
- Why Python is the most popular beginner language on the planet
- What you'll build by the end of this book
- How to install Python and VS Code
- How to write and run your very first program

## Why Python is Kind of a Big Deal

Let me hit you with some names: **Netflix**, **Instagram**, **Spotify**, **NASA**, **Google**. What do they have in common? They all use Python. Heavily.

Netflix uses Python to recommend which shows to binge next. Instagram's entire backend started with Python. NASA uses it to process space data. And the entire AI revolution - ChatGPT, image generators, self-driving cars - is built primarily in Python.

But here's the real reason you should learn Python: **it reads like English.** Seriously, compare these:

**Java (the "formal email" of programming):**
```java
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
```

**Python (the "text message" of programming):**
```python
print("Hello, World!")
```

One line. That's it. No curly braces, no semicolons, no "public static void" nonsense. Python respects your time.

## What You'll Build in This Book

Here's a sneak peek at what's coming. By the end of this book, you'll have built:

- A **Mad Libs Generator** (Sprint 1 project)
- A **Personal Finance Tracker** (Sprint 2)
- A **Web Scraper** that grabs real data from websites (Sprint 3)
- A **REST API** (Sprint 4)
- An **AI-powered app** using real machine learning (Sprint 5)

And you'll understand every single line of code. No copy-pasting from Stack Overflow and praying it works. (Okay, maybe a little. We all do it.)

## Installing Python

Time to get our hands dirty. This part takes about 5 minutes.

### Windows

1. Go to [python.org/downloads](https://python.org/downloads)
2. Click the big yellow "Download Python 3.x" button
3. Run the installer
4. **CRITICAL STEP:** Check the box that says **"Add Python to PATH"** at the bottom of the installer. I cannot stress this enough. If you skip this, nothing will work and you'll think programming is broken. It's not. You just forgot the checkbox.
5. Click "Install Now"

### Mac

1. Go to [python.org/downloads](https://python.org/downloads)
2. Download the macOS installer
3. Run it, click through the prompts
4. Mac comes with an older Python pre-installed, but you want the latest version from python.org

### Linux

You probably already have Python installed because you're running Linux and therefore already mass the "technically inclined" vibe check. But just in case:

```bash
sudo apt update
sudo apt install python3 python3-pip
```

### Verify It Worked

Open a terminal (Command Prompt on Windows, Terminal on Mac/Linux) and type:

```bash
python -version
```

You should see something like `Python 3.12.x`. If you see that, you're golden. If Windows gives you an error, try `python3 -version` instead.

> **Wait, What?** On some systems, `python` points to Python 2 (which is ancient and retired). If `python -version` shows `2.x`, use `python3` for everything in this book.

## Installing VS Code

You *could* write Python in Notepad. You could also cut your lawn with scissors. Let's use the right tool.

1. Go to [code.visualstudio.com](https://code.visualstudio.com)
2. Download and install for your operating system
3. Open VS Code
4. Click the Extensions icon on the left sidebar (it looks like four little squares)
5. Search for **"Python"** and install the one by Microsoft (it'll be the first result with millions of downloads)
6. While you're at it, search for **"Pylance"** and install that too - it gives you autocomplete superpowers

That's your setup. VS Code + Python extension = a fantastic coding experience with syntax highlighting, error detection, and a built-in terminal.

## Your First Program

This is it. The moment. Let's write code.

1. Open VS Code
2. Create a new file: **File > New File**
3. Save it as `hello.py` (the `.py` extension tells your computer "this is Python")
4. Type this:

```python
print("Hello, World!")
```

5. Run it by clicking the play button (triangle) in the top-right corner, or open the terminal in VS Code (View > Terminal) and type:

```bash
python hello.py
```

You should see:

```
Hello, World!
```

Congratulations. You're a programmer now. No, seriously. That's how it starts. Every developer on earth wrote this exact line at some point. You just joined the club.

### So What Just Happened?

Let's break it down:

- `print()` is a **function** - think of it as a command you're giving Python. "Hey Python, show this on the screen."
- `"Hello, World!"` is a **string** - any text wrapped in quotes. Python knows it's text because of the quotes.
- The parentheses `()` are how you hand information to a function. You're saying: "print *this*."

That's it. You gave Python an instruction, and it followed it. That's all programming is - giving instructions to a computer, one line at a time.

Let's try a few more:

```python
print("My name is Inigo Montoya.")
print("You killed my father.")
print("Prepare to die.")
```

Run it. Each `print()` shows up on its own line. You're basically writing a script (pun intended).

> **Fun Fact:** The "Hello, World!" tradition started in 1978 in a book about the C programming language. Nearly 50 years later, we're still doing it. If it ain't broke, don't fix it.

## Your Turn

Time to fly solo. Create a new file called `chapter1_practice.py` and write code that:

1. Prints your name
2. Prints your favorite joke (or a terrible pun - those are better)
3. Prints a math result using `print()`:

```python
print("My name is Ada Lovelace")
print("Why do programmers prefer dark mode? Because light attracts bugs!")
print(42 + 58)
```

Yeah, Python can do math right inside `print()`. We'll get way deeper into that in Chapter 3.

> **Pro Tip:** If you're coming from another language, note that `print()` is a function in Python 3, not a statement. `print "hello"` without parentheses will throw an error. The parentheses aren't optional.

## TL;DR

- Python is the most beginner-friendly, widely-used programming language - powering everything from Instagram to AI
- Install Python from python.org (**check "Add to PATH" on Windows!**)
- Install VS Code + the Python extension for a smooth coding experience
- `print()` displays stuff on the screen - it's your first Python function
- You just wrote your first program. You're officially a programmer. Tell your mom.

---

# Chapter 2: Variables: Giving Names to Stuff

> **Sprint 1** | **10 min read** | **Code: [github link](https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/sprint-1-basics/chapter-02-variables/)**

Imagine your brain had no names for anything. You couldn't say "pass me my phone." You'd have to say "pass me that flat glowing rectangle that I stare at for six hours a day." Names make life easier. Variables are how we give names to stuff in Python.

## What You'll Learn
- What variables are and how to create them
- The four basic data types: strings, integers, floats, and booleans
- How to check a variable's type
- Naming rules that'll keep you out of trouble
- f-strings - the single coolest feature for beginners

## Variables: Labeled Boxes

Think of a variable as a **labeled box**. You write a name on the outside (the variable name), and you put something inside (the value). Later, when you need that thing, you just call it by its label.

```python
player_name = "Zelda"
player_health = 100
player_level = 7.5
is_alive = True
```

That's it. Four variables, four values. Let's break down what's happening:

- `player_name` is a box labeled "player_name" with the text `"Zelda"` inside
- `player_health` is a box with the number `100` inside
- `player_level` has `7.5` (a decimal number)
- `is_alive` has `True` (a yes/no value)

The `=` sign doesn't mean "equals" like in math class. It means **"put this value in this box."** It's an assignment, not a comparison. (We'll get to actual comparison in Chapter 5.)

## The Four Basic Data Types

Python has four types you'll use constantly:

| Type | What It Is | Example |
|---|------|-----|
| `str` | Text (string) | `"Hello"`, `'Netflix'` |
| `int` | Whole number (integer) | `42`, `-7`, `0` |
| `float` | Decimal number | `3.14`, `-0.5`, `99.99` |
| `bool` | True or False (boolean) | `True`, `False` |

Strings need quotes (single `'` or double `"` - Python doesn't care which, just be consistent). Numbers don't get quotes. Booleans are capitalized: `True` and `False`, not `true` or `false`.

```python
movie = "Inception"          # str
year = 2010                  # int
rating = 8.8                 # float
is_mind_bending = True       # bool
```

## The type() Function - What's in the Box?

Ever pick up a mystery package and shake it? Python has a built-in way to check what type of data is in a variable:

```python
movie = "Inception"
year = 2010
rating = 8.8
is_mind_bending = True

print(type(movie))           # <class 'str'>
print(type(year))            # <class 'int'>
print(type(rating))          # <class 'float'>
print(type(is_mind_bending)) # <class 'bool'>
```

`type()` is like an X-ray machine for your variables. Super handy when things break and you're not sure why. (Spoiler: it's usually because something is a string when you thought it was a number.)

## Naming Rules: The Dos and Don'ts

Python has opinions about variable names. Some are hard rules (break them and Python yells at you), and some are style conventions (break them and other programmers judge you silently).

**Hard Rules:**
- Can contain letters, numbers, and underscores
- Must start with a letter or underscore (not a number)
- No spaces
- Case-sensitive (`Name` and `name` are different variables)
- Can't use Python's reserved words (`if`, `for`, `True`, `class`, etc.)

```python
# GOOD variable names
user_name = "Mario"
score_2 = 150
_secret = "hidden"

# BAD - these will crash
# 2nd_place = "Luigi"    # Can't start with a number
# user name = "Peach"    # No spaces allowed
# class = "Warrior"      # 'class' is a reserved word
```

**Style Conventions (snake_case is king):**

```python
# Python style (snake_case) - DO THIS
player_health = 100
max_score = 999
is_game_over = False

# Other languages' style - DON'T do this in Python
playerHealth = 100    # This is camelCase (JavaScript vibes)
MaxScore = 999        # This is PascalCase (C# energy)
MAXSCORE = 999        # ALL CAPS is reserved for constants
```

Use `snake_case`: all lowercase, words separated by underscores. It's the Python way. When in Rome, use underscores.

## f-strings: The Single Coolest Feature for Beginners

Okay, you've got variables. How do you combine them with text? You could do this:

```python
name = "Tony Stark"
age = 48
print("My name is " + name + " and I am " + str(age) + " years old.")
```

That works, but it looks like someone assembled a sentence with duct tape. Enter **f-strings** - the elegant way:

```python
name = "Tony Stark"
age = 48
print(f"My name is {name} and I am {age} years old.")
```

Output:
```
My name is Tony Stark and I am 48 years old.
```

See that little `f` before the opening quote? That tells Python: "Hey, anything inside `{}` is a variable - go grab its value." That's it. No plus signs, no `str()` conversion, no mess.

You can even do math inside the curly braces:

```python
price = 19.99
quantity = 3
print(f"Total: ${price * quantity}")
```

Output:
```
Total: $59.97
```

f-strings are going to be your best friend in this book. We'll use them in almost every chapter from here on out.

> **Fun Fact:** f-strings were added in Python 3.6 (2016). Before that, people used `.format()` and `%` formatting, which were clunkier. If you see old tutorials using `"Hello, {}".format(name)`, that's the old way. f-strings are better in every way.

## Reassigning Variables: It's YOUR Box

Remember the box analogy? You can empty a box and put something new in it whenever you want:

```python
mood = "happy"
print(mood)        # happy

mood = "hungry"
print(mood)        # hungry

mood = "coding"
print(mood)        # coding
```

Each time you assign a new value, the old one is gone. Python doesn't ask "are you sure?" It just does it.

And here's something that trips people up coming from other languages:

```python
x = 10        # x is an integer
x = "ten"     # now x is a string!?
print(type(x)) # <class 'str'>
```

> **Wait, What?** "Why can I put a string in a variable that had a number?" Because Python uses **dynamic typing**. The variable doesn't have a fixed type - the *value* does. The box doesn't care what you put in it. A box that held books can now hold shoes. Python is chill like that.

This is different from languages like Java or C++ where you declare a variable's type upfront and it's locked in forever. Python says: "Nah, live your life."

> **Pro Tip:** If you're coming from JavaScript, Java, or C#, note that Python has no `let`, `const`, `var`, or type declarations. You just write `x = 5` and Python figures out the rest. There's no `int x = 5;` - that semicolon alone will give Python a panic attack.

## Multiple Assignment (The Shortcut)

Feeling fancy? Assign multiple variables in one line:

```python
name, age, city = "Peter Parker", 22, "New York"
print(f"{name}, age {age}, from {city}")
```

Output:
```
Peter Parker, age 22, from New York
```

Or give multiple variables the same value:

```python
x = y = z = 0
print(x, y, z)  # 0 0 0
```

This is handy for initializing counters or scores at the start of a program.

## Your Turn: Build an "About Me" Card

Create a file called `about_me.py` and build a little profile card using variables and f-strings:

```python
# Create these variables with YOUR info
name = "Your Name"
age = 25
city = "Your City"
hobby = "gaming"
favorite_show = "Stranger Things"
python_skill = 1  # on a scale of 1-10

# Print a formatted card
print("=" * 40)
print(f"  Name:          {name}")
print(f"  Age:           {age}")
print(f"  City:          {city}")
print(f"  Hobby:         {hobby}")
print(f"  Favorite Show: {favorite_show}")
print(f"  Python Skill:  {python_skill}/10")
print("=" * 40)
print(f"  {name} will be a {python_skill + 5}/10 by Sprint 3!")
```

Run it. Admire your work. Change the values. Notice how everything updates automatically because you used variables instead of hardcoding the text. That's the power of variables - change one thing, and it ripples everywhere.

**Bonus challenge:** Add a `is_student` boolean variable and use it in an f-string: `f"Student: {is_student}"`

## TL;DR

- **Variables** are labeled boxes that store values: `name = "Zelda"`
- **Four basic types:** `str` (text), `int` (whole numbers), `float` (decimals), `bool` (True/False)
- Use `type()` to check what type a variable is
- **Naming:** use `snake_case`, start with a letter, no spaces, no reserved words
- **f-strings** are the best way to mix variables with text: `f"Hello, {name}!"`
- Python is **dynamically typed** - a variable's type can change. Python doesn't judge.
- You can reassign variables anytime. It's your box. Do what you want with it.

---

# Chapter 3: Numbers & Math: Python is Your New Calculator

> **Sprint 1** | **12 min read** | **Code: [github link](https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/sprint-1-basics/chapter-03-numbers-math/)**

Remember when your math teacher said "you won't always have a calculator"? Well, you now have something way better. Python can do everything your TI-84 could do, plus a million things it couldn't. And unlike your math teacher, Python never judges you for using it.

## What You'll Learn
- Every math operator Python offers
- Order of operations (yes, PEMDAS matters here too)
- Why `"5"` is NOT the same as `5`
- How to get input from users
- Handy built-in math functions

## All the Math Operators

Python's arithmetic operators work exactly like you'd expect, with a couple of bonus ones your calculator didn't have:

```python
print(10 + 3)    # 13    Addition
print(10 - 3)    # 7     Subtraction
print(10 * 3)    # 30    Multiplication
print(10 / 3)    # 3.333 Division (always returns a float!)
print(10 // 3)   # 3     Floor division (rounds down, no decimals)
print(10 % 3)    # 1     Modulo (the remainder)
print(10 ** 3)   # 1000  Exponentiation (10 to the power of 3)
```

A few things to note:

**Regular division `/` always gives you a float**, even when it divides evenly:

```python
print(10 / 2)    # 5.0 (not 5)
```

**Floor division `//` drops the decimals** - it doesn't round, it chops:

```python
print(7 // 2)    # 3 (not 3.5, not 4... just 3)
```

**Modulo `%` gives you the remainder.** This one seems random but it's crazy useful. Need to check if a number is even? If `number % 2 == 0`, it's even. Need to cycle through colors? Modulo. It shows up everywhere.

```python
print(10 % 3)   # 1 (10 / 3 = 3 remainder 1)
print(10 % 2)   # 0 (10 is even - no remainder)
print(7 % 2)    # 1 (7 is odd)
```

> **Fun Fact:** The `**` operator is Python's way of doing exponents. Other languages use `^` for this, but in Python, `^` does something completely different (bitwise XOR - don't worry about it yet). So `2 ** 10` gives you 1024, not `2 ^ 10`.

## PEMDAS: Order of Operations

Python follows the same order of operations you learned in school. Remember PEMDAS? (Some people learned BODMAS or BEDMAS - same thing, different accent.)

**P**arentheses > **E**xponents > **M**ultiplication/**D**ivision > **A**ddition/**S**ubtraction

```python
result = 2 + 3 * 4
print(result)    # 14 (not 20!)
```

Python does `3 * 4` first (12), then adds 2. If you want addition first, use parentheses:

```python
result = (2 + 3) * 4
print(result)    # 20
```

When in doubt, add parentheses. They make your code clearer AND ensure the right order. Nobody ever got fired for using too many parentheses.

```python
# Hard to read:
total = price * quantity + price * quantity * tax_rate - discount

# Much clearer:
total = (price * quantity) + (price * quantity * tax_rate) - discount
```

## Augmented Assignment: The Shortcuts

Updating a variable with math is so common that Python has shortcuts:

```python
score = 100

score = score + 10   # The long way
score += 10          # The shortcut (same thing)

score -= 5           # score = score - 5
score *= 2           # score = score * 2
score /= 4           # score = score / 4
score //= 3          # score = score // 3
score %= 7           # score = score % 7
score **= 2          # score = score ** 2
```

`+=` is by far the most common. You'll see it everywhere. It just means "add this to whatever's already there."

```python
lives = 3
lives -= 1
print(f"Lives remaining: {lives}")  # Lives remaining: 2
```

## Type Conversion: When "5" Isn't 5

Here's where it gets spicy. Look at this:

```python
a = "5"
b = "3"
print(a + b)  # "53"
```

Wait, what? 5 + 3 = 53? Nope. `"5"` and `"3"` are **strings** (they have quotes), not numbers. When you `+` two strings, Python glues them together. This is called **concatenation**, and it's one of the most common beginner bugs.

> **Wait, What?** "Why did my addition give me '55' instead of 10?" Because your numbers are secretly strings! This happens ALL the time with `input()` (which we'll cover in a second). The fix: convert them to numbers with `int()` or `float()`.

The fix is **type conversion**:

```python
a = "5"
b = "3"
print(int(a) + int(b))    # 8 (now they're integers!)
print(float(a) + float(b)) # 8.0 (now they're floats!)
```

You can convert between types like this:

```python
# String to number
age = int("25")        # 25 (integer)
price = float("9.99")  # 9.99 (float)

# Number to string
score = str(100)       # "100" (string now)
pi = str(3.14)         # "3.14" (string now)

# Float to int (chops the decimal!)
rounded = int(3.99)    # 3 (not 4! it truncates, doesn't round)

# Int to float
precise = float(5)     # 5.0
```

Notice that `int()` doesn't round - it chops. `int(3.99)` is `3`, not `4`. If you want actual rounding, use `round()` (we'll cover that soon).

## The input() Function: Talk to Me

So far, our programs have been monologues. Let's make them conversations. `input()` lets you ask the user for information:

```python
name = input("What's your name? ")
print(f"Hey, {name}! Welcome to the game.")
```

When Python hits `input()`, it pauses, shows the message, and waits for the user to type something and press Enter. Whatever they type gets stored in the variable.

**Here's the critical thing to remember about `input()`:**

**`input()` ALWAYS returns a string.** Always. Even if the user types a number.

```python
age = input("How old are you? ")
print(type(age))  # <class 'str'> - it's a STRING!
```

If someone types `25`, you get the string `"25"`, not the integer `25`. This means you can't do math with it directly:

```python
age = input("How old are you? ")
# print(age + 5)  # ERROR! Can't add a string and an integer

# Do this instead:
age = int(input("How old are you? "))  # Convert immediately
print(f"In 5 years, you'll be {age + 5}")
```

That `int(input(...))` combo is a pattern you'll use a LOT. Burn it into your brain. You're wrapping `input()` inside `int()` so the conversion happens right away.

```python
# The pattern for getting numbers from users:
whole_number = int(input("Enter a number: "))
decimal_number = float(input("Enter a price: "))
```

> **Pro Tip:** If the user types "abc" when you're expecting a number, `int("abc")` will crash your program with a `ValueError`. We'll learn how to handle that gracefully in Sprint 2 with try/except. For now, just trust your users (famous last words).

## Built-in Math Functions

Python comes with some handy math functions right out of the box:

```python
print(abs(-42))         # 42 (absolute value - removes the negative)
print(round(3.7))       # 4 (rounds to nearest integer)
print(round(3.14159, 2)) # 3.14 (rounds to 2 decimal places)
print(max(4, 7, 2, 9))  # 9 (returns the biggest)
print(min(4, 7, 2, 9))  # 2 (returns the smallest)
print(pow(2, 10))        # 1024 (same as 2 ** 10)
```

`round()` is especially useful for money:

```python
total = 19.99 * 3
tax = total * 0.08
final = total + tax

print(f"Total: ${round(final, 2)}")  # Total: $64.77
```

And if you need more advanced math (square roots, trigonometry, logarithms), Python has a `math` module:

```python
import math

print(math.sqrt(144))    # 12.0
print(math.pi)           # 3.141592653589793
print(math.ceil(3.2))    # 4 (rounds UP)
print(math.floor(3.8))   # 3 (rounds DOWN)
```

Don't worry about the `import` line for now. Just know it's there when you need it. We'll cover imports properly in Sprint 2.

## Your Turn: Tip Calculator

Build a tip calculator! Create a file called `tip_calculator.py`:

```python
# Tip Calculator
print("=== Tip Calculator ===")

# Get the bill amount
bill = float(input("What's the total bill? $"))

# Get the tip percentage
tip_percent = int(input("What tip % do you want to give? (15, 18, 20): "))

# Get the number of people splitting
people = int(input("How many people are splitting the bill? "))

# Calculate
tip_amount = bill * (tip_percent / 100)
total = bill + tip_amount
per_person = total / people

# Display results
print(f"\nBill:        ${bill:.2f}")
print(f"Tip ({tip_percent}%):   ${tip_amount:.2f}")
print(f"Total:       ${total:.2f}")
print(f"Per person:  ${round(per_person, 2):.2f}")
```

Run it and calculate some tips! Notice the `:.2f` inside the f-strings? That formats numbers to exactly 2 decimal places. Perfect for money. We'll cover more formatting tricks in Chapter 4.

**Bonus challenge:** Add a "round up" feature that rounds each person's share up to the nearest dollar. (Hint: `math.ceil()`)

## TL;DR

- Python has all the standard math operators plus `//` (floor division), `%` (modulo/remainder), and `**` (exponent)
- PEMDAS order of operations applies - when in doubt, use parentheses
- `"5"` (string) is NOT `5` (integer) - use `int()` or `float()` to convert
- `input()` **always returns a string**, even if the user types a number
- Pattern for numeric input: `int(input("prompt"))` or `float(input("prompt"))`
- Built-in math helpers: `abs()`, `round()`, `max()`, `min()`, `pow()`
- For advanced math, `import math` gives you `sqrt`, `pi`, `ceil`, `floor`, and more

---

# Chapter 4: Strings: Text is Everywhere

> **Sprint 1** | **12 min read** | **Code: [github link](https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/sprint-1-basics/chapter-04-strings/)**

Every text message you've sent, every tweet, every Netflix subtitle, every Google search, every password you've typed - strings. Text is the backbone of computing, and Python is ridiculously good at working with it. By the end of this chapter, you'll be slicing, dicing, and formatting text like a sushi chef.

## What You'll Learn
- Essential string methods that'll make your life easier
- Method chaining - combo moves for strings
- Slicing - cutting strings like a pizza
- Escape characters and raw strings
- f-string formatting superpowers

## String Methods: Your Text Toolkit

Remember how functions like `print()` do things? **Methods** are functions that belong to a specific data type. Strings come with a bunch of built-in methods. Think of them as tools in a Swiss Army knife - each one does something useful.

```python
message = "hello, world"

print(message.upper())       # HELLO, WORLD
print(message.lower())       # hello, world
print(message.title())       # Hello, World
print(message.capitalize())  # Hello, world
print(message.swapcase())    # HELLO, WORLD
```

Notice the pattern? It's `variable.method()`. The dot says "use this method on this string."

Here are the string methods you'll use most often:

```python
text = "  Hello, World!  "

# Cleaning up text
print(text.strip())          # "Hello, World!" (removes leading/trailing spaces)
print(text.lstrip())         # "Hello, World!  " (left side only)
print(text.rstrip())         # "  Hello, World!" (right side only)

# Searching
print(text.strip().startswith("Hello"))  # True
print(text.strip().endswith("!"))        # True
print("World" in text)                    # True (the 'in' keyword!)
print(text.count("l"))                    # 3

# Finding position
print(text.find("World"))    # 9 (index where "World" starts)
print(text.find("Python"))   # -1 (not found)
```

> **Pro Tip:** Python strings are **immutable** - they can't be changed in place. Every string method returns a **new** string. The original stays the same.

```python
name = "tony stark"
name.upper()          # This creates "TONY STARK" but doesn't save it!
print(name)           # Still "tony stark"

name = name.upper()   # NOW it's saved
print(name)           # "TONY STARK"
```

This trips up beginners all the time. If you call a method but don't save the result, nothing happens. It's like making a photocopy but throwing it in the trash.

### Replacing and Splitting

```python
quote = "I am Iron Man"

# Replace parts of a string
print(quote.replace("Iron Man", "Batman"))  # "I am Batman"
print(quote.replace("I", "You"))            # "You am You ron Man" (replaces ALL occurrences!)

# Split a string into a list
colors = "red,green,blue,yellow"
color_list = colors.split(",")
print(color_list)  # ['red', 'green', 'blue', 'yellow']

# Join a list back into a string
print(" | ".join(color_list))  # "red | green | blue | yellow"

# Check content
print("hello123".isalnum())    # True (letters and numbers only)
print("hello".isalpha())       # True (letters only)
print("12345".isdigit())       # True (digits only)
print("hello".islower())       # True
print("HELLO".isupper())       # True
```

`.split()` and `.join()` are a power duo. Split breaks a string apart, join puts pieces back together. You'll use these constantly when working with data.

## Method Chaining: Combo Moves

Why call one method when you can chain several together? Since each method returns a new string, you can call another method on the result:

```python
user_input = "   hElLo WoRlD   "
clean = user_input.strip().lower().replace("world", "Python")
print(clean)  # "hello python"
```

That single line: (1) strips the spaces, (2) lowercases everything, (3) replaces "world" with "Python." Three operations, one line. It reads left to right, each method working on the result of the previous one.

Think of it like combo moves in a fighting game. Individually they're fine, but chaining them together? That's where the real damage happens.

```python
# Cleaning up messy user input in one shot
email = "   User@Example.COM   "
clean_email = email.strip().lower()
print(clean_email)  # "user@example.com"
```

## Slicing: Cutting Strings Like Pizza

Every character in a string has a position number called an **index**. Python starts counting at 0 (yes, programmers are weird):

```
 H   e   l   l   o
 0   1   2   3   4     <- positive index
-5  -4  -3  -2  -1     <- negative index
```

You can grab individual characters with square brackets:

```python
word = "Hello"
print(word[0])    # H (first character)
print(word[1])    # e (second character)
print(word[-1])   # o (last character!)
print(word[-2])   # l (second to last)
```

Negative indices count from the end. `[-1]` is always the last character. Super useful when you don't know how long the string is.

**Slicing** lets you grab a chunk of a string with `[start:stop:step]`:

```python
text = "Hello, World!"

print(text[0:5])     # "Hello" (from 0 up to but NOT including 5)
print(text[7:12])    # "World"
print(text[:5])      # "Hello" (start defaults to 0)
print(text[7:])      # "World!" (goes to the end)
print(text[:])       # "Hello, World!" (copy the whole thing)
print(text[::2])     # "Hlo ol!" (every 2nd character)
print(text[::-1])    # "!dlroW ,olleH" (reversed!)
```

The key thing to remember: `[start:stop]` goes up to but **does not include** the stop index. Think of it like a hotel checkout - you stay until that day but you don't stay *on* that day.

```python
# Practical example: extracting parts of a date
date = "2025-03-15"
year = date[:4]      # "2025"
month = date[5:7]    # "03"
day = date[8:]       # "15"
print(f"{month}/{day}/{year}")  # "03/15/2025"
```

The reverse trick `[::-1]` is a classic Python one-liner and a favorite interview question:

```python
word = "racecar"
print(word == word[::-1])  # True - it's a palindrome!
```

## Escape Characters and Raw Strings

What if you need a quote inside a string? Or a newline? Escape characters start with a backslash `\`:

```python
# Newline
print("Line 1\nLine 2")
# Line 1
# Line 2

# Tab
print("Name:\tTony Stark")
# Name:    Tony Stark

# Backslash itself
print("C:\\Users\\Documents")
# C:\Users\Documents

# Quote inside a string
print("She said \"hello\"")
# She said "hello"

# Or just use the other type of quote
print('She said "hello"')
# She said "hello"
```

If you have a string with lots of backslashes (like a Windows file path), use a **raw string** with `r` prefix:

```python
# Without raw string - chaos
# path = "C:\new_folder\test"  # \n becomes a newline!

# With raw string - sanity
path = r"C:\new_folder\test"
print(path)  # C:\new_folder\test
```

**Multi-line strings** use triple quotes:

```python
poem = """Roses are red,
Violets are blue,
Python is awesome,
And so are you."""
print(poem)
```

Triple quotes preserve line breaks and are perfect for long blocks of text. You'll see them used for documentation strings (docstrings) later.

## f-string Formatting: The Advanced Stuff

You already know basic f-strings from Chapter 2. Let's unlock the advanced features.

**Number formatting:**

```python
price = 49.99
tax = price * 0.0825

print(f"Price: ${price:.2f}")       # Price: $49.99 (2 decimal places)
print(f"Tax: ${tax:.2f}")           # Tax: $4.12
print(f"Big number: {1000000:,}")   # Big number: 1,000,000 (commas!)
print(f"Percentage: {0.856:.1%}")   # Percentage: 85.6%
```

The format spec goes after a colon inside the curly braces. `.2f` means "2 decimal places, float format." `,` adds thousand separators. `.1%` converts to a percentage with 1 decimal place.

**Padding and alignment:**

```python
for item, price in [("Coffee", 4.99), ("Sandwich", 8.50), ("Cookie", 2.25)]:
    print(f"{item:<15} ${price:>6.2f}")
```

Output:
```
Coffee           $ 4.99
Sandwich         $ 8.50
Cookie           $ 2.25
```

- `<15` means left-align in a 15-character wide field
- `>6` means right-align in a 6-character wide field
- `^` centers the text

This is great for building neat, aligned output without messing with spaces manually.

**Expressions inside f-strings:**

```python
name = "python"
print(f"Uppercase: {name.upper()}")    # Uppercase: PYTHON
print(f"Length: {len(name)}")           # Length: 6
print(f"Is cool: {10 > 5}")            # Is cool: True
print(f"Quick math: {7 * 6}")          # Quick math: 42
```

You can put any valid Python expression inside those curly braces. Methods, functions, math, comparisons - whatever you need.

## Your Turn: Username Generator

Build a username generator! Create `username_generator.py`:

```python
# Username Generator
print("=== Username Generator ===\n")

# Get user info
first_name = input("Enter your first name: ").strip().lower()
last_name = input("Enter your last name: ").strip().lower()
lucky_number = input("Enter your lucky number: ").strip()
birth_year = input("Enter your birth year: ").strip()

# Generate username options
option1 = f"{first_name}.{last_name}{lucky_number}"
option2 = f"{first_name[0]}{last_name}{birth_year[-2:]}"
option3 = f"{last_name[::-1]}_{first_name[:3]}"
option4 = f"{first_name}{last_name[0].upper()}_{lucky_number}"

print(f"\nHere are your username options:")
print(f"  1. {option1}")
print(f"  2. {option2}")
print(f"  3. {option3}")
print(f"  4. {option4}")
print(f"\nAll usernames are {len(option1)}-{len(max(option1, option2, option3, option4, key=len))} characters long.")
```

**Bonus challenges:**
1. Add a 5th option that uses `.replace()` to swap vowels with numbers (a=4, e=3, i=1, o=0)
2. Let the user pick their favorite and print it in ALL CAPS as their "official gamer tag"

## TL;DR

- **String methods** are your text Swiss Army knife: `.upper()`, `.lower()`, `.strip()`, `.replace()`, `.split()`, `.join()`
- **Strings are immutable** - methods return NEW strings, they don't change the original
- **Method chaining** lets you combo methods: `text.strip().lower().replace("a", "b")`
- **Indexing** starts at 0; negative indices count from the end (`[-1]` = last character)
- **Slicing** with `[start:stop:step]` - stop is exclusive; `[::-1]` reverses a string
- **Escape characters:** `\n` (newline), `\t` (tab), `\\` (backslash); use `r""` for raw strings
- **f-string formatting:** `:.2f` for decimals, `:,` for commas, `:<10` for padding

---

# Chapter 5: Making Decisions: if, elif, else

> **Sprint 1** | **12 min read** | **Code: [github link](https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/sprint-1-basics/chapter-05-decisions/)**

Every app you've ever used makes decisions. "Is the password correct? Show the dashboard. Wrong? Show an error." "Is the player's health zero? Game over." "Is the user over 18? Show the content." Without decisions, programs would just be straight lines - boring and useless. Time to give your code a brain.

## What You'll Learn
- Comparison operators - the questions Python asks
- if/elif/else - the decision-making trio
- Logical operators: and, or, not
- Nested vs. flat conditions (and why flat is better)
- Truthy and falsy values
- The one-line ternary operator

## Comparison Operators: Asking Python Questions

Before Python can make a decision, it needs to ask a question. Comparison operators are those questions, and they always return `True` or `False`:

```python
print(10 > 5)      # True    "Is 10 greater than 5?"
print(10 < 5)      # False   "Is 10 less than 5?"
print(10 >= 10)    # True    "Is 10 greater than or equal to 10?"
print(10 <= 9)     # False   "Is 10 less than or equal to 9?"
print(10 == 10)    # True    "Is 10 equal to 10?"
print(10 != 5)     # True    "Is 10 not equal to 5?"
```

> **Wait, What?** `=` vs `==` - one assigns, one compares. `x = 5` puts 5 in the box. `x == 5` asks "is x equal to 5?" Mix them up and Python gets very confused. This is the #1 beginner bug. Tattoo it on your brain: **one equals for putting, two equals for asking.**

These work with strings too:

```python
print("apple" == "apple")   # True
print("apple" == "Apple")   # False (case matters!)
print("a" < "b")            # True (alphabetical order)
print("banana" > "apple")   # True (b comes after a)
```

## if / elif / else: The Decision Trio

Here's the structure. It reads almost like English:

```python
temperature = 35

if temperature > 30:
    print("It's hot! Stay hydrated.")
elif temperature > 20:
    print("Nice weather! Go outside.")
elif temperature > 10:
    print("It's chilly. Grab a jacket.")
else:
    print("It's freezing. Stay in bed.")
```

Output: `It's hot! Stay hydrated.`

Let's break it down:

1. `if` checks the first condition. If it's `True`, run that block and skip everything else.
2. `elif` (short for "else if") checks the next condition, but ONLY if all previous conditions were `False`.
3. `else` is the catch-all - runs if nothing above was `True`. No condition needed.

**The colon `:` at the end of each line is mandatory.** Forget it and Python throws a syntax error.

**The indentation (4 spaces) is mandatory.** That's how Python knows which code belongs to which condition. No curly braces like other languages - Python uses whitespace. It's cleaner, but it means spacing actually matters.

```python
age = 20

if age >= 18:
    print("You can vote!")
    print("You can also buy a lottery ticket!")    # Still inside the if
print("This always prints, regardless of age.")     # Outside the if (no indent)
```

You can have as many `elif` blocks as you want, but only one `if` and one `else`:

```python
grade = 85

if grade >= 90:
    letter = "A"
elif grade >= 80:
    letter = "B"
elif grade >= 70:
    letter = "C"
elif grade >= 60:
    letter = "D"
else:
    letter = "F"

print(f"Your grade: {letter}")  # Your grade: B
```

Python checks conditions **from top to bottom** and stops at the first `True`. That's why order matters. If you put `grade >= 60` first, everyone above 60 would get a D.

## Logical Operators: The Bouncers at the Club

Sometimes one condition isn't enough. Enter `and`, `or`, and `not` - the logical operators. Think of them as bouncers at a club.

**`and`** - BOTH conditions must be True (strict bouncer):

```python
age = 25
has_id = True

if age >= 21 and has_id:
    print("Welcome to the club!")
else:
    print("Sorry, can't let you in.")
```

**`or`** - At LEAST one condition must be True (chill bouncer):

```python
is_vip = False
is_on_guest_list = True

if is_vip or is_on_guest_list:
    print("Come on in!")
else:
    print("Back of the line, buddy.")
```

**`not`** - Flips True to False and vice versa (the contrarian):

```python
is_raining = False

if not is_raining:
    print("Let's go for a walk!")
```

You can combine them:

```python
age = 25
has_id = True
is_banned = False

if age >= 21 and has_id and not is_banned:
    print("Welcome!")
```

**Operator precedence:** `not` is evaluated first, then `and`, then `or`. When in doubt, use parentheses:

```python
# Confusing
if a or b and c:
    ...

# Clear
if a or (b and c):
    ...
```

## Nested Conditions vs. Flat (Flat Wins)

You *can* put if statements inside other if statements. It's called nesting:

```python
# Nested (hard to read)
age = 25
has_ticket = True
is_vip = False

if age >= 18:
    if has_ticket:
        if is_vip:
            print("VIP entrance, right this way!")
        else:
            print("General admission, enjoy the show!")
    else:
        print("You need a ticket!")
else:
    print("Must be 18 or older.")
```

That works, but it's a pyramid of doom. Every level of nesting makes your code harder to follow. Here's the flat version:

```python
# Flat (much better)
age = 25
has_ticket = True
is_vip = False

if age < 18:
    print("Must be 18 or older.")
elif not has_ticket:
    print("You need a ticket!")
elif is_vip:
    print("VIP entrance, right this way!")
else:
    print("General admission, enjoy the show!")
```

Same logic, same result, but way easier to read. The trick is to **check for failures first** (too young? no ticket?) and handle them early. The happy path goes at the end. This pattern is called "early return" or "guard clauses," and experienced developers swear by it.

## Truthy and Falsy: Python's Vibe Check

Here's something that surprises beginners: you don't always need a comparison operator in an `if` statement. Python can evaluate any value as either "truthy" or "falsy."

**Falsy values** (Python treats these as False):
- `False`
- `0` (zero)
- `0.0` (zero float)
- `""` (empty string)
- `[]` (empty list)
- `None` (Python's version of "nothing")

**Everything else is truthy.**

```python
name = ""
if name:
    print(f"Hello, {name}!")
else:
    print("You didn't enter a name!")
# Output: You didn't enter a name!
```

```python
items_in_cart = 3
if items_in_cart:
    print(f"You have {items_in_cart} items. Ready to checkout?")
else:
    print("Your cart is empty!")
# Output: You have 3 items. Ready to checkout?
```

This is super handy for checking if something exists or has a value. Instead of writing `if name != ""`, you just write `if name`. Cleaner, more Pythonic.

```python
# Instead of this
if len(my_list) > 0:
    print("List has items")

# Do this
if my_list:
    print("List has items")
```

## The Ternary Operator: One-Liner Decisions

Sometimes you have a simple if/else and you want to write it in one line. Python's ternary operator (also called a conditional expression) lets you do that:

```python
age = 20
status = "adult" if age >= 18 else "minor"
print(status)  # adult
```

It reads like English: "status is 'adult' IF age is >= 18, ELSE 'minor'."

```python
# Regular if/else
if score >= 50:
    result = "Pass"
else:
    result = "Fail"

# Same thing, one line
result = "Pass" if score >= 50 else "Fail"
```

This is great for simple assignments. Don't go overboard though - if your condition is complex, stick with a regular if/else. Code readability is not a place to show off.

```python
# This is fine
mood = "happy" if sun_is_out else "meh"

# This is a war crime against readability
x = "a" if condition1 else "b" if condition2 else "c" if condition3 else "d"
```

## Your Turn: Movie Rating Classifier

Create `movie_rater.py` - a program that classifies movies based on user input:

```python
# Movie Rating Classifier
print("=== Movie Rating Classifier ===\n")

title = input("Movie title: ")
genre = input("Genre (action/comedy/horror/drama): ").lower().strip()
score = float(input("Your rating (0-10): "))
would_rewatch = input("Would you rewatch it? (yes/no): ").lower().strip()

# Classify the rating
if score >= 9:
    verdict = "MASTERPIECE"
elif score >= 7:
    verdict = "Great"
elif score >= 5:
    verdict = "Decent"
elif score >= 3:
    verdict = "Meh"
else:
    verdict = "Terrible"

# Generate review
print(f"\n{'=' * 40}")
print(f"Movie: {title}")
print(f"Genre: {genre.title()}")
print(f"Score: {score}/10 - {verdict}")

if score >= 7 and would_rewatch == "yes":
    print("Recommendation: Must watch!")
elif score >= 5 or would_rewatch == "yes":
    print("Recommendation: Worth a try.")
else:
    print("Recommendation: Skip it.")

# Bonus genre comment
if genre == "horror" and score < 5:
    print("Hot take: Bad horror movies are still fun at sleepovers.")
elif genre == "action" and score >= 8:
    print("Explosions AND a good plot? Rare W.")

print(f"{'=' * 40}")
```

**Bonus challenges:**
1. Add an "age-appropriate" check: ask for the user's age and warn them if the genre is "horror" and they're under 13
2. Add a "rewatch count" feature: if they'd rewatch it AND scored it 9+, print "Future comfort movie detected"

## TL;DR

- **Comparison operators** (`==`, `!=`, `>`, `<`, `>=`, `<=`) return `True` or `False`
- **`=` assigns, `==` compares** - the most important distinction for beginners
- **if/elif/else** checks conditions top to bottom; first `True` wins
- **Logical operators:** `and` (both true), `or` (at least one true), `not` (flip it)
- **Flat is better than nested** - check for failures early, happy path at the end
- **Truthy/falsy:** empty strings, 0, `None`, and empty collections are falsy; everything else is truthy
- **Ternary:** `value_if_true if condition else value_if_false` for simple one-liners

---

# Chapter 6: Lists: Your First Superpower

> **Sprint 1** | **12 min read** | **Code: [github link](https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/sprint-1-basics/chapter-06-lists/)**

A variable holds one thing. A list holds EVERYTHING. It's like going from a sticky note to a filing cabinet. Up until now, every variable you've created stored a single value. But what if you need to store 50 student names? 1000 scores? A playlist of songs? You're not going to make 1000 separate variables. That's what lists are for, and they're about to change your whole game.

## What You'll Learn
- Creating and accessing lists
- Adding, removing, and modifying items
- Sorting and searching
- The legendary list comprehension

## Creating and Accessing Lists

A list is an ordered collection of items wrapped in square brackets:

```python
# A list of strings
fruits = ["apple", "banana", "cherry", "mango"]

# A list of numbers
scores = [95, 87, 72, 100, 63]

# A mixed list (Python doesn't care about types)
random_stuff = ["hello", 42, 3.14, True, None]

# An empty list
empty = []
```

Access items by their index. Just like strings, lists start counting at 0:

```python
fruits = ["apple", "banana", "cherry", "mango"]

print(fruits[0])     # apple (first item)
print(fruits[1])     # banana (second item)
print(fruits[-1])    # mango (last item!)
print(fruits[-2])    # cherry (second to last)
```

> **Wait, What?** "Lists start at 0, not 1. I know. Programmers are weird." There's actually a historical reason - it's about memory offsets - but honestly, you just have to accept it. The first item is at index 0. The second is at index 1. If a list has 4 items, the last index is 3. You'll get used to it faster than you think.

Slicing works too, same as strings:

```python
fruits = ["apple", "banana", "cherry", "mango", "kiwi"]

print(fruits[1:3])    # ['banana', 'cherry']
print(fruits[:3])     # ['apple', 'banana', 'cherry']
print(fruits[2:])     # ['cherry', 'mango', 'kiwi']
print(fruits[::-1])   # ['kiwi', 'mango', 'cherry', 'banana', 'apple'] (reversed!)
```

Unlike strings, lists are **mutable** - you can change them:

```python
fruits = ["apple", "banana", "cherry"]
fruits[1] = "blueberry"
print(fruits)  # ['apple', 'blueberry', 'cherry']
```

## Modifying Lists: Adding and Removing

Lists come with methods for adding and removing items. This is where lists really flex.

### Adding Items

```python
heroes = ["Iron Man", "Thor"]

# append() - add to the END
heroes.append("Hulk")
print(heroes)  # ['Iron Man', 'Thor', 'Hulk']

# insert() - add at a specific position
heroes.insert(1, "Spider-Man")
print(heroes)  # ['Iron Man', 'Spider-Man', 'Thor', 'Hulk']

# extend() - add multiple items at once
heroes.extend(["Black Widow", "Hawkeye"])
print(heroes)  # ['Iron Man', 'Spider-Man', 'Thor', 'Hulk', 'Black Widow', 'Hawkeye']
```

> **Wait, What?** `append()` vs `extend()` - `append` adds ONE item (even if it's a list, it adds the whole list as a single item). `extend` unpacks the items and adds them individually. Try `heroes.append(["A", "B"])` and see what happens - you'll get a list inside a list.

### Removing Items

```python
heroes = ["Iron Man", "Spider-Man", "Thor", "Hulk", "Hawkeye"]

# remove() - remove by VALUE (first occurrence)
heroes.remove("Thor")
print(heroes)  # ['Iron Man', 'Spider-Man', 'Hulk', 'Hawkeye']

# pop() - remove by INDEX and return the removed item
removed = heroes.pop(1)
print(removed)     # Spider-Man
print(heroes)      # ['Iron Man', 'Hulk', 'Hawkeye']

# pop() with no argument removes the LAST item
last = heroes.pop()
print(last)        # Hawkeye
print(heroes)      # ['Iron Man', 'Hulk']

# del - remove by index (doesn't return anything)
del heroes[0]
print(heroes)      # ['Hulk']

# clear() - nuclear option, removes everything
heroes.clear()
print(heroes)      # []
```

Use `remove()` when you know the value. Use `pop()` when you know the index and want to use the removed item. Use `del` when you know the index but don't need the item back.

## Sorting

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6]

# sort() - sorts IN PLACE (modifies the original list)
numbers.sort()
print(numbers)  # [1, 1, 2, 3, 4, 5, 6, 9]

# Reverse sort
numbers.sort(reverse=True)
print(numbers)  # [9, 6, 5, 4, 3, 2, 1, 1]

# sorted() - returns a NEW sorted list (original unchanged)
original = [3, 1, 4, 1, 5]
new_list = sorted(original)
print(original)   # [3, 1, 4, 1, 5] (unchanged!)
print(new_list)    # [1, 1, 3, 4, 5]
```

The difference between `sort()` and `sorted()` is crucial:
- `.sort()` changes the list permanently and returns `None`
- `sorted()` leaves the original alone and gives you a new sorted list

When in doubt, use `sorted()`. It's safer because you don't lose the original order.

```python
# Sorting strings (alphabetical)
names = ["Charlie", "Alice", "Bob"]
names.sort()
print(names)  # ['Alice', 'Bob', 'Charlie']

# Reverse a list (without sorting)
names.reverse()
print(names)  # ['Charlie', 'Bob', 'Alice']
```

## Useful List Operations

```python
numbers = [10, 20, 30, 20, 40]

# Length
print(len(numbers))         # 5

# Check if something is in the list
print(30 in numbers)        # True
print(99 in numbers)        # False
print(99 not in numbers)    # True

# Count occurrences
print(numbers.count(20))    # 2

# Find the index of an item
print(numbers.index(30))    # 2

# Min, max, sum
print(min(numbers))         # 10
print(max(numbers))         # 40
print(sum(numbers))         # 120
```

The `in` keyword is gold. It reads like English: `if "pizza" in toppings:` - beautiful.

### enumerate() - Index AND Value

When you loop through a list (we'll cover loops properly in Chapter 7, but here's a preview), sometimes you need both the item AND its position:

```python
fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
```

Output:
```
0: apple
1: banana
2: cherry
```

You can even start counting from 1:

```python
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")
```

Output:
```
1. apple
2. banana
3. cherry
```

## List Comprehensions: The Show-Off Move

This is where Python gets elegant. A **list comprehension** lets you create a new list by transforming or filtering an existing one - in a single line.

The old way:

```python
numbers = [1, 2, 3, 4, 5]
squared = []
for n in numbers:
    squared.append(n ** 2)
print(squared)  # [1, 4, 9, 16, 25]
```

The list comprehension way:

```python
numbers = [1, 2, 3, 4, 5]
squared = [n ** 2 for n in numbers]
print(squared)  # [1, 4, 9, 16, 25]
```

One line. Same result. The syntax is `[expression for item in iterable]`.

You can add a filter with `if`:

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Only even numbers
evens = [n for n in numbers if n % 2 == 0]
print(evens)  # [2, 4, 6, 8, 10]

# Only even numbers, squared
even_squares = [n ** 2 for n in numbers if n % 2 == 0]
print(even_squares)  # [4, 16, 36, 64, 100]
```

And with strings:

```python
names = ["alice", "BOB", "Charlie", "dave"]
clean_names = [name.strip().title() for name in names]
print(clean_names)  # ['Alice', 'Bob', 'Charlie', 'Dave']
```

> **Don't Panic:** List comprehensions look strange at first. Every single Python developer had a "what the heck is this?" moment when they first saw one. Read it from left to right: "give me `n ** 2` FOR each `n` IN `numbers` IF `n` is even." You'll love them in a week. I promise.

A quick guide for reading them:

```python
# Template:
# [what_to_do   for item in collection   if condition]

# "Give me each name uppercased, from the names list, if the name isn't empty"
upper_names = [name.upper() for name in names if name]
```

## Your Turn: Grocery List Manager

Build a simple grocery list manager in `grocery_list.py`:

```python
# Grocery List Manager
print("=== Grocery List Manager ===")
print("Commands: add, remove, show, sort, clear, quit\n")

grocery_list = []

while True:
    command = input("What do you want to do? ").lower().strip()

    if command == "add":
        item = input("What item? ").strip().title()
        if item in grocery_list:
            print(f"'{item}' is already on the list!")
        else:
            grocery_list.append(item)
            print(f"Added '{item}'. ({len(grocery_list)} items total)")

    elif command == "remove":
        item = input("Which item? ").strip().title()
        if item in grocery_list:
            grocery_list.remove(item)
            print(f"Removed '{item}'.")
        else:
            print(f"'{item}' isn't on the list!")

    elif command == "show":
        if grocery_list:
            print("\nYour grocery list:")
            for i, item in enumerate(grocery_list, 1):
                print(f"  {i}. {item}")
            print()
        else:
            print("Your list is empty!")

    elif command == "sort":
        grocery_list.sort()
        print("List sorted alphabetically!")

    elif command == "clear":
        grocery_list.clear()
        print("List cleared!")

    elif command == "quit":
        print(f"Final list: {grocery_list}")
        print("Bye!")
        break

    else:
        print("Unknown command. Try: add, remove, show, sort, clear, quit")
```

Don't worry if the `while True` loop looks unfamiliar - we'll cover loops fully in Chapter 7. For now, just know it keeps the program running until you type "quit."

**Bonus challenge:** Add a "search" command that checks if an item is on the list, and a "count" command that shows how many items you have.

## TL;DR

- **Lists** are ordered, mutable collections: `fruits = ["apple", "banana"]`
- **Index** starts at 0; use `[-1]` for the last item
- **Add:** `append()` (one item), `insert()` (at position), `extend()` (multiple)
- **Remove:** `remove()` (by value), `pop()` (by index, returns it), `del` (by index)
- **sort()** changes the list; **sorted()** returns a new one
- **Useful:** `len()`, `in`, `count()`, `index()`, `min()`, `max()`, `sum()`, `enumerate()`
- **List comprehensions** create new lists in one line: `[x**2 for x in nums if x > 0]`
- Lists start at 0. Accept it. Love it. Move on.

---

# Chapter 7: Loops: Doing Things on Repeat

> **Sprint 1** | **12 min read** | **Code: [github link](https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/sprint-1-basics/chapter-07-loops/)**

Imagine having to manually send 1000 emails one at a time. Or counting every item in a warehouse by hand. Or liking every photo on your friend's Instagram, one. by. one. Loops are the reason programmers still have their sanity. They let you say "do this thing, but like, a thousand times" and then go grab coffee while the computer does the work.

## What You'll Learn
- `for` loops - when you know what you're looping through
- `range()` - the loop's best friend
- `while` loops - when you don't know how many times
- `break` and `continue` - escape hatches
- Nested loops - when one loop isn't enough

## for Loops: Do This for Each Thing

A `for` loop goes through a collection of items and does something with each one. Think of it like a conveyor belt - each item gets the same treatment:

```python
avengers = ["Iron Man", "Thor", "Hulk", "Black Widow", "Hawkeye"]

for hero in avengers:
    print(f"{hero} is ready for battle!")
```

Output:
```
Iron Man is ready for battle!
Thor is ready for battle!
Hulk is ready for battle!
Black Widow is ready for battle!
Hawkeye is ready for battle!
```

Here's how to read it: "FOR each `hero` IN the `avengers` list, do this." The variable `hero` takes on the value of each item, one at a time. First it's `"Iron Man"`, then `"Thor"`, then `"Hulk"`, and so on.

You can name the loop variable whatever you want, but make it descriptive:

```python
# Good - you know exactly what's happening
for student in students:
    print(student)

for number in numbers:
    print(number * 2)

# Works but... what's 'x'?
for x in students:
    print(x)
```

You can loop over strings too (each character is an item):

```python
for letter in "Python":
    print(letter)
# P
# y
# t
# h
# o
# n
```

## range(): The Loop's Best Friend

What if you want to loop a specific number of times but you don't have a list? That's what `range()` is for. It generates a sequence of numbers.

**Three forms of range:**

```python
# range(stop) - 0 to stop-1
for i in range(5):
    print(i)
# 0, 1, 2, 3, 4

# range(start, stop) - start to stop-1
for i in range(2, 6):
    print(i)
# 2, 3, 4, 5

# range(start, stop, step) - with custom step
for i in range(0, 20, 5):
    print(i)
# 0, 5, 10, 15

# Count backwards
for i in range(10, 0, -1):
    print(i)
# 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
```

Just like slicing, `range()` goes up to but **doesn't include** the stop number. `range(5)` gives you 0 through 4, not 0 through 5.

Practical example - print a times table:

```python
number = 7
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
```

Output:
```
7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
...
7 x 10 = 70
```

## while Loops: When You Don't Know How Many Times

`for` loops are great when you know what you're iterating over. But sometimes you want to keep going until something happens. Enter `while`:

```python
password = ""
while password != "python123":
    password = input("Enter the password: ")

print("Access granted!")
```

This keeps asking for the password until the user gets it right. We have no idea how many tries it'll take - could be 1, could be 100. That's the sweet spot for `while`.

The pattern is: **while this condition is True, keep looping.**

```python
# Countdown
count = 5
while count > 0:
    print(count)
    count -= 1    # DON'T FORGET THIS or you get an infinite loop!
print("Liftoff!")
```

Output:
```
5
4
3
2
1
Liftoff!
```

See that `count -= 1`? That's crucial. If you forget to change the variable that your `while` condition checks, the condition stays `True` forever and your program runs until the heat death of the universe (or until you hit Ctrl+C).

> **Pro Tip:** If your program seems frozen, it's probably stuck in an infinite loop. Press `Ctrl+C` to break out. It happens to everyone. Even senior developers accidentally create infinite loops - they just press Ctrl+C faster.

**Common while loop patterns:**

```python
# Accumulator - add things up
total = 0
while True:
    price = input("Enter a price (or 'done'): ")
    if price == "done":
        break
    total += float(price)
print(f"Total: ${total:.2f}")

# Validation - keep asking until valid input
age = -1
while age < 0 or age > 150:
    age = int(input("Enter your age (0-150): "))
print(f"Got it, you're {age}!")
```

## break and continue: The Escape Hatches

### break - "I'm Outta Here!"

`break` immediately exits the loop. No more iterations, no more checking conditions. It's the emergency exit.

```python
# Search for a name
names = ["Alice", "Bob", "Charlie", "Dave", "Eve"]

search = "Charlie"
for name in names:
    if name == search:
        print(f"Found {search}!")
        break
    print(f"Checking {name}...")
```

Output:
```
Checking Alice...
Checking Bob...
Found Charlie!
```

Without `break`, the loop would keep checking Dave and Eve even after finding Charlie. Why waste the effort?

### continue - "Skip This One"

`continue` skips the rest of the current iteration and jumps to the next one. It's like saying "nah, next."

```python
# Print only odd numbers
for i in range(10):
    if i % 2 == 0:
        continue     # Skip even numbers
    print(i)
# 1, 3, 5, 7, 9
```

```python
# Process only valid entries
scores = [95, -1, 87, 0, 72, -5, 100]

for score in scores:
    if score <= 0:
        continue    # Skip invalid scores
    print(f"Processing score: {score}")
```

Think of `break` as leaving the building. `continue` is skipping one floor on the elevator.

## Nested Loops: Loop-ception

Sometimes you need a loop inside a loop. The inner loop runs completely for each iteration of the outer loop:

```python
# Print a grid
for row in range(3):
    for col in range(4):
        print("*", end=" ")
    print()  # New line after each row
```

Output:
```
* * * *
* * * *
* * * *
```

The outer loop runs 3 times (rows). For each row, the inner loop runs 4 times (columns). That's 3 x 4 = 12 stars total.

A more practical example - finding matching pairs:

```python
colors = ["red", "blue", "green"]
sizes = ["S", "M", "L"]

for color in colors:
    for size in sizes:
        print(f"{color}-{size}", end="  ")
    print()
```

Output:
```
red-S  red-M  red-L
blue-S  blue-M  blue-L
green-S  green-M  green-L
```

Nested loops can make your brain hurt. That's normal. Just remember: the inner loop resets and runs completely every time the outer loop takes a step.

> **Pro Tip:** Avoid going more than 2 levels deep with nested loops. If you find yourself at 3 or more levels, there's probably a better way. We'll learn about functions in Sprint 2, which help break things up.

## The else Clause on Loops (Weird But Useful)

Python has a feature that confuses even experienced programmers from other languages: loops can have an `else` block.

```python
for i in range(5):
    print(i)
else:
    print("Loop completed!")
```

Output:
```
0
1
2
3
4
Loop completed!
```

> **Wait, What?** "Yes, loops can have an `else`. No, it's not what you think." The `else` block runs ONLY if the loop finished **without** hitting a `break`. If the loop was interrupted by `break`, the `else` is skipped.

This is actually really useful for search patterns:

```python
numbers = [2, 4, 6, 8, 10]

for num in numbers:
    if num % 2 != 0:
        print(f"Found an odd number: {num}")
        break
else:
    print("All numbers are even!")
# Output: All numbers are even!
```

Without `for/else`, you'd need a flag variable. With it, the code is cleaner. But honestly? Most Python developers don't use this feature often. It's good to know it exists, but don't feel pressured to use it.

## Useful Loop Patterns

Here are patterns you'll use all the time:

```python
# Building a list with a loop
squares = []
for i in range(1, 6):
    squares.append(i ** 2)
print(squares)  # [1, 4, 9, 16, 25]

# Summing values
total = 0
for price in [9.99, 14.50, 3.75, 22.00]:
    total += price
print(f"Total: ${total:.2f}")  # Total: $50.24

# Finding something
names = ["Alice", "Bob", "Charlie"]
target = "Bob"
found = False
for name in names:
    if name == target:
        found = True
        break
print(f"Found {target}: {found}")

# Looping with index using enumerate
fruits = ["apple", "banana", "cherry"]
for i, fruit in enumerate(fruits, 1):
    print(f"{i}. {fruit}")
```

## Your Turn: Multiplication Table Printer

Create `multiplication_table.py`:

```python
# Multiplication Table Printer
print("=== Multiplication Table ===\n")

size = int(input("Table size (e.g., 10 for 10x10): "))

# Print header row
print("    ", end="")
for i in range(1, size + 1):
    print(f"{i:4}", end="")
print()
print("    " + "--" * size)

# Print each row
for row in range(1, size + 1):
    print(f"{row:3} |", end="")
    for col in range(1, size + 1):
        result = row * col
        print(f"{result:4}", end="")
    print()

print(f"\nThat's {size * size} multiplication facts!")
```

Run it with a size of 10 and admire your perfectly aligned multiplication table.

**Bonus challenges:**
1. Highlight (add an asterisk) any result that's a perfect square
2. Add a mode that lets the user quiz themselves: show `5 x 7 = ?` and check their answer
3. Track how many they get right and show a score at the end

## TL;DR

- **`for` loops** iterate over a collection: `for item in collection:`
- **`range()`** generates numbers: `range(stop)`, `range(start, stop)`, `range(start, stop, step)`
- **`while` loops** run until a condition is False - don't forget to update the condition variable!
- **`break`** exits the loop immediately; **`continue`** skips to the next iteration
- **Nested loops:** the inner loop runs fully for each outer loop iteration
- **`for/else`:** the `else` block runs only if the loop completes without `break`
- If your program freezes, you probably made an infinite loop - hit `Ctrl+C`
- When in doubt about `for` vs `while`: if you're going through a collection, use `for`. If you're waiting for a condition, use `while`.

---

# Chapter 8: Tuples & Sets: Lists' Cousins

> **Sprint 1** | **12 min read** | **Code: [github link](https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/sprint-1-basics/chapter-08-tuples-sets/)**

If lists are the extroverts of Python data types - flexible, changeable, always growing - tuples are the introverts and sets are the bouncers. Tuples are quiet, reliable, and never change. Sets refuse to let duplicates in. Together with lists, these three data types cover almost every way you'll need to store collections of data.

## What You'll Learn
- Tuples: what they are, when to use them, and why immutability matters
- Tuple unpacking and the swap trick
- Sets: the duplicate destroyers
- Set operations (union, intersection, difference) with Marvel examples
- When to use list vs tuple vs set

## Tuples: The "Read-Only" List

A tuple looks like a list, but with parentheses instead of square brackets:

```python
# A tuple
coordinates = (10, 20)
rgb_color = (255, 128, 0)
person = ("Tony Stark", 48, "Genius")

# A list (for comparison)
shopping = ["milk", "eggs", "bread"]
```

You can access items with indexing and slicing, just like lists:

```python
person = ("Tony Stark", 48, "Genius")
print(person[0])     # Tony Stark
print(person[-1])    # Genius
print(person[1:])    # (48, 'Genius')
```

But here's the catch: **you can't change a tuple after you create it.** That's the whole point.

```python
person = ("Tony Stark", 48, "Genius")
# person[1] = 49   # TypeError: 'tuple' object does not support item assignment
```

No appending. No removing. No sorting in place. It's locked down. Sealed. Immutable.

### "Why Would I Want That?"

Great question. Here's why tuples exist:

1. **Safety.** Some data shouldn't change. GPS coordinates, RGB colors, database records - if something accidentally modifies them, bad things happen. Tuples prevent that.

2. **Performance.** Tuples are slightly faster than lists because Python knows they won't change. For most programs you won't notice, but it matters at scale.

3. **Dictionary keys.** You'll learn about dictionaries in Sprint 2, but here's a preview: you can use tuples as dictionary keys, but not lists. That's because keys must be immutable.

4. **Signals intent.** When another programmer sees a tuple, they immediately know: "this data isn't supposed to change." It's a communication tool.

```python
# Things that make sense as tuples
months = ("Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")
http_status = (200, "OK")
screen_resolution = (1920, 1080)

# Things that make sense as lists
shopping_cart = ["laptop", "mouse", "keyboard"]  # You'll add/remove items
high_scores = [500, 450, 400, 350]               # New scores get added
```

### Tuple Quirks

A few things that trip people up:

```python
# A tuple with one item needs a trailing comma
single = (42,)     # This is a tuple
not_a_tuple = (42) # This is just the number 42 with pointless parentheses

print(type(single))       # <class 'tuple'>
print(type(not_a_tuple))  # <class 'int'>

# You can create tuples without parentheses (tuple packing)
point = 10, 20
print(type(point))  # <class 'tuple'>

# len, in, count, index all work
colors = ("red", "green", "blue", "green")
print(len(colors))           # 4
print("red" in colors)       # True
print(colors.count("green")) # 2
print(colors.index("blue"))  # 2
```

That single-element tuple thing is a classic gotcha. `(42)` is just math grouping. `(42,)` is a tuple. The comma is what makes it a tuple, not the parentheses.

## Tuple Unpacking: The Elegant Move

This is one of Python's most satisfying features. Instead of accessing tuple items by index, you can unpack them into separate variables in one shot:

```python
# Instead of this
person = ("Peter Parker", 22, "New York")
name = person[0]
age = person[1]
city = person[2]

# Do this
name, age, city = ("Peter Parker", 22, "New York")
print(f"{name}, {age}, from {city}")
# Peter Parker, 22, from New York
```

One line instead of three. And it reads beautifully. The number of variables on the left must match the number of items in the tuple.

This works with lists too, but it's most commonly used with tuples.

### The * Operator for "Everything Else"

What if you only care about the first item and want to lump the rest together?

```python
first, *rest = (1, 2, 3, 4, 5)
print(first)  # 1
print(rest)   # [2, 3, 4, 5] (a list!)

leader, *team, benchwarmer = ("Cap", "Iron Man", "Thor", "Hulk", "Hawkeye")
print(leader)       # Cap
print(team)         # ['Iron Man', 'Thor', 'Hulk']
print(benchwarmer)  # Hawkeye
```

The `*` collects all the "extras" into a list. It's like saying "I'll take the first one, the last one, and shove everything in between into a bag."

## The Swap Trick

In most languages, swapping two variables requires a temporary variable:

```python
# The old-school way
a = 1
b = 2
temp = a
a = b
b = temp
```

Python's tuple unpacking makes this a one-liner:

```python
a = 1
b = 2
a, b = b, a
print(a, b)  # 2 1
```

That's it. No temp variable. Under the hood, Python creates a tuple `(b, a)` and unpacks it into `(a, b)`. It's clean, it's Pythonic, and it's a great party trick at coding meetups. (Okay, maybe not a *great* party trick.)

## Sets: The Bouncers

A set is an **unordered** collection with **no duplicates**. Think of it as a bouncer at a club: every name gets in, but only once. Try to get in twice? "You're already inside, buddy."

```python
# Create a set with curly braces
colors = {"red", "green", "blue"}

# Or from a list (instant deduplication!)
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique_numbers = set(numbers)
print(unique_numbers)  # {1, 2, 3, 4}
```

That deduplication trick is incredibly useful. Got a list with duplicates? Wrap it in `set()` and they're gone.

```python
# Empty set - this is a gotcha!
empty_set = set()      # Correct
empty_dict = {}        # This is an empty DICTIONARY, not a set!
```

### Adding and Removing

```python
fruits = {"apple", "banana", "cherry"}

# Add an item
fruits.add("mango")
print(fruits)  # {'apple', 'banana', 'cherry', 'mango'} (order may vary)

# Add a duplicate - nothing happens, no error
fruits.add("apple")
print(fruits)  # Still the same set, no second "apple"

# Remove an item (raises error if not found)
fruits.remove("banana")

# Discard an item (no error if not found - safer!)
fruits.discard("kiwi")  # No error, even though "kiwi" isn't there

# Pop a random item (sets are unordered, so you can't pick which one)
removed = fruits.pop()
print(f"Removed: {removed}")

# Clear everything
fruits.clear()
```

> **Pro Tip:** Use `discard()` instead of `remove()` when you're not sure if the item is in the set. `remove()` throws a `KeyError` if the item doesn't exist; `discard()` just shrugs and moves on.

### Sets Are Unordered

This is important: sets have **no index** and **no order**. You can't do `my_set[0]`. The items might print in a different order each time.

```python
numbers = {3, 1, 4, 1, 5, 9}
print(numbers)  # Maybe {1, 3, 4, 5, 9} - you can't predict the order
# print(numbers[0])  # TypeError! Sets don't support indexing
```

If you need order, use a list. If you need uniqueness, use a set. If you need both... convert between them as needed.

## Set Operations: The Marvel Example

This is where sets really shine. They can do math-like operations that would take multiple loops with lists.

Let's say we have two teams of superheroes:

```python
avengers = {"Iron Man", "Thor", "Hulk", "Black Widow", "Captain America"}
guardians = {"Star-Lord", "Gamora", "Groot", "Rocket", "Thor"}
```

(Yes, Thor is in both. Multiverse stuff.)

**Union** - everyone from both teams (combined roster):

```python
all_heroes = avengers | guardians  # or avengers.union(guardians)
print(all_heroes)
# {'Iron Man', 'Thor', 'Hulk', 'Black Widow', 'Captain America',
#  'Star-Lord', 'Gamora', 'Groot', 'Rocket'}
# Thor appears only ONCE - no duplicates!
```

**Intersection** - heroes on BOTH teams:

```python
both_teams = avengers & guardians  # or avengers.intersection(guardians)
print(both_teams)
# {'Thor'}
```

**Difference** - in Avengers but NOT in Guardians:

```python
avengers_only = avengers - guardians  # or avengers.difference(guardians)
print(avengers_only)
# {'Iron Man', 'Hulk', 'Black Widow', 'Captain America'}
```

**Symmetric Difference** - in one team OR the other, but NOT both:

```python
exclusive = avengers ^ guardians  # or avengers.symmetric_difference(guardians)
print(exclusive)
# {'Iron Man', 'Hulk', 'Black Widow', 'Captain America',
#  'Star-Lord', 'Gamora', 'Groot', 'Rocket'}
# Thor is excluded because he's in both!
```

These operations are not just cool - they're blazing fast. Checking if an item is in a set is nearly instant, no matter how large the set is. Doing the same with a list gets slower as the list grows.

**Subset and superset checks:**

```python
og_avengers = {"Iron Man", "Thor", "Hulk"}
print(og_avengers.issubset(avengers))      # True (all of them are in avengers)
print(avengers.issuperset(og_avengers))    # True (avengers contains all of them)
print(avengers.isdisjoint(guardians))      # False (they share Thor)
```

## When to Use What: The Decision Guide

Here's your cheat sheet:

| Feature | List `[]` | Tuple `()` | Set `{}` |
|-----|------|------|-----|
| Ordered? | Yes | Yes | No |
| Mutable? | Yes | No | Yes |
| Duplicates? | Allowed | Allowed | Not allowed |
| Indexable? | Yes | Yes | No |
| Use when... | You need a changeable, ordered collection | Data shouldn't change | You need unique items or set math |

**Use a list when:**
- You need to add/remove items
- Order matters
- You'll access items by position

**Use a tuple when:**
- Data shouldn't change (coordinates, config values, database rows)
- You want to use it as a dictionary key (Sprint 2)
- You're returning multiple values from a function (Sprint 2)

**Use a set when:**
- You need to eliminate duplicates
- You need fast "is this item in here?" checks
- You need union/intersection/difference operations

## Your Turn: Playlist Duplicate Finder

Create `playlist_dedup.py`:

```python
# Playlist Duplicate Finder
print("=== Playlist Duplicate Finder ===\n")

# Simulate two playlists
playlist_road_trip = [
    "Bohemian Rhapsody", "Hotel California", "Sweet Child O' Mine",
    "Don't Stop Believin'", "Bohemian Rhapsody", "Back in Black",
    "Hotel California", "Thunderstruck", "Livin' on a Prayer"
]

playlist_workout = [
    "Lose Yourself", "Eye of the Tiger", "Stronger",
    "Don't Stop Believin'", "Thunderstruck", "Till I Collapse",
    "Remember the Name", "Stronger"
]

# Find duplicates within each playlist
road_trip_set = set(playlist_road_trip)
workout_set = set(playlist_workout)

road_trip_dupes = len(playlist_road_trip) - len(road_trip_set)
workout_dupes = len(playlist_workout) - len(workout_set)

print(f"Road Trip playlist: {len(playlist_road_trip)} songs, {road_trip_dupes} duplicates")
print(f"Workout playlist: {len(playlist_workout)} songs, {workout_dupes} duplicates")

# Songs in both playlists
shared = road_trip_set & workout_set
print(f"\nSongs in BOTH playlists: {shared}")

# Songs unique to each
only_road = road_trip_set - workout_set
only_workout = workout_set - road_trip_set
print(f"Only in Road Trip: {only_road}")
print(f"Only in Workout: {only_workout}")

# Merged super-playlist (no duplicates!)
mega_playlist = road_trip_set | workout_set
print(f"\nMega playlist ({len(mega_playlist)} unique songs):")
for i, song in enumerate(sorted(mega_playlist), 1):
    print(f"  {i}. {song}")

# Bonus: use tuple unpacking
print("\n-- Now Playing --")
current_song, *up_next = sorted(mega_playlist)
print(f"Now playing: {current_song}")
print(f"Up next: {up_next[0]}")
print(f"Songs remaining: {len(up_next)}")
```

**Bonus challenges:**
1. Let the user add songs to either playlist via `input()` and re-run the analysis
2. Find which songs appear more than once in the road trip playlist (not just that duplicates exist, but which specific songs are duplicated)
3. Create a tuple of `(song_title, playlist_name)` for each song and practice unpacking

## TL;DR

- **Tuples** are immutable (read-only) lists: `point = (10, 20)` - use for data that shouldn't change
- **Tuple unpacking** assigns each item to a variable: `name, age = ("Alice", 30)`
- **Swap trick:** `a, b = b, a` - no temp variable needed
- **Sets** are unordered collections with no duplicates: `unique = {1, 2, 3}`
- **Set deduplication:** `set([1, 1, 2, 2, 3])` gives you `{1, 2, 3}`
- **Set operations:** `|` (union), `&` (intersection), `-` (difference), `^` (symmetric difference)
- **Use lists** for ordered, changeable collections
- **Use tuples** for fixed data (coordinates, configs, multi-return values)
- **Use sets** for uniqueness and set math

---

# Sprint 1 Checkpoint: Mad Libs Generator

> **Project** | **30 min build** | **Code: [starter](https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/sprint-1-basics/sprint-1-project/starter/) | [solution](https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/sprint-1-basics/sprint-1-project/solution/)**

Congratulations! You just finished Sprint 1. Eight chapters. Variables, strings, numbers, decisions, lists, loops, tuples, sets. That's a LOT of Python, and you should feel genuinely proud. Seriously - most people who say "I'll learn to code" never get past Chapter 2. You're here at the checkpoint. That puts you ahead of 90% of people who downloaded this book.

Now let's prove you learned something. We're going to build a **Mad Libs Generator** that uses practically everything from Sprint 1.

## What You're Building

If you've never played Mad Libs: it's a word game where you fill in blanks with random words (nouns, verbs, adjectives, etc.) without seeing the story. Then you read the story out loud and it's usually ridiculous. It's been making road trips bearable since 1958.

Our version will:
1. Present multiple story templates to choose from
2. Ask the user for words (nouns, verbs, adjectives, etc.)
3. Fill in the blanks and display the story
4. Ask if they want to play again
5. Track how many rounds they've played

## Skills You'll Use

| Skill | Where You Learned It |
|----|-----------|
| `input()` and `print()` | Chapters 1 & 3 |
| Variables and f-strings | Chapter 2 |
| Type conversion (`int()`) | Chapter 3 |
| String methods (`.strip()`, `.title()`) | Chapter 4 |
| if/elif/else decisions | Chapter 5 |
| Lists and indexing | Chapter 6 |
| while loops and for loops | Chapter 7 |
| Tuples (for word categories) | Chapter 8 |

Look at that. Everything. This is the payoff.

## Step-by-Step Guide

### Step 1: Set Up Your Story Templates

Create a file called `mad_libs.py`. Start by defining your story templates. Each template is a string with placeholders, and we'll pair it with the list of words it needs:

```python
# Story templates
# Each story is a tuple: (title, template_string, list of (placeholder, word_type) tuples)

stories = [
    (
        "The Adventure",
        "Once upon a time, a {adjective1} {noun1} decided to {verb1} to the {place1}. "
        "Along the way, they met a {adjective2} {animal1} who was {verb2_ing} a {noun2}. "
        "\"That's the most {adjective3} thing I've ever seen!\" they {verb3_past}. "
        "Together, they {verb4_past} all the way to {place2} and ate {number1} {food1}s.",
        [
            ("adjective1", "adjective (like 'sparkly')"),
            ("noun1", "noun (person, place, or thing)"),
            ("verb1", "verb (like 'run')"),
            ("place1", "a place"),
            ("adjective2", "another adjective"),
            ("animal1", "an animal"),
            ("verb2_ing", "a verb ending in -ing"),
            ("noun2", "another noun"),
            ("adjective3", "yet another adjective"),
            ("verb3_past", "a verb in past tense"),
            ("verb4_past", "another past tense verb"),
            ("place2", "another place"),
            ("number1", "a number"),
            ("food1", "a food"),
        ]
    ),
    (
        "The Job Interview",
        "Interviewer: So, tell me about yourself.\n"
        "You: Well, I'm a {adjective1} {noun1} with {number1} years of experience in {verb1_ing}.\n"
        "Interviewer: Interesting. What's your greatest {noun2}?\n"
        "You: I once {verb2_past} an entire {noun3} in just {number2} minutes while {verb3_ing}.\n"
        "Interviewer: {exclamation}! That's {adjective2}. When can you start?\n"
        "You: I can start {verb4_ing} immediately. I just need a {adjective3} {noun4} and a {noun5}.",
        [
            ("adjective1", "adjective"),
            ("noun1", "noun"),
            ("number1", "a number"),
            ("verb1_ing", "verb ending in -ing"),
            ("noun2", "noun"),
            ("verb2_past", "past tense verb"),
            ("noun3", "noun"),
            ("number2", "a number"),
            ("verb3_ing", "verb ending in -ing"),
            ("exclamation", "an exclamation (like 'Wow' or 'Yikes')"),
            ("adjective2", "adjective"),
            ("verb4_ing", "verb ending in -ing"),
            ("adjective3", "adjective"),
            ("noun4", "noun"),
            ("noun5", "noun"),
        ]
    ),
    (
        "The Movie Review",
        "I just watched \"{noun1}: The {adjective1} {noun2}\" and I have {adjective2} feelings. "
        "The lead actor {verb1_past} through every scene like a {adjective3} {animal1}. "
        "The special effects were so {adjective4} that I {verb2_past} in my seat. "
        "The plot twist where the {noun3} turned out to be a {noun4}? "
        "I screamed \"{exclamation}!\" and threw my {noun5} at the screen. "
        "{number1}/10, would {verb3} again.",
        [
            ("noun1", "a name"),
            ("adjective1", "adjective"),
            ("noun2", "noun"),
            ("adjective2", "adjective"),
            ("verb1_past", "past tense verb"),
            ("adjective3", "adjective"),
            ("animal1", "animal"),
            ("adjective4", "adjective"),
            ("verb2_past", "past tense verb"),
            ("noun3", "noun"),
            ("noun4", "noun"),
            ("exclamation", "an exclamation"),
            ("noun5", "noun"),
            ("number1", "number (1-10)"),
            ("verb3", "verb"),
        ]
    ),
]
```

### Step 2: Build the Game Loop

Now let's build the main game logic:

```python
# Game state
rounds_played = 0
words_used = set()  # Track unique words they've used (sets - Chapter 8!)

print("=" * 50)
print("   WELCOME TO MAD LIBS GENERATOR!")
print("   Fill in the blanks. Chaos will follow.")
print("=" * 50)

while True:
    # Show available stories
    print("\nChoose a story:")
    for i, (title, _, _) in enumerate(stories, 1):
        print(f"  {i}. {title}")

    # Get their choice
    choice = input(f"\nPick a number (1-{len(stories)}): ").strip()

    # Validate the choice
    if not choice.isdigit() or int(choice) < 1 or int(choice) > len(stories):
        print("Invalid choice! Try again.")
        continue

    choice_index = int(choice) - 1
    title, template, word_list = stories[choice_index]
```

### Step 3: Collect Words from the User

```python
    # Collect words
    print(f"\n-- {title} --")
    print("Give me the following words:\n")

    collected_words = {}

    for placeholder, word_type in word_list:
        word = input(f"  Enter {word_type}: ").strip()

        # Clean up the input a little
        if word == "":
            word = "banana"  # Default for lazy players
            print(f"  (Nothing entered - using 'banana' because why not)")

        collected_words[placeholder] = word
        words_used.add(word.lower())  # Track unique words
```

Don't worry about the `{}` dictionary syntax - that's a preview of Sprint 2. For now, just know it maps each placeholder name to the word the user entered.

### Step 4: Fill In the Story and Display It

```python
    # Fill in the template
    story = template
    for placeholder, word in collected_words.items():
        story = story.replace("{" + placeholder + "}", word.upper())

    # Display the result
    print("\n" + "=" * 50)
    print(f"  {title.upper()}")
    print("=" * 50)
    print()
    print(story)
    print()
    print("=" * 50)

    rounds_played += 1
```

### Step 5: Play Again Loop

```python
    # Stats
    print(f"\nRounds played: {rounds_played}")
    print(f"Unique words used: {len(words_used)}")

    # Play again?
    again = input("\nPlay again? (yes/no): ").lower().strip()
    if again not in ("yes", "y", "yeah", "sure", "yep"):
        break

# Goodbye message
print(f"\n{'=' * 50}")
print(f"  Thanks for playing!")
print(f"  Total rounds: {rounds_played}")
print(f"  Unique words you used: {len(words_used)}")
if len(words_used) > 20:
    print("  Impressive vocabulary!")
elif len(words_used) > 10:
    print("  Nice word variety!")
else:
    print("  Someone likes reusing words... no judgment.")
print(f"{'=' * 50}")
```

### The Complete File

Put steps 1-5 together in `mad_libs.py` and run it. You should be able to:

- Choose a story template
- Enter words for each blank
- See your ridiculous story
- Play multiple rounds
- See your stats at the end

## Ways to Make It Your Own

Once you've got the basic version working, try these enhancements:

1. **Add your own story templates** - the sillier the better
2. **Add a "random word" option** - create lists of random nouns, verbs, adjectives and pick from them when the user types "random"
3. **Save the best stories** - collect them in a list and print a "greatest hits" at the end
4. **Add categories** - "funny," "scary," "work-appropriate" story groups
5. **Score system** - rate each story on a silliness scale based on the words used

## What's Coming in Sprint 2

You've got the basics down. Sprint 2 is where things get interesting:

- **Dictionaries** - the data structure that powers most real-world programs
- **Functions** - stop repeating yourself and start building reusable blocks
- **Error handling** - your programs stop crashing on bad input
- **File I/O** - read from and write to actual files
- **Modules** - tap into Python's massive standard library

The project? A **Personal Finance Tracker** that reads and writes files, handles errors gracefully, and is actually useful in your daily life.

---

Take a break. You've earned it. Go touch grass, pet a dog, watch an episode of something. When you come back, Sprint 2 is waiting.

---

# Welcome to Sprint 2: Now You're Cooking

> **Chapters 9-14** | **Estimated Time: 3-4 hours** | **Difficulty: Intermediate**

Look at you. You survived Sprint 1. You know variables, loops, lists, conditionals - you've got the vocabulary of a Python speaker. But right now, you're kind of like someone who knows how to boil water and make toast. Technically, you can feed yourself. But nobody's calling you a chef.

Sprint 2 is where you become the chef.

## What's on the Menu

Over the next six chapters, you're going to unlock the tools that separate "I'm learning Python" from "I know Python." Here's what's coming:

- **Chapter 9:** Dictionaries - accessing data by name instead of number (game-changer)
- **Chapter 10:** Functions - stop copy-pasting code forever
- **Chapter 11:** Modules & packages - use code written by thousands of other developers
- **Chapter 12:** File handling - save data so it survives when your program stops
- **Chapter 13:** Error handling - make your code crash-proof (or at least crash-graceful)
- **Chapter 14:** Lambda, map, filter, reduce - one-liner wizardry

## The Sprint 2 Project: Expense Tracker

By the end of this sprint, you'll build a fully functional **Expense Tracker** that saves data to CSV files, handles errors gracefully, uses functions to stay organized, and actually persists between sessions. It's the kind of thing you could genuinely use in real life. Or at least, the kind of thing that makes you feel productive before you go back to impulse-buying on Amazon.

The training wheels are off. The stabilizers are gone. But you've got this - because everything you learned in Sprint 1 is about to click into place.

Let's cook.

---

# Chapter 9: Dictionaries: The Real MVP

> **Sprint 2, Chapter 9** | **Estimated Time: 12-15 minutes** | **Difficulty: Intermediate**

Lists are great. You know that. You've been slicing them, looping through them, and generally having a good time. But lists have a secret weakness - you can only access things by number. "Give me item number 3." That works, but what if you could say "Give me the *email*" or "Give me the *price*"? What if you could access things by NAME?

Enter dictionaries. The real MVP of Python data structures.

## Key-Value Pairs: Like a Real Dictionary (But Better)

Think about an actual dictionary. You look up a **word** and get a **definition**. You don't say "give me the 47,382nd entry." You say "give me the definition of 'serendipity.'"

Python dictionaries work the same way. Instead of word and definition, we call them **key** and **value**. You give it a key, it gives you the value. Simple as that.

```python
# A real-world example: a student's profile
student = {
    "name": "Priya",
    "age": 22,
    "major": "Computer Science",
    "gpa": 3.8
}
```

See those curly braces `{}`? That's how Python knows it's a dictionary. Each entry is a `key: value` pair, separated by commas. The key is always a string (usually), and the value can be anything - a string, a number, a list, even another dictionary.

> **Remember When?** Remember lists from Chapter 6? Dictionaries are like lists that went to college. Lists store things in order by position. Dictionaries store things by label. Both are useful, but dictionaries are what you reach for when your data has *meaning*.

## Creating Dictionaries

You've already seen one way. Here are all the ways to create a dictionary:

```python
# Method 1: Curly braces (most common)
person = {"name": "Alex", "age": 30}

# Method 2: dict() constructor
person = dict(name="Alex", age=30)

# Method 3: Empty dictionary (fill it later)
person = {}

# Method 4: From a list of tuples
person = dict([("name", "Alex"), ("age", 30)])
```

Method 1 is what you'll use 90% of the time. Method 2 is nice when your keys are simple strings. Methods 3 and 4 exist for specific situations, but don't stress about them.

## Accessing Values: [] vs .get()

There are two ways to grab a value from a dictionary. One is reckless. One is safe.

```python
student = {"name": "Priya", "age": 22, "major": "CS"}

# Method 1: Square brackets (reckless)
print(student["name"])    # Priya
print(student["age"])     # 22

# Method 2: .get() (safe)
print(student.get("name"))    # Priya
print(student.get("gpa"))     # None (no crash!)
```

Here's the difference: if you use square brackets and the key doesn't exist, Python throws a `KeyError` and your program crashes. If you use `.get()` and the key doesn't exist, it quietly returns `None`. No drama.

```python
# This crashes:
# print(student["gpa"])   # KeyError: 'gpa'

# This doesn't:
print(student.get("gpa"))           # None
print(student.get("gpa", "N/A"))    # N/A (custom default)
```

That second argument to `.get()` is a default value. "If you can't find the key, give me this instead." It's incredibly useful.

> **Pro Tip:** Use square brackets `[]` when you're *sure* the key exists and you *want* it to crash if it doesn't (because that means something is seriously wrong). Use `.get()` when the key *might* not exist and that's okay.

## Adding, Updating, and Deleting

Dictionaries are mutable - you can change them whenever you want.

```python
student = {"name": "Priya", "age": 22}

# Adding a new key-value pair
student["major"] = "Computer Science"
student["gpa"] = 3.8
print(student)
# {'name': 'Priya', 'age': 22, 'major': 'Computer Science', 'gpa': 3.8}

# Updating an existing value
student["age"] = 23    # Happy birthday, Priya!
print(student["age"])  # 23

# Deleting a key-value pair
del student["gpa"]
print(student)
# {'name': 'Priya', 'age': 23, 'major': 'Computer Science'}

# .pop() - delete AND get the value back
major = student.pop("major")
print(major)      # Computer Science
print(student)    # {'name': 'Priya', 'age': 23}
```

Notice that adding and updating use the exact same syntax: `dict[key] = value`. If the key exists, it updates. If it doesn't, it creates. Python figures it out.

## Looping Through Dictionaries

This is where dictionaries get really fun. You can loop through keys, values, or both.

```python
scores = {"math": 95, "english": 87, "science": 92, "history": 78}

# Loop through keys (default behavior)
for subject in scores:
    print(subject)
# math, english, science, history

# Loop through values
for score in scores.values():
    print(score)
# 95, 87, 92, 78

# Loop through both (this is the good one)
for subject, score in scores.items():
    print(f"{subject}: {score}")
# math: 95
# english: 87
# science: 92
# history: 78
```

`.items()` is the one you'll use the most. It gives you both the key and the value on each loop, unpacked into two variables. It's clean, it's readable, it's *chef's kiss*.

```python
# Practical example: find the highest score
scores = {"math": 95, "english": 87, "science": 92, "history": 78}

best_subject = ""
best_score = 0

for subject, score in scores.items():
    if score > best_score:
        best_score = score
        best_subject = subject

print(f"Best subject: {best_subject} ({best_score})")
# Best subject: math (95)
```

## Checking if a Key Exists

Before you access a key, you might want to check if it's there.

```python
student = {"name": "Priya", "age": 22}

# Check if a key exists
if "name" in student:
    print("Name found!")

if "gpa" not in student:
    print("No GPA on file.")
```

The `in` keyword checks keys, not values. If you want to check values, use `in student.values()`.

## Nested Dictionaries: Dictionaries Inside Dictionaries

Things get really powerful when you put dictionaries inside dictionaries. This is how real-world data is structured.

```python
# A class of students with their grades
classroom = {
    "priya": {
        "math": 95,
        "english": 87,
        "science": 92
    },
    "alex": {
        "math": 78,
        "english": 91,
        "science": 85
    },
    "jordan": {
        "math": 88,
        "english": 76,
        "science": 94
    }
}

# Access Priya's math grade
print(classroom["priya"]["math"])  # 95

# Loop through all students and their grades
for student, grades in classroom.items():
    average = sum(grades.values()) / len(grades)
    print(f"{student}: average = {average:.1f}")
# priya: average = 91.3
# alex: average = 84.7
# jordan: average = 86.0
```

Two levels of square brackets: `classroom["priya"]["math"]`. First, get Priya's dictionary. Then, get the math value from that dictionary. It reads like English: "from the classroom, get priya's math."

You can also have lists of dictionaries - this is extremely common when working with data from the internet (APIs, databases, etc.):

```python
# A list of products (like you'd get from an online store API)
products = [
    {"name": "Laptop", "price": 999, "in_stock": True},
    {"name": "Mouse", "price": 29, "in_stock": True},
    {"name": "Webcam", "price": 79, "in_stock": False}
]

# Find all in-stock products under $100
affordable = [p["name"] for p in products if p["in_stock"] and p["price"] < 100]
print(affordable)  # ['Mouse']
```

## Dictionary Comprehensions

Just like list comprehensions (remember those from Chapter 7?), you can create dictionaries with a one-liner.

```python
# Create a dictionary of squares
squares = {x: x**2 for x in range(1, 6)}
print(squares)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Convert a list of names to a dictionary with name lengths
names = ["Priya", "Alex", "Jordan"]
name_lengths = {name: len(name) for name in names}
print(name_lengths)  # {'Priya': 5, 'Alex': 4, 'Jordan': 6}

# Filter a dictionary (only keep scores above 85)
scores = {"math": 95, "english": 87, "science": 72, "history": 78}
good_scores = {subj: score for subj, score in scores.items() if score > 85}
print(good_scores)  # {'math': 95, 'english': 87}
```

The syntax is `{key_expression: value_expression for item in iterable}`. It's the same idea as list comprehensions, but with a colon separating the key and value.

## Merging Dictionaries

Sometimes you need to combine two dictionaries into one. Python gives you a few ways.

```python
defaults = {"theme": "light", "language": "en", "font_size": 14}
user_prefs = {"theme": "dark", "font_size": 18}

# Method 1: ** spread operator (Python 3.5+)
settings = {**defaults, **user_prefs}
print(settings)
# {'theme': 'dark', 'language': 'en', 'font_size': 18}

# Method 2: | merge operator (Python 3.9+)
settings = defaults | user_prefs
print(settings)
# {'theme': 'dark', 'language': 'en', 'font_size': 18}

# Method 3: .update() (modifies in place)
settings = defaults.copy()    # Don't modify the original!
settings.update(user_prefs)
print(settings)
# {'theme': 'dark', 'language': 'en', 'font_size': 18}
```

Notice that when both dictionaries have the same key (like "theme"), the second one wins. The user's preferences override the defaults. That's usually exactly what you want.

> **Wait, What?** The `**` spread operator "unpacks" a dictionary into key-value pairs. When you write `{**dict1, **dict2}`, you're saying "take everything from dict1, then take everything from dict2, and put it all in a new dictionary." If there are duplicates, the last one wins. It's like merging two playlists - the second playlist's version of a song takes priority.

## Useful Dictionary Methods Cheat Sheet

Here are the methods you'll use the most:

```python
student = {"name": "Priya", "age": 22, "major": "CS"}

student.keys()      # dict_keys(['name', 'age', 'major'])
student.values()    # dict_values(['Priya', 22, 'CS'])
student.items()     # dict_items([('name', 'Priya'), ('age', 22), ('major', 'CS')])
student.get("gpa", 0)   # 0 (safe access with default)
student.pop("major")     # Removes and returns 'CS'
student.copy()           # Shallow copy
student.clear()          # Empties the dictionary
len(student)             # Number of key-value pairs
```

## Your Turn: Contact Book

Build a contact book program that lets users:

1. Add a contact (name, phone, email)
2. Look up a contact by name
3. Update a contact's info
4. Delete a contact
5. Display all contacts
6. Quit

Each contact should be stored as a dictionary inside a main contacts dictionary. Use `.get()` for safe lookups and `.items()` for displaying all contacts.

**Starter hint:**

```python
contacts = {}

while True:
    print("\n-- Contact Book --")
    print("1. Add Contact")
    print("2. Look Up Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Show All Contacts")
    print("6. Quit")

    choice = input("\nPick an option: ")

    if choice == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        email = input("Email: ")
        contacts[name] = {"phone": phone, "email": email}
        print(f"Added {name}!")

    # ... fill in the rest!
```

Full solution available at:
`https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/sprint-2-intermediate/chapter-09-dictionaries/`

## TL;DR

- **Dictionaries** store data as **key-value pairs** - access by name, not position.
- Use `dict["key"]` when you're sure the key exists. Use `dict.get("key")` when you're not.
- Add/update with `dict["key"] = value`. Delete with `del dict["key"]` or `.pop("key")`.
- Loop with `.keys()`, `.values()`, or `.items()` (the best one).
- **Nested dictionaries** let you store complex, structured data.
- **Dictionary comprehensions** create dictionaries in one line: `{k: v for k, v in stuff}`.
- **Merge** with `{**dict1, **dict2}` or `dict1 | dict2`.
- Dictionaries are everywhere in Python. APIs, configs, databases - they all speak dictionary.

---

# Chapter 10: Functions: Stop Repeating Yourself

> **Sprint 2, Chapter 10** | **Estimated Time: 15 minutes** | **Difficulty: Intermediate**

Copy-pasting code is like writing the same essay for every class. Sure, it works. But the moment you need to change something, you're editing it in twelve different places, and you WILL forget one. Functions let you write it once and reuse it forever.

Think of a function like a recipe. You define it once - "here's how to make pancakes" - and then you just say "make pancakes" whenever you want them. You don't re-explain the recipe every time.

## Defining and Calling Functions

Here's the simplest function in the world:

```python
def greet():
    print("Hello, world!")

# Call it
greet()   # Hello, world!
greet()   # Hello, world!
greet()   # Hello, world!
```

`def` means "I'm defining a function." Then you give it a name, parentheses, and a colon. Everything indented underneath is the function's body - the code that runs when you call it.

Calling a function is just its name followed by parentheses: `greet()`. Those parentheses are important. Without them, you're just *referring* to the function, not *running* it.

```python
print(greet)    # <function greet at 0x...>  (the function object itself)
print(greet())  # Hello, world!  then  None  (calls the function)
```

## Parameters and Arguments

Functions get really useful when they accept input.

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Priya")    # Hello, Priya!
greet("Alex")     # Hello, Alex!
greet("Jordan")   # Hello, Jordan!
```

`name` is a **parameter** - the variable name in the function definition. `"Priya"` is an **argument** - the actual value you pass in when calling it. People use these terms interchangeably, but now you know the difference and can be annoyingly precise at parties.

Multiple parameters? No problem:

```python
def introduce(name, age, city):
    print(f"I'm {name}, {age} years old, from {city}.")

introduce("Priya", 22, "Mumbai")
# I'm Priya, 22 years old, from Mumbai.
```

## Return Values: Getting Something Back

So far, our functions just print stuff. But the real power is when they *return* a value - give something back that you can store, use, or pass to another function.

```python
def add(a, b):
    return a + b

result = add(3, 5)
print(result)   # 8

# Use it directly in expressions
total = add(10, 20) + add(5, 5)
print(total)    # 40
```

`return` is the magic word. It sends a value back to wherever the function was called. The function stops executing the moment it hits `return`.

```python
def is_adult(age):
    if age >= 18:
        return True
    return False

# Even cleaner:
def is_adult(age):
    return age >= 18
```

> **Wait, What?** "None?! Why does my function return None?" If your function doesn't have a `return` statement, it returns `None` by default. This trips up everyone at least once. If you're saving the result of a function and getting `None`, check if you forgot to `return`.

```python
def add_broken(a, b):
    a + b           # Calculates but doesn't return!

result = add_broken(3, 5)
print(result)   # None  (whoops!)

def add_fixed(a, b):
    return a + b    # Now it actually gives you the answer

result = add_fixed(3, 5)
print(result)   # 8
```

## Default Parameters: The Safety Net

Sometimes you want a parameter to have a fallback value if the caller doesn't provide one.

```python
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Priya")              # Hello, Priya!
greet("Alex", "Hey")        # Hey, Alex!
greet("Jordan", "Yo")       # Yo, Jordan!
```

`greeting="Hello"` means "use 'Hello' unless they give me something else." Default parameters must come *after* non-default ones. Python needs to know which arguments go where.

```python
def create_profile(name, age, city="Unknown", active=True):
    return {
        "name": name,
        "age": age,
        "city": city,
        "active": active
    }

# Only provide what you need
profile = create_profile("Priya", 22)
print(profile)
# {'name': 'Priya', 'age': 22, 'city': 'Unknown', 'active': True}

profile = create_profile("Alex", 30, "London")
print(profile)
# {'name': 'Alex', 'age': 30, 'city': 'London', 'active': True}
```

## Keyword Arguments: Explicit Is Better

When a function has lots of parameters, positional arguments get confusing. Keyword arguments let you name what you're passing.

```python
def create_user(name, age, email, role="viewer"):
    return {"name": name, "age": age, "email": email, "role": role}

# Positional (works but hard to read)
user = create_user("Priya", 22, "priya@email.com", "admin")

# Keyword (crystal clear)
user = create_user(
    name="Priya",
    age=22,
    email="priya@email.com",
    role="admin"
)
```

With keyword arguments, order doesn't matter. You can even mix positional and keyword, but positional must come first.

```python
# This works:
user = create_user("Priya", age=22, email="priya@email.com")

# This doesn't (positional after keyword):
# user = create_user(name="Priya", 22, "priya@email.com")  # SyntaxError!
```

## *args and **kwargs: The Flexible Friends

Sometimes you don't know how many arguments a function will receive. `*args` and `**kwargs` handle that.

```python
# *args: accept any number of positional arguments
def add_all(*numbers):
    return sum(numbers)

print(add_all(1, 2))           # 3
print(add_all(1, 2, 3, 4, 5)) # 15
print(add_all(10))             # 10
```

`*args` collects all extra positional arguments into a tuple. You can name it anything (`*nums`, `*items`), but `*args` is the convention.

```python
# **kwargs: accept any number of keyword arguments
def build_profile(**info):
    return info

profile = build_profile(name="Priya", age=22, city="Mumbai")
print(profile)  # {'name': 'Priya', 'age': 22, 'city': 'Mumbai'}
```

`**kwargs` collects all extra keyword arguments into a dictionary. Again, the name is just convention.

```python
# Combining everything
def super_function(required, *args, **kwargs):
    print(f"Required: {required}")
    print(f"Extra positional: {args}")
    print(f"Extra keyword: {kwargs}")

super_function("hello", 1, 2, 3, color="blue", size="large")
# Required: hello
# Extra positional: (1, 2, 3)
# Extra keyword: {'color': 'blue', 'size': 'large'}
```

> **Pro Tip:** If you're coming from JavaScript, Python functions are like arrow functions but without the `this` headaches. No binding issues, no accidental context loss. `def` is `function`, `return` is `return`, and everything just works. The main difference: Python doesn't hoist functions (well, not exactly), and indentation replaces curly braces.

## Scope: Local vs Global

Variables created inside a function exist only inside that function. This is called **scope**.

```python
def my_function():
    secret = "I only exist in here"
    print(secret)

my_function()       # I only exist in here
# print(secret)     # NameError: name 'secret' is not defined
```

The variable `secret` is **local** to the function. Once the function ends, it's gone. Like a Snapchat message for variables.

Variables created outside functions are **global** - accessible everywhere.

```python
greeting = "Hello"    # Global

def say_hi(name):
    print(f"{greeting}, {name}!")   # Can READ global variables

say_hi("Priya")   # Hello, Priya!
```

You can *read* global variables from inside a function, but you can't *modify* them without the `global` keyword. And honestly? Don't use `global`. It leads to messy, unpredictable code. If a function needs data, pass it as a parameter. If a function produces data, return it.

```python
# Don't do this:
counter = 0
def increment():
    global counter
    counter += 1

# Do this instead:
def increment(counter):
    return counter + 1

counter = 0
counter = increment(counter)
```

## Functions as First-Class Objects

Here's something that might blow your mind: in Python, functions are objects. You can pass them around like any other value.

```python
def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def speak(func, text):
    return func(text)

print(speak(shout, "hello"))     # HELLO
print(speak(whisper, "HELLO"))   # hello
```

We're passing the function itself (not calling it - no parentheses) as an argument. The `speak` function then calls it. This is a powerful pattern that shows up everywhere in Python, especially with `map()`, `filter()`, and `sorted()`.

```python
# Practical example: custom sorting
students = [
    {"name": "Priya", "gpa": 3.8},
    {"name": "Alex", "gpa": 3.2},
    {"name": "Jordan", "gpa": 3.9}
]

def get_gpa(student):
    return student["gpa"]

# Sort by GPA
ranked = sorted(students, key=get_gpa, reverse=True)
for s in ranked:
    print(f"{s['name']}: {s['gpa']}")
# Jordan: 3.9
# Priya: 3.8
# Alex: 3.2
```

## Multiple Return Values

Python functions can return multiple values using tuples (remember those from Chapter 8?).

```python
def get_stats(numbers):
    return min(numbers), max(numbers), sum(numbers) / len(numbers)

low, high, avg = get_stats([4, 8, 15, 16, 23, 42])
print(f"Low: {low}, High: {high}, Average: {avg:.1f}")
# Low: 4, High: 42, Average: 18.0
```

It looks like magic, but Python is just packing the values into a tuple and then unpacking them into separate variables.

## Your Turn: Password Strength Checker

Write a function called `check_password` that takes a password string and returns a strength rating: "Weak", "Medium", or "Strong".

Rules:
- **Weak:** Less than 8 characters
- **Medium:** At least 8 characters AND has both letters and numbers
- **Strong:** At least 12 characters, has uppercase, lowercase, numbers, AND special characters

Also write a `has_special_chars` helper function that checks for special characters.

```python
def has_special_chars(password):
    special = "!@#$%^&*()_+-=[]{}|;:',.<>?/"
    # Your code here

def check_password(password):
    # Your code here
    pass

# Test it
print(check_password("abc"))           # Weak
print(check_password("hello123"))      # Medium
print(check_password("MyP@ssw0rd!23")) # Strong
```

Full solution available at:
`https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/sprint-2-intermediate/chapter-10-functions/`

## TL;DR

- **Functions** let you write reusable blocks of code with `def`.
- **Parameters** are placeholders; **arguments** are the actual values you pass in.
- **`return`** sends a value back. No `return` = you get `None`.
- **Default parameters** give fallback values: `def greet(name, greeting="Hi")`.
- **Keyword arguments** make calls readable: `greet(name="Priya")`.
- **`*args`** collects extra positional args into a tuple. **`**kwargs`** collects extra keyword args into a dict.
- Variables inside functions are **local** - they disappear when the function ends.
- Functions are **first-class objects** - pass them around like any other value.
- When in doubt, make it a function. Seriously.

---

# Chapter 11: Modules & Packages: Standing on Giants' Shoulders

> **Sprint 2, Chapter 11** | **Estimated Time: 12-15 minutes** | **Difficulty: Intermediate**

Why build everything from scratch when thousands of developers have already built it for you? That would be like insisting on growing your own wheat every time you want a sandwich.

Python's real superpower isn't the language itself - it's the ecosystem. There are tens of thousands of ready-made packages for everything from sending emails to training AI models. And you get to use them with a single line of code.

## Import Styles: Three Ways to Borrow Code

A **module** is just a Python file full of useful stuff. A **package** is a folder full of modules. When you `import` something, you're saying "hey, let me use that code."

```python
# Style 1: Import the whole module
import random
print(random.randint(1, 10))

# Style 2: Import specific things
from random import randint, choice
print(randint(1, 10))
print(choice(["pizza", "tacos", "sushi"]))

# Style 3: Import with an alias
import datetime as dt
today = dt.date.today()
print(today)
```

**Style 1** is the safest - you always know where a function came from because it's prefixed with the module name. **Style 2** is convenient for things you use a lot. **Style 3** is great for modules with long names.

One style you should almost never use:

```python
# Don't do this (imports EVERYTHING into your namespace)
from random import *
```

This dumps every function from the module into your code, and you lose track of where things came from. It's like dumping every tool from the toolbox onto the floor. Sure, they're all "available," but good luck finding anything.

> **Remember When?** Remember how we used `random` in the username generator back in the early chapters? That was a module! You've been using modules this whole time. Now you'll understand what's actually happening behind the scenes.

## Standard Library Greatest Hits

Python comes with a massive standard library - modules that are installed automatically with Python. No `pip install` needed. Here are the greatest hits.

### random - When You Need Chaos

```python
import random

# Random integer between 1 and 100
print(random.randint(1, 100))

# Random choice from a list
foods = ["pizza", "tacos", "ramen", "sushi"]
print(random.choice(foods))

# Shuffle a list in place
cards = ["A", "K", "Q", "J", "10"]
random.shuffle(cards)
print(cards)   # Different every time!

# Random float between 0 and 1
print(random.random())   # 0.7234... something

# Random sample (pick 3 without repeating)
lottery = random.sample(range(1, 50), 3)
print(lottery)   # e.g., [17, 42, 3]
```

### datetime - Time Is on Your Side

```python
from datetime import datetime, date, timedelta

# Current date and time
now = datetime.now()
print(now)                           # 2026-04-01 14:30:00.123456
print(now.strftime("%B %d, %Y"))     # April 01, 2026
print(now.strftime("%I:%M %p"))      # 02:30 PM

# Just the date
today = date.today()
print(today)              # 2026-04-01
print(today.year)         # 2026
print(today.month)        # 4
print(today.weekday())    # 2 (Wednesday, 0=Monday)

# Date math with timedelta
tomorrow = today + timedelta(days=1)
last_week = today - timedelta(weeks=1)
print(f"Tomorrow: {tomorrow}")
print(f"Last week: {last_week}")

# How many days until New Year?
new_year = date(2027, 1, 1)
days_left = (new_year - today).days
print(f"Days until 2027: {days_left}")
```

### os - Talk to Your Computer

```python
import os

# Current working directory
print(os.getcwd())

# List files in a directory
files = os.listdir(".")
print(files)

# Check if a file exists
if os.path.exists("data.txt"):
    print("File found!")
else:
    print("No such file.")

# Create a directory
os.makedirs("output/reports", exist_ok=True)

# Get environment variables
home = os.environ.get("HOME", "Not found")
print(f"Home directory: {home}")
```

### math - For When You Need Real Math

```python
import math

print(math.pi)          # 3.141592653589793
print(math.sqrt(144))   # 12.0
print(math.ceil(4.1))   # 5 (round up)
print(math.floor(4.9))  # 4 (round down)
print(math.factorial(5)) # 120 (5! = 5*4*3*2*1)

# Practical: calculate distance between two points
def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(distance(0, 0, 3, 4))  # 5.0
```

### json - The Internet's Favorite Format

JSON is how the internet passes data around. It looks almost exactly like Python dictionaries, which makes it really easy to work with.

```python
import json

# Python dictionary to JSON string
data = {"name": "Priya", "age": 22, "scores": [95, 87, 92]}
json_string = json.dumps(data, indent=2)
print(json_string)
# {
#   "name": "Priya",
#   "age": 22,
#   "scores": [95, 87, 92]
# }

# JSON string back to Python dictionary
parsed = json.loads(json_string)
print(parsed["name"])   # Priya
print(type(parsed))     # <class 'dict'>
```

We'll use JSON a lot more in Chapter 12 when we learn file handling. For now, just know that `json.dumps()` converts Python to JSON, and `json.loads()` converts JSON back to Python.

## pip install: Getting Packages from the Internet

The standard library is great, but the real magic is **PyPI** (Python Package Index) - a massive repository of packages built by the community. Over 500,000 packages and counting.

To install a package, you use `pip`:

```bash
# Install a package
pip install requests

# Install a specific version
pip install requests==2.31.0

# Install multiple packages
pip install requests flask pandas

# See what's installed
pip list

# Uninstall a package
pip uninstall requests
```

Let's install and use `requests`, the most popular package for making web requests:

```python
# After: pip install requests
import requests

response = requests.get("https://api.github.com")
print(response.status_code)   # 200
print(response.json())        # The response as a dictionary
```

Three lines of code to talk to the internet. That's the power of packages.

## Virtual Environments: Keeping Your Projects from Fighting

Here's the problem: you're working on Project A, which needs `requests` version 2.25. Then you start Project B, which needs `requests` version 2.31. If you install both globally, they'll conflict.

Virtual environments solve this. They're isolated Python environments for each project. Think of them like separate apartments - each project gets its own space with its own furniture.

```bash
# Create a virtual environment
python -m venv myproject_env

# Activate it (Windows)
myproject_env\Scripts\activate

# Activate it (Mac/Linux)
source myproject_env/bin/activate

# Your terminal prompt changes to show you're in the venv
# (myproject_env) $

# Now pip install only affects THIS environment
pip install requests

# When you're done
deactivate
```

> **Pro Tip:** Always create a virtual environment for every new project. It takes 5 seconds and saves hours of debugging dependency conflicts. The standard workflow is: create folder, create venv, activate venv, pip install stuff, start coding.

### requirements.txt: Sharing Your Dependencies

When you share your project, other people need to know what packages to install. That's what `requirements.txt` is for.

```bash
# Save your current packages to a file
pip freeze > requirements.txt

# Someone else can install everything at once
pip install -r requirements.txt
```

A typical `requirements.txt` looks like:

```
requests==2.31.0
flask==3.0.0
pandas==2.1.0
```

It's like a grocery list for your project. "Here's everything you need to run this code."

## Creating Your Own Modules

You can also make your own modules. It's literally just a Python file.

```python
# helpers.py
def greet(name):
    return f"Hello, {name}!"

def add(a, b):
    return a + b

PI = 3.14159
```

```python
# main.py (same folder)
import helpers

print(helpers.greet("Priya"))   # Hello, Priya!
print(helpers.add(3, 5))        # 8
print(helpers.PI)               # 3.14159

# Or import specific things
from helpers import greet, PI
print(greet("Alex"))   # Hello, Alex!
```

That's it. Any `.py` file can be imported as a module. This is how you keep your code organized as projects grow.

## The if __name__ == "__main__" Pattern

You'll see this in almost every Python file. Here's what it does:

```python
# my_module.py
def calculate_tax(amount, rate=0.08):
    return amount * rate

# This code ONLY runs if you execute this file directly
# It does NOT run if someone imports this file
if __name__ == "__main__":
    # Test our function
    print(calculate_tax(100))    # 8.0
    print(calculate_tax(50, 0.1))  # 5.0
```

When you run `python my_module.py`, `__name__` is `"__main__"`, so the test code runs. When someone does `import my_module`, `__name__` is `"my_module"`, so the test code is skipped. It's a way to have test code that doesn't interfere with imports.

## Your Turn: Random Quote Generator from JSON

Create a file called `quotes.json` with at least 10 quotes:

```json
{
    "quotes": [
        {"text": "Be yourself; everyone else is already taken.", "author": "Oscar Wilde"},
        {"text": "Two things are infinite: the universe and human stupidity.", "author": "Albert Einstein"},
        {"text": "In the middle of difficulty lies opportunity.", "author": "Albert Einstein"}
    ]
}
```

Then write a Python script that:
1. Loads the quotes from the JSON file
2. Picks a random quote
3. Displays it nicely formatted
4. Asks if the user wants another quote (loop until they say no)
5. Bonus: Let the user filter quotes by author

You'll need: `json`, `random`, and file handling (sneak peek of Chapter 12 - use `open("quotes.json") as f` and `json.load(f)`).

Full solution available at:
`https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/sprint-2-intermediate/chapter-11-modules/`

## TL;DR

- **Modules** are Python files with reusable code. **Packages** are folders of modules.
- Three import styles: `import x`, `from x import y`, `import x as z`. Avoid `from x import *`.
- **Standard library** highlights: `random`, `datetime`, `os`, `math`, `json`.
- **pip** installs packages from PyPI: `pip install requests`.
- **Virtual environments** keep project dependencies isolated: `python -m venv myenv`.
- **requirements.txt** documents your dependencies for others.
- Any `.py` file is a module. Use `if __name__ == "__main__":` to separate importable code from test code.
- Don't reinvent the wheel. Someone probably already wrote a package for what you need.

---

# Chapter 12: File Handling: Reading & Writing Like a Pro

> **Sprint 2, Chapter 12** | **Estimated Time: 12-15 minutes** | **Difficulty: Intermediate**

So far, everything we've built disappears when the program stops. That's like writing a novel and forgetting to hit save. Your contact book? Gone. Your quiz scores? Poof. Your user data? Vanished into the void.

Let's fix that. This chapter is about making your data *survive*.

## Writing Files: The with Statement

The safest way to write to a file in Python is the `with` statement. It opens the file, lets you do your thing, and then automatically closes it when you're done - even if something goes wrong.

```python
# Write to a file
with open("hello.txt", "w") as f:
    f.write("Hello, world!\n")
    f.write("This is my first file.\n")
    f.write("Python is awesome.\n")
```

Let's break that down:
- `open("hello.txt", "w")` - opens (or creates) a file called `hello.txt` in **write** mode
- `as f` - gives us a variable `f` to work with (short for "file")
- `f.write()` - writes text to the file
- `\n` - newline character (hit Enter)

The `"w"` mode creates the file if it doesn't exist. But be careful: if the file already exists, **it overwrites everything**. It's the nuclear option.

> **Wait, What?** Always use `with open()`. If you use `open()` without `with`, you have to remember to call `f.close()` yourself. And if your code crashes before it gets to `f.close()`, your data might not get saved. The `with` statement handles all of that automatically. Trust me on this one.

```python
# Writing multiple lines at once
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open("multi.txt", "w") as f:
    f.writelines(lines)

# Writing with print (yes, print can write to files!)
with open("print_file.txt", "w") as f:
    print("This goes to the file!", file=f)
    print("So does this!", file=f)
```

## Reading Files

Now let's read those files back.

```python
# Method 1: Read the entire file as one big string
with open("hello.txt", "r") as f:
    content = f.read()
print(content)
# Hello, world!
# This is my first file.
# Python is awesome.

# Method 2: Read all lines into a list
with open("hello.txt", "r") as f:
    lines = f.readlines()
print(lines)
# ['Hello, world!\n', 'This is my first file.\n', 'Python is awesome.\n']

# Method 3: Read line by line (best for large files)
with open("hello.txt", "r") as f:
    for line in f:
        print(line.strip())   # .strip() removes the \n
# Hello, world!
# This is my first file.
# Python is awesome.
```

Method 3 is the most memory-efficient. It reads one line at a time instead of loading the entire file into memory. For a small text file, it doesn't matter. For a 2GB log file? It matters a lot.

The `"r"` in `open("hello.txt", "r")` means read mode. It's actually the default, so you can leave it out: `open("hello.txt")` does the same thing.

## Appending: Adding Without Destroying

What if you want to add to a file without wiping everything? That's **append** mode: `"a"`.

```python
# Add to existing file
with open("hello.txt", "a") as f:
    f.write("This line was added later.\n")
    f.write("And so was this one.\n")
```

Now `hello.txt` has its original three lines plus two new ones. Nothing was deleted. It's like adding entries to a journal instead of starting a new one every day.

```python
# Practical example: a simple logger
from datetime import datetime

def log_message(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("app.log", "a") as f:
        f.write(f"[{timestamp}] {message}\n")

log_message("Application started")
log_message("User logged in")
log_message("Data saved successfully")
```

Your `app.log` file will look like:

```
[2026-04-01 14:30:00] Application started
[2026-04-01 14:30:01] User logged in
[2026-04-01 14:30:02] Data saved successfully
```

## File Modes Cheat Sheet

| Mode | What It Does | Creates File? | Overwrites? |
|---|-------|--------|-------|
| `"r"` | Read only | No (error if missing) | No |
| `"w"` | Write only | Yes | Yes (destroys old data!) |
| `"a"` | Append | Yes | No (adds to end) |
| `"r+"` | Read and write | No | Depends on position |
| `"x"` | Create and write | Yes (error if exists) | N/A |

## Checking if a File Exists

Before reading a file, you might want to make sure it's actually there.

```python
import os

if os.path.exists("data.txt"):
    with open("data.txt", "r") as f:
        content = f.read()
    print(content)
else:
    print("File not found! Creating it...")
    with open("data.txt", "w") as f:
        f.write("Fresh start!\n")
```

## CSV Files: Spreadsheet Data in Python

CSV (Comma-Separated Values) is the simplest way to store tabular data. Every spreadsheet app can open it. It looks like this:

```
name,age,city
Priya,22,Mumbai
Alex,30,London
Jordan,25,New York
```

Python's built-in `csv` module makes reading and writing CSV files painless.

### Writing CSV Files

```python
import csv

# Writing with csv.writer
students = [
    ["name", "age", "grade"],
    ["Priya", 22, "A"],
    ["Alex", 30, "B+"],
    ["Jordan", 25, "A-"]
]

with open("students.csv", "w", newline="") as f:
    writer = csv.writer(f)
    for row in students:
        writer.writerow(row)

# Or write all rows at once
with open("students.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(students)
```

That `newline=""` parameter prevents extra blank lines on Windows. Just always include it.

### Reading CSV Files

```python
import csv

# Method 1: csv.reader (gives you lists)
with open("students.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
# ['name', 'age', 'grade']
# ['Priya', '22', 'A']
# ['Alex', '30', 'B+']
# ['Jordan', '25', 'A-']
```

> **Pro Tip:** `csv.DictReader` is almost always better than `csv.reader`. Instead of accessing columns by index (`row[0]`, `row[1]`), you access them by header name (`row["name"]`, `row["age"]`). It's more readable, and your code won't break if the column order changes.

```python
# Method 2: csv.DictReader (gives you dictionaries - way better)
with open("students.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"{row['name']} is {row['age']} years old with grade {row['grade']}")
# Priya is 22 years old with grade A
# Alex is 30 years old with grade B+
# Jordan is 25 years old with grade A-
```

And writing with `DictWriter`:

```python
import csv

students = [
    {"name": "Priya", "age": 22, "grade": "A"},
    {"name": "Alex", "age": 30, "grade": "B+"},
    {"name": "Jordan", "age": 25, "grade": "A-"}
]

with open("students.csv", "w", newline="") as f:
    fieldnames = ["name", "age", "grade"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(students)
```

## JSON Files: The Internet's Favorite Format

You met `json` briefly in Chapter 11. Now let's use it with files. JSON is perfect for storing structured data - dictionaries, lists, nested data. It's what every web API speaks.

```python
import json

# Write Python data to a JSON file
data = {
    "app_name": "My Todo App",
    "version": "1.0",
    "tasks": [
        {"title": "Learn Python", "done": True},
        {"title": "Build a project", "done": False},
        {"title": "Get hired", "done": False}
    ]
}

with open("data.json", "w") as f:
    json.dump(data, f, indent=2)
```

This creates a beautiful, readable JSON file:

```json
{
  "app_name": "My Todo App",
  "version": "1.0",
  "tasks": [
    {
      "title": "Learn Python",
      "done": true
    },
    {
      "title": "Build a project",
      "done": false
    },
    {
      "title": "Get hired",
      "done": false
    }
  ]
}
```

Reading it back:

```python
import json

with open("data.json", "r") as f:
    data = json.load(f)

print(data["app_name"])           # My Todo App
print(data["tasks"][0]["title"])   # Learn Python

# Modify and save back
data["tasks"][0]["done"] = True
with open("data.json", "w") as f:
    json.dump(data, f, indent=2)
```

Notice the difference:
- `json.dump()` / `json.load()` - work with **files**
- `json.dumps()` / `json.loads()` - work with **strings**

The 's' stands for 'string'. Dump to string, load from string.

## Practical Example: Settings Manager

Here's a real-world pattern - loading and saving app settings:

```python
import json
import os

SETTINGS_FILE = "settings.json"

DEFAULT_SETTINGS = {
    "theme": "light",
    "font_size": 14,
    "language": "en",
    "notifications": True
}

def load_settings():
    if os.path.exists(SETTINGS_FILE):
        with open(SETTINGS_FILE, "r") as f:
            return json.load(f)
    return DEFAULT_SETTINGS.copy()

def save_settings(settings):
    with open(SETTINGS_FILE, "w") as f:
        json.dump(settings, f, indent=2)

# Usage
settings = load_settings()
print(f"Current theme: {settings['theme']}")

settings["theme"] = "dark"
settings["font_size"] = 18
save_settings(settings)
print("Settings saved!")
```

First run: no settings file exists, so it uses defaults. After you change and save, the settings persist across runs. Your app remembers things now. It's alive. Well, not alive. But it has memory.

## Your Turn: Diary App

Build a diary/journal app that:

1. Asks the user for a diary entry
2. Saves it to a file with the current date and time
3. Can display all past entries
4. Each entry is timestamped and separated by a divider

**Starter hint:**

```python
from datetime import datetime

DIARY_FILE = "diary.txt"

def add_entry():
    entry = input("\nWhat's on your mind?\n> ")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

    with open(DIARY_FILE, "a") as f:
        f.write(f"\n-- {timestamp} --\n")
        f.write(f"{entry}\n")

    print("Entry saved!")

def read_entries():
    # Your code here - read and display the diary file
    pass

# Main loop
while True:
    print("\n-- My Diary --")
    print("1. New Entry")
    print("2. Read Entries")
    print("3. Quit")

    choice = input("\nChoice: ")
    # ... handle choices
```

**Bonus challenges:**
- Store entries as JSON instead of plain text
- Add the ability to search entries by keyword
- Add entry categories (work, personal, ideas)

Full solution available at:
`https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/sprint-2-intermediate/chapter-12-file-handling/`

## TL;DR

- **Always use `with open()`** - it handles closing the file automatically.
- **Write mode (`"w"`)** creates or overwrites. **Append mode (`"a"`)** adds without destroying. **Read mode (`"r"`)** is the default.
- For large files, read **line by line** with a for loop instead of `.read()`.
- **CSV**: Use `csv.DictReader` and `csv.DictWriter` for readable, maintainable code.
- **JSON**: Use `json.dump()`/`json.load()` for files, `json.dumps()`/`json.loads()` for strings.
- `newline=""` in your `open()` call prevents double-spacing in CSV files on Windows.
- Your programs can finally remember things between runs. That's a superpower.

---

# Chapter 13: Error Handling: When Things Go Wrong (And They Will)

> **Sprint 2, Chapter 13** | **Estimated Time: 12-15 minutes** | **Difficulty: Intermediate**

Here's a truth bomb: your code WILL crash. Not might. Will. Every developer in the world writes code that breaks. The difference between a junior and a senior isn't that the senior writes bug-free code - it's that the senior's code breaks *gracefully*.

Think of error handling like a seatbelt. You don't wear a seatbelt because you plan to crash. You wear it because you're not an idiot.

## The Common Exceptions Tour

Before we learn to catch errors, let's meet the usual suspects. These are the errors you'll see most often, and recognizing them is half the battle.

```python
# TypeError - wrong type for an operation
result = "hello" + 5
# TypeError: can only concatenate str (not "int") to str

# ValueError - right type, wrong value
number = int("hello")
# ValueError: invalid literal for int() with base 10: 'hello'

# KeyError - dictionary key doesn't exist
data = {"name": "Priya"}
print(data["age"])
# KeyError: 'age'

# IndexError - list index out of range
colors = ["red", "blue", "green"]
print(colors[10])
# IndexError: list index out of range

# NameError - variable doesn't exist
print(undefined_variable)
# NameError: name 'undefined_variable' is not defined

# FileNotFoundError - file doesn't exist
with open("nonexistent.txt") as f:
    content = f.read()
# FileNotFoundError: [Errno 2] No such file or directory: 'nonexistent.txt'

# ZeroDivisionError - math says no
result = 10 / 0
# ZeroDivisionError: division by zero

# AttributeError - object doesn't have that method/property
number = 42
number.upper()
# AttributeError: 'int' object has no attribute 'upper'
```

> **Don't Panic:** Errors aren't failures. They're Python telling you exactly what went wrong and where. Read the last line of the error message first - it tells you the error type and what happened. Then look at the line number. It's actually being helpful. Like a friend who says "Hey, you have spinach in your teeth" instead of letting you walk around like that.

## try/except: Your Safety Net

The `try/except` block lets you attempt something risky and handle the fallout if it goes wrong.

```python
try:
    number = int(input("Enter a number: "))
    print(f"You entered: {number}")
except ValueError:
    print("That's not a number!")
```

If the user types "42", it works normally. If they type "pizza", Python catches the `ValueError` and runs the `except` block instead of crashing. The program keeps going.

```python
# Without error handling:
age = int(input("Age: "))   # Crashes if user types "twenty"

# With error handling:
try:
    age = int(input("Age: "))
except ValueError:
    print("Please enter a number, not text.")
    age = 0   # Fallback value
```

## Catching Specific vs General Exceptions

You should always catch *specific* exceptions when you can.

```python
# Good - specific exceptions
try:
    data = {"name": "Priya"}
    print(data["age"])
except KeyError:
    print("Key not found!")

# Okay for quick scripts - catch multiple specific exceptions
try:
    value = int(input("Number: "))
    result = 10 / value
except ValueError:
    print("That's not a valid number.")
except ZeroDivisionError:
    print("Can't divide by zero!")

# You can also group them
try:
    # risky code
    value = int(input("Number: "))
    result = 10 / value
except (ValueError, ZeroDivisionError) as e:
    print(f"Something went wrong: {e}")
```

Catching the general `Exception` is like using a giant net to catch fish - sure, you'll catch everything, but you might also catch a boot, a tire, and a very confused turtle.

```python
# Avoid this unless you have a good reason
try:
    # some code
    pass
except Exception:
    print("Something went wrong!")  # But WHAT went wrong??

# If you must catch everything, at least log the error
try:
    risky_operation()
except Exception as e:
    print(f"Error: {type(e).__name__}: {e}")
```

The `as e` part captures the exception object so you can see what actually happened. Always do this if you're catching broad exceptions.

## else and finally: The Cleanup Crew

`try/except` has two optional sidekicks: `else` and `finally`.

```python
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("That's not a number!")
else:
    # Only runs if NO exception occurred
    print(f"Great! {number} squared is {number ** 2}")
finally:
    # ALWAYS runs, no matter what
    print("Thanks for playing!")
```

- **`else`** runs only if the `try` block succeeded. It's the "if everything went well" block.
- **`finally`** runs no matter what - exception or no exception. It's the "cleanup" block. Use it for things that must happen regardless: closing connections, saving progress, etc.

```python
# Practical example: file handling with full error handling
def read_config(filename):
    try:
        with open(filename, "r") as f:
            config = f.read()
    except FileNotFoundError:
        print(f"Config file '{filename}' not found. Using defaults.")
        config = "default settings"
    except PermissionError:
        print(f"No permission to read '{filename}'.")
        config = "default settings"
    else:
        print(f"Config loaded successfully from '{filename}'.")
    finally:
        print("Config initialization complete.")

    return config
```

## Raising Your Own Exceptions

Sometimes YOU want to be the one throwing the error. Maybe a function received invalid input and you want to stop everything with a clear message.

```python
def set_age(age):
    if age < 0:
        raise ValueError("Age can't be negative!")
    if age > 150:
        raise ValueError("That's not a realistic age!")
    return age

# This works fine
set_age(25)

# These raise exceptions
try:
    set_age(-5)
except ValueError as e:
    print(e)   # Age can't be negative!

try:
    set_age(200)
except ValueError as e:
    print(e)   # That's not a realistic age!
```

`raise` is the keyword. You create an exception with a descriptive message, and it bubbles up until something catches it. If nothing catches it, the program crashes with your message.

```python
def withdraw(balance, amount):
    if amount <= 0:
        raise ValueError("Withdrawal amount must be positive")
    if amount > balance:
        raise ValueError(f"Insufficient funds. Balance: ${balance}")
    return balance - amount

try:
    new_balance = withdraw(100, 150)
except ValueError as e:
    print(f"Transaction failed: {e}")
# Transaction failed: Insufficient funds. Balance: $100
```

## Custom Exception Classes

For bigger projects, you can create your own exception types. This makes your error handling more specific and meaningful.

```python
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        self.deficit = amount - balance
        super().__init__(
            f"Cannot withdraw ${amount}. "
            f"Balance: ${balance}. "
            f"Short by: ${self.deficit}"
        )

class InvalidAmountError(Exception):
    pass

def withdraw(balance, amount):
    if amount <= 0:
        raise InvalidAmountError("Amount must be positive")
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount

try:
    new_balance = withdraw(100, 250)
except InsufficientFundsError as e:
    print(e)
    print(f"You're short by ${e.deficit}")
except InvalidAmountError as e:
    print(e)
```

Don't worry if custom exceptions feel advanced right now. We'll dig deeper into classes in Sprint 3. For now, just know that the pattern exists.

## The try/except Loop Pattern

One of the most useful patterns is wrapping user input in a try/except loop that keeps asking until they get it right.

```python
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("That's not a valid number. Try again!")

# This will keep asking until the user enters a real number
age = get_number("Enter your age: ")
price = get_number("Enter the price: ")
```

This is the bulletproof input pattern. The user can type "fish" seventeen times and your program won't crash. It'll just patiently ask again. Like a kindergarten teacher.

> **Remember When?** Remember the tip calculator from Chapter 3? If someone typed "pizza" instead of a number, the whole thing crashed. Now you can make it unbreakable. That's growth.

## Five Practical Debugging Tips

When errors happen and you're staring at your screen in confusion, try these:

**1. Read the error message. No, actually read it.**

```python
# Python gives you the file, line number, and error type
# Traceback (most recent call last):
#   File "app.py", line 15, in calculate_total
#     result = price * quantity
# TypeError: can't multiply sequence by non-int of type 'str'
```

Start from the bottom. `TypeError` - wrong type. `can't multiply sequence by non-int of type 'str'` - you're trying to multiply a string. Line 15 in `app.py`. Go fix it.

**2. Print everything.**

```python
def calculate(data):
    print(f"DEBUG: data = {data}, type = {type(data)}")  # Temporary
    # ... rest of function
```

When in doubt, print the value AND its type. Half of all bugs are type mismatches.

**3. Isolate the problem.**

Comment out code until the error goes away. Then uncomment line by line until it comes back. Now you've found the culprit.

**4. Check your assumptions.**

"I'm SURE this variable is a list." Are you? Print it. "This file DEFINITELY exists." Does it? Check. Your assumptions are lying to you more often than you think.

**5. Rubber duck debugging.**

Explain your code, line by line, to a rubber duck (or a pet, or an imaginary friend, or an actual friend who owes you a favor). The act of explaining it out loud often reveals the bug. This is a real technique used by actual professional developers. No, seriously.

## Your Turn: Crash-Proof Tip Calculator

Take this basic tip calculator and make it completely crash-proof:

```python
# The fragile version
meal_cost = float(input("Meal cost: $"))
tip_percent = float(input("Tip percentage: "))
num_people = int(input("Split between how many people? "))

tip = meal_cost * (tip_percent / 100)
total = meal_cost + tip
per_person = total / num_people

print(f"\nTip: ${tip:.2f}")
print(f"Total: ${total:.2f}")
print(f"Per person: ${per_person:.2f}")
```

Your crash-proof version should handle:
- Non-numeric input (ValueError)
- Zero or negative meal cost
- Negative tip percentage
- Zero or negative number of people (ZeroDivisionError)
- Use the `get_number` loop pattern from this chapter
- Wrap the whole thing in a "calculate again?" loop

Full solution available at:
`https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/sprint-2-intermediate/chapter-13-error-handling/`

## TL;DR

- **Your code will crash.** Error handling decides whether it crashes gracefully or explosively.
- **`try/except`** catches exceptions before they kill your program.
- Always catch **specific exceptions** (`ValueError`, `KeyError`) instead of bare `except`.
- **`else`** runs when no exception occurs. **`finally`** runs no matter what.
- **`raise`** lets you throw your own exceptions with custom messages.
- **Custom exception classes** make your errors more descriptive (we'll learn more about classes in Sprint 3).
- **Read error messages** from the bottom up. Python is literally telling you what went wrong.
- The **try/except input loop** pattern is your best friend for user-facing code.
- Debugging is a skill, not a talent. Print stuff, isolate the problem, and talk to a duck.

---

# Chapter 14: Lambda, Map, Filter, Reduce: The One-Liners

> **Sprint 2, Chapter 14** | **Estimated Time: 12-15 minutes** | **Difficulty: Intermediate**

What if I told you that you could replace a 5-line loop with a single line of code? You'd probably say "that sounds either amazing or unreadable." And honestly? You'd be right on both counts.

Welcome to functional programming lite. These tools won't replace everything you've learned - but they'll give you some seriously elegant shortcuts for common patterns.

> **Don't Panic:** This chapter looks fancy, but it's really just shortcuts for things you already know how to do with loops. If `map()` and `filter()` confuse you, you can always fall back to a regular for loop. Nobody will judge you. (Okay, some people on Reddit might. But ignore those people.)

## Lambda Functions: Anonymous and Proud

A lambda is a tiny, nameless function that fits on one line. It's for when you need a quick function and don't want to waste three lines defining it.

```python
# Regular function
def double(x):
    return x * 2

# Lambda equivalent
double = lambda x: x * 2

# Both work the same way
print(double(5))   # 10
```

The syntax is: `lambda parameters: expression`. No `def`, no name, no `return` - the expression IS the return value.

```python
# One parameter
square = lambda x: x ** 2
print(square(4))   # 16

# Multiple parameters
add = lambda a, b: a + b
print(add(3, 7))   # 10

# With a conditional
grade = lambda score: "Pass" if score >= 60 else "Fail"
print(grade(75))    # Pass
print(grade(45))    # Fail
```

Now, here's the thing: storing a lambda in a variable kind of defeats the purpose. If you're going to name it, just write a regular function - it's more readable. Lambdas shine when you use them *inline*, as throwaway functions passed to other functions.

```python
# This is where lambdas actually make sense
students = [
    {"name": "Priya", "gpa": 3.8},
    {"name": "Alex", "gpa": 3.2},
    {"name": "Jordan", "gpa": 3.9}
]

# Sort by GPA using a lambda (no need for a named function)
ranked = sorted(students, key=lambda s: s["gpa"], reverse=True)
for s in ranked:
    print(f"{s['name']}: {s['gpa']}")
# Jordan: 3.9
# Priya: 3.8
# Alex: 3.2
```

That `key=lambda s: s["gpa"]` is saying: "for each student `s`, the sorting key is their GPA." Clean, compact, readable. This is the lambda sweet spot.

## map(): Transform Everything

`map()` applies a function to every item in a list (or any iterable). It's the "do this to all of them" function.

```python
# Without map (regular loop)
numbers = [1, 2, 3, 4, 5]
squared = []
for n in numbers:
    squared.append(n ** 2)
print(squared)   # [1, 4, 9, 16, 25]

# With map
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)   # [1, 4, 9, 16, 25]
```

`map(function, iterable)` returns a map object (lazy - doesn't compute until needed). Wrap it in `list()` to see the results.

More practical examples:

```python
# Convert strings to integers
str_numbers = ["10", "20", "30", "40"]
int_numbers = list(map(int, str_numbers))
print(int_numbers)   # [10, 20, 30, 40]

# Clean up user input
names = ["  priya  ", "ALEX", " jordan"]
cleaned = list(map(lambda n: n.strip().title(), names))
print(cleaned)   # ['Priya', 'Alex', 'Jordan']

# Extract one field from a list of dictionaries
products = [
    {"name": "Laptop", "price": 999},
    {"name": "Mouse", "price": 29},
    {"name": "Keyboard", "price": 79}
]
prices = list(map(lambda p: p["price"], products))
print(prices)   # [999, 29, 79]

# Apply a discount to all prices
discounted = list(map(lambda p: round(p * 0.9, 2), prices))
print(discounted)   # [899.1, 26.1, 71.1]
```

Notice how `map(int, str_numbers)` doesn't need a lambda - `int` is already a function that takes one argument. When the function already exists, just pass it directly.

## filter(): Keep Only the Good Stuff

`filter()` keeps items that pass a test. The function should return `True` (keep) or `False` (discard).

```python
# Without filter
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = []
for n in numbers:
    if n % 2 == 0:
        evens.append(n)
print(evens)   # [2, 4, 6, 8, 10]

# With filter
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)   # [2, 4, 6, 8, 10]
```

The lambda returns `True` for even numbers and `False` for odd ones. `filter()` keeps only the `True` ones.

```python
# Filter out empty strings
words = ["hello", "", "world", "", "python", ""]
non_empty = list(filter(None, words))
print(non_empty)   # ['hello', 'world', 'python']

# Adults only
people = [
    {"name": "Priya", "age": 22},
    {"name": "Timmy", "age": 10},
    {"name": "Alex", "age": 30},
    {"name": "Zoe", "age": 15}
]
adults = list(filter(lambda p: p["age"] >= 18, people))
print(adults)
# [{'name': 'Priya', 'age': 22}, {'name': 'Alex', 'age': 30}]

# Passing scores only
scores = [45, 78, 92, 33, 67, 88, 51, 95]
passing = list(filter(lambda s: s >= 60, scores))
print(passing)   # [78, 92, 67, 88, 95]
```

The `filter(None, words)` trick filters out anything "falsy" - empty strings, `0`, `None`, `False`, etc. Handy for cleaning data.

## Combining map() and filter()

The real power comes from chaining these together.

```python
# Get names of students with GPA above 3.5
students = [
    {"name": "Priya", "gpa": 3.8},
    {"name": "Alex", "gpa": 3.2},
    {"name": "Jordan", "gpa": 3.9},
    {"name": "Sam", "gpa": 2.9}
]

# Step 1: Filter (keep GPA > 3.5)
# Step 2: Map (extract just the names)
honor_roll = list(map(
    lambda s: s["name"],
    filter(lambda s: s["gpa"] > 3.5, students)
))
print(honor_roll)   # ['Priya', 'Jordan']
```

This reads inside-out: first filter, then map. It works, but honestly? The list comprehension version is more readable:

```python
# Same thing, but more Pythonic
honor_roll = [s["name"] for s in students if s["gpa"] > 3.5]
print(honor_roll)   # ['Priya', 'Jordan']
```

We'll talk about when to use which in a moment.

## reduce(): Boil It All Down

`reduce()` takes a list and boils it down to a single value. It applies a function to the first two items, then applies the function to the result and the third item, and so on until there's only one value left.

Unlike `map` and `filter`, `reduce` isn't built-in - you have to import it.

```python
from functools import reduce

# Sum all numbers (the hard way, to show how reduce works)
numbers = [1, 2, 3, 4, 5]
total = reduce(lambda a, b: a + b, numbers)
print(total)   # 15

# How it works, step by step:
# Step 1: 1 + 2 = 3
# Step 2: 3 + 3 = 6
# Step 3: 6 + 4 = 10
# Step 4: 10 + 5 = 15
```

The lambda takes two arguments: the **accumulator** (running result) and the **current item**.

```python
from functools import reduce

# Find the maximum value
numbers = [34, 67, 12, 89, 45]
maximum = reduce(lambda a, b: a if a > b else b, numbers)
print(maximum)   # 89

# Multiply all numbers together
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda a, b: a * b, numbers)
print(product)   # 120 (1 * 2 * 3 * 4 * 5)

# Flatten a list of lists
nested = [[1, 2], [3, 4], [5, 6]]
flat = reduce(lambda a, b: a + b, nested)
print(flat)   # [1, 2, 3, 4, 5, 6]

# Build a sentence from words
words = ["Python", "is", "actually", "pretty", "cool"]
sentence = reduce(lambda a, b: f"{a} {b}", words)
print(sentence)   # Python is actually pretty cool
```

Real talk: `reduce()` is the least-used of this bunch in modern Python. For summing, use `sum()`. For min/max, use `min()` and `max()`. For joining strings, use `" ".join()`. But `reduce()` is worth knowing because it shows up in other languages and in data processing.

## The Honest Comparison: When to Use What

Here's the truth. In Python, you have three ways to do the same thing:

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Goal: Get squares of even numbers

# Method 1: Regular loop
result = []
for n in numbers:
    if n % 2 == 0:
        result.append(n ** 2)
print(result)   # [4, 16, 36, 64, 100]

# Method 2: map + filter
result = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))
print(result)   # [4, 16, 36, 64, 100]

# Method 3: List comprehension (Pythonic winner)
result = [n ** 2 for n in numbers if n % 2 == 0]
print(result)   # [4, 16, 36, 64, 100]
```

**My honest recommendation:**

| Situation | Use |
|------|---|
| Simple transformation | List comprehension |
| Simple filtering | List comprehension |
| Both together | List comprehension |
| Already have a named function | `map()` or `filter()` |
| Need lazy evaluation (huge data) | `map()` or `filter()` (without `list()`) |
| Sorting with custom key | `lambda` with `sorted()` |
| Complex multi-step pipeline | Regular loop (readability wins) |
| Reducing to single value | `sum()`, `max()`, `min()`, or `reduce()` |

List comprehensions are the Pythonic way. But `map`, `filter`, and `lambda` are tools you should know because:
1. You'll see them in other people's code constantly
2. Some situations genuinely call for them
3. They're essential in other languages (JavaScript's `.map()`, `.filter()`, `.reduce()`)

## Bonus: sorted() with Lambda

This is probably the most common real-world use of lambda:

```python
# Sort strings by length
words = ["banana", "pie", "strawberry", "kiwi"]
by_length = sorted(words, key=lambda w: len(w))
print(by_length)   # ['pie', 'kiwi', 'banana', 'strawberry']

# Sort dictionaries by a specific field
employees = [
    {"name": "Priya", "salary": 75000},
    {"name": "Alex", "salary": 65000},
    {"name": "Jordan", "salary": 85000}
]

by_salary = sorted(employees, key=lambda e: e["salary"], reverse=True)
for e in by_salary:
    print(f"{e['name']}: ${e['salary']:,}")
# Jordan: $85,000
# Priya: $75,000
# Alex: $65,000

# Sort by multiple criteria (last name, then first name)
names = ["Jordan Smith", "Alex Smith", "Priya Patel", "Alex Johnson"]
sorted_names = sorted(names, key=lambda n: (n.split()[-1], n.split()[0]))
print(sorted_names)
# ['Alex Johnson', 'Priya Patel', 'Alex Smith', 'Jordan Smith']
```

That last one sorts by last name first, then by first name within the same last name. The `key` function returns a tuple, and Python compares tuples element by element.

## Your Turn: Student Grade Processor

You have this data:

```python
students = [
    {"name": "Priya", "scores": [95, 87, 92, 88]},
    {"name": "Alex", "scores": [72, 68, 75, 80]},
    {"name": "Jordan", "scores": [88, 92, 95, 90]},
    {"name": "Sam", "scores": [55, 60, 58, 62]},
    {"name": "Taylor", "scores": [91, 89, 94, 87]}
]
```

Using lambda, map, filter, and/or list comprehensions, write code to:

1. Calculate each student's average score (use `map`)
2. Filter to only students with average above 80 (use `filter`)
3. Sort the passing students by average, highest first (use `sorted` with `lambda`)
4. Create a final report showing each passing student's name and letter grade:
   - 90+: A
   - 80-89: B
   - 70-79: C
   - Below 70: F
5. Use `reduce` to find the overall class average

**Starter hint:**

```python
from functools import reduce

students = [
    {"name": "Priya", "scores": [95, 87, 92, 88]},
    {"name": "Alex", "scores": [72, 68, 75, 80]},
    {"name": "Jordan", "scores": [88, 92, 95, 90]},
    {"name": "Sam", "scores": [55, 60, 58, 62]},
    {"name": "Taylor", "scores": [91, 89, 94, 87]}
]

# Step 1: Add average to each student
with_averages = list(map(
    lambda s: {**s, "average": sum(s["scores"]) / len(s["scores"])},
    students
))

# Step 2: Filter to passing students (average > 80)
# Your code here...

# Step 3: Sort by average, highest first
# Your code here...

# Step 4: Generate letter grades
# Your code here...

# Step 5: Overall class average using reduce
# Your code here...
```

Full solution available at:
`https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/sprint-2-intermediate/chapter-14-lambda-map-filter/`

## TL;DR

- **Lambda** functions are one-line, anonymous functions: `lambda x: x * 2`.
- **`map(func, iterable)`** applies a function to every item. Like a conveyor belt.
- **`filter(func, iterable)`** keeps items where the function returns `True`. Like a bouncer.
- **`reduce(func, iterable)`** boils a list down to a single value. Import from `functools`.
- **List comprehensions** are usually more Pythonic than `map`/`filter` for simple cases.
- The killer use case for **lambda** is `sorted(data, key=lambda x: x["field"])`.
- These tools show up everywhere in data science, web development, and other people's code. Know them even if you prefer comprehensions.
- If a one-liner is harder to read than a three-line loop, use the loop. Cleverness is not a virtue.

---

# Sprint 2 Checkpoint: Expense Tracker

> **Sprint 2 Project** | **Estimated Time: 45-60 minutes** | **Skills: Chapters 9-14**

Sprint 2 complete. You're officially not a beginner anymore.

Think about where you were six chapters ago. You could make lists and loop through them. Now? You can organize data with dictionaries, write reusable functions, import powerful libraries, save data to files, handle errors gracefully, and write one-liners that would make a senior developer nod approvingly.

That's a serious level-up. Time to prove it.

## What You're Building

An **Expense Tracker** that runs in the terminal. It lets you add expenses, view them by category, see spending summaries, and - here's the important part - it saves everything to a CSV file so your data survives between sessions.

This isn't a toy. This is a tool you could actually use. (Or at least show off in an interview.)

### Features

- Add an expense (amount, category, description, auto-dated)
- View all expenses
- View expenses filtered by category
- See a spending summary (total per category + grand total)
- Data persists in a CSV file
- Crash-proof user input (no more explosions when someone types "banana" for the amount)

### Skills You'll Use

| Feature | Chapter |
|-----|-----|
| Storing expense data as dictionaries | Chapter 9 - Dictionaries |
| Organizing code into reusable functions | Chapter 10 - Functions |
| Using `csv`, `datetime`, and `os` modules | Chapter 11 - Modules |
| Reading/writing CSV files | Chapter 12 - File Handling |
| Input validation and error handling | Chapter 13 - Error Handling |
| Sorting and filtering with lambda | Chapter 14 - Lambda & Friends |

## Step-by-Step Build Guide

### Step 1: Set Up the Foundation

Create a file called `expense_tracker.py`. Start with your imports and constants.

```python
import csv
import os
from datetime import datetime

EXPENSE_FILE = "expenses.csv"
CATEGORIES = ["Food", "Transport", "Entertainment", "Bills", "Shopping", "Other"]
```

### Step 2: Write the Load Function

This function reads existing expenses from the CSV file. If the file doesn't exist yet, it returns an empty list.

```python
def load_expenses():
    """Load expenses from CSV file. Returns a list of dictionaries."""
    if not os.path.exists(EXPENSE_FILE):
        return []

    expenses = []
    try:
        with open(EXPENSE_FILE, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                row["amount"] = float(row["amount"])
                expenses.append(row)
    except (FileNotFoundError, csv.Error) as e:
        print(f"Error loading expenses: {e}")
        return []

    return expenses
```

Notice how we convert the amount back to a float. CSV files store everything as strings, so we need to convert numeric data back when reading.

### Step 3: Write the Save Function

This function writes all expenses to the CSV file.

```python
def save_expenses(expenses):
    """Save all expenses to CSV file."""
    fieldnames = ["date", "category", "amount", "description"]
    try:
        with open(EXPENSE_FILE, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(expenses)
    except IOError as e:
        print(f"Error saving expenses: {e}")
```

### Step 4: Write the Input Helper

Remember the crash-proof input pattern from Chapter 13? Let's make a reusable version.

```python
def get_amount(prompt):
    """Get a valid positive number from the user."""
    while True:
        try:
            amount = float(input(prompt))
            if amount <= 0:
                print("Amount must be positive. Try again.")
                continue
            return round(amount, 2)
        except ValueError:
            print("That's not a valid number. Try again.")


def get_category():
    """Let the user pick a category from the list."""
    print("\nCategories:")
    for i, cat in enumerate(CATEGORIES, 1):
        print(f"  {i}. {cat}")

    while True:
        try:
            choice = int(input("Pick a category (number): "))
            if 1 <= choice <= len(CATEGORIES):
                return CATEGORIES[choice - 1]
            print(f"Please enter a number between 1 and {len(CATEGORIES)}.")
        except ValueError:
            print("That's not a valid number. Try again.")
```

### Step 5: Add an Expense

```python
def add_expense(expenses):
    """Add a new expense to the list."""
    print("\n-- Add Expense --")

    amount = get_amount("Amount: $")
    category = get_category()
    description = input("Description (optional): ").strip() or "No description"
    date = datetime.now().strftime("%Y-%m-%d")

    expense = {
        "date": date,
        "category": category,
        "amount": amount,
        "description": description
    }

    expenses.append(expense)
    save_expenses(expenses)
    print(f"\nAdded: ${amount:.2f} for {category} - {description}")
```

### Step 6: View Expenses

```python
def view_all_expenses(expenses):
    """Display all expenses in a formatted table."""
    if not expenses:
        print("\nNo expenses recorded yet. Start spending! (Responsibly.)")
        return

    print(f"\n{'Date':<12} {'Category':<15} {'Amount':>10} {'Description'}")
    print("-" * 55)

    for e in expenses:
        print(f"{e['date']:<12} {e['category']:<15} ${e['amount']:>9.2f} {e['description']}")

    total = sum(e["amount"] for e in expenses)
    print("-" * 55)
    print(f"{'TOTAL':<27} ${total:>9.2f}")


def view_by_category(expenses):
    """View expenses filtered by category."""
    if not expenses:
        print("\nNo expenses recorded yet.")
        return

    category = get_category()
    filtered = list(filter(lambda e: e["category"] == category, expenses))

    if not filtered:
        print(f"\nNo expenses in {category}.")
        return

    print(f"\n-- {category} Expenses --")
    for e in filtered:
        print(f"  {e['date']} - ${e['amount']:.2f} - {e['description']}")

    total = sum(e["amount"] for e in filtered)
    print(f"\n  Total {category}: ${total:.2f}")
```

### Step 7: Spending Summary

```python
def spending_summary(expenses):
    """Show total spending per category."""
    if not expenses:
        print("\nNo expenses recorded yet.")
        return

    print("\n-- Spending Summary --")

    # Group expenses by category
    category_totals = {}
    for e in expenses:
        cat = e["category"]
        category_totals[cat] = category_totals.get(cat, 0) + e["amount"]

    # Sort by amount (highest first)
    sorted_cats = sorted(category_totals.items(), key=lambda x: x[1], reverse=True)

    grand_total = sum(category_totals.values())

    for cat, total in sorted_cats:
        percentage = (total / grand_total) * 100
        bar = "#" * int(percentage / 2)
        print(f"  {cat:<15} ${total:>9.2f} ({percentage:>5.1f}%) {bar}")

    print(f"\n  {'Grand Total':<15} ${grand_total:>9.2f}")
```

### Step 8: The Main Menu

```python
def main():
    """Main application loop."""
    expenses = load_expenses()
    print("=" * 40)
    print("   EXPENSE TRACKER")
    print("=" * 40)

    while True:
        print("\n-- Menu --")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View by Category")
        print("4. Spending Summary")
        print("5. Quit")

        choice = input("\nChoice: ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_all_expenses(expenses)
        elif choice == "3":
            view_by_category(expenses)
        elif choice == "4":
            spending_summary(expenses)
        elif choice == "5":
            print("\nGoodbye! Stay on budget!")
            break
        else:
            print("Invalid choice. Please enter 1-5.")


if __name__ == "__main__":
    main()
```

### Step 9: Run It!

Save the file and run it:

```bash
python expense_tracker.py
```

Try adding a few expenses, viewing them, checking the summary. Close the program and run it again - your expenses are still there because they're saved to `expenses.csv`.

## Challenge Upgrades

If you breezed through the basic version, try these enhancements:

1. **Delete an expense** - Show numbered expenses and let the user pick one to remove
2. **Monthly report** - Filter expenses by month and show monthly totals
3. **Budget limits** - Set a budget per category and warn when approaching the limit
4. **Export summary** - Save the spending summary to a separate text file
5. **JSON storage** - Replace CSV with JSON for more flexible data storage

## The Full Code

The complete, working expense tracker is available at:
`https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/sprint-2-intermediate/sprint-2-checkpoint-expense-tracker/`

The repo includes:
- `expense_tracker.py` - The complete solution
- `expense_tracker_starter.py` - A skeleton with function signatures and comments
- `sample_expenses.csv` - Sample data to test with

## What's Next: Sprint 3

You've just built a real application. It has a menu system, file persistence, error handling, and organized code. That's not a tutorial exercise - that's a project.

Sprint 3 is where things get *really* interesting. You're going to learn **Object-Oriented Programming** - the paradigm that powers everything from video games to web apps to AI systems. You'll learn about classes, objects, inheritance, and all the patterns that make large-scale software possible.

You'll build a **Library Management System** that puts all of it together.

But first, take a break. You earned it. Go outside, touch grass, tell someone you're now an intermediate Python developer. Because you are.

See you in Sprint 3.

---

# Welcome to Sprint 3: Object-Oriented - Think in Objects

> **Chapters 15-18** | **Estimated Time: 2-3 hours** | **Difficulty: Intermediate-Advanced**

Okay. Deep breath.

You're about to learn Object-Oriented Programming. OOP. The thing that makes beginners' eyes glaze over and sends half of every bootcamp class running for the exit.

But here's a secret: **it's not that hard.** It just *sounds* hard because people explain it with abstract examples about "Animal" classes and "Shape" hierarchies that have nothing to do with real life. We're not going to do that. (Okay, we'll use shapes *once*. But we'll feel bad about it.)

Instead, we're going to open a pizza shop.

You'll create a `Pizza` class, give it toppings and a price, teach it to calculate its own total, and eventually build an entire ordering system. By the end of this sprint, you'll look at every app on your phone and think, "Oh, that's just objects."

## What's Coming

- **Chapter 15:** Classes & objects - building your own types
- **Chapter 16:** Inheritance - passing down traits from parent to child
- **Chapter 17:** Magic methods - making your objects work with `+`, `print()`, and more
- **Chapter 18:** Encapsulation, polymorphism & design principles - thinking like an architect

## The Sprint 3 Project: Library Management System

You'll build a full **Library Management System** with `Book`, `Member`, and `Library` classes, complete with JSON file persistence. Real OOP. Real data. Real satisfying.

Here's the thing: if you made it through Sprint 2 - functions, file handling, error handling, lambdas - you already have every tool you need. OOP is just a new way of *organizing* those tools. It's not harder. It's just different.

And different is good. Different is how you level up.

Let's think in objects.

---

# Chapter 15: Classes & Objects - Building Your Own Types

> **Sprint 3** | **10 min read** | **Code: [github link](https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/sprint-3-oop/chapter-15-classes-and-objects/)**

Imagine you're opening a pizza shop. You need to track each pizza - its size, toppings, price. You *could* use a dictionary for each pizza:

```python
pizza1 = {"size": "large", "toppings": ["pepperoni", "mushrooms"], "price": 15.99}
pizza2 = {"size": "medium", "toppings": ["margherita"], "price": 12.99}
```

But what if you want every pizza to be able to calculate its own total with tax? Or describe itself? Or check if it's vegetarian? Dictionaries can hold data, but they can't *do* things. You'd need separate functions floating around, and pretty soon your code looks like a junk drawer.

What if there was a better way?

There is. It's called a **class**.

## What You'll Learn

- Why OOP matters (and why every app you use relies on it)
- How to define a class and create objects
- The `__init__` method - the automatic setup function
- `self` - demystified, once and for all
- Class vs instance attributes
- Methods - things your object can do

## Why Should I Care?

Every app, game, and website you use is built with OOP. That Instagram post you liked? An object. That Spotify song in your queue? An object. That Uber ride you took? Also an object - with attributes like `driver`, `pickup_location`, `fare`, and methods like `cancel()` and `rate_driver()`.

OOP isn't some academic exercise. It's the way professional software is actually built. And once you get it, you'll never want to go back to juggling loose variables and random functions.

## The Pizza Shop Analogy

Here's the core idea, and it's simpler than you think:

- A **class** is a recipe. It describes *what a pizza is* - it has a size, toppings, and a price.
- An **object** is an actual pizza. Made from the recipe, sitting on the counter, ready to eat.

One recipe, infinite pizzas. One class, infinite objects.

That's it. That's OOP.

## Your First Class

```python
class Pizza:
    def __init__(self, size, toppings, price):
        self.size = size
        self.toppings = toppings
        self.price = price

# Create actual pizzas (objects)
my_pizza = Pizza("large", ["pepperoni", "mushrooms"], 15.99)
your_pizza = Pizza("medium", ["margherita"], 12.99)

print(my_pizza.size)       # large
print(your_pizza.toppings)  # ['margherita']
```

Let's break this down piece by piece.

### `class Pizza:` - The Recipe

This line says "I'm defining a new type called Pizza." By convention, class names use **CamelCase** (capital first letter of each word). Not `pizza`, not `PIZZA`, not `my_pizza_class`. Just `Pizza`.

### `__init__` - The Setup Function

```python
def __init__(self, size, toppings, price):
```

This is the **initializer** (some people call it the constructor). It runs automatically every time you create a new Pizza object. You never call `__init__` directly - Python calls it for you.

Think of it like the moment the pizza comes out of the oven. The second it exists, it *already* has a size, toppings, and a price. That's what `__init__` does - it sets up the object the instant it's born.

### `self` - The Most Confusing Word in Python

Okay, let's talk about `self`. It trips up literally everyone. Here's the simple version:

**`self` means "this particular pizza."**

When you write `self.size = size`, you're saying "this pizza's size is whatever was passed in." When `my_pizza` is created, `self` refers to `my_pizza`. When `your_pizza` is created, `self` refers to `your_pizza`.

It's just Python's way of saying "the object we're currently talking about."

```python
class Pizza:
    def __init__(self, size, toppings, price):
        self.size = size          # THIS pizza's size
        self.toppings = toppings  # THIS pizza's toppings
        self.price = price        # THIS pizza's price
```

> **Don't Panic:** If `self` confuses you, you're in excellent company. It confuses *everyone* at first. Seriously - there are thousands of Stack Overflow questions about it. Just remember: **self = "this specific object."** Use it, and one day it'll click. Promise.

### Why Do We Need `self`?

Because a class is a recipe for *many* objects. Python needs to know which pizza you're talking about:

```python
pepperoni = Pizza("large", ["pepperoni"], 14.99)
veggie = Pizza("small", ["mushrooms", "peppers"], 11.99)

# These are DIFFERENT pizzas with DIFFERENT sizes
print(pepperoni.size)  # large
print(veggie.size)     # small
```

`self` is what keeps them separate. Without it, Python would have no idea whose `size` you mean.

## Methods - Things Your Object Can Do

A class isn't just data storage. The whole point is that objects can *do stuff*. Those actions are called **methods** - they're just functions that live inside a class.

```python
class Pizza:
    def __init__(self, size, toppings, price):
        self.size = size
        self.toppings = toppings
        self.price = price

    def describe(self):
        topping_list = ", ".join(self.toppings)
        return f"{self.size} pizza with {topping_list} - ${self.price}"

    def total_with_tax(self, tax_rate=0.08):
        return round(self.price * (1 + tax_rate), 2)

    def is_vegetarian(self):
        meat = {"pepperoni", "sausage", "bacon", "ham", "chicken"}
        return not any(t in meat for t in self.toppings)
```

```python
my_pizza = Pizza("large", ["pepperoni", "mushrooms"], 15.99)

print(my_pizza.describe())
# large pizza with pepperoni, mushrooms - $15.99

print(my_pizza.total_with_tax())
# 17.27

print(my_pizza.is_vegetarian())
# False
```

Notice how every method takes `self` as its first parameter. That's how the method knows which pizza it's working on. When you call `my_pizza.describe()`, Python secretly passes `my_pizza` as `self` behind the scenes.

> **Remember When?** Remember dictionaries from Chapter 9? A class is like a dictionary that can also *do things*. A dictionary holds data: `pizza["size"]`. A class holds data *and* behavior: `pizza.size` plus `pizza.describe()`. It's the upgrade you didn't know you needed.

## Class vs Instance Attributes

There are two kinds of attributes:

**Instance attributes** belong to a specific object. Each pizza has its own size and toppings. These are the ones you set in `__init__` with `self.something`.

**Class attributes** are shared by ALL objects of that class. They're defined directly in the class body:

```python
class Pizza:
    restaurant = "Py's Pizzeria"  # Class attribute - same for ALL pizzas
    total_pizzas_made = 0         # Class attribute - shared counter

    def __init__(self, size, toppings, price):
        self.size = size           # Instance attribute - unique per pizza
        self.toppings = toppings   # Instance attribute
        self.price = price         # Instance attribute
        Pizza.total_pizzas_made += 1
```

```python
p1 = Pizza("large", ["pepperoni"], 15.99)
p2 = Pizza("small", ["cheese"], 9.99)

print(p1.restaurant)          # Py's Pizzeria
print(p2.restaurant)          # Py's Pizzeria (same!)
print(Pizza.total_pizzas_made)  # 2
```

**Rule of thumb:** If every object should share the same value, make it a class attribute. If each object gets its own value, make it an instance attribute.

## Putting It All Together

Let's build a slightly more complete pizza ordering system:

```python
class Pizza:
    restaurant = "Py's Pizzeria"

    def __init__(self, size, toppings):
        self.size = size
        self.toppings = toppings
        self.price = self._calculate_price()

    def _calculate_price(self):
        base = {"small": 8.99, "medium": 11.99, "large": 14.99}
        topping_cost = len(self.toppings) * 1.50
        return base.get(self.size, 11.99) + topping_cost

    def describe(self):
        topping_list = ", ".join(self.toppings) if self.toppings else "just cheese"
        return f"{self.size.title()} pizza with {topping_list} - ${self.price:.2f}"

    def total_with_tax(self, tax_rate=0.08):
        return round(self.price * (1 + tax_rate), 2)


# Let's order some pizza
order = [
    Pizza("large", ["pepperoni", "mushrooms"]),
    Pizza("small", []),
    Pizza("medium", ["olives", "onions", "peppers"]),
]

print(f"Order from {Pizza.restaurant}")
print("-" * 40)

total = 0
for pizza in order:
    print(pizza.describe())
    total += pizza.total_with_tax()

print("-" * 40)
print(f"Total (with tax): ${total:.2f}")
```

Output:

```
Order from Py's Pizzeria
--------------------
Large pizza with pepperoni, mushrooms - $17.99
Small pizza with just cheese - $8.99
Medium pizza with olives, onions, peppers - $16.49
--------------------
Total (with tax): $46.95
```

Look at that. Clean, organized, and each pizza knows how to describe itself and calculate its own price. Try doing *that* with a pile of dictionaries.

## Common Mistakes

**Forgetting `self` in method definitions:**

```python
# WRONG - will crash
class Pizza:
    def describe():  # Missing self!
        return f"{self.size} pizza"

# RIGHT
class Pizza:
    def describe(self):
        return f"{self.size} pizza"
```

**Forgetting `self` when accessing attributes:**

```python
# WRONG - will crash
def describe(self):
    return f"{size} pizza"  # What's 'size'? Python doesn't know

# RIGHT
def describe(self):
    return f"{self.size} pizza"  # Ah, THIS pizza's size
```

**Using the class name instead of `self`:**

```python
# WRONG (usually) - this changes it for ALL pizzas
def apply_discount(self):
    Pizza.price = Pizza.price * 0.9

# RIGHT - changes it for THIS pizza
def apply_discount(self):
    self.price = self.price * 0.9
```

## Your Turn

Time to practice. Create a `Dog` class with:

1. Instance attributes: `name`, `breed`, `age`
2. A method `bark()` that returns `"{name} says: Woof!"`
3. A method `dog_years()` that returns the age multiplied by 7
4. A method `describe()` that returns a formatted string like `"Buddy is a 3-year-old Golden Retriever"`
5. A class attribute `species` set to `"Canis familiaris"`

Create at least two Dog objects and call all their methods.

**Bonus:** Add a method `is_puppy()` that returns `True` if the dog is under 2 years old.

## TL;DR

- A **class** is a blueprint/recipe. An **object** is a thing made from that blueprint
- `__init__` runs automatically when you create an object - it sets up the initial data
- `self` means "this specific object" - it's how each object keeps its own data separate
- **Instance attributes** (`self.x`) are unique to each object. **Class attributes** are shared by all objects
- **Methods** are functions inside a class - they define what an object can *do*
- OOP = data + behavior, bundled together. It's a dictionary that can do things
- If `self` is still confusing, keep going. It clicks with practice. Everyone gets there eventually

---

# Chapter 16: Inheritance - Passing Down the Family Traits

> **Sprint 3** | **10 min read** | **Code: [github link](https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/sprint-3-oop/chapter-16-inheritance/)**

In real life, you inherit traits from your parents. Brown eyes, terrible dance moves, strong opinions about pizza toppings, that one laugh that sounds exactly like your dad's. You didn't choose these things. They just... came with the package.

In Python, classes can inherit too. And honestly? It's one of the most useful tricks in all of programming.

## What You'll Learn

- Why inheritance saves you from copy-paste nightmares
- How to create parent and child classes
- What gets inherited (spoiler: everything)
- How to override methods - doing it YOUR way
- `super()` - calling your parent class for help
- `isinstance()` - checking the family tree
- A brief, responsible look at multiple inheritance

## Why Should I Care?

Picture this: you're building a game. You have `Warrior`, `Mage`, and `Archer` classes. They all have `name`, `health`, and a `take_damage()` method. Without inheritance, you'd copy-paste the same code into three different classes. Then when you need to change how damage works, you'd have to change it in three places. Then you'd miss one. Then you'd have a bug. Then you'd cry.

Inheritance fixes that. You write the shared stuff once in a parent class, and the child classes get it for free.

Every major framework uses this. Django models? Inheritance. Flask views? Inheritance. Exception handling (which you learned in Chapter 13)? That entire system is built on inheritance. `ValueError` inherits from `Exception`, which inherits from `BaseException`. You've been *using* inheritance this whole time.

## The Basics: Parent and Child

Let's go back to the pizza shop. We have a `Pizza` class, but now we want to add specialty pizzas - a `DeepDish` and a `ThinCrust`. They're both pizzas, but with some differences.

```python
class Pizza:
    """The parent class - the original recipe."""

    def __init__(self, size, toppings):
        self.size = size
        self.toppings = toppings

    def describe(self):
        topping_list = ", ".join(self.toppings) if self.toppings else "cheese"
        return f"{self.size} pizza with {topping_list}"

    def bake_time(self):
        return 15  # minutes
```

Now, a `DeepDish` is a pizza - it has a size and toppings - but it takes longer to bake and has a thicker crust. Instead of rewriting everything, we **inherit**:

```python
class DeepDish(Pizza):
    """Inherits from Pizza. Gets everything Pizza has, for free."""

    def bake_time(self):
        return 25  # Deep dish needs more time

    def describe(self):
        return f"{super().describe()} (deep dish style)"
```

```python
regular = Pizza("large", ["pepperoni"])
chunky_boi = DeepDish("large", ["sausage", "peppers"])

print(regular.describe())
# large pizza with pepperoni

print(chunky_boi.describe())
# large pizza with sausage, peppers (deep dish style)

print(regular.bake_time())    # 15
print(chunky_boi.bake_time())  # 25
```

Look at what happened. `DeepDish` never defined `__init__`. It didn't need to - it inherited it from `Pizza`. It automatically has `size` and `toppings`. It just overrode the methods it wanted to change.

That's inheritance in a nutshell: **get everything from your parent, change only what you need.**

## What Gets Inherited

Everything. Methods, attributes, the whole package. A child class is a copy of the parent with the option to add or change things.

```python
class ThinCrust(Pizza):
    pass  # Literally no changes - it's identical to Pizza
```

```python
skinny = ThinCrust("medium", ["basil", "mozzarella"])
print(skinny.describe())     # medium pizza with basil, mozzarella
print(skinny.bake_time())    # 15
```

`ThinCrust` does nothing of its own, but it works perfectly. It got *everything* from `Pizza`. The `pass` keyword just means "nothing to add here."

> **Don't Panic:** Inheritance is just one class borrowing from another. That's it. If you understood functions - how one function can call another - you can understand this. A child class just *starts with* everything its parent has.

## Overriding Methods - Doing It YOUR Way

When a child class defines a method with the same name as the parent, it **overrides** (replaces) the parent's version:

```python
class Pizza:
    def bake_time(self):
        return 15

class DeepDish(Pizza):
    def bake_time(self):
        return 25  # Overrides the parent's bake_time
```

When you call `deep_dish.bake_time()`, Python checks the child first. If it finds the method there, it uses it. If not, it goes up to the parent. It's like asking a teenager a question - they'll give their own answer if they have one, otherwise they'll go ask their parents.

## `super()` - Calling Mom for Help

Sometimes you don't want to completely replace the parent's method. You want to *extend* it - do everything the parent does, plus a little extra. That's where `super()` comes in.

```python
class Pizza:
    def __init__(self, size, toppings):
        self.size = size
        self.toppings = toppings
        self.price = self._calculate_price()

    def _calculate_price(self):
        base = {"small": 8.99, "medium": 11.99, "large": 14.99}
        return base.get(self.size, 11.99) + len(self.toppings) * 1.50

class StuffedCrust(Pizza):
    def __init__(self, size, toppings, cheese_type="mozzarella"):
        super().__init__(size, toppings)  # Call Pizza's __init__
        self.cheese_type = cheese_type    # Add our own attribute
        self.price += 3.00               # Stuffed crust costs extra

    def describe(self):
        base = super().describe() if hasattr(Pizza, 'describe') else ""
        return f"{self.size} stuffed crust ({self.cheese_type}) with {', '.join(self.toppings)}"
```

`super()` means "call the parent class's version of this method." So `super().__init__(size, toppings)` runs `Pizza.__init__`, setting up `size`, `toppings`, and `price`. Then `StuffedCrust` adds its own `cheese_type` and adjusts the price.

Think of `super()` as calling your mom for help. "Hey Mom, do the usual setup. I'll handle the rest."

```python
fancy = StuffedCrust("large", ["pepperoni", "mushrooms"], "cheddar")
print(fancy.size)         # large (from Pizza)
print(fancy.cheese_type)  # cheddar (StuffedCrust's own)
print(fancy.price)        # 20.99 (Pizza's price + $3)
```

## A More Practical Example

Let's step outside the pizza shop for a moment and look at something you'd actually build:

```python
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.is_active = True

    def deactivate(self):
        self.is_active = False
        return f"{self.username} has been deactivated"

    def display(self):
        status = "Active" if self.is_active else "Inactive"
        return f"{self.username} ({self.email}) - {status}"


class AdminUser(User):
    def __init__(self, username, email, access_level="full"):
        super().__init__(username, email)
        self.access_level = access_level
        self.admin_actions = []

    def ban_user(self, user):
        user.deactivate()
        self.admin_actions.append(f"Banned {user.username}")
        return f"{user.username} has been banned by {self.username}"

    def display(self):
        base = super().display()
        return f"{base} [ADMIN: {self.access_level}]"


class PremiumUser(User):
    def __init__(self, username, email, subscription="monthly"):
        super().__init__(username, email)
        self.subscription = subscription

    def display(self):
        base = super().display()
        return f"{base} [Premium: {self.subscription}]"
```

```python
alice = User("alice", "alice@email.com")
admin = AdminUser("admin_bob", "bob@email.com")
premium = PremiumUser("charlie", "charlie@email.com", "yearly")

print(alice.display())
# alice (alice@email.com) - Active

print(admin.display())
# admin_bob (bob@email.com) - Active [ADMIN: full]

print(admin.ban_user(alice))
# alice has been banned by admin_bob

print(alice.display())
# alice (alice@email.com) - Inactive

print(premium.display())
# charlie (charlie@email.com) - Active [Premium: yearly]
```

Three user types, shared login logic, each with their own special powers. That's inheritance doing what it does best.

## `isinstance()` - Checking the Family Tree

Sometimes you need to check what type an object is. Maybe you want to verify someone is an admin before letting them ban people:

```python
print(isinstance(admin, AdminUser))  # True
print(isinstance(admin, User))       # True (AdminUser IS a User)
print(isinstance(alice, AdminUser))  # False (regular User, not Admin)
```

Notice that `admin` is both an `AdminUser` AND a `User`. That's because inheritance creates an "is a" relationship. An `AdminUser` *is a* `User` with extra powers.

```python
def perform_admin_action(user, target):
    if isinstance(user, AdminUser):
        return user.ban_user(target)
    return "Permission denied. Nice try though."

print(perform_admin_action(admin, alice))   # alice has been banned by admin_bob
print(perform_admin_action(premium, alice))  # Permission denied. Nice try though.
```

## Multiple Inheritance - A Brief Warning

Python lets a class inherit from *multiple* parents:

```python
class FlyingCar(Car, Airplane):
    pass
```

This is legal Python. A `FlyingCar` gets everything from both `Car` and `Airplane`. Sounds cool, right?

It is. Until `Car` and `Airplane` both have a `fuel_level` attribute and a `start_engine()` method that work differently. Then Python has to figure out which one to use, and things get confusing fast.

> **Pro Tip:** Multiple inheritance is like dual-wielding swords. Looks amazing in movies. In practice, you'll probably stab yourself. Stick with single inheritance until you have a really good reason not to. When you see it in the wild, it's usually with **mixins** - small, focused classes that add one specific feature. That's the safe way to do it.

We won't dive deeper into multiple inheritance here. Just know it exists, and that most Python developers use it sparingly and carefully.

## Your Turn

Build a vehicle hierarchy:

1. Create a parent class `Vehicle` with:
   - Attributes: `make`, `model`, `year`, `fuel_level` (starts at 100)
   - Method `drive(km)` that reduces fuel (1 unit per 10 km) and returns a message
   - Method `describe()` that returns a formatted string

2. Create `ElectricVehicle(Vehicle)` that:
   - Adds a `battery_capacity` attribute
   - Overrides `drive()` to use less fuel (1 unit per 15 km, because EVs are efficient)
   - Adds a `charge()` method that sets fuel_level back to 100

3. Create `Truck(Vehicle)` that:
   - Adds a `payload_capacity` attribute
   - Overrides `drive()` to use more fuel (1 unit per 5 km, because trucks are thirsty)
   - Adds a `load(weight)` method

4. Create instances of all three, drive them around, and print their states.

**Bonus:** Add a `HybridVehicle` that inherits from `Vehicle` and has both a `fuel_level` and `battery_level`.

## TL;DR

- **Inheritance** lets a child class get all the methods and attributes of a parent class for free
- Syntax: `class Child(Parent):` - that's it, the parentheses do all the work
- Children can **override** methods to change behavior
- `super()` calls the parent's version of a method - use it when you want to extend, not replace
- `isinstance(obj, ClassName)` checks if an object belongs to a class (or its parents)
- **Multiple inheritance** exists but use it carefully - stick with single inheritance for now
- Inheritance = "write the common stuff once, specialize as needed." Less copy-paste, fewer bugs, happier developer

---

# Chapter 17: Magic Methods & Operator Overloading

> **Sprint 3** | **10 min read** | **Code: [github link](https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/sprint-3-oop/chapter-17-magic-methods/)**

What if your custom objects could work with `+`, `-`, `==`, and `print()` just like numbers and strings do? What if you could write `price1 + price2` and get back a new price object, or `print(my_object)` and get something useful instead of `<__main__.Pizza object at 0x7f...>`?

That's magic methods. And yes, they really do feel like magic.

## What You'll Learn

- What magic methods are (and why they have those weird double underscores)
- `__str__` and `__repr__` - making your objects printable
- `__len__` and `__getitem__` - making objects act like lists
- `__add__` and `__eq__` - custom math and comparisons
- `__lt__`, `__gt__` - who's bigger?
- A taste of `__enter__` and `__exit__` (context managers)

## Why Should I Care?

You know how you can do `len("hello")` on a string and `len([1, 2, 3])` on a list and they both just... work? That's because both strings and lists implement a magic method called `__len__` behind the scenes. The `len()` function just calls it.

Libraries like **pandas** and **numpy** use magic methods *everywhere*. That's how you can add two DataFrames together or compare arrays with `>`. It's how `with open("file.txt")` works. It's how `for item in my_object` works. Magic methods are the secret engine behind Python's clean, readable syntax.

If you want your objects to feel like first-class Python citizens instead of awkward outsiders, magic methods are how you get there.

> **Remember When?** Remember when we used `len()` on lists and strings? That called `__len__` behind the scenes. When you wrote `"hello" + " world"`, that called `__add__`. When you did `for item in my_list`, that called `__iter__` and `__next__`. You've been using magic methods all along. Now you'll learn to write your own.

## What Are Magic Methods?

Magic methods (also called **dunder methods**, short for "double underscore") are special methods that Python calls automatically in certain situations. You've already met one - `__init__`, which runs when you create an object.

Here's the pattern: when you write normal Python syntax, Python translates it into magic method calls:

| You Write | Python Calls |
|------|-------|
| `len(obj)` | `obj.__len__()` |
| `print(obj)` | `obj.__str__()` |
| `obj1 + obj2` | `obj1.__add__(obj2)` |
| `obj1 == obj2` | `obj1.__eq__(obj2)` |
| `obj[index]` | `obj.__getitem__(index)` |
| `for x in obj` | `obj.__iter__()` |

That's the whole trick. There's no actual "magic." Python sees `+` and calls `__add__`. It sees `len()` and calls `__len__`. You define these methods, and your objects suddenly work with Python's built-in syntax.

> **Don't Panic:** The double underscores look intimidating, but these are just regular methods with funny names. You define them exactly like any other method. The only difference is that Python calls them automatically when you use certain syntax.

## `__str__` and `__repr__` - Making Objects Printable

Right now, if you print a custom object, you get garbage:

```python
class Pizza:
    def __init__(self, size, toppings):
        self.size = size
        self.toppings = toppings

p = Pizza("large", ["pepperoni"])
print(p)  # <__main__.Pizza object at 0x7f3b2c1a4f10>
```

Nobody wants to see a memory address. Let's fix that with `__str__`:

```python
class Pizza:
    def __init__(self, size, toppings):
        self.size = size
        self.toppings = toppings

    def __str__(self):
        topping_list = ", ".join(self.toppings)
        return f"{self.size} pizza with {topping_list}"

    def __repr__(self):
        return f"Pizza('{self.size}', {self.toppings})"
```

```python
p = Pizza("large", ["pepperoni", "mushrooms"])

print(p)  # large pizza with pepperoni, mushrooms
print(repr(p))  # Pizza('large', ['pepperoni', 'mushrooms'])
```

The difference:
- **`__str__`** is the "pretty" version - what users see. Called by `print()` and `str()`.
- **`__repr__`** is the "developer" version - what you'd type to recreate the object. Called in the REPL and by `repr()`.

**Rule of thumb:** `__str__` is for humans. `__repr__` is for developers. If you only implement one, make it `__repr__` - Python falls back to it when `__str__` isn't defined.

## `__len__` and `__getitem__` - Acting Like a List

Want your object to work with `len()` and square brackets? Easy:

```python
class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add(self, song):
        self.songs.append(song)

    def __len__(self):
        return len(self.songs)

    def __getitem__(self, index):
        return self.songs[index]

    def __str__(self):
        return f"Playlist '{self.name}' ({len(self)} songs)"
```

```python
rock = Playlist("Classic Rock")
rock.add("Bohemian Rhapsody")
rock.add("Stairway to Heaven")
rock.add("Hotel California")

print(len(rock))    # 3
print(rock[0])      # Bohemian Rhapsody
print(rock[-1])     # Hotel California
print(rock)         # Playlist 'Classic Rock' (3 songs)

# Bonus: __getitem__ makes it iterable for free!
for song in rock:
    print(f"  Now playing: {song}")
```

By implementing `__getitem__`, your Playlist magically works with `for` loops too. Python sees `__getitem__` and thinks "oh, I can iterate over this by calling `[0]`, `[1]`, `[2]`..." Pretty neat.

## `__add__` and `__eq__` - Custom Math and Comparisons

This is where it gets fun. Let's build a `Money` class that actually understands addition and equality:

```python
class Money:
    def __init__(self, amount, currency="USD"):
        self.amount = round(amount, 2)
        self.currency = currency

    def __add__(self, other):
        if isinstance(other, Money):
            if self.currency != other.currency:
                raise ValueError(f"Can't add {self.currency} and {other.currency}")
            return Money(self.amount + other.amount, self.currency)
        if isinstance(other, (int, float)):
            return Money(self.amount + other, self.currency)
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Money):
            return self.amount == other.amount and self.currency == other.currency
        return NotImplemented

    def __str__(self):
        symbols = {"USD": "$", "EUR": "\u20ac", "GBP": "\u00a3"}
        symbol = symbols.get(self.currency, self.currency + " ")
        return f"{symbol}{self.amount:.2f}"

    def __repr__(self):
        return f"Money({self.amount}, '{self.currency}')"
```

```python
price = Money(9.99)
tax = Money(0.80)
total = price + tax  # Calls price.__add__(tax)

print(total)         # $10.79
print(price == tax)  # False
print(Money(5) == Money(5))  # True

# You can even add a plain number
tip = total + 2.00
print(tip)           # $12.79

# But mixing currencies? Nope.
dollars = Money(10, "USD")
euros = Money(10, "EUR")
# dollars + euros  # ValueError: Can't add USD and EUR
```

The `+ ` operator isn't just for numbers anymore. *Your* objects understand it. That's operator overloading, and it's genuinely powerful.

### What's `NotImplemented`?

When you return `NotImplemented` (note: not the *exception* `NotImplementedError`, just the value `NotImplemented`), you're telling Python: "I don't know how to handle this." Python will then try the *other* object's method. It's a polite way of saying "not my problem."

## `__lt__`, `__gt__` - Who's Bigger?

Want to sort your objects? You need comparison methods:

```python
class Money:
    # ... (same __init__ as above)

    def __lt__(self, other):
        if isinstance(other, Money) and self.currency == other.currency:
            return self.amount < other.amount
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Money) and self.currency == other.currency:
            return self.amount > other.amount
        return NotImplemented

    def __le__(self, other):
        return self == other or self < other

    def __ge__(self, other):
        return self == other or self > other
```

```python
cheap = Money(4.99)
expensive = Money(49.99)

print(cheap < expensive)   # True
print(cheap > expensive)   # False

# Now you can sort a list of Money objects!
prices = [Money(15.99), Money(3.49), Money(27.00), Money(9.99)]
prices.sort()
for p in prices:
    print(p)
# $3.49
# $9.99
# $15.99
# $27.00
```

> **Pro Tip:** Python has a `functools.total_ordering` decorator that fills in the missing comparison methods for you. Define `__eq__` and one of `__lt__`/`__gt__`/`__le__`/`__ge__`, and it generates the rest. Less typing, same result.

```python
from functools import total_ordering

@total_ordering
class Money:
    def __init__(self, amount, currency="USD"):
        self.amount = round(amount, 2)
        self.currency = currency

    def __eq__(self, other):
        if isinstance(other, Money):
            return self.amount == other.amount and self.currency == other.currency
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Money) and self.currency == other.currency:
            return self.amount < other.amount
        return NotImplemented

    # __gt__, __le__, __ge__ are auto-generated!
```

## `__enter__` and `__exit__` - Context Managers (Quick Taste)

Remember `with open("file.txt") as f:`? That `with` block calls two magic methods:

- `__enter__` - runs when you enter the `with` block
- `__exit__` - runs when you leave it (even if there's an error)

Here's a quick example - a timer that measures how long a block of code takes:

```python
import time

class Timer:
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.elapsed = time.time() - self.start
        print(f"Elapsed: {self.elapsed:.4f} seconds")
        return False  # Don't suppress exceptions
```

```python
with Timer():
    # Do some work
    total = sum(range(1_000_000))
    print(f"Sum: {total}")

# Sum: 499999500000
# Elapsed: 0.0312 seconds
```

The `with` block guarantees `__exit__` runs no matter what, even if your code throws an error. That's why `with open(...)` is so reliable - it always closes the file. We'll see more of this pattern in later chapters, but now you know the secret: it's just two magic methods.

## The Full Magic Method Cheat Sheet

Here are the ones you'll use most often:

| Method | Triggered By | Purpose |
|----|-------|-----|
| `__init__` | `MyClass()` | Set up the object |
| `__str__` | `print(obj)`, `str(obj)` | Human-readable string |
| `__repr__` | REPL, `repr(obj)` | Developer-readable string |
| `__len__` | `len(obj)` | Return length |
| `__getitem__` | `obj[key]` | Index/key access |
| `__setitem__` | `obj[key] = val` | Index/key assignment |
| `__contains__` | `x in obj` | Membership test |
| `__add__` | `obj + other` | Addition |
| `__sub__` | `obj - other` | Subtraction |
| `__mul__` | `obj * other` | Multiplication |
| `__eq__` | `obj == other` | Equality check |
| `__lt__` | `obj < other` | Less than |
| `__gt__` | `obj > other` | Greater than |
| `__bool__` | `if obj:` | Truthiness |
| `__iter__` | `for x in obj` | Iteration |
| `__enter__` | `with obj:` | Enter context |
| `__exit__` | End of `with` | Exit context |

You don't need to memorize this. Bookmark it. Come back when you need one.

## Your Turn

Build a complete `Money` class with the following:

1. `__init__(self, amount, currency="USD")` - store amount (rounded to 2 decimals) and currency
2. `__str__` - display as `$10.99` (use proper symbol for USD, EUR, GBP)
3. `__repr__` - display as `Money(10.99, 'USD')`
4. `__add__` - add two Money objects (same currency only) or add a number
5. `__sub__` - subtract Money objects or numbers
6. `__eq__` - check if two Money objects are equal (same amount AND currency)
7. `__lt__` and `__gt__` - compare amounts (same currency only)
8. `__mul__` - multiply by a number (useful for tax: `price * 1.08`)
9. `__bool__` - `Money(0)` is falsy, anything else is truthy

Test it:

```python
price = Money(29.99)
tax = price * 0.08
total = price + tax
discount = Money(5.00)
final = total - discount

print(f"Price: {price}")
print(f"Tax: {tax}")
print(f"Total: {total}")
print(f"After discount: {final}")
print(f"Is free? {not final}")
```

**Bonus:** Add `__radd__` so that `5.00 + Money(10)` works too (not just `Money(10) + 5.00`).

## TL;DR

- **Magic methods** (dunder methods) are special methods Python calls automatically for built-in operations
- `__str__` makes `print()` work nicely; `__repr__` is the developer-facing version
- `__add__`, `__sub__`, `__eq__`, `__lt__` let your objects use `+`, `-`, `==`, `<`
- `__len__` and `__getitem__` make your objects work with `len()` and `[]`
- `__enter__` and `__exit__` power the `with` statement
- Return `NotImplemented` (not `NotImplementedError`) when your method can't handle the other type
- You've been using magic methods since Chapter 1 - `print()`, `len()`, `+`, `for` loops all rely on them
- The double underscores look scary but they're just regular methods that Python happens to call automatically

---

# Chapter 18: Encapsulation, Polymorphism & Design Principles

> **Sprint 3** | **12 min read** | **Code: [github link](https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/sprint-3-oop/chapter-18-design-principles/)**

Welcome to the chapter where you go from "I can write classes" to "I can *design systems*." This is the difference between knowing how to cook and being a chef. Between playing guitar chords and writing a song. Between stacking LEGO bricks and building the Millennium Falcon.

The concepts in this chapter have fancy names - encapsulation, polymorphism, composition, SOLID. They sound like a university lecture. But they're actually just common-sense ideas with expensive vocabulary. And once you know them, you'll write code that's genuinely easier to change, test, and explain.

## What You'll Learn

- Encapsulation - keeping your object's internals private
- Polymorphism - same method name, different behavior
- Composition vs inheritance - "has a" vs "is a"
- The SOLID principles - simplified, no enterprise jargon

## Why Should I Care?

Two reasons. First, job interviews love these concepts. If someone asks "explain polymorphism," you want an answer, not a blank stare.

But more importantly: these principles prevent your code from turning into an unmaintainable mess. You know that codebase at work that nobody wants to touch? The one where changing one thing breaks three other things? It probably ignored every concept in this chapter. These ideas exist because developers learned the hard way what happens without them.

## Encapsulation - Keep Your Internals Private

Encapsulation means "don't let the outside world mess with your object's guts." It's like a restaurant kitchen: you order food (public interface), but you don't walk into the kitchen and start adjusting the oven temperature (internal state).

Python doesn't have *true* private attributes like Java or C++. Instead, it uses **naming conventions**:

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner          # Public - anyone can see/change this
        self._account_id = id(self)  # Protected - "please don't touch" (single underscore)
        self.__balance = balance     # Private - "seriously don't touch" (double underscore)

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self.__balance += amount
        return self.__balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal must be positive")
        if amount > self.__balance:
            raise ValueError("Insufficient funds")
        self.__balance -= amount
        return self.__balance

    def get_balance(self):
        return self.__balance

    def __str__(self):
        return f"{self.owner}'s account: ${self.__balance:.2f}"
```

```python
account = BankAccount("Alice", 1000)

# Public - works fine
print(account.owner)  # Alice

# Protected - works but you SHOULDN'T
print(account._account_id)  # 140234567890 (works, but it's a hint to stay away)

# Private - Python mangles the name to prevent access
# print(account.__balance)  # AttributeError!

# The RIGHT way to interact with balance:
account.deposit(500)
print(account.get_balance())  # 1500

account.withdraw(200)
print(account)  # Alice's account: $1300.00
```

Here's the cheat sheet:

| Convention | Example | Meaning |
|------|-----|-----|
| `self.name` | Public | Go ahead, use it freely |
| `self._name` | Protected | "Hey, this is internal. Use at your own risk." |
| `self.__name` | Private | Python actually renames it to prevent accidental access |

The double underscore triggers **name mangling** - Python renames `__balance` to `_BankAccount__balance` behind the scenes. You *can* still access it if you really try, but it's Python's way of putting a "DO NOT ENTER" sign on the door.

> **Don't Panic:** Python's approach to privacy is sometimes called "we're all consenting adults here." It trusts you to respect the conventions rather than enforcing strict rules. A single underscore `_` is usually all you need. Double underscore `__` is for when you really want to prevent subclass name collisions. Don't overuse it.

**Practical rule:** Use single underscore `_` for internal methods and attributes. Use double underscore `__` rarely. Use public attributes when there's no reason to hide them. Python isn't Java - you don't need getters and setters for everything.

## Polymorphism - Same Name, Different Behavior

Here's the $50 word for a $5 concept.

> **Fun Fact:** "Polymorphism" comes from Greek, meaning "many forms." It's a fancy way of saying "different objects can respond to the same method name in their own way." That's it. That's the whole thing.

You've actually already seen this. When you call `len()` on a string, a list, or a dictionary, each one responds differently - but the method name is the same. That's polymorphism.

Let's see it with our own classes. The classic example (sorry, we're using shapes - it's the law):

```python
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement area()")

    def describe(self):
        return f"{self.__class__.__name__}: area = {self.area():.2f}"


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height
```

Now here's the magic:

```python
shapes = [Circle(5), Rectangle(4, 6), Triangle(3, 8)]

for shape in shapes:
    print(shape.describe())

# Circle: area = 78.54
# Rectangle: area = 24.00
# Triangle: area = 12.00
```

One loop, three different classes, one method name. Each shape knows how to calculate its own area. The calling code doesn't care *which* shape it's dealing with - it just calls `.area()` and gets the right answer.

That's polymorphism. You write code that works with the *interface* (all shapes have `.area()`), not the specific type. It makes your code flexible and extensible - you can add a `Pentagon` class tomorrow without changing the loop.

### Polymorphism Without Inheritance

In Python, you don't even need inheritance for polymorphism. Thanks to **duck typing** ("if it walks like a duck and quacks like a duck..."), any object with the right method works:

```python
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class Parrot:
    def speak(self):
        return "Polly wants a cracker!"

# These classes share NO parent, but they all have speak()
animals = [Dog(), Cat(), Parrot()]

for animal in animals:
    print(animal.speak())
```

Python doesn't check if `animal` *is a* certain type. It just checks if `animal` *has* a `speak()` method. If it does, great. If it doesn't, you get an error. This is duck typing, and it's one of Python's superpowers.

## Composition vs Inheritance - "Has A" vs "Is A"

This is one of the most important design decisions in OOP, and getting it wrong leads to tangled, fragile code.

**Inheritance** says: "A `Dog` **is an** `Animal`."
**Composition** says: "A `Car` **has an** `Engine`."

Here's the difference in code:

### Inheritance Approach

```python
class Car(Engine):  # A car IS an engine? That's weird...
    pass
```

### Composition Approach

```python
class Engine:
    def __init__(self, horsepower, fuel_type):
        self.horsepower = horsepower
        self.fuel_type = fuel_type
        self.running = False

    def start(self):
        self.running = True
        return f"{self.fuel_type} engine started ({self.horsepower} HP)"

    def stop(self):
        self.running = False
        return "Engine stopped"


class Car:
    def __init__(self, make, model, engine):
        self.make = make
        self.model = model
        self.engine = engine  # Car HAS an engine

    def start(self):
        return f"{self.make} {self.model}: {self.engine.start()}"

    def stop(self):
        return f"{self.make} {self.model}: {self.engine.stop()}"
```

```python
v8 = Engine(450, "gasoline")
mustang = Car("Ford", "Mustang", v8)

print(mustang.start())
# Ford Mustang: gasoline engine started (450 HP)
```

The beauty here: you can swap engines without changing the `Car` class at all.

```python
electric_motor = Engine(300, "electric")
tesla = Car("Tesla", "Model 3", electric_motor)

print(tesla.start())
# Tesla Model 3: electric engine started (300 HP)
```

Same car class, different engine. That's the power of composition - your objects are built from interchangeable parts.

### When to Use Which?

Here's a practical guide:

**Use inheritance when:**
- There's a clear "is a" relationship (a `Dog` IS an `Animal`)
- The child genuinely shares *all* the parent's behavior
- You want to reuse and extend existing code

**Use composition when:**
- There's a "has a" relationship (a `Car` HAS an `Engine`)
- You want to swap components at runtime
- The relationship doesn't fit a neat hierarchy
- You catch yourself creating deep inheritance chains (more than 2-3 levels deep)

**The famous advice:** "Favor composition over inheritance." This doesn't mean never use inheritance. It means when you're not sure, composition is usually the safer bet. Inheritance creates tight coupling - change the parent, and all children change too. Composition is looser and more flexible.

## Let's Combine Everything

Here's a more realistic example that uses encapsulation, polymorphism, and composition together:

```python
class PaymentProcessor:
    """Base class for payment methods (polymorphism)."""
    def process(self, amount):
        raise NotImplementedError


class CreditCard(PaymentProcessor):
    def __init__(self, number, name):
        self._number = number  # Encapsulation: protected
        self.name = name

    def process(self, amount):
        last_four = self._number[-4:]
        return f"Charged ${amount:.2f} to card ending in {last_four}"


class PayPal(PaymentProcessor):
    def __init__(self, email):
        self.email = email

    def process(self, amount):
        return f"Charged ${amount:.2f} to PayPal ({self.email})"


class Order:
    """Uses composition - an order HAS a payment processor."""
    def __init__(self, items, payment_method):
        self.items = items
        self._payment = payment_method  # Composition

    def total(self):
        return sum(price for _, price in self.items)

    def checkout(self):
        amount = self.total()
        result = self._payment.process(amount)  # Polymorphism!
        return f"Order total: ${amount:.2f}\n{result}"
```

```python
card = CreditCard("4111111111111234", "Alice")
paypal = PayPal("alice@email.com")

order1 = Order([("Widget", 9.99), ("Gadget", 24.99)], card)
order2 = Order([("Thingamajig", 14.99)], paypal)

print(order1.checkout())
# Order total: $34.98
# Charged $34.98 to card ending in 1234

print(order2.checkout())
# Order total: $14.99
# Charged $14.99 to PayPal (alice@email.com)
```

Same `Order` class, different payment methods. The order doesn't know or care whether it's dealing with a credit card, PayPal, or crypto. It just calls `.process()`. That's polymorphism and composition working together.

## SOLID Principles - The Cliff Notes

SOLID is a set of five design principles that help you write maintainable code. They were originally described for enterprise Java, but the ideas apply everywhere. Here's each one in plain English, no corporate jargon.

**S - Single Responsibility Principle.** Each class should do one thing. A `User` class manages user data. A `UserValidator` class validates user data. A `UserDatabase` class saves user data. Don't cram it all into one mega-class. If you're describing your class and you need to use the word "and," it probably does too much.

**O - Open/Closed Principle.** Your code should be open for extension but closed for modification. Translation: you should be able to add new features without changing existing code. Our payment example nails this - adding `BitcoinPayment` just means writing a new class. We never touch `Order`, `CreditCard`, or `PayPal`.

**L - Liskov Substitution Principle.** If you have a function that expects a `Shape`, it should work with any subclass of `Shape` (Circle, Rectangle, Triangle) without breaking. Your child classes shouldn't violate the promises made by the parent. If `Shape.area()` returns a number, `Circle.area()` should too - not a string, not `None`, not a list of cats.

**I - Interface Segregation Principle.** Don't force a class to implement methods it doesn't need. If you have a `Worker` interface with `code()`, `test()`, and `make_coffee()`, your `Developer` class shouldn't be required to implement `make_coffee()`. (Although, let's be honest, most developers *do* make a lot of coffee.) Split big interfaces into smaller, focused ones.

**D - Dependency Inversion Principle.** High-level code shouldn't depend on low-level details. Our `Order` class depends on the `PaymentProcessor` abstraction, not on `CreditCard` specifically. This means you can swap in a new payment method without the `Order` knowing or caring. Depend on abstractions, not concrete implementations.

> **Don't Panic:** These fancy words are just names for common-sense ideas. You've probably been doing some of these already without knowing it. When you wrote small, focused functions in Sprint 2? That's the Single Responsibility Principle. When your code worked with lists AND tuples because they both support iteration? That's the Liskov Substitution Principle. You were already thinking this way. Now you just have the vocabulary.

## Your Turn

Let's refactor the vehicle hierarchy from Chapter 16 using composition:

1. Create an `Engine` class with attributes: `fuel_type`, `horsepower`, `efficiency` (km per fuel unit)

2. Create a `Vehicle` class that HAS an engine (composition):
   - Attributes: `make`, `model`, `year`, `engine`, `fuel_level` (starts at 100)
   - Method `drive(km)` that uses `self.engine.efficiency` to calculate fuel consumption
   - Method `describe()` that includes engine info

3. Create different engine types:
   - `gasoline_engine = Engine("gasoline", 200, 10)` (10 km per fuel unit)
   - `electric_motor = Engine("electric", 300, 15)` (15 km per unit)
   - `diesel_engine = Engine("diesel", 250, 8)` (8 km per unit)

4. Create vehicles with swappable engines:

```python
sedan = Vehicle("Toyota", "Camry", 2024, gasoline_engine)
ev = Vehicle("Tesla", "Model 3", 2024, electric_motor)
truck = Vehicle("Ford", "F-150", 2024, diesel_engine)
```

5. Add a `Fleet` class that contains multiple vehicles and can report total fuel usage.

**Bonus:** Make the `Vehicle` class support `__str__`, `__lt__` (compare by year), and `__len__` (returns fuel_level, because why not).

## TL;DR

- **Encapsulation** means hiding internals: `_protected` (convention), `__private` (name-mangled)
- Python's privacy is by convention, not enforcement - "we're all consenting adults"
- **Polymorphism** means same method name, different behavior. Call `.area()` on any shape, get the right answer
- Python's duck typing gives you polymorphism for free - no inheritance required
- **Composition** ("has a") is often better than inheritance ("is a") - it's more flexible and less fragile
- **SOLID** principles are common-sense rules for clean design. You don't need to memorize acronyms to write good code
- The goal of all these concepts: code that's easy to change, test, and explain to the next person
- These aren't academic abstractions - they're the difference between a codebase people enjoy working on and one that makes them update their resume

---

# Sprint 3 Checkpoint: Library Management System

> **Project** | **45-60 min build** | **Starter & Solution: [github link](https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/sprint-3-oop/sprint-3-project-library/)**

Sprint 3 done. Take a second to appreciate what just happened.

You now think in objects. You look at a problem and you see classes, attributes, methods, relationships. That's a fundamental shift in how you write code - and honestly, in how you *think* about code. Most of the software in the world is built this way, and now you can read it, write it, and reason about it.

Let's prove it by building something real.

## The Project: Library Management System

You're going to build a Library Management System with three core classes - `Book`, `Member`, and `Library` - that handles checkouts, returns, searching, and saves everything to a JSON file so your data survives between runs.

This isn't a toy example. It touches every skill from this sprint:

| Concept | Where You'll Use It |
|-----|----------|
| Classes & `__init__` (Ch. 15) | Every class you build |
| Methods & `self` (Ch. 15) | Every method you write |
| Inheritance (Ch. 16) | `EBook` and `AudioBook` extend `Book` |
| Magic methods (Ch. 17) | `__str__`, `__repr__`, `__len__` on `Library` |
| Encapsulation (Ch. 18) | Protected attributes, controlled access |
| Composition (Ch. 18) | `Library` HAS books and members |
| Polymorphism (Ch. 18) | Different book types, same interface |

Plus file handling and error handling from Sprint 2. See? It all connects.

## Step 1: The Book Class

Start with the foundation. A book has a title, author, ISBN, and availability status.

```python
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True
        self._borrower = None

    def check_out(self, member_name):
        if not self.is_available:
            raise ValueError(f"'{self.title}' is already checked out")
        self.is_available = False
        self._borrower = member_name
        return f"'{self.title}' checked out to {member_name}"

    def return_book(self):
        if self.is_available:
            raise ValueError(f"'{self.title}' wasn't checked out")
        borrower = self._borrower
        self.is_available = True
        self._borrower = None
        return f"'{self.title}' returned by {borrower}"

    def __str__(self):
        status = "Available" if self.is_available else f"Checked out to {self._borrower}"
        return f"'{self.title}' by {self.author} (ISBN: {self.isbn}) - {status}"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', '{self.isbn}')"

    def to_dict(self):
        """Convert to dictionary for JSON saving."""
        return {
            "type": self.__class__.__name__,
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "is_available": self.is_available,
            "borrower": self._borrower,
        }
```

Notice the `to_dict()` method - that's how we'll save to JSON later. Also notice `_borrower` has a single underscore. It's internal data that should only be changed through `check_out()` and `return_book()`. That's encapsulation in action.

## Step 2: Specialized Book Types (Inheritance)

An eBook has a file format. An audiobook has a narrator and duration. Both are still books.

```python
class EBook(Book):
    def __init__(self, title, author, isbn, file_format="PDF"):
        super().__init__(title, author, isbn)
        self.file_format = file_format

    def __str__(self):
        base = super().__str__()
        return f"{base} [EBook: {self.file_format}]"

    def to_dict(self):
        data = super().to_dict()
        data["file_format"] = self.file_format
        return data


class AudioBook(Book):
    def __init__(self, title, author, isbn, narrator, duration_hours):
        super().__init__(title, author, isbn)
        self.narrator = narrator
        self.duration_hours = duration_hours

    def __str__(self):
        base = super().__str__()
        return f"{base} [AudioBook: {self.duration_hours}h, narrated by {self.narrator}]"

    def to_dict(self):
        data = super().to_dict()
        data["narrator"] = self.narrator
        data["duration_hours"] = self.duration_hours
        return data
```

Inheritance at work: `EBook` and `AudioBook` get `check_out()`, `return_book()`, and everything else from `Book` for free. They just add their own special attributes.

## Step 3: The Member Class

A library member can borrow books and has a borrowing history.

```python
class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []
        self._max_books = 5

    def borrow(self, book):
        if len(self.borrowed_books) >= self._max_books:
            raise ValueError(f"{self.name} has reached the borrowing limit ({self._max_books})")
        result = book.check_out(self.name)
        self.borrowed_books.append(book.isbn)
        return result

    def return_book(self, book):
        if book.isbn not in self.borrowed_books:
            raise ValueError(f"{self.name} didn't borrow '{book.title}'")
        result = book.return_book()
        self.borrowed_books.remove(book.isbn)
        return result

    def __str__(self):
        count = len(self.borrowed_books)
        return f"Member: {self.name} (ID: {self.member_id}) - {count} book(s) borrowed"

    def __repr__(self):
        return f"Member('{self.name}', '{self.member_id}')"

    def to_dict(self):
        return {
            "name": self.name,
            "member_id": self.member_id,
            "borrowed_books": self.borrowed_books,
        }
```

## Step 4: The Library Class (Composition + Magic Methods)

The `Library` class is the heart of the system. It HAS books and HAS members (composition). It supports `len()` and string formatting (magic methods).

```python
import json
from pathlib import Path


class Library:
    def __init__(self, name):
        self.name = name
        self._books = {}       # isbn -> Book
        self._members = {}     # member_id -> Member

    def add_book(self, book):
        if book.isbn in self._books:
            raise ValueError(f"Book with ISBN {book.isbn} already exists")
        self._books[book.isbn] = book
        return f"Added: {book.title}"

    def add_member(self, member):
        if member.member_id in self._members:
            raise ValueError(f"Member ID {member.member_id} already exists")
        self._members[member.member_id] = member
        return f"Registered: {member.name}"

    def find_book(self, query):
        """Search by title or author (case-insensitive)."""
        query = query.lower()
        results = []
        for book in self._books.values():
            if query in book.title.lower() or query in book.author.lower():
                results.append(book)
        return results

    def checkout_book(self, member_id, isbn):
        member = self._members.get(member_id)
        if not member:
            raise ValueError(f"No member with ID {member_id}")
        book = self._books.get(isbn)
        if not book:
            raise ValueError(f"No book with ISBN {isbn}")
        return member.borrow(book)

    def return_book(self, member_id, isbn):
        member = self._members.get(member_id)
        if not member:
            raise ValueError(f"No member with ID {member_id}")
        book = self._books.get(isbn)
        if not book:
            raise ValueError(f"No book with ISBN {isbn}")
        return member.return_book(book)

    def available_books(self):
        return [b for b in self._books.values() if b.is_available]

    # -- Magic methods --

    def __len__(self):
        return len(self._books)

    def __str__(self):
        available = len(self.available_books())
        total = len(self)
        return f"{self.name}: {total} books ({available} available), {len(self._members)} members"

    def __contains__(self, isbn):
        return isbn in self._books

    # -- JSON persistence --

    def save(self, filepath="library_data.json"):
        data = {
            "name": self.name,
            "books": [b.to_dict() for b in self._books.values()],
            "members": [m.to_dict() for m in self._members.values()],
        }
        with open(filepath, "w") as f:
            json.dump(data, f, indent=2)
        return f"Library saved to {filepath}"

    @classmethod
    def load(cls, filepath="library_data.json"):
        with open(filepath, "r") as f:
            data = json.load(f)

        library = cls(data["name"])

        # Rebuild books (polymorphism: different types, same loading logic)
        book_classes = {"Book": Book, "EBook": EBook, "AudioBook": AudioBook}
        for book_data in data["books"]:
            book_type = book_data.pop("type", "Book")
            is_available = book_data.pop("is_available")
            borrower = book_data.pop("borrower")
            BookClass = book_classes.get(book_type, Book)
            book = BookClass(**book_data)
            book.is_available = is_available
            book._borrower = borrower
            library.add_book(book)

        # Rebuild members
        for member_data in data["members"]:
            borrowed = member_data.pop("borrowed_books")
            member = Member(**member_data)
            member.borrowed_books = borrowed
            library.add_member(member)

        return library
```

## Step 5: Put It All Together

Here's a script that exercises the entire system:

```python
def main():
    # Create the library
    lib = Library("City Central Library")

    # Add books (polymorphism - different types, same interface)
    lib.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald", "978-0743273565"))
    lib.add_book(Book("1984", "George Orwell", "978-0451524935"))
    lib.add_book(EBook("Python Crash Course", "Eric Matthes", "978-1718502703", "EPUB"))
    lib.add_book(AudioBook("Dune", "Frank Herbert", "978-0441013593", "Scott Brick", 21.5))

    # Add members
    lib.add_member(Member("Alice", "M001"))
    lib.add_member(Member("Bob", "M002"))

    # Library overview
    print(lib)
    print()

    # Search for books
    results = lib.find_book("python")
    for book in results:
        print(f"  Found: {book}")
    print()

    # Check out some books
    print(lib.checkout_book("M001", "978-0743273565"))
    print(lib.checkout_book("M001", "978-1718502703"))
    print(lib.checkout_book("M002", "978-0441013593"))
    print()

    # Check status
    print(lib)
    print()

    print("Available books:")
    for book in lib.available_books():
        print(f"  {book}")
    print()

    # Return a book
    print(lib.return_book("M001", "978-0743273565"))
    print()

    # Magic method: __contains__
    print(f"Has ISBN 978-0451524935? {'978-0451524935' in lib}")
    print(f"Total books: {len(lib)}")
    print()

    # Save to JSON
    print(lib.save())

    # Load from JSON (proof it works)
    loaded_lib = Library.load()
    print(f"\nLoaded: {loaded_lib}")


if __name__ == "__main__":
    main()
```

Expected output:

```
City Central Library: 4 books (4 available), 2 members

  Found: 'Python Crash Course' by Eric Matthes (ISBN: 978-1718502703) - Available [EBook: EPUB]

'The Great Gatsby' checked out to Alice
'Python Crash Course' checked out to Alice
'Dune' checked out to Bob

City Central Library: 4 books (1 available), 2 members

Available books:
  '1984' by George Orwell (ISBN: 978-0451524935) - Available

'The Great Gatsby' returned by Alice

Has ISBN 978-0451524935? True
Total books: 4

Library saved to library_data.json

Loaded: City Central Library: 4 books (2 available), 2 members
```

## Stretch Goals

Already finished? Try adding:

1. **Due dates.** When a book is checked out, record the date. Add a method to check for overdue books (more than 14 days).

2. **Fines.** Calculate late fees at $0.25 per day. Store the fine on the `Member` object.

3. **Search improvements.** Add search by availability, by type (`EBook` vs `AudioBook`), or by member (show all books a member has borrowed).

4. **A command-line interface.** Use `input()` and a menu loop to let users interact with the library from the terminal. Something like:

```
Welcome to City Central Library!
1. Search for a book
2. Check out a book
3. Return a book
4. View available books
5. Save & quit
```

5. **Exception handling.** Wrap the main flow in try/except blocks so the program doesn't crash on bad input.

## What You Used From This Sprint

Take a look at what you just built:

- **Classes and objects** - `Book`, `Member`, `Library` (Chapter 15)
- **`__init__` and `self`** - everywhere (Chapter 15)
- **Inheritance** - `EBook` and `AudioBook` extending `Book` (Chapter 16)
- **`super()`** - child constructors calling parent setup (Chapter 16)
- **Magic methods** - `__str__`, `__repr__`, `__len__`, `__contains__` (Chapter 17)
- **Encapsulation** - `_borrower`, `_books`, `_members`, `_max_books` (Chapter 18)
- **Composition** - `Library` HAS books and members (Chapter 18)
- **Polymorphism** - `EBook`, `AudioBook`, and `Book` all work the same way (Chapter 18)
- **File handling** - JSON save/load (Sprint 2, Chapter 12)
- **Error handling** - `ValueError` for invalid operations (Sprint 2, Chapter 13)

That's not a toy program. That's a real system with real design patterns. You should feel good about this.

## What's Next

You're past the halfway point of the book. Most people who start learning to code quit before getting here. You didn't. That means something. It means you're the kind of person who pushes through the hard parts, who doesn't quit when `self` is confusing or when inheritance doesn't click on the first try.

Sprint 4 is where things get *really* exciting. You're going to take everything you've built - your Python fundamentals, your OOP skills - and start building things that connect to the real world: APIs, web scraping, databases. The code you write is about to escape your terminal and start talking to the internet.

But first, take a break. Build the library project. Maybe go outside. You've earned it.

See you in Sprint 4.

---

# Welcome to Sprint 4: Pro Moves

> **Chapters 19-25** | **Estimated Time: 4-5 hours** | **Difficulty: Advanced (But You're Ready)**

Let's get something out of the way first.

**If you've made it to Sprint 4, you're already in the top 10% of Python learners.** Most people buy a programming book and stop at Chapter 3. You've built classes, handled errors, written file I/O, and survived inheritance. You're not a beginner anymore. Stop calling yourself one.

This sprint is where you go from "I know Python" to "I *use* Python." These are the tools professional developers reach for every single day - decorators, generators, APIs, databases, web scraping, testing, and clean code practices. This is what separates hobby coders from people who get hired.

If Python basics were learning to drive, this sprint is learning to drive stick, parallel park, and drift. (Okay, maybe not drift. But close.)

## What's Coming

- **Chapter 19:** Decorators - functions that upgrade other functions
- **Chapter 20:** Generators & iterators - memory-friendly data processing
- **Chapter 21:** APIs - talking to the internet
- **Chapter 22:** Databases - storing data for real
- **Chapter 23:** Web scraping - extracting data from websites
- **Chapter 24:** Testing - proving your code actually works
- **Chapter 25:** Type hints, linting & clean code - writing code like a professional

## The Sprint 4 Project: Job Listing Scraper & Dashboard

You'll build a complete **Job Listing Scraper** that pulls data from the web, stores it in a database, exposes it through a simple API, and includes a full test suite. Every chapter in this sprint feeds directly into this project.

Here's the best part: after this sprint, you're ONE sprint away from building AI applications. One. Let that sink in.

Let's go pro.

---

# Chapter 19: Decorators - Functions That Upgrade Functions

> **Sprint 4, Chapter 19** | **Estimated Time: 20-25 minutes** | **Difficulty: Advanced**

## Why Should I Care?

Have you ever seen code like this?

```python
@app.route("/home")
def home():
    return "Welcome!"
```

Or this?

```python
@login_required
def dashboard():
    return render_template("dashboard.html")
```

That `@` symbol is a **decorator**. And they're everywhere. Flask uses `@app.route` for web URLs. Django uses `@login_required` for authentication. pytest uses `@pytest.fixture` for test setup. FastAPI uses `@app.get` for API endpoints.

If you want to work with any modern Python framework, you need to understand decorators. And here's the good news - they're simpler than they look.

## The Gift Wrapping Analogy

Think of decorators as **gift wrapping**.

You have a gift (your function). It does something useful. A decorator wraps that gift with extra behavior - maybe a nice bow, maybe some tissue paper, maybe a card that says "Happy Birthday." The gift inside doesn't change. It still does exactly what it always did. But now it has something extra on the outside.

A `@timer` decorator wraps your function with timing code. A `@login_required` decorator wraps your function with an authentication check. The original function stays the same. The wrapper adds the extra behavior.

That's it. That's decorators.

## Functions Are Objects (A Quick Refresher)

Before we can understand decorators, we need to remember something important: **in Python, functions are objects.** You can pass them around, store them in variables, and return them from other functions.

```python
def greet(name):
    return f"Hello, {name}!"

# Store a function in a variable
say_hello = greet
print(say_hello("Alice"))  # Hello, Alice!

# Pass a function as an argument
def call_twice(func, arg):
    print(func(arg))
    print(func(arg))

call_twice(greet, "Bob")
# Hello, Bob!
# Hello, Bob!
```

Notice we wrote `greet` without parentheses when assigning it to `say_hello`. That's because we're passing the function itself, not calling it. `greet` is the function. `greet("Alice")` is calling the function.

> **Remember When?** In Chapter 10, we passed functions as arguments to `map()` and `filter()`. Same idea here. Functions are just values you can hand around like any other variable.

## Functions That Return Functions

Here's where it gets interesting. A function can **return another function**:

```python
def make_greeter(greeting):
    def greeter(name):
        return f"{greeting}, {name}!"
    return greeter

hello = make_greeter("Hello")
howdy = make_greeter("Howdy")

print(hello("Alice"))   # Hello, Alice!
print(howdy("Bob"))     # Howdy, Bob!
```

Read that carefully. `make_greeter` doesn't return a string. It returns a **function**. And that inner function (`greeter`) remembers the `greeting` variable from its parent, even after `make_greeter` has finished running.

This is called a **closure** - a function that remembers values from the scope where it was created.

## Closures: Functions That Remember

Let's make this concrete:

```python
def make_multiplier(factor):
    def multiply(number):
        return number * factor
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))   # 10
print(triple(5))   # 15
print(double(10))  # 20
```

`double` remembers that `factor` is 2. `triple` remembers that `factor` is 3. They each "closed over" their own copy of `factor`. That's a closure.

Why does this matter? Because **decorators are closures.** Understanding closures is the key to understanding decorators.

## Your First Decorator (Step by Step)

Let's build a decorator from scratch. We'll make one that prints a message before and after any function runs.

### Step 1: Write the wrapper function

```python
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function.")
        func()
        print("Something happened after the function.")
    return wrapper
```

Look at what this does:
1. It takes a function (`func`) as input
2. It creates a new function (`wrapper`) that calls the original function with some extra behavior
3. It returns the new function

### Step 2: Use it manually

```python
def say_hello():
    print("Hello!")

# "Decorate" the function manually
say_hello = my_decorator(say_hello)

# Now call it
say_hello()
```

Output:
```
Something is happening before the function.
Hello!
Something happened after the function.
```

The original `say_hello` just printed "Hello!" But after wrapping it, we get the extra behavior too. The function was **decorated**.

### Step 3: Use the @ syntax

That `say_hello = my_decorator(say_hello)` line is exactly what the `@` symbol does. These two are identical:

```python
# The manual way
def say_hello():
    print("Hello!")
say_hello = my_decorator(say_hello)

# The @ way (syntactic sugar)
@my_decorator
def say_hello():
    print("Hello!")
```

The `@` version is just cleaner. That's it. There's no magic. `@my_decorator` means "pass this function to `my_decorator` and replace it with whatever `my_decorator` returns."

> **Don't Panic:** Decorators are just functions that take a function and return a new function. Read that three times and it'll click. Seriously. Read it again. One more time. See? It clicked.

## Handling Arguments with *args and **kwargs

Our decorator above only works with functions that take no arguments. Let's fix that:

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}...")
        result = func(*args, **kwargs)
        print(f"{func.__name__} finished.")
        return result
    return wrapper

@my_decorator
def add(a, b):
    return a + b

@my_decorator
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(add(3, 5))
# Calling add...
# add finished.
# 8

print(greet("Alice", greeting="Hey"))
# Calling greet...
# greet finished.
# Hey, Alice!
```

The `*args, **kwargs` pattern means "accept any arguments and pass them through." This makes our decorator work with **any** function, regardless of its parameters.

## Practical Decorator: @timer

Here's a decorator you'll actually use. It measures how long a function takes to run:

```python
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
    return "Done!"

@timer
def sum_numbers(n):
    return sum(range(n))

print(slow_function())
# slow_function took 1.0012 seconds
# Done!

print(sum_numbers(1_000_000))
# sum_numbers took 0.0234 seconds
# 499999500000
```

This is genuinely useful. When you're trying to figure out why your program is slow, slap `@timer` on your functions and find the bottleneck.

## Practical Decorator: @logger

This one logs every function call with its arguments:

```python
def logger(func):
    def wrapper(*args, **kwargs):
        args_str = ", ".join([repr(a) for a in args])
        kwargs_str = ", ".join([f"{k}={repr(v)}" for k, v in kwargs.items()])
        all_args = ", ".join(filter(None, [args_str, kwargs_str]))
        print(f"[LOG] {func.__name__}({all_args})")
        result = func(*args, **kwargs)
        print(f"[LOG] {func.__name__} returned {repr(result)}")
        return result
    return wrapper

@logger
def calculate_total(price, tax_rate=0.08):
    return price * (1 + tax_rate)

calculate_total(100, tax_rate=0.1)
# [LOG] calculate_total(100, tax_rate=0.1)
# [LOG] calculate_total returned 110.00000000000001
```

In production code, you'd write to a log file instead of printing, but the idea is the same.

## Preserving Function Identity with functools.wraps

There's one gotcha with decorators. When you decorate a function, the wrapper replaces it - including its name and docstring:

```python
@timer
def my_function():
    """This is my function."""
    pass

print(my_function.__name__)    # wrapper  (not "my_function"!)
print(my_function.__doc__)     # None     (docstring is gone!)
```

Fix this with `functools.wraps`:

```python
import functools
import time

def timer(func):
    @functools.wraps(func)  # This preserves the original function's identity
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def my_function():
    """This is my function."""
    pass

print(my_function.__name__)    # my_function (correct!)
print(my_function.__doc__)     # This is my function. (preserved!)
```

Always use `@functools.wraps(func)` in your decorators. It's a one-liner and it prevents subtle bugs.

## @property: Pythonic Getters and Setters

Python has a built-in decorator that's incredibly useful: `@property`. It lets you access a method as if it were an attribute.

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value
    
    @property
    def area(self):
        import math
        return math.pi * self._radius ** 2

circle = Circle(5)
print(circle.radius)     # 5 (looks like an attribute, but it's a method)
print(circle.area)       # 78.53981633974483

circle.radius = 10       # Uses the setter
print(circle.area)       # 314.1592653589793

# circle.radius = -1     # ValueError: Radius cannot be negative
```

Notice how `circle.area` doesn't have parentheses. It looks like a regular attribute, but it's actually computed every time you access it. This is the Pythonic way to do getters and setters - no `get_radius()` and `set_radius()` methods needed.

## A Real-World Example: Retry Decorator

Here's a decorator you might actually use in production - it retries a function if it fails:

```python
import functools
import time

def retry(max_attempts=3, delay=1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts:
                        raise
                    print(f"Attempt {attempt} failed: {e}. Retrying in {delay}s...")
                    time.sleep(delay)
        return wrapper
    return decorator

@retry(max_attempts=3, delay=2)
def fetch_data(url):
    import random
    if random.random() < 0.7:  # 70% chance of failure
        raise ConnectionError("Server not responding")
    return {"data": "success"}

# This will retry up to 3 times if it fails
result = fetch_data("https://api.example.com")
```

Notice this is a decorator *with arguments* (`max_attempts`, `delay`). That requires an extra layer of nesting - a function that returns the decorator. It looks complicated, but it's just one more layer of the same pattern.

## Your Turn: Build a @timer Decorator

**Challenge:** Build a `@timer` decorator that:

1. Measures how long a function takes to run
2. Prints the function name, arguments, and elapsed time
3. Uses `functools.wraps` to preserve function identity
4. Returns the original function's result

Test it with:

```python
@timer
def fibonacci(n):
    """Calculate the nth Fibonacci number recursively."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

result = fibonacci(30)
print(f"Result: {result}")
```

**Starter code:** [https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/sprint-4-pro/chapter-19-decorators/](https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/sprint-4-pro/chapter-19-decorators/)

## TL;DR

| Concept | What It Does |
|--|--|
| First-class functions | Functions can be passed around like any other value |
| Closure | A function that remembers variables from its enclosing scope |
| Decorator | A function that takes a function and returns a new function with added behavior |
| `@decorator` syntax | Shorthand for `func = decorator(func)` |
| `*args, **kwargs` | Accept and pass through any arguments |
| `functools.wraps` | Preserves the decorated function's name and docstring |
| `@property` | Makes a method behave like an attribute |

**The one-sentence version:** A decorator is just a function that wraps another function to add extra behavior, and the `@` symbol is just a shortcut for applying it.

Next up: Generators and Iterators - where we learn to process data without loading it all into memory at once.

---

# Chapter 20: Generators & Iterators - Memory-Friendly Loops

> **Sprint 4, Chapter 20** | **Estimated Time: 15-20 minutes** | **Difficulty: Advanced**

## Why Should I Care?

Imagine you need to process a 10 GB log file. You could load the entire thing into memory... and watch your laptop freeze, crash, and possibly catch fire. Or you could process it one line at a time, using barely any memory at all.

That's what generators do. They let you work with huge amounts of data - or even *infinite* amounts of data - without running out of memory. Data pipelines, machine learning preprocessing, reading massive files, streaming data from APIs - generators are everywhere in professional Python code.

## The Netflix Analogy

Think about the difference between **downloading** and **streaming**.

If you wanted to watch every movie on Netflix, you *could* download all of them first. That would take... well, you'd need a warehouse of hard drives. Or you could **stream** - watch one movie at a time, and the next one loads only when you hit play.

**Lists are like downloading.** They compute and store every value upfront. **Generators are like streaming.** They compute one value at a time, only when you ask for it.

Same movies. Same data. Radically different memory usage.

## The Iterator Protocol (Quick Version)

Before generators, let's understand what they're built on. In Python, anything you can loop over with `for` is called an **iterable**. Lists, strings, dictionaries, files - all iterables.

Under the hood, Python uses two special methods to make looping work:

```python
# What Python actually does when you write: for x in [1, 2, 3]
my_list = [1, 2, 3]
iterator = iter(my_list)    # Calls __iter__() - gets an iterator

print(next(iterator))       # Calls __next__() - gets 1
print(next(iterator))       # Gets 2
print(next(iterator))       # Gets 3
# next(iterator)            # Raises StopIteration
```

An **iterator** is an object with a `__next__()` method. Each call to `next()` gives you the next value. When there are no more values, it raises `StopIteration`. That's it. That's the entire protocol.

You can build your own iterator class:

```python
class Countdown:
    def __init__(self, start):
        self.current = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value

for num in Countdown(5):
    print(num)
# 5, 4, 3, 2, 1
```

That works, but it's a lot of code for a simple countdown. There's a much better way.

## Generators: The Easy Way

A **generator** is a function that uses `yield` instead of `return`. And it does the same thing as that entire `Countdown` class above, in about three lines:

```python
def countdown(start):
    current = start
    while current > 0:
        yield current
        current -= 1

for num in countdown(5):
    print(num)
# 5, 4, 3, 2, 1
```

That's it. `yield` is the magic word.

Here's what makes `yield` special: when a generator function hits `yield`, it **pauses**. It hands back the value and freezes in place. The next time you ask for a value (via `next()` or a `for` loop), it **resumes** exactly where it left off.

> **Don't Panic:** `yield` is just `return` that remembers where it left off. That's literally all it is.

Let's trace through it step by step:

```python
def simple_gen():
    print("Step 1")
    yield "A"
    print("Step 2")
    yield "B"
    print("Step 3")
    yield "C"
    print("Done")

gen = simple_gen()        # Nothing happens yet!
print(next(gen))          # "Step 1" prints, then yields "A"
print(next(gen))          # "Step 2" prints, then yields "B"
print(next(gen))          # "Step 3" prints, then yields "C"
# next(gen)               # "Done" prints, then StopIteration
```

Notice: **creating the generator does nothing.** It doesn't start running until you call `next()` on it. This is called **lazy evaluation** - values are computed only when needed.

> **Remember When?** Remember lists from Sprint 1? Generators are just lazy lists. They compute values one at a time instead of all at once. Same data, less memory.

## Generator Expressions: The One-Liner

Just like list comprehensions give you a one-liner for lists, **generator expressions** give you a one-liner for generators. The syntax is identical, except you use parentheses instead of square brackets:

```python
# List comprehension - creates the entire list in memory
squares_list = [x ** 2 for x in range(1000000)]

# Generator expression - creates values one at a time
squares_gen = (x ** 2 for x in range(1000000))

print(type(squares_list))  # <class 'list'>
print(type(squares_gen))   # <class 'generator'>
```

The list version creates one million numbers in memory right now. The generator version creates... nothing yet. It'll compute each square only when you ask for it.

You can use generator expressions anywhere you'd use a list comprehension:

```python
# Sum of squares (no list needed - just pass the generator)
total = sum(x ** 2 for x in range(1000000))

# Find the first even square over 100
result = next(x ** 2 for x in range(1000) if x ** 2 > 100 and x % 2 == 0)
print(result)  # 144
```

When you pass a generator expression as the only argument to a function, you can drop the extra parentheses. `sum(x**2 for x in range(10))` instead of `sum((x**2 for x in range(10)))`.

## Memory Comparison: Lists vs Generators

Let's see the difference in real numbers:

```python
import sys

# A list of 1 million numbers
big_list = [x for x in range(1_000_000)]
print(f"List size: {sys.getsizeof(big_list):,} bytes")
# List size: 8,448,728 bytes (~8 MB)

# A generator for 1 million numbers
big_gen = (x for x in range(1_000_000))
print(f"Generator size: {sys.getsizeof(big_gen):,} bytes")
# Generator size: 200 bytes

# That's a 42,000x difference!
```

The list uses about 8 megabytes. The generator uses 200 bytes. Same million numbers. The generator just doesn't compute them until it needs to.

For 10 million numbers, the list would use ~80 MB. For 100 million, ~800 MB. The generator? Still 200 bytes.

## Practical Example: Reading Large Files

This is probably the most common real-world use of generators. Processing files line by line without loading the whole thing into memory:

```python
def read_large_file(file_path):
    """Read a file line by line using a generator."""
    with open(file_path, "r") as file:
        for line in file:
            yield line.strip()

def find_errors(file_path):
    """Find all error lines in a log file."""
    for line in read_large_file(file_path):
        if "ERROR" in line:
            yield line

# Process a 10 GB log file using barely any memory
for error_line in find_errors("server.log"):
    print(error_line)
```

Each line is read, checked, and either yielded or discarded. At any given moment, only one line is in memory. You could process a terabyte file this way.

## Chaining Generators: Data Pipelines

Generators really shine when you chain them together into a pipeline:

```python
def read_csv_lines(file_path):
    """Read CSV lines, skip header."""
    with open(file_path) as f:
        next(f)  # Skip header
        for line in f:
            yield line.strip()

def parse_fields(lines):
    """Split each line into fields."""
    for line in lines:
        yield line.split(",")

def filter_by_amount(records, min_amount):
    """Keep only records above a minimum amount."""
    for record in records:
        if float(record[2]) > min_amount:
            yield record

# Chain them together - nothing runs until the for loop starts
lines = read_csv_lines("transactions.csv")
records = parse_fields(lines)
big_transactions = filter_by_amount(records, 1000)

for record in big_transactions:
    print(record)
```

Each step processes one item at a time and hands it to the next step. It's like an assembly line - nothing is stored, everything flows through.

## Infinite Generators

Because generators don't compute everything upfront, they can be **infinite**:

```python
def count_forever(start=0):
    """Count from start to infinity."""
    n = start
    while True:
        yield n
        n += 1

def fibonacci():
    """Generate Fibonacci numbers forever."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Take the first 10 Fibonacci numbers
from itertools import islice

first_10 = list(islice(fibonacci(), 10))
print(first_10)  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

You can't do `list(fibonacci())` - that would try to create an infinite list and crash. But you can take as many as you need with `islice`.

> **Wait, What?** "An infinite loop that doesn't crash?" Yes! Because `yield` pauses the loop. The infinite `while True` only runs one iteration at a time. As long as you stop asking for values at some point, it's perfectly fine.

## The itertools Module: Generator Superpowers

Python's `itertools` module is a treasure chest of generator tools:

```python
from itertools import count, cycle, repeat, chain, islice

# count: infinite counter
for i in islice(count(10, 2), 5):  # Start at 10, step 2
    print(i)  # 10, 12, 14, 16, 18

# cycle: repeat a sequence forever
colors = cycle(["red", "green", "blue"])
for _ in range(7):
    print(next(colors))  # red, green, blue, red, green, blue, red

# chain: combine multiple iterables
combined = chain([1, 2], [3, 4], [5, 6])
print(list(combined))  # [1, 2, 3, 4, 5, 6]
```

## When to Use Generators vs Lists

| Use a **List** when... | Use a **Generator** when... |
|--|--|
| You need to access items by index | You only need to iterate once |
| You need to iterate multiple times | The data is large or infinite |
| You need the length | Memory is a concern |
| You need to sort or reverse | You're chaining operations |
| The data is small | You're reading from files or network |

## Your Turn: Fibonacci Generator

**Challenge:** Build a `fibonacci` generator that:

1. Yields Fibonacci numbers one at a time
2. Can optionally take a `limit` parameter (max value)
3. Write a second generator that filters for even Fibonacci numbers only

```python
# Your goal:
for num in fibonacci(limit=100):
    print(num)
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89

for num in even_fibonacci(limit=100):
    print(num)
# 0, 2, 8, 34
```

**Starter code:** [https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/sprint-4-pro/chapter-20-generators/](https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/sprint-4-pro/chapter-20-generators/)

## TL;DR

| Concept | What It Does |
|--|--|
| Iterator | An object with `__next__()` that produces values one at a time |
| Generator function | A function with `yield` that becomes an iterator |
| `yield` | Like `return` but pauses and resumes |
| Generator expression | `(x for x in iterable)` - lazy version of list comprehension |
| Lazy evaluation | Values computed only when needed |
| `itertools` | Standard library module with generator utilities |

**The one-sentence version:** Generators let you process data one piece at a time instead of loading everything into memory, using `yield` to pause and resume a function.

Next up: APIs - where we teach Python to talk to the internet.

---

# Chapter 21: Working with APIs - Talking to the Internet

> **Sprint 4, Chapter 21** | **Estimated Time: 20-25 minutes** | **Difficulty: Advanced**

## Why Should I Care?

Every time you check the weather on your phone, that app doesn't have its own weather satellites. It asks someone else's server for the data. Every time you see stock prices update in real time, your app is calling an API. Social media bots, AI chatbots, payment processing, maps, translation services - all APIs.

**APIs are how programs talk to each other over the internet.** If you want to build anything that connects to the outside world - and you do - you need this chapter.

## The Restaurant Analogy

Think of an API like **ordering at a restaurant**.

- **You** are the client (your Python program)
- **The menu** is the API documentation (what you can order)
- **Your order** is the request (what you're asking for)
- **The waiter** is the API (the intermediary)
- **The kitchen** is the server (where the work happens)
- **Your food** is the response (what you get back)

You don't walk into the kitchen and cook your own food. You don't need to know *how* the kitchen works. You just read the menu, place your order, and the waiter brings you what you asked for.

APIs work exactly the same way. You don't need to know how Google's weather service works internally. You just send a request and get data back.

## HTTP Methods: The Four Magic Words

When you talk to an API, you use **HTTP methods** - think of them as different types of requests:

| Method | What It Does | Restaurant Analogy |
|--|--|--|
| `GET` | Read/retrieve data | "Can I see the menu?" |
| `POST` | Create new data | "I'd like to place an order." |
| `PUT` | Update existing data | "Actually, change my order to..." |
| `DELETE` | Remove data | "Cancel my order." |

90% of the time, you'll use `GET` (reading data) and `POST` (sending data). The others are important but less common for beginners.

## The requests Library

Python's built-in `urllib` library can make HTTP requests, but it's painful to use. The `requests` library is what everyone actually uses. It's not built-in, so install it first:

```bash
pip install requests
```

### Your First API Call

Let's start with the simplest possible API call - getting a random joke:

```python
import requests

response = requests.get("https://official-joke-api.appspot.com/random_joke")

print(response.status_code)  # 200
print(response.json())
# {'type': 'general', 'setup': 'Why did the scarecrow win an award?',
#  'punchline': 'Because he was outstanding in his field.'}
```

That's it. Three lines of code and you're talking to the internet.

Let's break it down:

1. `requests.get(url)` - sends a GET request to that URL
2. `response.status_code` - the HTTP status code (200 means success)
3. `response.json()` - parses the response body as JSON (a Python dictionary)

## Status Codes: What the Server Is Telling You

When the server responds, it includes a status code that tells you what happened:

| Code | Meaning | What to Do |
|--|--|--|
| `200` | OK - success! | Parse the data |
| `201` | Created - new resource made | Your POST worked |
| `400` | Bad Request - you messed up | Check your request |
| `401` | Unauthorized - need credentials | Add an API key |
| `403` | Forbidden - not allowed | You don't have permission |
| `404` | Not Found - doesn't exist | Check the URL |
| `429` | Too Many Requests - slow down | Wait and retry |
| `500` | Server Error - they messed up | Not your fault, try again later |

The easy rule: **2xx means success, 4xx means you did something wrong, 5xx means the server did something wrong.**

> **Pro Tip:** Always check the response status code before trying to parse the data. A `404` response doesn't have the data you expect, and trying to parse it will give you confusing errors.

## Parsing JSON Responses

Most APIs return data in **JSON** format (JavaScript Object Notation). Good news - JSON maps directly to Python dictionaries and lists:

```python
import requests

response = requests.get("https://api.github.com/users/python")

if response.status_code == 200:
    data = response.json()
    
    print(f"Name: {data['name']}")
    print(f"Location: {data['location']}")
    print(f"Public repos: {data['public_repos']}")
    print(f"Followers: {data['followers']}")
else:
    print(f"Error: {response.status_code}")
```

JSON objects become Python dicts. JSON arrays become Python lists. JSON strings, numbers, booleans, and null become their Python equivalents. It's a seamless translation.

## Sending Data with POST Requests

GET retrieves data. POST sends data. Here's how:

```python
import requests

# POST with JSON data
data = {
    "title": "My Post",
    "body": "This is the content.",
    "userId": 1
}

response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json=data  # Automatically converts to JSON and sets headers
)

print(response.status_code)  # 201 (Created)
print(response.json())
# {'title': 'My Post', 'body': 'This is the content.', 'userId': 1, 'id': 101}
```

The `json=data` parameter is a shortcut that:
1. Converts your Python dict to a JSON string
2. Sets the `Content-Type` header to `application/json`

## Query Parameters

Many APIs let you customize your request with query parameters - the stuff after the `?` in a URL:

```python
import requests

# Instead of building the URL manually...
# requests.get("https://api.github.com/search/repositories?q=python&sort=stars")

# ...use the params argument (cleaner)
params = {
    "q": "python",
    "sort": "stars",
    "per_page": 5
}

response = requests.get(
    "https://api.github.com/search/repositories",
    params=params
)

data = response.json()
for repo in data["items"]:
    print(f"{repo['name']}: {repo['stargazers_count']:,} stars")
```

Using `params=` is cleaner than building the URL string yourself, and it handles special characters automatically.

## API Keys and Authentication

Most serious APIs require authentication - usually an **API key**. This is a unique string that identifies you and tracks your usage.

```python
import requests

# Method 1: API key as a query parameter
response = requests.get(
    "https://api.example.com/data",
    params={"api_key": "your_key_here"}
)

# Method 2: API key in headers (more common, more secure)
headers = {
    "Authorization": "Bearer your_api_key_here"
}
response = requests.get(
    "https://api.example.com/data",
    headers=headers
)

# Method 3: Basic authentication
response = requests.get(
    "https://api.example.com/data",
    auth=("username", "password")
)
```

> **Wait, What?** "Where do I get an API key?" Sign up on the API provider's website. Most have a free tier. OpenWeatherMap, GitHub, NewsAPI - they all give you a key when you register.

**Important:** Never put API keys directly in your code, especially if you're pushing to GitHub. Use environment variables:

```python
import os
import requests

api_key = os.environ.get("WEATHER_API_KEY")

if not api_key:
    print("Error: Set the WEATHER_API_KEY environment variable")
else:
    response = requests.get(
        "https://api.openweathermap.org/data/2.5/weather",
        params={"q": "London", "appid": api_key}
    )
```

## Rate Limiting: Don't Be That Person

APIs limit how many requests you can make in a given time period. This is called **rate limiting**. Hit the limit and you'll get a `429 Too Many Requests` response.

```python
import requests
import time

def polite_request(url, max_retries=3, delay=1):
    """Make a request with retry logic for rate limiting."""
    for attempt in range(max_retries):
        response = requests.get(url)
        
        if response.status_code == 200:
            return response
        elif response.status_code == 429:
            wait_time = int(response.headers.get("Retry-After", delay))
            print(f"Rate limited. Waiting {wait_time} seconds...")
            time.sleep(wait_time)
        else:
            response.raise_for_status()  # Raise an exception for other errors
    
    print("Max retries exceeded")
    return None
```

General rules:
- Read the API docs for rate limits
- Add a small delay between requests (`time.sleep(1)`)
- Cache responses when possible (don't ask for the same data twice)
- Handle 429 responses gracefully

## Error Handling for API Calls

API calls can fail in many ways - network errors, timeouts, bad responses. Always handle errors:

```python
import requests

def safe_api_call(url, timeout=10):
    """Make an API call with proper error handling."""
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()  # Raises exception for 4xx/5xx
        return response.json()
    
    except requests.exceptions.Timeout:
        print(f"Request timed out after {timeout} seconds")
        return None
    
    except requests.exceptions.ConnectionError:
        print("Could not connect. Check your internet connection.")
        return None
    
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error: {e}")
        return None
    
    except requests.exceptions.JSONDecodeError:
        print("Response was not valid JSON")
        return None

# Use it
data = safe_api_call("https://api.github.com/users/python")
if data:
    print(f"Name: {data['name']}")
```

The `timeout=10` parameter prevents your program from hanging forever if the server doesn't respond. Always set a timeout.

> **Don't Panic:** API error handling looks like a lot of code, but it's the same pattern every time. Write it once, reuse it forever. Professional developers copy-paste this pattern into every project.

## Putting It All Together: A Complete API Client

Let's build a simple GitHub user lookup tool:

```python
import requests

class GitHubClient:
    """Simple GitHub API client."""
    
    BASE_URL = "https://api.github.com"
    
    def __init__(self, token=None):
        self.session = requests.Session()
        if token:
            self.session.headers["Authorization"] = f"Bearer {token}"
    
    def get_user(self, username):
        """Get info about a GitHub user."""
        response = self.session.get(
            f"{self.BASE_URL}/users/{username}",
            timeout=10
        )
        
        if response.status_code == 404:
            print(f"User '{username}' not found.")
            return None
        
        response.raise_for_status()
        data = response.json()
        
        return {
            "name": data.get("name", "N/A"),
            "bio": data.get("bio", "N/A"),
            "public_repos": data["public_repos"],
            "followers": data["followers"],
            "url": data["html_url"]
        }
    
    def get_repos(self, username, sort="stars"):
        """Get a user's repositories."""
        response = self.session.get(
            f"{self.BASE_URL}/users/{username}/repos",
            params={"sort": sort, "per_page": 5},
            timeout=10
        )
        response.raise_for_status()
        
        return [
            {"name": repo["name"], "stars": repo["stargazers_count"]}
            for repo in response.json()
        ]

# Use it
client = GitHubClient()

user = client.get_user("python")
if user:
    print(f"Name: {user['name']}")
    print(f"Bio: {user['bio']}")
    print(f"Repos: {user['public_repos']}")
    print(f"Followers: {user['followers']:,}")

print("\nTop repos:")
for repo in client.get_repos("python"):
    print(f"  {repo['name']}: {repo['stars']:,} stars")
```

Notice we used `requests.Session()` - this reuses the connection and headers across multiple requests. More efficient and cleaner.

## Your Turn: Weather Checker

**Challenge:** Build a weather checker using the free wttr.in API (no API key needed!):

```python
import requests

def get_weather(city):
    """Get weather for a city using wttr.in."""
    response = requests.get(
        f"https://wttr.in/{city}",
        params={"format": "j1"}  # JSON format
    )
    
    if response.status_code == 200:
        data = response.json()
        current = data["current_condition"][0]
        
        return {
            "city": city,
            "temp_c": current["temp_C"],
            "temp_f": current["temp_F"],
            "description": current["weatherDesc"][0]["value"],
            "humidity": current["humidity"],
            "wind_speed": current["windspeedKmph"]
        }
    return None

# Test it
weather = get_weather("London")
if weather:
    print(f"Weather in {weather['city']}:")
    print(f"  Temperature: {weather['temp_c']}C / {weather['temp_f']}F")
    print(f"  Conditions: {weather['description']}")
    print(f"  Humidity: {weather['humidity']}%")
```

Extend it to:
1. Accept city names from user input
2. Handle errors (bad city names, no internet)
3. Compare weather between two cities

**Starter code:** [https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/sprint-4-pro/chapter-21-apis/](https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/sprint-4-pro/chapter-21-apis/)

## TL;DR

| Concept | What It Does |
|--|--|
| API | A way for programs to talk to each other over the internet |
| `requests.get(url)` | Send a GET request (retrieve data) |
| `requests.post(url, json=data)` | Send a POST request (send data) |
| `response.status_code` | HTTP status code (200 = OK, 404 = not found) |
| `response.json()` | Parse the response as a Python dictionary |
| `params={}` | Add query parameters to the URL |
| `headers={}` | Add headers (like API keys) to the request |
| `timeout=10` | Don't wait forever for a response |
| `response.raise_for_status()` | Raise an exception if the status code is 4xx or 5xx |

**The one-sentence version:** Use the `requests` library to send HTTP requests to APIs, get back JSON data, and always handle errors and check status codes.

Next up: Databases - where we learn to store data for real, not just in files.

---

# Chapter 22: Databases with Python - Storing Data for Real

> **Sprint 4, Chapter 22** | **Estimated Time: 20-25 minutes** | **Difficulty: Advanced**

## Why Should I Care?

Every app you've ever used has a database behind it. Instagram stores your photos and likes. Spotify stores your playlists and listening history. Amazon stores your orders, payment info, and that wish list you've been building since 2015. Even the simplest to-do app needs to remember your tasks after you close it.

Up until now, we've been saving data to text files, CSV files, and JSON files. That works for small projects, but it falls apart fast. Try searching a million-row CSV file. Try making sure two users don't edit the same file at the same time. Try updating one field without rewriting the entire file.

Databases solve all of these problems. And Python comes with one built in.

## The Spreadsheet Analogy

CSV files are like spreadsheets. Databases are like spreadsheets with superpowers - they can search millions of rows in milliseconds, enforce rules about what data is allowed, handle multiple users at once, and never lose your data if the power goes out.

Think of a database as a collection of spreadsheets (called **tables**), where each spreadsheet has defined columns (called **fields** or **columns**) and each row is a record. The difference is that databases have a powerful query language called **SQL** that lets you ask complex questions about your data instantly.

## SQLite: A Database in Your Pocket

There are many database systems - PostgreSQL, MySQL, MongoDB, Oracle. They all require installing and running a separate server. Except one.

**SQLite** is a database that lives in a single file. No server needed. No installation. No configuration. And it's **built into Python**. Just `import sqlite3` and go.

Don't let the simplicity fool you - SQLite handles databases up to 281 terabytes. It's used in every iPhone, every Android phone, every Chrome browser, and every Firefox browser. It's the most widely deployed database engine in the world.

```python
import sqlite3

# Create a database (or open it if it already exists)
conn = sqlite3.connect("my_app.db")

# Create a cursor (this is how you send SQL commands)
cursor = conn.cursor()

print("Database created!")

# Always close when done
conn.close()
```

That's it. You now have a database. The file `my_app.db` was created in your current directory.

## Creating Tables

Before you can store data, you need to create a **table** - the structure that defines what your data looks like:

```python
import sqlite3

conn = sqlite3.connect("my_app.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        age INTEGER,
        created_at TEXT DEFAULT CURRENT_TIMESTAMP
    )
""")

conn.commit()  # Save changes to disk
conn.close()
```

Let's decode that SQL:

| Part | Meaning |
|--|--|
| `CREATE TABLE IF NOT EXISTS` | Make a table (don't crash if it already exists) |
| `id INTEGER PRIMARY KEY AUTOINCREMENT` | Auto-numbering ID column (1, 2, 3...) |
| `name TEXT NOT NULL` | Text column, required (can't be empty) |
| `email TEXT UNIQUE NOT NULL` | Text column, required, must be unique |
| `age INTEGER` | Number column, optional |
| `DEFAULT CURRENT_TIMESTAMP` | Auto-fill with current date/time |

> **Don't Panic:** SQL looks like a foreign language at first, but it reads almost like English. "CREATE a TABLE called users with these columns." Once you see a few examples, you'll pick up the pattern fast.

## CRUD Operations: The Four Things You Do with Data

Every database interaction boils down to four operations. Developers call them **CRUD**:

- **C**reate (INSERT)
- **R**ead (SELECT)
- **U**pdate (UPDATE)
- **D**elete (DELETE)

Let's go through each one.

### Create: INSERT

```python
import sqlite3

conn = sqlite3.connect("my_app.db")
cursor = conn.cursor()

# Insert a single record
cursor.execute("""
    INSERT INTO users (name, email, age)
    VALUES (?, ?, ?)
""", ("Alice", "alice@email.com", 28))

# Insert multiple records
users = [
    ("Bob", "bob@email.com", 34),
    ("Charlie", "charlie@email.com", 22),
    ("Diana", "diana@email.com", 31),
]
cursor.executemany("""
    INSERT INTO users (name, email, age)
    VALUES (?, ?, ?)
""", users)

conn.commit()
print(f"Inserted {cursor.rowcount} users")

conn.close()
```

See those `?` marks? Those are **placeholders**. This is critically important, so let's talk about it.

### NEVER Use f-strings in SQL (Security Warning)

This is one of the most important things in this entire book:

```python
# NEVER DO THIS - SQL injection vulnerability!
name = input("Enter name: ")
cursor.execute(f"SELECT * FROM users WHERE name = '{name}'")

# What if someone types: ' OR '1'='1
# The query becomes: SELECT * FROM users WHERE name = '' OR '1'='1'
# That returns EVERY user in the database!

# Or worse: '; DROP TABLE users; -
# That DELETES your entire table!
```

This is called **SQL injection**, and it's one of the most common security vulnerabilities in web applications. The fix is simple - always use parameterized queries:

```python
# ALWAYS DO THIS - safe!
name = input("Enter name: ")
cursor.execute("SELECT * FROM users WHERE name = ?", (name,))
```

The `?` placeholder tells SQLite to treat the value as data, not as SQL code. Problem solved. No exceptions. **Always use `?` placeholders.**

> **Wait, What?** "Is SQL injection really that dangerous?" Yes. In 2017, Equifax suffered a breach that exposed 147 million people's personal data due to a vulnerability that could have been prevented with parameterized queries. This isn't theoretical.

### Read: SELECT

```python
import sqlite3

conn = sqlite3.connect("my_app.db")
cursor = conn.cursor()

# Get all users
cursor.execute("SELECT * FROM users")
all_users = cursor.fetchall()
for user in all_users:
    print(user)
# (1, 'Alice', 'alice@email.com', 28, '2024-01-15 10:30:00')
# (2, 'Bob', 'bob@email.com', 34, '2024-01-15 10:30:00')
# ...

# Get specific columns
cursor.execute("SELECT name, email FROM users")
for row in cursor.fetchall():
    print(f"{row[0]} - {row[1]}")

# Filter with WHERE
cursor.execute("SELECT * FROM users WHERE age > ?", (25,))
older_users = cursor.fetchall()

# Get just one record
cursor.execute("SELECT * FROM users WHERE email = ?", ("alice@email.com",))
alice = cursor.fetchone()
print(alice)  # (1, 'Alice', 'alice@email.com', 28, '2024-01-15 10:30:00')

# Sort results
cursor.execute("SELECT * FROM users ORDER BY age DESC")

# Limit results
cursor.execute("SELECT * FROM users LIMIT 5")

conn.close()
```

Key fetch methods:
- `fetchone()` - get the next single row (or `None` if no more rows)
- `fetchall()` - get all remaining rows as a list of tuples
- `fetchmany(n)` - get the next `n` rows

### Getting Named Columns with Row Factory

Tuples are fine, but accessing columns by index (`row[0]`, `row[1]`) is error-prone. Use `Row` factory to access columns by name:

```python
import sqlite3

conn = sqlite3.connect("my_app.db")
conn.row_factory = sqlite3.Row  # Enable named access

cursor = conn.cursor()
cursor.execute("SELECT * FROM users WHERE name = ?", ("Alice",))
user = cursor.fetchone()

# Now you can use column names!
print(user["name"])    # Alice
print(user["email"])   # alice@email.com
print(user["age"])     # 28

conn.close()
```

Much better than remembering that name is index 1 and email is index 2.

### Update: UPDATE

```python
import sqlite3

conn = sqlite3.connect("my_app.db")
cursor = conn.cursor()

# Update one user's age
cursor.execute("""
    UPDATE users SET age = ? WHERE email = ?
""", (29, "alice@email.com"))

# Update multiple fields
cursor.execute("""
    UPDATE users SET name = ?, age = ? WHERE id = ?
""", ("Alicia", 29, 1))

conn.commit()
print(f"Updated {cursor.rowcount} rows")

conn.close()
```

Always include a `WHERE` clause in your `UPDATE` statements. Without it, you'll update **every** row in the table. Ask me how I know.

### Delete: DELETE

```python
import sqlite3

conn = sqlite3.connect("my_app.db")
cursor = conn.cursor()

# Delete a specific user
cursor.execute("DELETE FROM users WHERE id = ?", (3,))

conn.commit()
print(f"Deleted {cursor.rowcount} rows")

conn.close()
```

Same warning as `UPDATE` - always use `WHERE`. `DELETE FROM users` without a `WHERE` clause deletes everything. Every row. Gone. No undo.

## Context Managers: The Right Way

Manually calling `conn.close()` is fragile - if an error happens before that line, the connection stays open. Use a context manager instead:

```python
import sqlite3

def get_all_users():
    with sqlite3.connect("my_app.db") as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users ORDER BY name")
        return [dict(row) for row in cursor.fetchall()]

# The connection auto-commits on success and auto-closes when done
users = get_all_users()
for user in users:
    print(user)
```

The `with` statement ensures the connection is properly handled - it commits on success and rolls back on error.

> **Remember When?** We used context managers for file handling in Sprint 2 - `with open("file.txt") as f:`. Same pattern here. Python loves context managers because they guarantee cleanup.

## Building a Complete Database Module

Let's build something real. Here's a clean database module for managing tasks:

```python
import sqlite3
from datetime import datetime

DB_NAME = "tasks.db"

def get_connection():
    """Get a database connection with row factory."""
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def create_tables():
    """Create the tasks table if it doesn't exist."""
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT,
                priority TEXT DEFAULT 'medium',
                completed INTEGER DEFAULT 0,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
        """)

def add_task(title, description="", priority="medium"):
    """Add a new task."""
    with get_connection() as conn:
        cursor = conn.execute(
            "INSERT INTO tasks (title, description, priority) VALUES (?, ?, ?)",
            (title, description, priority)
        )
        return cursor.lastrowid

def get_all_tasks(show_completed=False):
    """Get all tasks, optionally including completed ones."""
    with get_connection() as conn:
        if show_completed:
            query = "SELECT * FROM tasks ORDER BY created_at DESC"
            rows = conn.execute(query).fetchall()
        else:
            query = "SELECT * FROM tasks WHERE completed = 0 ORDER BY priority, created_at DESC"
            rows = conn.execute(query).fetchall()
        return [dict(row) for row in rows]

def complete_task(task_id):
    """Mark a task as completed."""
    with get_connection() as conn:
        cursor = conn.execute(
            "UPDATE tasks SET completed = 1 WHERE id = ?",
            (task_id,)
        )
        return cursor.rowcount > 0

def delete_task(task_id):
    """Delete a task."""
    with get_connection() as conn:
        cursor = conn.execute(
            "DELETE FROM tasks WHERE id = ?",
            (task_id,)
        )
        return cursor.rowcount > 0

# Usage
if __name__ == "__main__":
    create_tables()
    
    # Add some tasks
    add_task("Learn SQLite", "Chapter 22 of Python Crash Course", "high")
    add_task("Build a project", "Sprint 4 checkpoint", "medium")
    add_task("Take a break", "You've earned it", "low")
    
    # List tasks
    print("Open tasks:")
    for task in get_all_tasks():
        print(f"  [{task['id']}] {task['title']} ({task['priority']})")
    
    # Complete a task
    complete_task(1)
    
    print("\nAfter completing task 1:")
    for task in get_all_tasks():
        print(f"  [{task['id']}] {task['title']} ({task['priority']})")
```

This is a pattern you'll use over and over: one function per operation, each with its own connection, each using parameterized queries.

## Brief ORM Intro: SQLAlchemy

Writing raw SQL is fine for learning and small projects, but bigger projects use an **ORM** (Object-Relational Mapper). An ORM lets you interact with your database using Python objects instead of SQL strings.

The most popular Python ORM is **SQLAlchemy**. Here's what the same task code looks like:

```python
# This is just a preview - don't worry about memorizing this
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base, Session

Base = declarative_base()

class Task(Base):
    __tablename__ = "tasks"
    
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    priority = Column(String, default="medium")
    completed = Column(Boolean, default=False)

engine = create_engine("sqlite:///tasks.db")
Base.metadata.create_all(engine)

# Adding a task becomes:
with Session(engine) as session:
    task = Task(title="Learn SQLAlchemy", priority="high")
    session.add(task)
    session.commit()

# Querying becomes:
with Session(engine) as session:
    open_tasks = session.query(Task).filter_by(completed=False).all()
    for task in open_tasks:
        print(task.title)
```

See how you work with `Task` objects instead of writing SQL? That's the appeal of ORMs. You'll use them extensively in web development (Django has its own ORM, Flask uses SQLAlchemy).

For now, focus on raw SQL with `sqlite3`. Understanding SQL directly makes you a better developer, and the ORM will make more sense later.

## Your Turn: Convert Expense Tracker to SQLite

> **Remember When?** The expense tracker from Sprint 2 used CSV files. Let's upgrade it to a real database.

**Challenge:** Build an expense tracker with SQLite that can:

1. Create an `expenses` table (id, amount, category, description, date)
2. Add expenses
3. List all expenses
4. Show totals by category
5. Delete expenses

Here's the schema to get you started:

```python
cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        amount REAL NOT NULL,
        category TEXT NOT NULL,
        description TEXT,
        date TEXT DEFAULT CURRENT_TIMESTAMP
    )
""")
```

And here's the category summary query (a taste of SQL's power):

```python
cursor.execute("""
    SELECT category, 
           COUNT(*) as count, 
           SUM(amount) as total,
           AVG(amount) as average
    FROM expenses 
    GROUP BY category 
    ORDER BY total DESC
""")
```

Try doing *that* with a CSV file.

**Starter code:** [https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/sprint-4-pro/chapter-22-databases/](https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/sprint-4-pro/chapter-22-databases/)

## TL;DR

| Concept | What It Does |
|--|--|
| SQLite | File-based database, built into Python |
| `sqlite3.connect("file.db")` | Create/open a database |
| `cursor.execute(sql, params)` | Run a SQL command with safe parameters |
| `?` placeholders | Prevent SQL injection (ALWAYS use these) |
| `fetchone()` / `fetchall()` | Get query results |
| `conn.commit()` | Save changes to disk |
| `conn.row_factory = sqlite3.Row` | Access columns by name instead of index |
| `with sqlite3.connect() as conn:` | Auto-commit and auto-close |
| CRUD | Create (INSERT), Read (SELECT), Update (UPDATE), Delete (DELETE) |

**The one-sentence version:** Use `sqlite3` to store data in a real database file, always use `?` placeholders to prevent SQL injection, and use context managers for clean connections.

Next up: Web Scraping - where we teach Python to read websites and extract data.

---

# Chapter 23: Web Scraping - Extracting Data from the Web

> **Sprint 4, Chapter 23** | **Estimated Time: 20-25 minutes** | **Difficulty: Advanced**

## Why Should I Care?

Not everything has a nice, clean API. Sometimes the data you want is on a website but there's no API to access it. Price comparisons, news headlines, research data, job listings, product reviews, sports statistics - the data is right there on the page. You just need a way to grab it.

That's web scraping. And Python is ridiculously good at it.

Price monitoring tools that alert you when something goes on sale? Scrapers. Those "best flights" comparison sites? Scrapers. Academic researchers collecting data from hundreds of sources? Scrapers. Your future job listing dashboard project at the end of this sprint? Scraper.

## The Newspaper Analogy

APIs are like **politely asking for data**. You call the restaurant, place your order, and they deliver. Web scraping is like **reading the newspaper yourself and taking notes**. The information is published and public - you're just reading it programmatically instead of with your eyes.

Your Python script visits a web page (just like your browser does), reads the HTML (just like your browser does), and extracts the specific pieces you care about (which your browser shows visually, but you grab as data).

## HTML Basics: Just Enough to Scrape

You don't need to learn HTML deeply. You just need to understand enough to tell Python what to look for. Here's the crash course:

```html
<html>
  <head>
    <title>My Page</title>
  </head>
  <body>
    <h1>Welcome</h1>
    <p class="intro">This is a paragraph.</p>
    <div id="content">
      <a href="https://example.com">Click here</a>
      <ul>
        <li>Item 1</li>
        <li>Item 2</li>
        <li>Item 3</li>
      </ul>
    </div>
  </body>
</html>
```

The key concepts:
- **Tags** come in pairs: `<p>text</p>` (opening and closing)
- **Attributes** add info to tags: `<p class="intro">` has a `class` attribute
- **Nesting**: Tags contain other tags, forming a tree
- **id**: A unique identifier (one per page) - `id="content"`
- **class**: A group label (many elements can share one) - `class="intro"`

Common tags you'll encounter:
| Tag | Purpose |
|--|--|
| `<h1>` to `<h6>` | Headings |
| `<p>` | Paragraphs |
| `<a href="...">` | Links |
| `<div>` | Generic container |
| `<span>` | Inline container |
| `<ul>`, `<li>` | Unordered list and items |
| `<table>`, `<tr>`, `<td>` | Tables, rows, cells |
| `<img src="...">` | Images |

> **Don't Panic:** You don't need to learn HTML deeply. Just enough to tell Python what to look for. If you can read the five-line example above, you know enough to start scraping.

## The Workflow: requests + BeautifulSoup

Web scraping in Python uses two libraries:
1. **requests** - downloads the web page (you learned this in Chapter 21)
2. **BeautifulSoup** - parses the HTML and lets you search through it

Install BeautifulSoup:

```bash
pip install beautifulsoup4
```

Here's the basic pattern - you'll use this every single time:

```python
import requests
from bs4 import BeautifulSoup

# Step 1: Download the page
url = "https://quotes.toscrape.com/"
response = requests.get(url)

# Step 2: Parse the HTML
soup = BeautifulSoup(response.text, "html.parser")

# Step 3: Find what you want
title = soup.find("title")
print(title.text)  # Quotes to Scrape
```

Three steps. Download, parse, find. That's the entire workflow.

## Finding Elements: find() and find_all()

`find()` returns the **first** matching element. `find_all()` returns **all** matching elements as a list.

```python
import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Find the first quote
first_quote = soup.find("span", class_="text")
print(first_quote.text)
# "The world as we have created it is a process of our thinking..."

# Find ALL quotes
all_quotes = soup.find_all("span", class_="text")
for quote in all_quotes:
    print(quote.text)

# Find by id
# element = soup.find(id="specific-id")

# Find by multiple attributes
# element = soup.find("div", {"class": "content", "id": "main"})
```

Notice `class_` with an underscore - that's because `class` is a reserved word in Python. BeautifulSoup uses `class_` instead.

## Extracting Text and Attributes

Once you've found an element, you can extract its text content or its attributes:

```python
import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Get the text inside a tag
quote = soup.find("span", class_="text")
print(quote.text)       # The quote text
print(quote.string)     # Same thing for simple elements

# Get an attribute
link = soup.find("a")
print(link["href"])     # The URL the link points to
print(link.get("href")) # Same thing (safer - returns None if missing)

# Get all attributes as a dictionary
print(link.attrs)       # {'href': '/login', 'class': ['...'], ...}
```

## CSS Selectors: The Power Tool

`find()` and `find_all()` are great for simple searches. For more complex searches, use **CSS selectors** with `select()`:

```python
import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Select by class (use a dot)
quotes = soup.select(".text")

# Select by id (use a hash)
# header = soup.select_one("#header")

# Select by tag
paragraphs = soup.select("p")

# Select nested elements (parent > child)
# Authors that are inside quote divs
authors = soup.select(".quote .author")

# Select by attribute
# links = soup.select('a[href^="https"]')  # Links starting with https
```

Common CSS selector patterns:
| Selector | Meaning |
|--|--|
| `tag` | All elements of that type |
| `.class` | All elements with that class |
| `#id` | Element with that id |
| `parent child` | child anywhere inside parent |
| `parent > child` | Direct child only |
| `tag.class` | Tag with that class |

`select()` returns a list (like `find_all`). `select_one()` returns the first match (like `find`).

## A Complete Scraping Example

Let's scrape all quotes from quotes.toscrape.com with their authors and tags:

```python
import requests
from bs4 import BeautifulSoup

def scrape_quotes(url):
    """Scrape quotes from a page."""
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    
    soup = BeautifulSoup(response.text, "html.parser")
    quotes = []
    
    for quote_div in soup.find_all("div", class_="quote"):
        text = quote_div.find("span", class_="text").text
        author = quote_div.find("small", class_="author").text
        tags = [tag.text for tag in quote_div.find_all("a", class_="tag")]
        
        quotes.append({
            "text": text,
            "author": author,
            "tags": tags
        })
    
    return quotes

# Scrape page 1
quotes = scrape_quotes("https://quotes.toscrape.com/")
for q in quotes:
    print(f'"{q["text"][:60]}..."')
    print(f'  - {q["author"]}')
    print(f'  Tags: {", ".join(q["tags"])}')
    print()
```

## Handling Pagination

Most websites spread content across multiple pages. Here's how to scrape all of them:

```python
import requests
from bs4 import BeautifulSoup
import time

def scrape_all_quotes():
    """Scrape quotes from ALL pages."""
    base_url = "https://quotes.toscrape.com"
    all_quotes = []
    page_url = base_url + "/"
    
    while page_url:
        print(f"Scraping: {page_url}")
        response = requests.get(page_url, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Scrape quotes on this page
        for quote_div in soup.find_all("div", class_="quote"):
            text = quote_div.find("span", class_="text").text
            author = quote_div.find("small", class_="author").text
            all_quotes.append({"text": text, "author": author})
        
        # Find the "next" button
        next_button = soup.find("li", class_="next")
        if next_button:
            next_link = next_button.find("a")["href"]
            page_url = base_url + next_link
        else:
            page_url = None  # No more pages
        
        time.sleep(1)  # Be polite - wait between requests
    
    return all_quotes

all_quotes = scrape_all_quotes()
print(f"\nTotal quotes scraped: {len(all_quotes)}")
```

Key points:
- Look for a "next" link on each page
- Build the full URL by combining the base URL with the relative link
- **Always add a delay** (`time.sleep(1)`) between requests - hammering a server with rapid requests is rude and might get you blocked

## Saving Scraped Data

Once you've scraped the data, save it. Here are two approaches:

```python
import json
import csv

# Save as JSON
def save_as_json(data, filename):
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Saved {len(data)} items to {filename}")

# Save as CSV
def save_as_csv(data, filename):
    if not data:
        return
    
    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
    print(f"Saved {len(data)} items to {filename}")

# Or save to SQLite (Chapter 22!)
import sqlite3

def save_to_database(quotes, db_name="quotes.db"):
    with sqlite3.connect(db_name) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS quotes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                text TEXT NOT NULL,
                author TEXT NOT NULL
            )
        """)
        conn.executemany(
            "INSERT INTO quotes (text, author) VALUES (?, ?)",
            [(q["text"], q["author"]) for q in quotes]
        )
    print(f"Saved {len(quotes)} quotes to {db_name}")
```

See how the chapters build on each other? APIs from Chapter 21, databases from Chapter 22, and now scraping to feed data into both.

## Error Handling for Scraping

Web pages change. Elements disappear. Servers go down. Your scraper needs to handle all of this:

```python
import requests
from bs4 import BeautifulSoup
import time

def robust_scrape(url, max_retries=3):
    """Scrape a page with proper error handling."""
    
    for attempt in range(max_retries):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, "html.parser")
            
            # Safely extract data (use .text only if element exists)
            title_tag = soup.find("h1")
            title = title_tag.text if title_tag else "No title found"
            
            return {"title": title, "url": url}
            
        except requests.exceptions.Timeout:
            print(f"Timeout on attempt {attempt + 1}")
            time.sleep(2)
            
        except requests.exceptions.HTTPError as e:
            print(f"HTTP error: {e}")
            return None
            
        except requests.exceptions.ConnectionError:
            print("Connection failed. Check your internet.")
            return None
    
    print(f"Failed after {max_retries} attempts")
    return None
```

The most common scraping bug: assuming an element exists. Always check before calling `.text`:

```python
# This crashes if the element doesn't exist
title = soup.find("h1").text  # AttributeError if no <h1>

# This is safe
title_tag = soup.find("h1")
title = title_tag.text if title_tag else "Not found"
```

## Ethics and Legality: Can I Scrape This?

Before you scrape anything, ask yourself these questions:

**The "Can I Scrape This?" Decision Guide:**

1. **Is there an API?** Use it instead. APIs are faster, more reliable, and the site owner prefers it.

2. **Check robots.txt.** Visit `example.com/robots.txt` - it tells you what bots are allowed to access. Respect it.

```python
import requests

# Check what's allowed
response = requests.get("https://quotes.toscrape.com/robots.txt")
print(response.text)
```

3. **Check the Terms of Service.** Some sites explicitly prohibit scraping. Read the ToS.

4. **Don't overload the server.** Add delays between requests. Don't make hundreds of requests per second.

5. **Don't scrape personal data.** Scraping public information is generally okay. Scraping personal data (emails, phone numbers) raises legal and ethical issues.

6. **Is the data copyrighted?** You can scrape it for personal analysis, but republishing someone else's content is a different story.

**General rules:**
- Public data for personal/research use: Usually fine
- Adding delays and respecting robots.txt: Always do this
- Scraping behind a login wall: Gray area - be careful
- Scraping and republishing content: Probably not okay
- Overwhelming a server with requests: Never okay

> **Pro Tip:** quotes.toscrape.com was literally built for practicing web scraping. It's a sandbox. For your learning projects, use sites like this that are designed for scraping practice.

## Your Turn: Scrape Quotes from quotes.toscrape.com

**Challenge:** Build a complete quote scraper that:

1. Scrapes all quotes from all pages of quotes.toscrape.com
2. Extracts the quote text, author, and tags
3. Saves results to both a JSON file and a SQLite database
4. Handles errors gracefully
5. Includes a 1-second delay between page requests

Here's a skeleton to get you started:

```python
import requests
from bs4 import BeautifulSoup
import json
import sqlite3
import time

def scrape_page(url):
    """Scrape quotes from a single page."""
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    
    quotes = []
    for div in soup.find_all("div", class_="quote"):
        # TODO: Extract text, author, and tags
        pass
    
    # TODO: Find the next page URL (or None if last page)
    next_url = None
    
    return quotes, next_url

def scrape_all():
    """Scrape all pages and return all quotes."""
    url = "https://quotes.toscrape.com/"
    all_quotes = []
    
    while url:
        print(f"Scraping: {url}")
        quotes, url = scrape_page(url)
        all_quotes.extend(quotes)
        if url:
            time.sleep(1)
    
    return all_quotes

if __name__ == "__main__":
    quotes = scrape_all()
    print(f"Scraped {len(quotes)} quotes!")
    
    # Save to JSON
    with open("quotes.json", "w") as f:
        json.dump(quotes, f, indent=2)
    
    # Save to SQLite (use what you learned in Chapter 22!)
```

**Starter code:** [https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/sprint-4-pro/chapter-23-scraping/](https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/sprint-4-pro/chapter-23-scraping/)

## TL;DR

| Concept | What It Does |
|--|--|
| `requests.get(url)` | Downloads a web page |
| `BeautifulSoup(html, "html.parser")` | Parses HTML into a searchable tree |
| `soup.find(tag, class_=...)` | Find the first matching element |
| `soup.find_all(tag, class_=...)` | Find all matching elements |
| `soup.select("css selector")` | Find elements using CSS selectors |
| `element.text` | Get the text inside an element |
| `element["attribute"]` | Get an attribute value |
| `time.sleep(1)` | Be polite - wait between requests |
| `robots.txt` | Check what the site allows you to scrape |

**The one-sentence version:** Use `requests` to download a web page and `BeautifulSoup` to search through its HTML and extract the data you need, always being respectful of the site's rules and server resources.

Next up: Testing - where we learn to prove our code actually works.

---

# Chapter 24: Testing - Proving Your Code Works

> **Sprint 4, Chapter 24** | **Estimated Time: 20-25 minutes** | **Difficulty: Advanced**

## Why Should I Care?

Picture this. It's Friday at 4:45 PM. You push a "small change" to production. You head home feeling productive. At 6 PM, your phone starts buzzing. The signup page is broken. New users can't create accounts. Your "small change" had a typo in the email validation function. Thousands of potential users hit an error page over the weekend.

A single test would have caught it.

"It works on my machine" isn't good enough. Tests catch bugs before your users do. They let you change code without fear. They're the difference between "I think this works" and "I know this works."

Every serious software company requires tests. Every open-source project worth using has tests. If you want to write professional code, you need to write tests.

## The Proofreading Analogy

Testing is like **proofreading an essay**. You could skip it - the essay is done, the ideas are there. But do you really want to submit it with typos, missing paragraphs, and your introduction accidentally pasted in twice?

You *could* proofread by reading the whole thing yourself. That's manual testing - running your program and clicking around. It works, but it's slow, tedious, and you'll miss things because you're human.

Automated tests are like having a robot proofreader that checks every word, every sentence, every paragraph, instantly, every time you make a change. It never gets tired. It never misses the same mistake twice.

## A Bug That Testing Would Have Caught

Let's look at a real example. Here's a discount calculator:

```python
def apply_discount(price, discount_percent):
    """Apply a percentage discount to a price."""
    return price - (price * discount_percent / 100)
```

Looks fine, right? Let's use it:

```python
print(apply_discount(100, 20))  # 80.0 - correct!
print(apply_discount(50, 10))   # 45.0 - correct!
```

Ship it! But wait... what about edge cases?

```python
print(apply_discount(100, 110))  # -10.0 - negative price?!
print(apply_discount(-50, 20))   # -40.0 - negative input?!
print(apply_discount(100, 0))    # 100.0 - okay
print(apply_discount(0, 50))     # 0.0 - okay
```

A 110% discount gives a **negative price** - the store pays the customer. That's a bug. If you had a test that checked "discount should not exceed 100%", you'd have caught it before deploying.

Here's the fixed version:

```python
def apply_discount(price, discount_percent):
    """Apply a percentage discount to a price."""
    if price < 0:
        raise ValueError("Price cannot be negative")
    if not 0 <= discount_percent <= 100:
        raise ValueError("Discount must be between 0 and 100")
    return price - (price * discount_percent / 100)
```

Now let's write tests that *prove* this works correctly.

## unittest: The Built-In Way (Brief)

Python comes with a testing framework called `unittest`. It works, but it's verbose:

```python
import unittest

class TestApplyDiscount(unittest.TestCase):
    def test_basic_discount(self):
        self.assertEqual(apply_discount(100, 20), 80.0)
    
    def test_zero_discount(self):
        self.assertEqual(apply_discount(100, 0), 100.0)
    
    def test_full_discount(self):
        self.assertEqual(apply_discount(100, 100), 0.0)
    
    def test_negative_price_raises_error(self):
        with self.assertRaises(ValueError):
            apply_discount(-50, 20)

if __name__ == "__main__":
    unittest.main()
```

It works, but all that `self.assertEqual`, `self.assertRaises`, and class boilerplate gets old fast. There's a better way.

## pytest: The Modern Way

**pytest** is the testing framework that professional Python developers actually use. It's simpler, more powerful, and more readable. Install it:

```bash
pip install pytest
```

Here's the same test, written with pytest:

```python
import pytest

def apply_discount(price, discount_percent):
    if price < 0:
        raise ValueError("Price cannot be negative")
    if not 0 <= discount_percent <= 100:
        raise ValueError("Discount must be between 0 and 100")
    return price - (price * discount_percent / 100)

def test_basic_discount():
    assert apply_discount(100, 20) == 80.0

def test_zero_discount():
    assert apply_discount(100, 0) == 100.0

def test_full_discount():
    assert apply_discount(100, 100) == 0.0

def test_negative_price_raises_error():
    with pytest.raises(ValueError):
        apply_discount(-50, 20)

def test_discount_over_100_raises_error():
    with pytest.raises(ValueError):
        apply_discount(100, 110)
```

No classes. No `self.assertEqual`. Just `assert` - Python's built-in keyword. pytest discovers functions that start with `test_` and runs them automatically.

Run your tests:

```bash
pytest test_discount.py -v
```

Output:
```
test_discount.py::test_basic_discount PASSED
test_discount.py::test_zero_discount PASSED
test_discount.py::test_full_discount PASSED
test_discount.py::test_negative_price_raises_error PASSED
test_discount.py::test_discount_over_100_raises_error PASSED

============= 5 passed in 0.02s =============
```

Five green checkmarks. That's the feeling you're chasing.

> **Don't Panic:** Testing feels like extra work. It is. But it's the kind of extra work that saves you hours of debugging later. Think of it as an investment: 5 minutes writing tests now saves 2 hours debugging at midnight.

## Writing Good Test Cases

Good tests follow the **AAA pattern**: Arrange, Act, Assert.

```python
def test_discount_calculation():
    # Arrange - set up the inputs
    price = 100
    discount = 20
    
    # Act - call the function
    result = apply_discount(price, discount)
    
    # Assert - check the result
    assert result == 80.0
```

What makes a good test?

1. **Test one thing.** Each test should check a single behavior.
2. **Use descriptive names.** `test_negative_price_raises_error` tells you exactly what it tests.
3. **Test edge cases.** Zero, negative numbers, empty strings, `None`, very large numbers.
4. **Test both success and failure.** Don't just test that correct inputs work - test that incorrect inputs fail properly.
5. **Tests should be independent.** Each test should work alone, not depend on other tests running first.

Here's a complete test suite for a password strength checker:

```python
import pytest

def check_password_strength(password):
    """Return 'weak', 'medium', or 'strong'."""
    if len(password) < 8:
        return "weak"
    
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*()_+-=" for c in password)
    
    score = sum([has_upper, has_lower, has_digit, has_special])
    
    if score >= 3 and len(password) >= 12:
        return "strong"
    elif score >= 2:
        return "medium"
    else:
        return "weak"

# -- Tests --

def test_short_password_is_weak():
    assert check_password_strength("abc") == "weak"

def test_empty_password_is_weak():
    assert check_password_strength("") == "weak"

def test_only_lowercase_is_weak():
    assert check_password_strength("abcdefgh") == "weak"

def test_mixed_case_and_digits_is_medium():
    assert check_password_strength("Abcdefg1") == "medium"

def test_strong_password():
    assert check_password_strength("MyP@ssw0rd2024") == "strong"

def test_long_with_variety_is_strong():
    assert check_password_strength("Hello!World9") == "strong"
```

> **Remember When?** Remember the password checker from Chapter 10? Perfect candidate for tests. If you built it then, go back and add tests now. Future you will thank you.

## Fixtures: Reusable Test Setup

Sometimes multiple tests need the same setup. **Fixtures** provide that:

```python
import pytest
import sqlite3

@pytest.fixture
def sample_users():
    """Provide sample user data for tests."""
    return [
        {"name": "Alice", "email": "alice@test.com", "age": 28},
        {"name": "Bob", "email": "bob@test.com", "age": 34},
        {"name": "Charlie", "email": "charlie@test.com", "age": 22},
    ]

@pytest.fixture
def db_connection():
    """Create a test database that's cleaned up after each test."""
    conn = sqlite3.connect(":memory:")  # In-memory database
    conn.execute("""
        CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            age INTEGER
        )
    """)
    yield conn  # This is where the test runs
    conn.close()  # Cleanup after the test

def test_insert_user(db_connection, sample_users):
    """Test inserting a user into the database."""
    user = sample_users[0]
    db_connection.execute(
        "INSERT INTO users (name, email, age) VALUES (?, ?, ?)",
        (user["name"], user["email"], user["age"])
    )
    
    result = db_connection.execute("SELECT * FROM users").fetchone()
    assert result[1] == "Alice"
    assert result[2] == "alice@test.com"

def test_unique_email_constraint(db_connection):
    """Test that duplicate emails are rejected."""
    db_connection.execute(
        "INSERT INTO users (name, email, age) VALUES (?, ?, ?)",
        ("Alice", "same@test.com", 28)
    )
    
    with pytest.raises(sqlite3.IntegrityError):
        db_connection.execute(
            "INSERT INTO users (name, email, age) VALUES (?, ?, ?)",
            ("Bob", "same@test.com", 34)
        )
```

Key fixture concepts:
- `@pytest.fixture` marks a function as a fixture
- Tests receive fixtures by including them as parameters (pytest handles the wiring)
- `yield` lets you do cleanup after the test
- `:memory:` SQLite databases are perfect for testing - they're fast and auto-delete

## Parametrize: Many Inputs, One Test

Instead of writing separate tests for every input, use `@pytest.mark.parametrize`:

```python
import pytest

def is_even(n):
    return n % 2 == 0

@pytest.mark.parametrize("number, expected", [
    (0, True),
    (1, False),
    (2, True),
    (3, False),
    (-2, True),
    (-3, False),
    (100, True),
])
def test_is_even(number, expected):
    assert is_even(number) == expected
```

One test function, seven test cases. pytest runs each one separately and reports which (if any) fail. This is incredibly powerful for testing functions with many possible inputs.

```python
@pytest.mark.parametrize("password, expected_strength", [
    ("", "weak"),
    ("abc", "weak"),
    ("abcdefgh", "weak"),
    ("Abcdefg1", "medium"),
    ("MyP@ssw0rd2024", "strong"),
])
def test_password_strength(password, expected_strength):
    assert check_password_strength(password) == expected_strength
```

## TDD: Test-Driven Development (The Red-Green-Refactor Cycle)

TDD flips the script: you write the test **before** you write the code.

The cycle:

1. **Red:** Write a test that fails (because the code doesn't exist yet)
2. **Green:** Write the simplest code that makes the test pass
3. **Refactor:** Clean up the code while keeping tests green

Let's try it. We want a function that converts temperatures:

**Step 1: Red - Write the test first**

```python
def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(100) == 212
    assert celsius_to_fahrenheit(-40) == -40

def test_fahrenheit_to_celsius():
    assert fahrenheit_to_celsius(32) == 0
    assert fahrenheit_to_celsius(212) == 100
    assert fahrenheit_to_celsius(-40) == -40
```

Run pytest: **FAIL** (functions don't exist yet). Red.

**Step 2: Green - Write the minimum code**

```python
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
```

Run pytest: **PASS**. Green.

**Step 3: Refactor - Improve if needed**

Maybe add input validation, type hints, or docstrings. Run tests after each change to make sure nothing breaks.

TDD feels backward at first. But it forces you to think about what your code should do *before* you write it, and it guarantees you have tests when you're done.

## Organizing Your Tests

For a real project, keep tests in a separate directory:

```
my_project/
    src/
        calculator.py
        password_checker.py
    tests/
        test_calculator.py
        test_password_checker.py
```

Name your test files `test_*.py` and your test functions `test_*`. pytest finds them automatically. Just run:

```bash
# Run all tests
pytest

# Run tests in a specific file
pytest tests/test_calculator.py

# Run a specific test
pytest tests/test_calculator.py::test_basic_discount

# Run with verbose output
pytest -v

# Run and stop at first failure
pytest -x

# Run tests matching a keyword
pytest -k "password"
```

## Bonus: Testing with Coverage

Want to know how much of your code is tested? Use `pytest-cov`:

```bash
pip install pytest-cov

pytest -cov=src -cov-report=term-missing
```

Output:
```
Name                    Stmts   Miss  Cover   Missing
---------------------------
src/calculator.py          10      0   100%
src/password_checker.py    15      3    80%   22-24
---------------------------
TOTAL                      25      3    88%
```

This tells you that lines 22-24 of `password_checker.py` aren't tested. Go write a test for those lines.

100% coverage isn't always necessary, but aiming for 80%+ is a good habit.

## Your Turn: Write Tests for Password Strength Checker

**Challenge:** Write a complete test suite for the password strength checker. Include:

1. Tests for weak passwords (too short, only lowercase)
2. Tests for medium passwords (mixed case with digits)
3. Tests for strong passwords (long with variety)
4. Tests for edge cases (empty string, very long password, only special characters)
5. Use `@pytest.mark.parametrize` for at least one test
6. Use a fixture to provide sample passwords

```python
# test_password.py
import pytest

# Import your password checker
from password_checker import check_password_strength

@pytest.fixture
def common_passwords():
    """Common passwords that should all be rated 'weak'."""
    return ["password", "12345678", "qwerty123", "letmein!!"]

@pytest.mark.parametrize("password, expected", [
    # Add your test cases here
])
def test_password_strength(password, expected):
    assert check_password_strength(password) == expected

def test_common_passwords_are_weak(common_passwords):
    for password in common_passwords:
        result = check_password_strength(password)
        # What should this assert?
```

**Starter code:** [https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/sprint-4-pro/chapter-24-testing/](https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/sprint-4-pro/chapter-24-testing/)

## TL;DR

| Concept | What It Does |
|--|--|
| `pytest` | Modern testing framework for Python |
| `assert` | Check that something is true (test fails if not) |
| `pytest.raises(Error)` | Test that code raises a specific exception |
| `@pytest.fixture` | Reusable test setup (and cleanup) |
| `@pytest.mark.parametrize` | Run one test with many different inputs |
| TDD (Red-Green-Refactor) | Write test first, then code, then clean up |
| `pytest -v` | Run tests with detailed output |
| `pytest -cov` | Check how much code your tests cover |

**The one-sentence version:** Write functions that start with `test_`, use `assert` to check results, and run `pytest` to automatically discover and execute all your tests.

Next up: Type Hints, Linting & Clean Code - the chapter that turns your code from "it works" to "it's professional."

---

# Chapter 25: Type Hints, Linting & Clean Code

> **Sprint 4, Chapter 25** | **Estimated Time: 15-20 minutes** | **Difficulty: Advanced**

## Why Should I Care?

You can write Python that works but is impossible to read. You can write functions where nobody - including you in two weeks - knows what types the parameters should be. You can write code that's inconsistently formatted, full of unused imports, and structured like a bowl of spaghetti.

And it'll still run. Python doesn't care.

But your teammates care. Your future self cares. The hiring manager reviewing your GitHub portfolio cares. Code readability, team collaboration, catching bugs early, and getting hired - clean code matters for all of these.

This chapter gives you the tools that professional developers use to write code that's not just correct, but *clear*.

## The Kitchen Analogy

Writing clean code is like keeping a clean kitchen. You CAN cook in a messy kitchen. The food tastes the same. But everything takes longer - you can't find the spatula, the cutting board is buried under dishes, and you accidentally grab the sugar instead of the salt.

A clean kitchen means you cook faster, make fewer mistakes, and other people can jump in and help.

Clean code is the same. Variables have clear names. Functions do one thing. Types are documented. Formatting is consistent. Anyone can read it, understand it, and modify it.

## Type Hints: Helping Your Future Self

Python is dynamically typed - you don't have to declare what type a variable is. That's great for quick scripts. But in larger projects, it becomes a problem:

```python
# What does this function expect? What does it return?
def process(data, flag):
    ...
```

Is `data` a string? A list? A dictionary? Is `flag` a boolean? An integer? A string? You'd have to read the entire function to find out.

**Type hints** fix this:

```python
def process(data: list[str], flag: bool) -> dict[str, int]:
    ...
```

Now you know instantly: `data` is a list of strings, `flag` is a boolean, and it returns a dictionary mapping strings to integers. No guessing.

### Basic Type Hints

```python
# Variable annotations
name: str = "Alice"
age: int = 28
price: float = 19.99
active: bool = True

# Function annotations
def greet(name: str) -> str:
    return f"Hello, {name}!"

def add(a: int, b: int) -> int:
    return a + b

def is_valid(email: str) -> bool:
    return "@" in email
```

The syntax is simple: `variable: type` for variables, `parameter: type` for function parameters, and `-> type` for return values.

### Collection Types

```python
# Lists, dicts, sets, tuples
def average(numbers: list[float]) -> float:
    return sum(numbers) / len(numbers)

def count_words(text: str) -> dict[str, int]:
    words = text.split()
    return {word: words.count(word) for word in set(words)}

def unique_names(names: list[str]) -> set[str]:
    return set(names)

def get_point() -> tuple[float, float]:
    return (3.14, 2.71)
```

### Optional and Union Types

```python
from typing import Optional

# This parameter might be None
def find_user(user_id: int) -> Optional[dict]:
    """Returns user dict or None if not found."""
    # ...
    return None

# A parameter that accepts multiple types (Python 3.10+)
def display(value: str | int) -> str:
    return str(value)

# For older Python versions
from typing import Union
def display(value: Union[str, int]) -> str:
    return str(value)
```

### Type Hints for Complex Functions

```python
from typing import Callable, Any

# Function that takes a callback
def retry(func: Callable, max_attempts: int = 3) -> Any:
    for attempt in range(max_attempts):
        try:
            return func()
        except Exception:
            if attempt == max_attempts - 1:
                raise

# Function with default values
def create_user(
    name: str,
    email: str,
    age: int = 0,
    active: bool = True
) -> dict[str, Any]:
    return {
        "name": name,
        "email": email,
        "age": age,
        "active": active
    }
```

### Important: Type Hints Don't Enforce Anything

Here's the thing - Python **ignores** type hints at runtime. They're documentation, not enforcement:

```python
def add(a: int, b: int) -> int:
    return a + b

# This "works" even though we pass strings
print(add("hello", " world"))  # "hello world"
```

No error. Python doesn't check types at runtime. Type hints are for **humans** and **tools** (like mypy, which we'll cover next).

> **Wait, What?** "If Python ignores them, why bother?" Because *you* don't ignore them. Your IDE doesn't ignore them. Your linter doesn't ignore them. Type hints catch bugs in your editor before you even run the code. They're like lane markings on a road - your car can cross them, but they tell you where you should be.

## mypy: The Type Checker

**mypy** is a tool that reads your type hints and checks them *before* you run your code. It catches type-related bugs at development time.

```bash
pip install mypy
```

Create a file called `calculator.py`:

```python
def add(a: int, b: int) -> int:
    return a + b

def divide(a: float, b: float) -> float:
    return a / b

# These lines have type errors
result: str = add(1, 2)          # Bug: int assigned to str
divide("10", 3)                   # Bug: str passed where float expected
```

Run mypy:

```bash
mypy calculator.py
```

Output:
```
calculator.py:8: error: Incompatible types in assignment
    (expression has type "int", variable has type "str")
calculator.py:9: error: Argument 1 to "divide" has incompatible type "str";
    expected "float"
Found 2 errors in 1 file
```

mypy found both bugs without running the code. In a large project, this catches errors that would otherwise slip through to production.

## PEP 8: Python's Style Guide

**PEP 8** is the official style guide for Python code. It was written by Guido van Rossum (Python's creator). Yes, there's an official opinion on whether to use tabs or spaces. (Spaces. Always spaces. Four of them.)

The key PEP 8 rules:

```python
# -- NAMING --

# Variables and functions: snake_case
user_name = "Alice"
def calculate_total():
    pass

# Classes: PascalCase
class ShoppingCart:
    pass

# Constants: UPPER_SNAKE_CASE
MAX_RETRIES = 3
DATABASE_URL = "sqlite:///app.db"

# -- SPACING --

# Two blank lines before top-level definitions
def function_one():
    pass


def function_two():
    pass


class MyClass:
    # One blank line between methods
    def method_one(self):
        pass
    
    def method_two(self):
        pass

# -- LINE LENGTH --

# Keep lines under 79 characters (or 88 with black)
# Break long lines like this:
result = (first_value
          + second_value
          + third_value)

# Or for function calls:
user = create_user(
    name="Alice",
    email="alice@example.com",
    age=28
)

# -- IMPORTS --

# Standard library first, then third-party, then local
import os
import sys

import requests
from bs4 import BeautifulSoup

from my_project.utils import helper
```

> **Fun Fact:** PEP stands for "Python Enhancement Proposal." PEP 8 was written in 2001 and has been the de facto standard ever since. The tabs-vs-spaces debate is officially settled in Python: four spaces. And yes, there was a whole episode of *Silicon Valley* about this.

## black: The Code Formatter That Ends All Arguments

Arguing about code formatting is a waste of time. **black** formats your code automatically, and it's opinionated - it makes the decisions so you don't have to.

```bash
pip install black
```

Before black:

```python
# Messy formatting
x={'name':'Alice','age':28,'scores':[90,85,92]}
def   calculate(  a,b,  c  ):
    return(a+b  *c)
result=calculate(1,2,    3)
if result>5 :
        print(  "big")
```

Run black:

```bash
black messy_code.py
```

After black:

```python
# Clean, consistent formatting
x = {"name": "Alice", "age": 28, "scores": [90, 85, 92]}


def calculate(a, b, c):
    return a + b * c


result = calculate(1, 2, 3)
if result > 5:
    print("big")
```

That's it. No configuration needed. No arguments about style. black decides, and everyone on the team uses the same format.

You can also check without modifying:

```bash
black -check my_file.py     # Check without changing
black -diff my_file.py      # Show what would change
black my_project/             # Format an entire directory
```

Most teams add black to their CI/CD pipeline so code is automatically formatted on every commit.

## pylint and flake8: The Grammar Checkers for Code

**Linters** analyze your code for potential errors, style violations, and suspicious patterns - like a grammar checker for code.

### flake8 (Lighter, Faster)

```bash
pip install flake8
```

```python
# sample.py
import os
import sys
import json  # Unused import

def bad_function(x,y):
    result = x+y
    unused_variable = 42
    if result == True:
        print ("hello")
    return result
```

```bash
flake8 sample.py
```

Output:
```
sample.py:3:1: F401 'json' imported but unused
sample.py:5:20: E231 missing whitespace after ','
sample.py:6:14: E225 missing whitespace around operator
sample.py:7:5: F841 local variable 'unused_variable' is assigned but never used
sample.py:8:8: E712 comparison to True should be 'if result:' or 'if result is True:'
sample.py:9:14: E211 whitespace before '('
```

Every issue identified with a specific code and line number.

### pylint (More Thorough, More Opinionated)

```bash
pip install pylint
```

pylint is stricter and catches more issues, including missing docstrings, too many arguments, and code complexity:

```bash
pylint sample.py
```

pylint gives your code a score out of 10. Aim for 8+.

### Which One Should You Use?

- **flake8** for quick style checks (most projects use this)
- **pylint** for thorough analysis (useful but noisy)
- **black** + **flake8** is the most common combination

## Before and After: Clean Code in Practice

Let's see a real transformation. Here's a function written quickly without thinking about cleanliness:

### Before

```python
def p(d):
    t = 0
    for i in d:
        t = t + i['a'] * (1 + i['r'])
    return t

data = [{'a': 100, 'r': 0.08}, {'a': 250, 'r': 0.1}, {'a': 50, 'r': 0.05}]
print(p(data))
```

What does this do? Who knows. Let's clean it up.

### After

```python
def calculate_total_with_tax(items: list[dict[str, float]]) -> float:
    """Calculate the total price of items including tax.
    
    Args:
        items: List of dicts with 'amount' and 'tax_rate' keys.
        
    Returns:
        Total price including tax for all items.
    """
    total = 0.0
    for item in items:
        total += item["amount"] * (1 + item["tax_rate"])
    return round(total, 2)


items = [
    {"amount": 100.00, "tax_rate": 0.08},
    {"amount": 250.00, "tax_rate": 0.10},
    {"amount": 50.00, "tax_rate": 0.05},
]

total = calculate_total_with_tax(items)
print(f"Total with tax: ${total}")
```

Same logic. Completely different readability. Changes made:
- Function name describes what it does
- Parameter names are descriptive
- Type hints tell you what goes in and what comes out
- Docstring explains the purpose
- Variable names have meaning (`total` not `t`, `item` not `i`)
- Output is formatted nicely

### Another Before and After

```python
# Before: A mess
def check(u, p):
    if len(p) < 8:
        return False
    if u == "":
        return False
    for c in "!@#$%":
        if c in p:
            return True
    return False
```

```python
# After: Professional
def validate_credentials(username: str, password: str) -> bool:
    """Check if username and password meet security requirements.
    
    Requirements:
        - Username must not be empty
        - Password must be at least 8 characters
        - Password must contain at least one special character
    """
    SPECIAL_CHARACTERS = "!@#$%"
    
    if not username:
        return False
    
    if len(password) < 8:
        return False
    
    has_special = any(char in SPECIAL_CHARACTERS for char in password)
    return has_special
```

## Putting It All Together: Your Clean Code Workflow

Here's the workflow professional developers use:

1. **Write code** with type hints and descriptive names
2. **Format** with black (`black my_file.py`)
3. **Lint** with flake8 (`flake8 my_file.py`)
4. **Type check** with mypy (`mypy my_file.py`)
5. **Test** with pytest (`pytest`)

Or automate it all. Most projects use a `Makefile` or scripts:

```bash
# Run everything at once
black src/ tests/
flake8 src/ tests/
mypy src/
pytest
```

Many developers configure their IDE to run black on save and show flake8/mypy warnings inline. VS Code does this beautifully with the Python extension.

## IDE Integration: Let Your Editor Help

If you use VS Code (and you should), install the Python extension and add this to your settings:

```json
{
    "python.formatting.provider": "black",
    "editor.formatOnSave": true,
    "python.linting.flake8Enabled": true,
    "python.linting.mypyEnabled": true
}
```

Now your code formats itself every time you save, and type errors show up as red squiggly lines. It's like having a co-pilot who catches your mistakes in real time.

## Your Turn: Add Type Hints and Linting to Expense Tracker

**Challenge:** Take the expense tracker from Chapter 22 and make it professional:

1. Add type hints to every function
2. Add docstrings to every function
3. Run black to format the code
4. Run flake8 and fix all warnings
5. Run mypy and fix all type errors

Here's what the refactored functions should look like:

```python
import sqlite3
from typing import Optional

DB_NAME: str = "expenses.db"


def add_expense(
    amount: float,
    category: str,
    description: str = ""
) -> int:
    """Add a new expense and return its ID.
    
    Args:
        amount: The expense amount (must be positive).
        category: Expense category (e.g., 'food', 'transport').
        description: Optional description of the expense.
        
    Returns:
        The ID of the newly created expense.
        
    Raises:
        ValueError: If amount is not positive.
    """
    if amount <= 0:
        raise ValueError("Amount must be positive")
    
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.execute(
            "INSERT INTO expenses (amount, category, description) VALUES (?, ?, ?)",
            (amount, category, description),
        )
        return cursor.lastrowid


def get_expenses(
    category: Optional[str] = None,
    limit: int = 50
) -> list[dict[str, object]]:
    """Retrieve expenses, optionally filtered by category.
    
    Args:
        category: If provided, only return expenses in this category.
        limit: Maximum number of expenses to return.
        
    Returns:
        List of expense dictionaries.
    """
    with sqlite3.connect(DB_NAME) as conn:
        conn.row_factory = sqlite3.Row
        if category:
            rows = conn.execute(
                "SELECT * FROM expenses WHERE category = ? ORDER BY date DESC LIMIT ?",
                (category, limit),
            ).fetchall()
        else:
            rows = conn.execute(
                "SELECT * FROM expenses ORDER BY date DESC LIMIT ?",
                (limit,),
            ).fetchall()
        return [dict(row) for row in rows]
```

**Starter code:** [https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/sprint-4-pro/chapter-25-clean-code/](https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/sprint-4-pro/chapter-25-clean-code/)

## TL;DR

| Tool | What It Does |
|--|--|
| Type hints (`x: int`) | Document what types your code expects |
| mypy | Check type hints for errors without running code |
| PEP 8 | Python's official style guide |
| black | Auto-format code (no configuration needed) |
| flake8 | Check for style violations and common errors |
| pylint | Thorough code analysis (more detailed than flake8) |

**The one-sentence version:** Use type hints to document your code's expectations, black to format it consistently, flake8 to catch mistakes, and mypy to verify types - these tools turn "code that works" into "code that's professional."

Next up: The Sprint 4 Checkpoint project - where you put everything from this sprint together into a real application.

---

# Sprint 4 Checkpoint: Job Listing Scraper & Dashboard

> **Estimated Time: 2-3 hours** | **Difficulty: Advanced** | **This is your masterpiece for Sprint 4**

Sprint 4 complete. Take a second and think about what you just learned: decorators, generators, APIs, databases, web scraping, testing, and clean code practices. Those aren't beginner topics. Those are the tools that professional Python developers use every single day.

**You now have the toolkit of a working developer.** Not a student. Not a hobbyist. A developer.

Let's prove it by building something real.

## The Project: Job Listing Scraper & Dashboard

You're going to build a complete application that scrapes job listings from the web, stores them in a database, provides a search interface, and includes a full test suite. Every chapter in this sprint feeds directly into this project.

Here's what you'll build:

1. **Scraper** - Collect job listings from a practice website (Chapter 23)
2. **Database** - Store listings in SQLite with proper schema (Chapter 22)
3. **Search Engine** - Query and filter listings (Chapter 22)
4. **API Client** - Fetch additional data from a public API (Chapter 21)
5. **Data Pipeline** - Process listings efficiently with generators (Chapter 20)
6. **Utilities** - Decorated helper functions for timing and logging (Chapter 19)
7. **Test Suite** - Prove it all works with pytest (Chapter 24)
8. **Clean Code** - Type hints, formatting, and linting throughout (Chapter 25)

## Skills Map

| Project Component | Chapter |
|--|--|
| `@timer` and `@logger` decorators | Chapter 19: Decorators |
| Generator-based data pipeline | Chapter 20: Generators |
| Fetching salary data from an API | Chapter 21: APIs |
| SQLite database for job listings | Chapter 22: Databases |
| Scraping job listings from HTML | Chapter 23: Web Scraping |
| pytest test suite with fixtures | Chapter 24: Testing |
| Type hints and black formatting | Chapter 25: Clean Code |

## Project Structure

```
job_scraper/
    scraper.py          # Web scraping logic
    database.py         # SQLite database operations
    api_client.py       # External API integration
    pipeline.py         # Generator-based data processing
    utils.py            # Decorators and helper functions
    dashboard.py        # Search and display interface
    main.py             # Entry point - ties everything together
    tests/
        test_scraper.py
        test_database.py
        test_pipeline.py
        test_utils.py
```

## Step-by-Step Build Guide

### Step 1: Set Up the Project (5 minutes)

Create the project structure and install dependencies:

```bash
mkdir job_scraper
cd job_scraper
mkdir tests

pip install requests beautifulsoup4 pytest black flake8 mypy
```

### Step 2: Build the Decorators (utils.py) - Chapter 19

Start with your utility decorators. You'll use these throughout the project:

```python
# utils.py
import functools
import time
from typing import Any, Callable


def timer(func: Callable) -> Callable:
    """Log how long a function takes to execute."""
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"[TIMER] {func.__name__} took {elapsed:.2f}s")
        return result
    return wrapper


def logger(func: Callable) -> Callable:
    """Log function calls with arguments and return values."""
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        args_str = ", ".join([repr(a) for a in args])
        kwargs_str = ", ".join([f"{k}={repr(v)}" for k, v in kwargs.items()])
        all_args = ", ".join(filter(None, [args_str, kwargs_str]))
        print(f"[LOG] Calling {func.__name__}({all_args})")
        result = func(*args, **kwargs)
        print(f"[LOG] {func.__name__} returned {type(result).__name__}")
        return result
    return wrapper


def retry(max_attempts: int = 3, delay: float = 1.0) -> Callable:
    """Retry a function if it raises an exception."""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts:
                        raise
                    print(f"[RETRY] Attempt {attempt} failed: {e}")
                    time.sleep(delay)
        return wrapper
    return decorator
```

### Step 3: Build the Database Layer (database.py) - Chapter 22

```python
# database.py
import sqlite3
from typing import Optional

DB_NAME: str = "jobs.db"


def get_connection() -> sqlite3.Connection:
    """Get a database connection with row factory enabled."""
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def create_tables() -> None:
    """Create the jobs table if it doesn't exist."""
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS jobs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                company TEXT NOT NULL,
                location TEXT,
                description TEXT,
                url TEXT UNIQUE,
                scraped_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
        """)


def insert_job(
    title: str,
    company: str,
    location: str = "",
    description: str = "",
    url: str = ""
) -> Optional[int]:
    """Insert a job listing. Returns the job ID or None if duplicate."""
    try:
        with get_connection() as conn:
            cursor = conn.execute(
                """INSERT INTO jobs (title, company, location, description, url)
                   VALUES (?, ?, ?, ?, ?)""",
                (title, company, location, description, url),
            )
            return cursor.lastrowid
    except sqlite3.IntegrityError:
        return None  # Duplicate URL


def search_jobs(
    keyword: str = "",
    location: str = "",
    limit: int = 20
) -> list[dict]:
    """Search jobs by keyword and/or location."""
    with get_connection() as conn:
        query = "SELECT * FROM jobs WHERE 1=1"
        params: list = []

        if keyword:
            query += " AND (title LIKE ? OR description LIKE ?)"
            params.extend([f"%{keyword}%", f"%{keyword}%"])

        if location:
            query += " AND location LIKE ?"
            params.append(f"%{location}%")

        query += " ORDER BY scraped_at DESC LIMIT ?"
        params.append(limit)

        rows = conn.execute(query, params).fetchall()
        return [dict(row) for row in rows]


def get_job_count() -> int:
    """Get the total number of jobs in the database."""
    with get_connection() as conn:
        result = conn.execute("SELECT COUNT(*) FROM jobs").fetchone()
        return result[0]


def get_companies() -> list[dict]:
    """Get all companies with their job counts."""
    with get_connection() as conn:
        rows = conn.execute("""
            SELECT company, COUNT(*) as job_count
            FROM jobs
            GROUP BY company
            ORDER BY job_count DESC
        """).fetchall()
        return [dict(row) for row in rows]
```

### Step 4: Build the Scraper (scraper.py) - Chapter 23

For this project, we'll scrape from a practice site. You can adapt this to any job board:

```python
# scraper.py
import requests
from bs4 import BeautifulSoup
import time
from typing import Optional
from utils import timer, retry


@retry(max_attempts=3, delay=2.0)
def fetch_page(url: str) -> Optional[str]:
    """Fetch a web page and return its HTML content."""
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.text


def parse_job_listings(html: str) -> list[dict[str, str]]:
    """Parse job listings from HTML content."""
    soup = BeautifulSoup(html, "html.parser")
    jobs: list[dict[str, str]] = []

    # Adapt these selectors to your target site
    for listing in soup.find_all("div", class_="quote"):
        title_tag = listing.find("span", class_="text")
        company_tag = listing.find("small", class_="author")
        tags = listing.find_all("a", class_="tag")

        if title_tag and company_tag:
            jobs.append({
                "title": title_tag.text.strip(),
                "company": company_tag.text.strip(),
                "location": "Remote",
                "description": ", ".join(tag.text for tag in tags),
                "url": "",
            })

    return jobs


def get_next_page_url(html: str, base_url: str) -> Optional[str]:
    """Find the URL of the next page, or None if this is the last page."""
    soup = BeautifulSoup(html, "html.parser")
    next_btn = soup.find("li", class_="next")

    if next_btn:
        link = next_btn.find("a")
        if link:
            return base_url + link["href"]

    return None


@timer
def scrape_all_jobs(base_url: str = "https://quotes.toscrape.com") -> list[dict[str, str]]:
    """Scrape all job listings from all pages."""
    all_jobs: list[dict[str, str]] = []
    url: Optional[str] = base_url + "/"

    while url:
        print(f"Scraping: {url}")
        html = fetch_page(url)

        if html is None:
            break

        jobs = parse_job_listings(html)
        all_jobs.extend(jobs)

        url = get_next_page_url(html, base_url)
        if url:
            time.sleep(1)  # Be polite

    return all_jobs
```

### Step 5: Build the Data Pipeline (pipeline.py) - Chapter 20

Use generators to process the scraped data efficiently:

```python
# pipeline.py
from typing import Generator


def filter_by_keyword(
    jobs: list[dict], keyword: str
) -> Generator[dict, None, None]:
    """Yield only jobs whose title or description contains the keyword."""
    keyword_lower = keyword.lower()
    for job in jobs:
        if (keyword_lower in job.get("title", "").lower()
                or keyword_lower in job.get("description", "").lower()):
            yield job


def clean_job_data(
    jobs: list[dict],
) -> Generator[dict, None, None]:
    """Clean and normalize job data."""
    seen_titles: set[str] = set()

    for job in jobs:
        # Strip whitespace
        cleaned = {k: v.strip() if isinstance(v, str) else v for k, v in job.items()}

        # Skip duplicates
        title_key = cleaned.get("title", "").lower()
        if title_key in seen_titles:
            continue
        seen_titles.add(title_key)

        yield cleaned


def format_for_display(
    jobs: list[dict],
) -> Generator[str, None, None]:
    """Format jobs as readable strings."""
    for i, job in enumerate(jobs, 1):
        yield (
            f"\n-- Job {i} --\n"
            f"Title:    {job.get('title', 'N/A')}\n"
            f"Company:  {job.get('company', 'N/A')}\n"
            f"Location: {job.get('location', 'N/A')}\n"
            f"Tags:     {job.get('description', 'N/A')}"
        )
```

### Step 6: Build the Dashboard (dashboard.py)

```python
# dashboard.py
from database import search_jobs, get_job_count, get_companies


def display_dashboard() -> None:
    """Display the main dashboard."""
    total = get_job_count()
    companies = get_companies()

    print("=" * 50)
    print("       JOB LISTING DASHBOARD")
    print("=" * 50)
    print(f"\nTotal listings: {total}")
    print(f"Companies: {len(companies)}")

    print("\nTop Companies:")
    for company in companies[:10]:
        print(f"  {company['company']}: {company['job_count']} listing(s)")

    print("\n" + "-" * 50)


def search_interface() -> None:
    """Interactive search interface."""
    while True:
        print("\nSearch Jobs (or 'quit' to exit)")
        keyword = input("Keyword: ").strip()

        if keyword.lower() == "quit":
            break

        location = input("Location (optional): ").strip()
        results = search_jobs(keyword=keyword, location=location)

        if results:
            print(f"\nFound {len(results)} result(s):\n")
            for job in results:
                print(f"  [{job['id']}] {job['title']}")
                print(f"       {job['company']} | {job['location']}")
                print()
        else:
            print("No jobs found matching your criteria.")
```

### Step 7: Tie It Together (main.py)

```python
# main.py
from scraper import scrape_all_jobs
from database import create_tables, insert_job, get_job_count
from pipeline import clean_job_data
from dashboard import display_dashboard, search_interface
from utils import timer


@timer
def run_scraper() -> int:
    """Scrape jobs and save to database."""
    print("Starting scraper...")
    raw_jobs = scrape_all_jobs()
    print(f"Scraped {len(raw_jobs)} raw listings")

    # Process through pipeline
    clean_jobs = list(clean_job_data(raw_jobs))
    print(f"After cleaning: {len(clean_jobs)} unique listings")

    # Save to database
    saved = 0
    for job in clean_jobs:
        result = insert_job(
            title=job["title"],
            company=job["company"],
            location=job.get("location", ""),
            description=job.get("description", ""),
            url=job.get("url", ""),
        )
        if result:
            saved += 1

    return saved


def main() -> None:
    """Main entry point."""
    create_tables()

    print("Job Listing Scraper & Dashboard")
    print("=" * 40)
    print("1. Scrape new listings")
    print("2. View dashboard")
    print("3. Search jobs")
    print("4. Exit")

    while True:
        choice = input("\nChoice (1-4): ").strip()

        if choice == "1":
            saved = run_scraper()
            print(f"Saved {saved} new listings to database")
            print(f"Total in database: {get_job_count()}")

        elif choice == "2":
            display_dashboard()

        elif choice == "3":
            search_interface()

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try 1-4.")


if __name__ == "__main__":
    main()
```

### Step 8: Write Tests (tests/) - Chapter 24

```python
# tests/test_database.py
import pytest
import sqlite3
from database import create_tables, insert_job, search_jobs, get_job_count

DB_NAME = ":memory:"


@pytest.fixture
def test_db(monkeypatch):
    """Create a fresh in-memory database for each test."""
    import database
    monkeypatch.setattr(database, "DB_NAME", ":memory:")

    # We need a persistent connection for in-memory databases
    conn = sqlite3.connect(":memory:")
    conn.row_factory = sqlite3.Row
    conn.execute("""
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            company TEXT NOT NULL,
            location TEXT,
            description TEXT,
            url TEXT UNIQUE,
            scraped_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """)

    def mock_get_connection():
        return conn

    monkeypatch.setattr(database, "get_connection", mock_get_connection)
    return conn


def test_insert_job(test_db):
    """Test inserting a job listing."""
    import database
    job_id = database.insert_job(
        title="Python Developer",
        company="Acme Corp",
        location="Remote",
        url="https://example.com/job1",
    )
    assert job_id is not None
    assert job_id > 0


def test_search_jobs_by_keyword(test_db):
    """Test searching jobs by keyword."""
    import database
    database.insert_job(
        title="Python Developer",
        company="Acme Corp",
        url="https://example.com/1",
    )
    database.insert_job(
        title="Java Developer",
        company="Other Corp",
        url="https://example.com/2",
    )

    results = database.search_jobs(keyword="Python")
    assert len(results) == 1
    assert results[0]["title"] == "Python Developer"


# tests/test_utils.py
import pytest
from utils import timer, logger


def test_timer_returns_result():
    """Test that @timer preserves the return value."""
    @timer
    def add(a, b):
        return a + b

    assert add(2, 3) == 5


def test_timer_preserves_function_name():
    """Test that @timer preserves __name__."""
    @timer
    def my_function():
        pass

    assert my_function.__name__ == "my_function"


# tests/test_pipeline.py
from pipeline import filter_by_keyword, clean_job_data


def test_filter_by_keyword():
    """Test filtering jobs by keyword."""
    jobs = [
        {"title": "Python Developer", "description": ""},
        {"title": "Java Developer", "description": ""},
        {"title": "Data Scientist", "description": "Python required"},
    ]

    results = list(filter_by_keyword(jobs, "python"))
    assert len(results) == 2


def test_clean_removes_duplicates():
    """Test that cleaning removes duplicate titles."""
    jobs = [
        {"title": "Python Developer", "company": "A"},
        {"title": "Python Developer", "company": "B"},
        {"title": "Java Developer", "company": "C"},
    ]

    results = list(clean_job_data(jobs))
    assert len(results) == 2
```

### Step 9: Clean Up - Chapter 25

Run the full clean code suite:

```bash
# Format everything
black *.py tests/*.py

# Check for style issues
flake8 *.py tests/*.py

# Check types
mypy *.py

# Run tests
pytest tests/ -v
```

Fix any issues that come up. This is the professional workflow.

## Starter and Solution Code

**Starter code (skeleton with TODOs):**
[https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/sprint-4-pro/checkpoint-job-scraper/starter/](https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/sprint-4-pro/checkpoint-job-scraper/starter/)

**Solution code (complete working project):**
[https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/sprint-4-pro/checkpoint-job-scraper/solution/](https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/sprint-4-pro/checkpoint-job-scraper/solution/)

## Extension Ideas

If you want to go further:

- **Add email alerts** - Send yourself an email when new jobs matching your criteria are found
- **Schedule the scraper** - Run it automatically every day using `schedule` or cron
- **Build a web interface** - Use Flask (you'll learn this in Sprint 5!) to create a browser-based dashboard
- **Add salary estimation** - Use a public API to estimate salaries based on job title and location
- **Export to CSV/Excel** - Let users download search results

## What You've Accomplished

Let's take stock. In Sprint 4, you learned:

- How to write and use **decorators** to add behavior to functions
- How to use **generators** to process data memory-efficiently
- How to call **APIs** and work with JSON data from the internet
- How to store and query data in a real **database**
- How to **scrape** data from websites
- How to write **tests** that prove your code works
- How to write **clean, professional code** with type hints and linting

These aren't academic exercises. These are the exact skills listed on job postings for Python developers. You just built them all into a single project.

---

**You're one sprint away from building AI applications. ONE. Let that sink in.**

Sprint 5 covers AI, machine learning, and building intelligent applications with Python. Everything you've learned - from variables in Sprint 1 to databases and APIs in Sprint 4 - comes together. You have the foundation. You're ready.

See you in Sprint 5.

---

# Welcome to Sprint 5: Python x AI - The Future is Now

> **Chapters 26-32** | **Estimated Time: 4-5 hours** | **Difficulty: You're Ready**

This is it. The final sprint. The big one. The reason half of you picked up this book in the first place.

You're about to learn what most people think requires a PhD, three years of research, and a mass of impenetrable math. Spoiler: it doesn't. You need Python (which you already know), some libraries (which you're about to install), and the willingness to type code and see what happens. Sound familiar? It should. That's been your strategy since Chapter 1, and look how far it's gotten you.

Over the next seven chapters, you'll go from raw data to AI-powered applications. You'll crunch numbers with NumPy. You'll analyze datasets with pandas like a data scientist on their third espresso. You'll make charts so beautiful your boss will think you hired a designer. You'll teach a computer to make predictions. You'll build apps powered by the same technology behind ChatGPT. And you'll automate the boring stuff so your computer works while you don't.

Let's talk about what's ahead:

- **Chapter 26:** NumPy - the engine under every AI library
- **Chapter 27:** Pandas - data analysis without the spreadsheet headaches
- **Chapter 28:** Data Visualization - making numbers tell stories
- **Chapter 29:** Machine Learning - teaching computers to learn from data
- **Chapter 30:** AI APIs & LLMs - building with OpenAI, Gemini, and more
- **Chapter 31:** LangChain & AI Agents - memory, documents, and the bleeding edge
- **Chapter 32:** Automation - letting Python do your job while you get coffee

You went from `print("Hello, World!")` to this. Most people who start learning to code never make it past week two. You're in Sprint 5. Let that sink in.

Welcome to the future. You're building it.

Let's go.

---

# Chapter 26: NumPy: The Foundation of Everything AI

> **Sprint 5, Chapter 26** | **10 min read** | **Code: [github link](https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/sprint-5-ai/chapter-26-numpy/)**

If Python lists are a bicycle, NumPy arrays are a Tesla. Same job - getting you from A to B. Wildly different speed. And once you drive the Tesla, you're never going back to pedaling.

## What You'll Learn
- Creating NumPy arrays (multiple ways)
- Shape and dtype - understanding your data's structure
- Indexing and slicing (you already know most of this)
- Element-wise math operations (no loops!)
- Broadcasting - NumPy's mind-reading trick
- Essential functions: mean, std, max, min, sum, reshape
- Why NumPy is dramatically faster than regular Python lists

## Why Should I Care?

Every single AI and machine learning library in Python - TensorFlow, PyTorch, scikit-learn, pandas - is built on top of NumPy. It's not optional. It's not a "nice to have." It's the foundation. Learning AI without NumPy is like learning to cook without knowing what a stove is.

NumPy makes math on large datasets fast, easy, and readable. Operations that would take a `for` loop and ten lines of code take one line with NumPy. And they run 50-100x faster. That's not a typo.

## Installing NumPy

Quick setup:

```bash
pip install numpy
```

Then in your Python file:

```python
import numpy as np
```

That `as np` part is a convention. Every NumPy tutorial, every Stack Overflow answer, every data science notebook uses `np`. It's like how everyone calls Robert Downey Jr. "RDJ." You *could* use the full name, but why?

## Creating Arrays

A NumPy array is like a Python list, but turbocharged. Here are all the ways to create one:

```python
import numpy as np

# From a regular list
scores = np.array([85, 92, 78, 95, 88])
print(scores)        # [85 92 78 95 88]
print(type(scores))  # <class 'numpy.ndarray'>

# A 2D array (list of lists = rows and columns)
grades = np.array([
    [85, 92, 78],
    [95, 88, 76],
    [90, 85, 92]
])
print(grades)
# [[85 92 78]
#  [95 88 76]
#  [90 85 92]]
```

NumPy also gives you shortcut functions for common arrays:

```python
# All zeros
zeros = np.zeros(5)
print(zeros)  # [0. 0. 0. 0. 0.]

# All ones
ones = np.ones(3)
print(ones)  # [1. 1. 1.]

# A range of numbers (like Python's range, but NumPy-style)
numbers = np.arange(0, 10, 2)
print(numbers)  # [0 2 4 6 8]

# Evenly spaced numbers between two values
smooth = np.linspace(0, 1, 5)
print(smooth)  # [0.   0.25 0.5  0.75 1.  ]

# 2D array of zeros (3 rows, 4 columns)
grid = np.zeros((3, 4))
print(grid)
# [[0. 0. 0. 0.]
#  [0. 0. 0. 0.]
#  [0. 0. 0. 0.]]

# Random numbers (super useful for testing)
random_scores = np.random.randint(60, 100, size=10)
print(random_scores)  # [72 85 63 91 88 77 95 68 84 90] (yours will vary)
```

> **Pro Tip:** `np.linspace(0, 1, 5)` gives you exactly 5 evenly spaced numbers between 0 and 1. This is incredibly useful for plotting charts and scientific computing. `np.arange` works like `range()` but returns an array.

## Shape and Dtype: Describing Your Data

Every NumPy array knows two things about itself: its **shape** (how many rows and columns) and its **dtype** (what type of data it holds).

```python
scores = np.array([85, 92, 78, 95, 88])
print(scores.shape)  # (5,)     - 1D array with 5 elements
print(scores.dtype)  # int64    - 64-bit integers

grades = np.array([
    [85, 92, 78],
    [95, 88, 76],
    [90, 85, 92]
])
print(grades.shape)  # (3, 3)   - 3 rows, 3 columns
print(grades.dtype)  # int64

# You can also check other properties
print(scores.ndim)   # 1  - one dimension
print(grades.ndim)   # 2  - two dimensions
print(grades.size)   # 9  - total number of elements
```

Think of `shape` as the dimensions of a spreadsheet. `(3, 3)` means 3 rows and 3 columns. `(5,)` means just a single row of 5 items. When you start doing machine learning, you'll check `.shape` constantly. It's the first thing you look at when something goes wrong.

```python
# You can specify the data type
precise = np.array([1, 2, 3], dtype=np.float64)
print(precise)       # [1. 2. 3.]
print(precise.dtype)  # float64

small = np.array([1, 2, 3], dtype=np.int8)
print(small.dtype)    # int8 - uses less memory
```

## Indexing and Slicing

> **Remember When?** Remember list slicing from Chapter 6? Good news: NumPy indexing works almost exactly the same way. You already know this.

```python
scores = np.array([85, 92, 78, 95, 88, 76, 91])

# Single element (same as lists)
print(scores[0])     # 85
print(scores[-1])    # 91

# Slicing (same as lists)
print(scores[1:4])   # [92 78 95]
print(scores[:3])    # [85 92 78]
print(scores[::2])   # [85 78 88 91] - every other element
```

For 2D arrays, you get an extra dimension to play with:

```python
grades = np.array([
    [85, 92, 78],
    [95, 88, 76],
    [90, 85, 92]
])

# Single element: [row, column]
print(grades[0, 1])    # 92 (first row, second column)

# Entire row
print(grades[1])       # [95 88 76]

# Entire column
print(grades[:, 2])    # [78 76 92] (all rows, third column)

# Sub-grid
print(grades[0:2, 1:3])
# [[92 78]
#  [88 76]]
```

Fancy indexing - selecting specific elements by condition:

```python
scores = np.array([85, 92, 78, 95, 88, 76, 91])

# Boolean indexing - this is incredibly powerful
high_scores = scores[scores >= 90]
print(high_scores)  # [92 95 91]

# What's happening under the hood:
mask = scores >= 90
print(mask)          # [False  True False  True False False  True]
print(scores[mask])  # [92 95 91]

# Combine conditions
good_range = scores[(scores >= 80) & (scores <= 90)]
print(good_range)  # [85 88]
```

This boolean indexing trick is everywhere in data science. "Give me all rows where sales > 1000." "Give me all students with GPA above 3.5." Same pattern every time.

## Math Operations: No Loops Needed

This is where NumPy gets magical. With regular Python lists, math requires loops. With NumPy, it just... works.

```python
scores = np.array([85, 92, 78, 95, 88])

# Add 5 to every score (curve!)
curved = scores + 5
print(curved)  # [90 97 83 100 93]

# Multiply every score by 0.9
scaled = scores * 0.9
print(scaled)  # [76.5 82.8 70.2 85.5 79.2]

# Square every score
squared = scores ** 2
print(squared)  # [7225 8464 6084 9025 7744]
```

Compare this to regular Python lists:

```python
# Regular Python - requires a loop
scores_list = [85, 92, 78, 95, 88]
curved_list = []
for s in scores_list:
    curved_list.append(s + 5)

# NumPy - one line
scores_np = np.array([85, 92, 78, 95, 88])
curved_np = scores_np + 5
```

Same result. Way less code. Way faster.

Operations between two arrays work element by element:

```python
midterm = np.array([85, 92, 78, 95, 88])
final = np.array([90, 88, 82, 91, 95])

# Average of midterm and final
average = (midterm + final) / 2
print(average)  # [87.5 90.  80.  93.  91.5]

# Difference
improvement = final - midterm
print(improvement)  # [ 5 -4  4 -4  7]
```

## Broadcasting: NumPy's Mind-Reading Trick

Broadcasting is when NumPy automatically figures out how to do math between arrays of different shapes. It sounds complicated, but you've already seen it:

```python
scores = np.array([85, 92, 78, 95, 88])

# scores has shape (5,), the number 5 has shape ()
# NumPy "broadcasts" the 5 to match: [5, 5, 5, 5, 5]
curved = scores + 5  # This is broadcasting!
```

A more interesting example:

```python
# A 3x3 grid of scores
grades = np.array([
    [85, 92, 78],
    [95, 88, 76],
    [90, 85, 92]
])

# Weight for each subject: [math_weight, science_weight, english_weight]
weights = np.array([0.4, 0.35, 0.25])

# Broadcasting: (3, 3) * (3,) - NumPy applies weights to each row
weighted = grades * weights
print(weighted)
# [[34.   32.2  19.5 ]
#  [38.   30.8  19.  ]
#  [36.   29.75 23.  ]]

# Total weighted score per student
total = weighted.sum(axis=1)
print(total)  # [85.7  87.8  88.75]
```

NumPy looks at the shapes, figures out how to stretch the smaller array to match the bigger one, and does the math. No loops. No fuss.

> **Don't Panic:** Broadcasting follows rules, but you don't need to memorize them right now. The key idea is: NumPy tries to make arrays compatible for math. If the shapes are close enough, it works. If not, you'll get a clear error message.

## Common Functions: Your NumPy Toolbox

These are the functions you'll use every single day:

```python
scores = np.array([85, 92, 78, 95, 88, 76, 91, 83])

# Statistics
print(np.mean(scores))    # 86.0    - average
print(np.median(scores))  # 86.5    - middle value
print(np.std(scores))     # 6.265   - standard deviation
print(np.max(scores))     # 95      - highest
print(np.min(scores))     # 76      - lowest
print(np.sum(scores))     # 688     - total

# Position finders
print(np.argmax(scores))  # 3  - index of the highest score
print(np.argmin(scores))  # 5  - index of the lowest score

# Sorting
sorted_scores = np.sort(scores)
print(sorted_scores)  # [76 78 83 85 88 91 92 95]
```

These also work on specific axes for 2D arrays:

```python
grades = np.array([
    [85, 92, 78],
    [95, 88, 76],
    [90, 85, 92]
])

# Average per student (across columns)
print(np.mean(grades, axis=1))  # [85.  86.33 89.]

# Average per subject (across rows)
print(np.mean(grades, axis=0))  # [90.  88.33 82.]
```

Think of `axis=0` as "going down" (across rows) and `axis=1` as "going across" (across columns). If that's confusing, just try both and see which gives you what you want. Everyone does that.

### Reshape: Changing the Shape of Your Data

```python
# Start with 12 numbers in a row
numbers = np.arange(1, 13)
print(numbers)        # [ 1  2  3  4  5  6  7  8  9 10 11 12]
print(numbers.shape)  # (12,)

# Reshape into 3 rows, 4 columns
grid = numbers.reshape(3, 4)
print(grid)
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]
print(grid.shape)     # (3, 4)

# Reshape into 4 rows, 3 columns
grid2 = numbers.reshape(4, 3)
print(grid2)
# [[ 1  2  3]
#  [ 4  5  6]
#  [ 7  8  9]
#  [10 11 12]]

# Use -1 to let NumPy figure out one dimension
grid3 = numbers.reshape(2, -1)  # 2 rows, NumPy calculates columns
print(grid3.shape)  # (2, 6)
```

> **Pro Tip:** `reshape(-1)` flattens any array back to 1D. The `-1` means "figure it out for me."

## Speed Comparison: List Loop vs NumPy

Time for the proof. Let's compare regular Python to NumPy:

```python
import numpy as np
import time

size = 1_000_000

# Create data
python_list = list(range(size))
numpy_array = np.arange(size)

# Time the Python list approach
start = time.time()
result_list = [x * 2 for x in python_list]
python_time = time.time() - start

# Time the NumPy approach
start = time.time()
result_numpy = numpy_array * 2
numpy_time = time.time() - start

print(f"Python list: {python_time:.4f} seconds")
print(f"NumPy array: {numpy_time:.4f} seconds")
print(f"NumPy is {python_time / numpy_time:.1f}x faster")
```

Typical output:

```
Python list: 0.0891 seconds
NumPy array: 0.0013 seconds
NumPy is 68.5x faster
```

Almost 70 times faster. On a million elements. And the gap gets bigger as your data gets bigger. This is why every data science library uses NumPy under the hood.

> **Don't Panic:** NumPy looks like a lot of new stuff, but 80% of it works exactly like lists. Indexing? Same as lists. Slicing? Same as lists. The main difference is that math operations work on the entire array at once instead of needing loops. You already know this stuff - NumPy just makes it faster.

## Your Turn: Student Scores Analysis

Create a file called `student_scores.py`. You have test scores for 5 students across 4 subjects:

```python
import numpy as np

# Rows = students, Columns = subjects (Math, Science, English, History)
scores = np.array([
    [85, 92, 78, 88],
    [95, 88, 76, 92],
    [70, 75, 82, 68],
    [90, 85, 92, 95],
    [88, 91, 87, 84]
])

# 1. Print the shape of the array

# 2. Calculate and print each student's average score (across subjects)

# 3. Calculate and print each subject's average score (across students)

# 4. Find the highest score in the entire array and its position

# 5. Find all scores above 90 using boolean indexing

# 6. Add a 5-point curve to all scores and print the new array

# 7. Which student has the highest overall average?
```

Expected output:

```
Shape: (5, 4)
Student averages: [85.75 87.75 73.75 90.5  87.5 ]
Subject averages: [85.6 86.2 83.  85.4]
Highest score: 95 at position (1, 0) and (3, 3)
Scores above 90: [92 95 92 92 95 91]
Curved scores (first row): [90 97 83 93]
Best student: Student 4 with average 90.5
```

## TL;DR

- NumPy arrays are like Python lists but dramatically faster for math operations
- `import numpy as np` - the universal convention
- Create arrays with `np.array()`, `np.zeros()`, `np.ones()`, `np.arange()`, `np.linspace()`
- `.shape` tells you dimensions, `.dtype` tells you data type
- Indexing and slicing work just like lists, plus `[row, col]` for 2D
- Boolean indexing: `arr[arr > 90]` gives you all elements matching the condition
- Math operations work element-wise - no loops needed
- Broadcasting lets NumPy do math between arrays of different sizes
- Key functions: `np.mean()`, `np.std()`, `np.max()`, `np.min()`, `np.sum()`, `np.sort()`
- `.reshape()` changes the shape of your data
- NumPy is 50-100x faster than regular Python lists for numerical operations
- Every AI/ML library is built on NumPy - this is the foundation of everything that follows

---

# Chapter 27: Pandas: Data Analysis Like a Boss

> **Sprint 5, Chapter 27** | **12 min read** | **Code: [github link](https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/sprint-5-ai/chapter-27-pandas/)**

If Excel and Python had a baby, it would be pandas. All the spreadsheet power, none of the mouse clicking. No more dragging formulas across 10,000 rows. No more accidentally sorting one column and scrambling all your data. Pandas does what Excel does - but in code, which means it's reproducible, automatable, and infinitely more powerful.

## What You'll Learn
- Series (one column) and DataFrame (the whole spreadsheet)
- Reading CSV files into pandas
- Selecting columns and rows
- Filtering data with conditions
- Sorting and groupby (pivot table vibes)
- Handling missing data
- `describe()` - instant statistics

## Why Should I Care?

Data science, business analytics, machine learning prep, financial analysis, marketing reports - they all start with pandas. If data is the new oil, pandas is the refinery. Every data science job listing mentions it. Every machine learning project starts by loading data into a pandas DataFrame. If you plan to work with data in any capacity, pandas is non-negotiable.

## Installing Pandas

```bash
pip install pandas
```

```python
import pandas as pd
```

Just like NumPy has `np`, pandas has `pd`. It's the law. Nobody will arrest you for writing `import pandas`, but other programmers will give you a look.

## Series: One Column of Data

A **Series** is a single column of data with labels. Think of it as a labeled list.

```python
import pandas as pd

# Create a Series from a list
scores = pd.Series([85, 92, 78, 95, 88])
print(scores)
# 0    85
# 1    92
# 2    78
# 3    95
# 4    88
# dtype: int64
```

Notice the numbers on the left? That's the **index** - automatic labels. You can set your own:

```python
scores = pd.Series(
    [85, 92, 78, 95, 88],
    index=["Alice", "Bob", "Charlie", "Diana", "Eve"]
)
print(scores)
# Alice      85
# Bob        92
# Charlie    78
# Diana      95
# Eve        88
# dtype: int64

# Access by label
print(scores["Diana"])    # 95

# Access by position
print(scores.iloc[0])     # 85
```

> **Remember When?** Remember dictionaries from Chapter 9? A Series is basically a dictionary with superpowers. Keys become the index, values become the data. And you get all of NumPy's math for free.

## DataFrame: The Whole Spreadsheet

A **DataFrame** is the star of the show. It's a table - rows and columns, just like a spreadsheet. Each column is a Series.

```python
import pandas as pd

# Create a DataFrame from a dictionary
data = {
    "name": ["Alice", "Bob", "Charlie", "Diana", "Eve"],
    "age": [25, 30, 35, 28, 32],
    "city": ["New York", "London", "Tokyo", "Paris", "Sydney"],
    "salary": [70000, 85000, 90000, 75000, 88000]
}

df = pd.DataFrame(data)
print(df)
#       name  age      city  salary
# 0    Alice   25  New York   70000
# 1      Bob   30    London   85000
# 2  Charlie   35     Tokyo   90000
# 3    Diana   28     Paris   75000
# 4      Eve   32    Sydney   88000
```

That's it. Dictionary keys become column names. Lists become the data. You just created a spreadsheet in three lines of code.

```python
# Quick info about your DataFrame
print(df.shape)     # (5, 4) - 5 rows, 4 columns
print(df.columns)   # Index(['name', 'age', 'city', 'salary'], dtype='object')
print(df.dtypes)
# name      object
# age        int64
# city      object
# salary     int64
```

## Reading Data from CSV

In the real world, you rarely type in data manually. You read it from files. The most common format is CSV (Comma-Separated Values).

```python
# Reading a CSV file
df = pd.read_csv("movies.csv")

# First 5 rows (always do this first!)
print(df.head())

# Last 5 rows
print(df.tail())

# How big is it?
print(df.shape)  # (1000, 8) - 1000 movies, 8 columns
```

Let's create a sample CSV to work with throughout this chapter:

```python
import pandas as pd

# Creating our sample movie dataset
movies_data = {
    "title": ["The Matrix", "Inception", "Interstellar", "The Dark Knight",
              "Pulp Fiction", "Forrest Gump", "The Godfather", "Parasite",
              "Get Out", "Mad Max: Fury Road"],
    "year": [1999, 2010, 2014, 2008, 1994, 1994, 1972, 2019, 2017, 2015],
    "genre": ["Sci-Fi", "Sci-Fi", "Sci-Fi", "Action", "Crime", "Drama",
              "Crime", "Thriller", "Horror", "Action"],
    "rating": [8.7, 8.8, 8.6, 9.0, 8.9, 8.8, 9.2, 8.5, 7.7, 8.1],
    "votes": [1900000, 2300000, 1800000, 2700000, 2100000, 2000000,
              1900000, 800000, 600000, 1000000],
    "runtime_min": [136, 148, 169, 152, 154, 142, 175, 132, 104, 120],
    "budget_millions": [63, 160, 165, 185, 8, 55, 6, 11, 5, 150],
    "revenue_millions": [467, 836, 701, 1005, 214, 678, 287, 266, 255, 375]
}

movies = pd.DataFrame(movies_data)
movies.to_csv("movies.csv", index=False)
print(movies.head())
```

## Selecting Columns and Rows

### Selecting Columns

```python
# Single column (returns a Series)
titles = movies["title"]
print(titles)
# 0          The Matrix
# 1           Inception
# 2        Interstellar
# ...

# Multiple columns (returns a DataFrame)
subset = movies[["title", "rating", "year"]]
print(subset.head())
#              title  rating  year
# 0       The Matrix     8.7  1999
# 1        Inception     8.8  2010
# 2     Interstellar     8.6  2014
```

### Selecting Rows

```python
# By position (iloc = integer location)
first_movie = movies.iloc[0]     # First row
print(first_movie)
# title             The Matrix
# year                    1999
# genre                 Sci-Fi
# rating                   8.7
# ...

# Slice of rows
first_three = movies.iloc[0:3]
print(first_three)

# Specific rows and columns
print(movies.iloc[0:3, [0, 3]])  # First 3 rows, title and rating columns

# By label (loc)
# (Our index is numbers, so loc and iloc look similar here)
print(movies.loc[0, "title"])  # "The Matrix"
```

> **Pro Tip:** `iloc` uses integer positions (like list indexing). `loc` uses labels (like dictionary keys). When your index is just numbers 0, 1, 2..., they look the same. But when your index is custom labels (like dates or names), `loc` is what you want.

## Filtering with Conditions

This is where pandas really starts to flex. Want to find all movies rated above 8.5? One line:

```python
# Movies rated above 8.5
great_movies = movies[movies["rating"] > 8.5]
print(great_movies[["title", "rating"]])
#              title  rating
# 0       The Matrix     8.7
# 1        Inception     8.8
# 2     Interstellar     8.6
# 3   The Dark Knight    9.0
# 4    Pulp Fiction      8.9
# 5    Forrest Gump      8.8
# 6    The Godfather     9.2

# Sci-Fi movies only
scifi = movies[movies["genre"] == "Sci-Fi"]
print(scifi["title"])
# 0      The Matrix
# 1       Inception
# 2    Interstellar

# Combine conditions with & (and) or | (or)
scifi_great = movies[(movies["genre"] == "Sci-Fi") & (movies["rating"] > 8.7)]
print(scifi_great[["title", "rating"]])
#        title  rating
# 1  Inception     8.8

# Movies from the 90s or rated above 9.0
classic_or_great = movies[(movies["year"] < 2000) | (movies["rating"] > 9.0)]
print(classic_or_great[["title", "year", "rating"]])
```

Notice the pattern: `df[condition]`. The condition creates a True/False mask (just like NumPy boolean indexing from Chapter 26), and pandas returns only the rows where it's True.

```python
# Check what values exist in a column
print(movies["genre"].unique())     # ['Sci-Fi' 'Action' 'Crime' 'Drama' 'Thriller' 'Horror']
print(movies["genre"].nunique())    # 6 unique genres
print(movies["genre"].value_counts())
# Sci-Fi      3
# Action      2
# Crime       2
# Drama       1
# Thriller    1
# Horror      1
```

## Sorting and Groupby

### Sorting

```python
# Sort by rating (highest first)
best_first = movies.sort_values("rating", ascending=False)
print(best_first[["title", "rating"]].head())
#              title  rating
# 6    The Godfather     9.2
# 3  The Dark Knight     9.0
# 4    Pulp Fiction      8.9
# 1        Inception     8.8
# 5    Forrest Gump      8.8

# Sort by year, then by rating
sorted_movies = movies.sort_values(["year", "rating"], ascending=[True, False])
print(sorted_movies[["title", "year", "rating"]])
```

### Groupby: Pivot Table Vibes

Groupby is like Excel pivot tables, but cooler. "Group my data by [some column], then calculate [some statistic]."

```python
# Average rating by genre
genre_avg = movies.groupby("genre")["rating"].mean()
print(genre_avg)
# genre
# Action      8.55
# Crime       9.05
# Drama       8.80
# Horror      7.70
# Sci-Fi      8.70
# Thriller    8.50

# Multiple statistics at once
genre_stats = movies.groupby("genre")["rating"].agg(["mean", "min", "max", "count"])
print(genre_stats)
#           mean  min  max  count
# genre
# Action    8.55  8.1  9.0      2
# Crime     9.05  8.9  9.2      2
# Drama     8.80  8.8  8.8      1
# Horror    7.70  7.7  7.7      1
# Sci-Fi    8.70  8.6  8.8      3
# Thriller  8.50  8.5  8.5      1

# Average budget and revenue by genre
money = movies.groupby("genre")[["budget_millions", "revenue_millions"]].mean()
print(money)
```

Here's the Groupby pattern: `df.groupby("column_to_group_by")["column_to_calculate"].operation()`. You'll use this pattern hundreds of times.

## Adding and Modifying Columns

```python
# Add a new column: profit
movies["profit_millions"] = movies["revenue_millions"] - movies["budget_millions"]
print(movies[["title", "profit_millions"]].head())
#            title  profit_millions
# 0     The Matrix              404
# 1      Inception              676
# 2   Interstellar              536
# 3  The Dark Knight            820
# 4   Pulp Fiction              206

# Add a column based on a condition
movies["is_blockbuster"] = movies["revenue_millions"] > 500
print(movies[["title", "is_blockbuster"]])

# Add a column with a calculation
movies["roi"] = (movies["revenue_millions"] / movies["budget_millions"]).round(1)
print(movies[["title", "budget_millions", "revenue_millions", "roi"]])
# Pulp Fiction: ROI of 26.8x on an $8M budget. Not bad, Tarantino.
```

## Handling Missing Data

Real-world data is messy. Columns have missing values. Pandas handles this gracefully with `NaN` (Not a Number).

```python
import pandas as pd
import numpy as np

# Create data with missing values
data = {
    "name": ["Alice", "Bob", "Charlie", "Diana", "Eve"],
    "age": [25, np.nan, 35, 28, np.nan],
    "salary": [70000, 85000, np.nan, 75000, 88000],
    "city": ["New York", "London", None, "Paris", "Sydney"]
}

df = pd.DataFrame(data)
print(df)
#       name   age   salary      city
# 0    Alice  25.0  70000.0  New York
# 1      Bob   NaN  85000.0    London
# 2  Charlie  35.0      NaN      None
# 3    Diana  28.0  75000.0     Paris
# 4      Eve   NaN  88000.0    Sydney
```

Finding missing data:

```python
# Which values are missing?
print(df.isna())
#     name    age  salary   city
# 0  False  False   False  False
# 1  False   True   False  False
# 2  False  False    True   True
# 3  False  False   False  False
# 4  False   True   False  False

# How many missing per column?
print(df.isna().sum())
# name      0
# age       2
# salary    1
# city      1
```

Fixing missing data:

```python
# Option 1: Drop rows with any missing data
clean = df.dropna()
print(clean)  # Only Alice, Diana - lost 3 rows!

# Option 2: Fill missing values with a specific value
filled = df.fillna({"age": df["age"].mean(), "salary": 0, "city": "Unknown"})
print(filled)
#       name   age   salary      city
# 0    Alice  25.0  70000.0  New York
# 1      Bob  29.3  85000.0    London
# 2  Charlie  35.0      0.0   Unknown
# 3    Diana  28.0  75000.0     Paris
# 4      Eve  29.3  88000.0    Sydney

# Option 3: Drop only rows where a specific column is missing
has_age = df.dropna(subset=["age"])
print(has_age)  # Keeps Alice, Charlie, Diana
```

> **Pro Tip:** `dropna()` is aggressive - it can remove a lot of data. `fillna()` with the mean or median is usually a better first choice for numerical columns. For categorical columns (like city), `fillna("Unknown")` is a safe bet.

## describe(): Instant Statistics

One function to rule them all:

```python
print(movies.describe())
#            year     rating        votes  runtime_min  budget_millions  revenue_millions
# count  10.0000  10.000000  10000000.00    10.000000        10.000000         10.000000
# mean 2004.2000   8.630000  1710000.000   143.200000        80.800000        508.400000
# std    14.3900   0.440454   672309.450    21.606000        72.800000        263.600000
# min  1972.0000   7.700000   600000.000   104.000000         5.000000        214.000000
# 25%  1995.2500   8.525000  1225000.000   131.000000         9.250000        267.750000
# 50%  2009.0000   8.750000  1900000.000   145.000000        59.000000        376.500000
# 75%  2014.7500   8.825000  2075000.000   156.500000       162.500000        692.250000
# max  2019.0000   9.200000  2700000.000   175.000000       185.000000       1005.000000
```

Count, mean, standard deviation, min, max, and quartiles - all in one call. This is the first thing every data scientist runs on a new dataset. Always.

```python
# describe() for a single column
print(movies["rating"].describe())

# For non-numeric columns
print(movies["genre"].describe())
# count        10
# unique        6
# top      Sci-Fi
# freq          3
```

> **Don't Panic:** Pandas has hundreds of methods. You need about 20 of them for 95% of your work. This chapter covers those 20. You can always look up the rest when you need them. The pandas documentation is excellent, and honestly, so is asking ChatGPT "how do I do X in pandas?"

## Useful Extras

A few more things you'll use constantly:

```python
# Rename columns
movies_clean = movies.rename(columns={"runtime_min": "runtime", "budget_millions": "budget"})

# Apply a function to every value in a column
movies["title_upper"] = movies["title"].apply(str.upper)

# String methods
movies["title_length"] = movies["title"].str.len()
short_titles = movies[movies["title"].str.contains("The")]

# Reset index after filtering
scifi = movies[movies["genre"] == "Sci-Fi"].reset_index(drop=True)
print(scifi)  # Index is now 0, 1, 2 instead of 0, 1, 2 (original positions)
```

## Your Turn: Movie Ratings Dataset Analysis

Create `movie_analysis.py` and work with the movie dataset we created above:

```python
import pandas as pd

# 1. Load the movies.csv file (or create the DataFrame from above)

# 2. Print the first 5 rows and the shape

# 3. What's the average rating across all movies?

# 4. Which movie has the highest rating? The lowest?

# 5. Filter: Find all movies made after 2010 with a rating above 8.0

# 6. Which genre has the highest average rating?

# 7. Which movie had the best ROI (revenue / budget)?

# 8. Add a "decade" column (1990s, 2000s, 2010s, etc.)
#    Hint: (movies["year"] // 10) * 10

# 9. What's the average budget by decade?

# 10. Sort movies by profit (revenue - budget) in descending order
```

Expected insights:
- The Godfather has the highest rating (9.2) and was made with just $6M
- Pulp Fiction has the best ROI: made $214M on just $8M (26.8x return)
- The 2010s had the highest average budgets
- Crime genre has the highest average rating

## TL;DR

- Pandas is Python's data analysis powerhouse - think Excel but with code
- `import pandas as pd` - the universal convention
- **Series** = one column; **DataFrame** = the whole table
- `pd.read_csv("file.csv")` loads data; `df.head()` previews it
- Select columns: `df["col"]` or `df[["col1", "col2"]]`
- Select rows: `df.iloc[0]` (by position) or `df.loc[0]` (by label)
- Filter: `df[df["col"] > value]` - same boolean indexing pattern as NumPy
- Sort: `df.sort_values("col", ascending=False)`
- Groupby: `df.groupby("col")["other_col"].mean()` - pivot table in one line
- Missing data: `df.isna().sum()` to find it, `df.fillna()` or `df.dropna()` to fix it
- `df.describe()` gives you instant statistics on every numeric column
- You only need about 20 pandas methods for 95% of your work - this chapter covered them

---

# Chapter 28: Data Visualization: Making Data Beautiful

> **Sprint 5, Chapter 28** | **12 min read** | **Code: [github link](https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/sprint-5-ai/chapter-28-data-visualization/)**

Data without visualization is like a movie without pictures. Technically the story is there, but nobody's paying attention. You could hand your boss a spreadsheet with 10,000 rows and say "the numbers are good." Or you could show them one chart that makes their eyebrows go up. Guess which one gets you the raise.

## What You'll Learn
- Matplotlib basics: line, scatter, bar, histogram, pie charts
- Making charts not ugly: labels, titles, colors, legends
- Subplots - multiple charts in one figure
- Seaborn - matplotlib but prettier
- Plotly - interactive charts that move
- Choosing the right chart for your data

## Why Should I Care?

Presentations. Reports. Dashboards. Job interviews. Blog posts. Every time you need to communicate something about data, you need a chart. Data visualization is the difference between "I analyzed the data" and "let me show you what I found." One gets a nod. The other gets attention.

Also, you'll use visualization constantly when building machine learning models. Plotting your data before feeding it to an algorithm is like reading the recipe before you start cooking. Highly recommended.

## Installing the Libraries

```bash
pip install matplotlib seaborn plotly
```

```python
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
```

That `matplotlib.pyplot as plt` is another one of those universal conventions. Every tutorial, every textbook, every notebook. Just `plt`.

## Matplotlib: The Foundation

Matplotlib is the original Python plotting library. It's not the prettiest out of the box, but it's the most flexible and everything else is built on top of it.

### Your First Chart: Line Plot

```python
import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [120, 135, 148, 162, 155, 178]

plt.plot(months, sales)
plt.title("Monthly Sales 2024")
plt.xlabel("Month")
plt.ylabel("Sales ($K)")
plt.show()
```

That's it. Five lines. You've got a chart.

Let's make it look better:

```python
plt.plot(months, sales, color="royalblue", marker="o", linewidth=2, markersize=8)
plt.title("Monthly Sales 2024", fontsize=16, fontweight="bold")
plt.xlabel("Month", fontsize=12)
plt.ylabel("Sales ($K)", fontsize=12)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

Now it looks like something you'd actually put in a presentation.

### Multiple Lines on One Chart

```python
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
product_a = [120, 135, 148, 162, 155, 178]
product_b = [90, 105, 112, 130, 142, 151]
product_c = [75, 80, 95, 88, 102, 110]

plt.plot(months, product_a, marker="o", label="Product A")
plt.plot(months, product_b, marker="s", label="Product B")
plt.plot(months, product_c, marker="^", label="Product C")

plt.title("Sales by Product", fontsize=14, fontweight="bold")
plt.xlabel("Month")
plt.ylabel("Sales ($K)")
plt.legend()  # Shows the labels
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

### Scatter Plot: Seeing Relationships

```python
import numpy as np

# Movie data
budgets = [63, 160, 165, 185, 8, 55, 6, 11, 5, 150]
revenues = [467, 836, 701, 1005, 214, 678, 287, 266, 255, 375]
ratings = [8.7, 8.8, 8.6, 9.0, 8.9, 8.8, 9.2, 8.5, 7.7, 8.1]

# Size of dots based on rating, color based on rating
plt.scatter(budgets, revenues, s=[r * 30 for r in ratings],
            c=ratings, cmap="coolwarm", alpha=0.7, edgecolors="black")

plt.colorbar(label="Rating")
plt.title("Budget vs Revenue", fontsize=14, fontweight="bold")
plt.xlabel("Budget ($M)")
plt.ylabel("Revenue ($M)")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

Scatter plots are perfect for answering "Is there a relationship between X and Y?" In this case: does spending more on a movie mean making more money? (Spoiler: sort of, but Pulp Fiction says otherwise.)

### Bar Chart: Comparing Categories

```python
genres = ["Sci-Fi", "Action", "Crime", "Drama", "Thriller", "Horror"]
avg_ratings = [8.70, 8.55, 9.05, 8.80, 8.50, 7.70]

colors = ["#2196F3", "#FF5722", "#4CAF50", "#FF9800", "#9C27B0", "#F44336"]

plt.bar(genres, avg_ratings, color=colors, edgecolor="black", linewidth=0.5)
plt.title("Average Rating by Genre", fontsize=14, fontweight="bold")
plt.xlabel("Genre")
plt.ylabel("Average Rating")
plt.ylim(7, 10)  # Start y-axis at 7 to show differences better
plt.tight_layout()
plt.show()
```

Horizontal bars work better when you have long category names:

```python
movies = ["The Godfather", "The Dark Knight", "Pulp Fiction",
          "Inception", "Forrest Gump", "The Matrix"]
ratings = [9.2, 9.0, 8.9, 8.8, 8.8, 8.7]

plt.barh(movies, ratings, color="steelblue", edgecolor="black")
plt.title("Top 6 Movies by Rating", fontsize=14, fontweight="bold")
plt.xlabel("Rating")
plt.xlim(8.5, 9.5)
plt.tight_layout()
plt.show()
```

### Histogram: Distribution of Data

```python
import numpy as np

# Generate 1000 random test scores
np.random.seed(42)
scores = np.random.normal(loc=75, scale=12, size=1000)

plt.hist(scores, bins=25, color="steelblue", edgecolor="black", alpha=0.7)
plt.title("Distribution of Test Scores", fontsize=14, fontweight="bold")
plt.xlabel("Score")
plt.ylabel("Number of Students")
plt.axvline(np.mean(scores), color="red", linestyle="-", label=f"Mean: {np.mean(scores):.1f}")
plt.legend()
plt.tight_layout()
plt.show()
```

Histograms answer the question: "What does the spread of my data look like?" The bell curve shape means most students scored near the average, with fewer at the extremes. You'll see this shape everywhere in statistics and ML.

### Pie Chart: Parts of a Whole

```python
genres = ["Sci-Fi", "Action", "Crime", "Drama", "Thriller", "Horror"]
counts = [3, 2, 2, 1, 1, 1]

colors = ["#2196F3", "#FF5722", "#4CAF50", "#FF9800", "#9C27B0", "#F44336"]

plt.pie(counts, labels=genres, colors=colors, autopct="%1.0f%%",
        startangle=90, explode=[0.05] * 6)
plt.title("Movies by Genre", fontsize=14, fontweight="bold")
plt.tight_layout()
plt.show()
```

> **Pro Tip:** Pie charts get a bad reputation in data science. They're fine for showing simple proportions (like budget breakdown), but bar charts are almost always easier to read when comparing values. Use pie charts sparingly.

## Making Charts Not Ugly

Here's the cheat sheet for going from "default matplotlib" to "actually presentable":

```python
import matplotlib.pyplot as plt
import numpy as np

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [120, 135, 148, 162, 155, 178]

# Set a style - this changes everything
plt.style.use("seaborn-v0_8-whitegrid")  # Clean, modern look

fig, ax = plt.subplots(figsize=(10, 6))  # Control the size

ax.plot(months, sales, color="#2196F3", marker="o", linewidth=2.5,
        markersize=8, markerfacecolor="white", markeredgewidth=2)

ax.set_title("Monthly Sales 2024", fontsize=18, fontweight="bold", pad=20)
ax.set_xlabel("Month", fontsize=13)
ax.set_ylabel("Sales ($K)", fontsize=13)
ax.set_ylim(100, 200)

# Add value labels on each point
for i, (month, sale) in enumerate(zip(months, sales)):
    ax.annotate(f"${sale}K", (month, sale), textcoords="offset points",
                xytext=(0, 12), ha="center", fontsize=10)

ax.grid(True, alpha=0.3)
fig.tight_layout()
plt.show()
```

Key upgrades:
- `plt.style.use()` - sets a global style theme
- `figsize=(10, 6)` - control the chart size
- `tight_layout()` - prevents labels from getting cut off
- Annotations - add data labels directly on the chart
- Custom colors with hex codes - no more default blue

Available styles you can try:

```python
# See all available styles
print(plt.style.available)

# Some good ones:
# "seaborn-v0_8-whitegrid" - clean and modern
# "ggplot" - R-inspired
# "fivethirtyeight" - news/data journalism style
# "dark_background" - dark mode
```

### Saving Charts

```python
# Save to file instead of displaying
plt.savefig("sales_chart.png", dpi=150, bbox_inches="tight")

# Other formats
plt.savefig("sales_chart.pdf")
plt.savefig("sales_chart.svg")  # Vector format - scales perfectly
```

## Subplots: Multiple Charts in One Figure

Sometimes one chart isn't enough. You want to show several views of the same data side by side.

```python
import matplotlib.pyplot as plt
import numpy as np

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Top-left: Line chart
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [120, 135, 148, 162, 155, 178]
axes[0, 0].plot(months, sales, marker="o", color="steelblue")
axes[0, 0].set_title("Monthly Sales", fontweight="bold")
axes[0, 0].set_ylabel("Sales ($K)")

# Top-right: Bar chart
genres = ["Sci-Fi", "Action", "Crime", "Drama"]
counts = [3, 2, 2, 1]
axes[0, 1].bar(genres, counts, color=["#2196F3", "#FF5722", "#4CAF50", "#FF9800"])
axes[0, 1].set_title("Movies by Genre", fontweight="bold")

# Bottom-left: Scatter plot
np.random.seed(42)
x = np.random.randn(100)
y = x * 2 + np.random.randn(100) * 0.5
axes[1, 0].scatter(x, y, alpha=0.6, color="purple")
axes[1, 0].set_title("Correlation Example", fontweight="bold")
axes[1, 0].set_xlabel("X")
axes[1, 0].set_ylabel("Y")

# Bottom-right: Histogram
scores = np.random.normal(75, 12, 500)
axes[1, 1].hist(scores, bins=20, color="coral", edgecolor="black")
axes[1, 1].set_title("Score Distribution", fontweight="bold")
axes[1, 1].set_xlabel("Score")

fig.suptitle("Dashboard Example", fontsize=16, fontweight="bold", y=1.02)
plt.tight_layout()
plt.show()
```

`plt.subplots(2, 2)` gives you a 2x2 grid. Access each chart with `axes[row, col]`. Fill them in with whatever chart types you want. This is how dashboards are born.

## Seaborn: Matplotlib But Prettier

Seaborn is built on top of matplotlib and makes statistical charts gorgeous with almost no effort.

```python
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Using our movie data
movies = pd.DataFrame({
    "title": ["The Matrix", "Inception", "Interstellar", "The Dark Knight",
              "Pulp Fiction", "Forrest Gump", "The Godfather", "Parasite",
              "Get Out", "Mad Max: Fury Road"],
    "genre": ["Sci-Fi", "Sci-Fi", "Sci-Fi", "Action", "Crime", "Drama",
              "Crime", "Thriller", "Horror", "Action"],
    "rating": [8.7, 8.8, 8.6, 9.0, 8.9, 8.8, 9.2, 8.5, 7.7, 8.1],
    "budget_millions": [63, 160, 165, 185, 8, 55, 6, 11, 5, 150],
    "revenue_millions": [467, 836, 701, 1005, 214, 678, 287, 266, 255, 375]
})
```

### Bar Plot

```python
plt.figure(figsize=(10, 6))
sns.barplot(data=movies, x="genre", y="rating", palette="viridis")
plt.title("Average Rating by Genre", fontsize=14, fontweight="bold")
plt.tight_layout()
plt.show()
```

One line of seaborn replaces about ten lines of matplotlib. And it looks better. The bars automatically show confidence intervals (those little lines on top). Seaborn thinks statistically by default.

### Box Plot

```python
# Create a bigger dataset for box plots
import numpy as np
np.random.seed(42)

data = pd.DataFrame({
    "department": np.random.choice(["Engineering", "Marketing", "Sales", "HR"], 200),
    "salary": np.random.normal(75000, 15000, 200),
    "satisfaction": np.random.uniform(1, 10, 200)
})

plt.figure(figsize=(10, 6))
sns.boxplot(data=data, x="department", y="salary", palette="Set2")
plt.title("Salary Distribution by Department", fontsize=14, fontweight="bold")
plt.ylabel("Salary ($)")
plt.tight_layout()
plt.show()
```

Box plots show you the median, quartiles, and outliers at a glance. They're the "tell me everything about this distribution in one shape" chart.

### Heatmap

```python
# Correlation matrix - how are variables related?
numeric_movies = movies[["rating", "budget_millions", "revenue_millions"]].copy()

plt.figure(figsize=(8, 6))
sns.heatmap(numeric_movies.corr(), annot=True, cmap="coolwarm",
            center=0, fmt=".2f", linewidths=1)
plt.title("Correlation Heatmap", fontsize=14, fontweight="bold")
plt.tight_layout()
plt.show()
```

A heatmap of correlations instantly shows you which variables are related. Dark red = strong positive correlation. Dark blue = strong negative. This is one of the first things data scientists plot with a new dataset.

### Pairplot: The Kitchen Sink

```python
# This one chart shows every relationship between every numeric column
sns.pairplot(movies[["rating", "budget_millions", "revenue_millions"]],
             diag_kind="hist", plot_kws={"alpha": 0.6})
plt.suptitle("Relationships Between Movie Variables", y=1.02)
plt.show()
```

One line. You get scatter plots for every pair of variables and histograms on the diagonal. It's like x-ray vision for your dataset.

## Plotly: Interactive Charts That Move

Plotly creates charts you can hover over, zoom into, and interact with. Perfect for dashboards and web apps.

```python
import plotly.express as px
import pandas as pd

movies = pd.DataFrame({
    "title": ["The Matrix", "Inception", "Interstellar", "The Dark Knight",
              "Pulp Fiction", "Forrest Gump", "The Godfather", "Parasite",
              "Get Out", "Mad Max: Fury Road"],
    "genre": ["Sci-Fi", "Sci-Fi", "Sci-Fi", "Action", "Crime", "Drama",
              "Crime", "Thriller", "Horror", "Action"],
    "rating": [8.7, 8.8, 8.6, 9.0, 8.9, 8.8, 9.2, 8.5, 7.7, 8.1],
    "budget_millions": [63, 160, 165, 185, 8, 55, 6, 11, 5, 150],
    "revenue_millions": [467, 836, 701, 1005, 214, 678, 287, 266, 255, 375]
})

# Interactive scatter plot
fig = px.scatter(
    movies,
    x="budget_millions",
    y="revenue_millions",
    color="genre",
    size="rating",
    hover_name="title",
    title="Budget vs Revenue (Hover for Details!)",
    labels={"budget_millions": "Budget ($M)", "revenue_millions": "Revenue ($M)"}
)
fig.show()  # Opens in your browser!
```

When you run this, a chart opens in your browser. Hover over any dot to see the movie name, genre, budget, revenue, and rating. Zoom in by dragging. This is what modern dashboards look like.

```python
# Interactive bar chart
fig = px.bar(
    movies.sort_values("rating", ascending=True),
    x="rating",
    y="title",
    orientation="h",
    color="genre",
    title="Movie Ratings",
    labels={"rating": "IMDb Rating", "title": "Movie"}
)
fig.show()

# Interactive line chart with animation
# (Imagine monthly data over several years)
fig = px.scatter(
    movies,
    x="budget_millions",
    y="revenue_millions",
    color="genre",
    hover_name="title",
    size_max=15,
    title="Movie Economics"
)
fig.update_layout(template="plotly_white")
fig.show()
```

> **Pro Tip:** Plotly charts can be embedded directly in web apps (Flask, Streamlit, Dash). If you want to build data dashboards, Plotly + Dash is one of the most popular combinations in the industry.

## Choosing the Right Chart

Here's your decision guide:

| Question You're Asking | Chart Type | Library Call |
|--|--|--|
| How does something change over time? | **Line chart** | `plt.plot()` |
| How do categories compare? | **Bar chart** | `plt.bar()` or `sns.barplot()` |
| What's the relationship between X and Y? | **Scatter plot** | `plt.scatter()` or `px.scatter()` |
| What does the distribution look like? | **Histogram** | `plt.hist()` or `sns.histplot()` |
| What are the proportions? | **Pie chart** | `plt.pie()` |
| How are variables correlated? | **Heatmap** | `sns.heatmap()` |
| How is data distributed across groups? | **Box plot** | `sns.boxplot()` |
| I want to see EVERYTHING | **Pair plot** | `sns.pairplot()` |
| I need interactivity | **Any Plotly chart** | `px.scatter()`, `px.bar()`, etc. |

When in doubt, start with a bar chart (for categories) or scatter plot (for relationships). You can always change it later.

> **Fun Fact:** Matplotlib was created by John Hunter in 2003 to replicate MATLAB's plotting capabilities in Python. The name literally comes from "MATLAB plotting library." Hunter wanted scientists who were used to MATLAB to feel right at home. The project became one of the most-used Python libraries in history.

## Pandas + Matplotlib: The Quick Way

Pandas DataFrames have built-in plotting that uses matplotlib under the hood:

```python
import pandas as pd
import matplotlib.pyplot as plt

movies = pd.DataFrame({
    "title": ["The Matrix", "Inception", "The Dark Knight", "Pulp Fiction", "The Godfather"],
    "rating": [8.7, 8.8, 9.0, 8.9, 9.2],
    "budget_millions": [63, 160, 185, 8, 6],
    "revenue_millions": [467, 836, 1005, 214, 287]
})

# Plot directly from a DataFrame
movies.plot(x="title", y="rating", kind="bar", figsize=(10, 5),
            title="Movie Ratings", legend=False, color="steelblue")
plt.ylabel("Rating")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()

# Scatter plot from DataFrame
movies.plot(x="budget_millions", y="revenue_millions", kind="scatter",
            figsize=(8, 6), title="Budget vs Revenue")
plt.show()
```

This is great for quick exploration. You're already in pandas, so why switch? For polished charts, use matplotlib or seaborn directly. For quick "what does this data look like?" plots, pandas is the fastest path.

## Your Turn: Movie Ratings Visual Dashboard

Create `movie_dashboard.py` and build a 2x2 dashboard:

```python
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Movie dataset (use the one from Chapter 27 or create it fresh)
movies = pd.DataFrame({
    "title": ["The Matrix", "Inception", "Interstellar", "The Dark Knight",
              "Pulp Fiction", "Forrest Gump", "The Godfather", "Parasite",
              "Get Out", "Mad Max: Fury Road"],
    "year": [1999, 2010, 2014, 2008, 1994, 1994, 1972, 2019, 2017, 2015],
    "genre": ["Sci-Fi", "Sci-Fi", "Sci-Fi", "Action", "Crime", "Drama",
              "Crime", "Thriller", "Horror", "Action"],
    "rating": [8.7, 8.8, 8.6, 9.0, 8.9, 8.8, 9.2, 8.5, 7.7, 8.1],
    "budget_millions": [63, 160, 165, 185, 8, 55, 6, 11, 5, 150],
    "revenue_millions": [467, 836, 701, 1005, 214, 678, 287, 266, 255, 375]
})

movies["profit_millions"] = movies["revenue_millions"] - movies["budget_millions"]

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# 1. Top-left: Bar chart of ratings (sorted)

# 2. Top-right: Scatter plot of budget vs revenue, colored by genre

# 3. Bottom-left: Horizontal bar chart of profit by movie

# 4. Bottom-right: Pie chart of genre distribution

fig.suptitle("Movie Dashboard", fontsize=18, fontweight="bold")
plt.tight_layout()
plt.savefig("movie_dashboard.png", dpi=150, bbox_inches="tight")
plt.show()
```

Challenge: Also create one interactive Plotly chart showing budget vs revenue with hover labels.

## TL;DR

- **Matplotlib** is the foundation: `plt.plot()`, `plt.scatter()`, `plt.bar()`, `plt.hist()`, `plt.pie()`
- Make charts pretty with labels, titles, colors, grid, `tight_layout()`, and `plt.style.use()`
- **Subplots**: `fig, axes = plt.subplots(rows, cols)` for multi-chart dashboards
- **Seaborn** makes statistical charts beautiful with minimal code: `sns.barplot()`, `sns.heatmap()`, `sns.boxplot()`
- **Plotly** creates interactive, browser-based charts: `px.scatter()`, `px.bar()`
- Save charts with `plt.savefig("chart.png", dpi=150)`
- Use pandas `.plot()` for quick exploration, dedicated libraries for polished output
- When in doubt: bar chart for categories, scatter for relationships, histogram for distributions

---

# Chapter 29: Machine Learning 101: Teaching Computers to Learn

> **Sprint 5, Chapter 29** | **12 min read** | **Code: [github link](https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/sprint-5-ai/chapter-29-machine-learning/)**

Teaching ML is like teaching a toddler. You show them examples: "This is a cat. This is a dog. This is a cat." Eventually, they figure out the pattern themselves. You never explicitly explain whiskers or floppy ears - they just *get it* after seeing enough examples. Machine learning works the same way. You give a computer enough data, and it figures out the rules on its own.

You're building machine learning models now. Most people who start coding never get here. Take a second to appreciate that.

## What You'll Learn
- What machine learning actually is (cutting through the hype)
- Three types: supervised, unsupervised, reinforcement
- The scikit-learn workflow: load, split, train, predict, evaluate
- Your first model: predicting house prices
- Train/test split and why it matters
- Measuring how good your model is
- Decision trees: 20 questions, but for data

## Why Should I Care?

Netflix recommends your next binge. Gmail catches spam before you see it. Spotify knows you'll love that song you've never heard. Your phone unlocks with your face. Doctors catch cancer earlier. Self-driving cars navigate streets. All of this is machine learning.

And the code is literally 5 lines. Seriously. I'll show you.

## What ML Is and Isn't

**Machine learning IS:**
- A way to find patterns in data
- Software that improves with more data (instead of more rules)
- Prediction based on past examples

**Machine learning IS NOT:**
- Magic
- Artificial consciousness
- A replacement for understanding your problem
- Always the right tool (sometimes an `if` statement is all you need)

Think of it this way: traditional programming is "here are the rules, apply them to data." Machine learning is "here's the data, figure out the rules."

```
Traditional:  Rules + Data -> Answers
ML:           Data + Answers -> Rules
```

## The Three Types of ML

### 1. Supervised Learning: "Learning with Answers"
You give the computer examples WITH the correct answers. It learns the pattern.
- "Here are 10,000 emails labeled spam or not-spam. Learn to tell the difference."
- "Here are 50,000 house prices with their features. Learn to predict prices."

### 2. Unsupervised Learning: "Finding Patterns"
You give the computer data WITHOUT answers. It finds structure on its own.
- "Here are 100,000 customers. Group them into clusters."
- "Find the weirdos in this data." (Anomaly detection)

### 3. Reinforcement Learning: "Trial and Error"
The computer tries stuff and gets rewards or penalties. Like training a dog with treats.
- Game-playing AI (AlphaGo, chess engines)
- Robot navigation
- Self-driving cars

We'll focus on **supervised learning** because it's the most common, the most practical, and the easiest to start with.

## Installing scikit-learn

```bash
pip install scikit-learn
```

scikit-learn (often imported as `sklearn`) is the most popular ML library in Python. It has a clean, consistent API: every model works the same way. Learn one, you've learned them all.

## The Scikit-Learn Workflow

Every single machine learning project follows this same flow:

```
1. Load your data
2. Split into training and testing sets
3. Choose a model
4. Train the model (fit)
5. Make predictions (predict)
6. Evaluate how good it is
```

That's it. Six steps. Let's do them.

## Your First Model: House Price Prediction

Let's predict house prices based on features like size, bedrooms, and age. This is a **regression** problem - predicting a number.

### Step 1: Load the Data

```python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# Create a sample dataset
np.random.seed(42)
n = 200

data = pd.DataFrame({
    "size_sqft": np.random.randint(800, 4000, n),
    "bedrooms": np.random.randint(1, 6, n),
    "age_years": np.random.randint(0, 50, n),
    "distance_downtown": np.random.uniform(0.5, 20, n).round(1)
})

# Price formula with some noise (this is what the model will try to learn)
data["price"] = (
    data["size_sqft"] * 150 +
    data["bedrooms"] * 20000 -
    data["age_years"] * 1500 -
    data["distance_downtown"] * 5000 +
    np.random.normal(0, 15000, n)  # Random noise
).round(-3)  # Round to nearest thousand

print(data.head())
#    size_sqft  bedrooms  age_years  distance_downtown    price
# 0       2937         2        42                3.2  362000.0
# 1       2235         4        18               16.5  288000.0
# ...

print(data.shape)  # (200, 5)
```

### Step 2: Split Into Features and Target

```python
# Features (X) = what the model sees
# Target (y) = what the model predicts
X = data[["size_sqft", "bedrooms", "age_years", "distance_downtown"]]
y = data["price"]

print(f"Features shape: {X.shape}")  # (200, 4)
print(f"Target shape: {y.shape}")    # (200,)
```

### Step 3: Train/Test Split

This is crucial. You split your data into two parts:
- **Training set** (80%): The model studies this. It's like homework.
- **Test set** (20%): You check the model on data it's never seen. It's the exam.

If you test on the same data you trained on, it's like giving someone the answer key before the test. Of course they'll do well. But can they actually think?

```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"Training set: {X_train.shape[0]} houses")  # 160 houses
print(f"Test set: {X_test.shape[0]} houses")        # 40 houses
```

### Step 4: Train the Model

```python
model = LinearRegression()
model.fit(X_train, y_train)

print("Model trained!")
```

That's it. Two lines. `LinearRegression()` creates the model. `.fit()` trains it. The model just learned the relationship between house features and prices by studying 160 examples.

> **Remember When?** Remember functions from Chapter 10? `model.fit()` and `model.predict()` are just method calls. You've been using `.append()` on lists, `.get()` on dictionaries, `.format()` on strings. This is the same thing. You've been ready for this.

### Step 5: Make Predictions

```python
predictions = model.predict(X_test)

# Compare predictions to actual prices
comparison = pd.DataFrame({
    "Actual": y_test.values[:5],
    "Predicted": predictions[:5].round(),
    "Difference": (y_test.values[:5] - predictions[:5]).round()
})
print(comparison)
#      Actual  Predicted  Difference
# 0  362000.0   358421.0      3579.0
# 1  154000.0   162893.0     -8893.0
# 2  483000.0   471205.0     11795.0
# 3  295000.0   301442.0     -6442.0
# 4  198000.0   205118.0     -7118.0
```

The predictions are close. Not perfect - there's noise in the data - but the model learned the general pattern.

### Step 6: Evaluate

```python
# Mean Absolute Error: on average, how far off are we?
mae = mean_absolute_error(y_test, predictions)
print(f"Average error: ${mae:,.0f}")  # Average error: $11,847

# R-squared: how much of the price variation does our model explain?
r2 = r2_score(y_test, predictions)
print(f"R-squared: {r2:.3f}")  # R-squared: 0.972

# What the model learned (coefficients)
for feature, coef in zip(X.columns, model.coef_):
    print(f"  {feature}: ${coef:,.0f} per unit")
# size_sqft: $150 per unit
# bedrooms: $20,142 per unit
# age_years: -$1,489 per unit
# distance_downtown: -$5,021 per unit
```

An R-squared of 0.972 means the model explains 97.2% of the variation in prices. The coefficients show what the model learned: bigger houses cost more ($150 per sq ft), more bedrooms add value ($20K each), older houses cost less, and farther from downtown costs less. The model figured this out by itself just by looking at examples.

### The Whole Thing in One Block

Here's the entire ML pipeline - load to evaluate:

```python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# 1. Load data
X = data[["size_sqft", "bedrooms", "age_years", "distance_downtown"]]
y = data["price"]

# 2. Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3-4. Create and train
model = LinearRegression()
model.fit(X_train, y_train)

# 5. Predict
predictions = model.predict(X_test)

# 6. Evaluate
print(f"MAE: ${mean_absolute_error(y_test, predictions):,.0f}")
print(f"R2: {r2_score(y_test, predictions):.3f}")
```

Five lines of actual ML code (steps 3-6). Everything else is just loading and preparing data. I told you it was five lines.

## Accuracy, Precision, Recall: How Good Is Your Model?

For **regression** (predicting numbers), we use:
- **MAE** (Mean Absolute Error): Average distance between prediction and reality
- **R-squared**: How much of the variation the model explains (1.0 = perfect)

For **classification** (predicting categories), we use:

```python
from sklearn.metrics import accuracy_score, precision_score, recall_score

# After making predictions on a classification problem:
# accuracy = accuracy_score(y_test, predictions)
# precision = precision_score(y_test, predictions)
# recall = recall_score(y_test, predictions)
```

- **Accuracy**: What percentage of predictions were correct? "Of 100 emails, I got 95 right."
- **Precision**: When I said "spam," how often was I right? "Of the 20 I called spam, 18 actually were."
- **Recall**: Of all the actual spam, how much did I catch? "There were 25 spam emails, and I caught 18."

Think of it as a doctor checking for a disease:
- **Precision**: "When I say you're sick, I'm usually right." (Avoids false alarms)
- **Recall**: "If you're sick, I'll catch it." (Doesn't miss cases)

You want both to be high. In medicine, recall matters more (don't miss a diagnosis). In spam filtering, precision matters more (don't send real emails to spam).

## Decision Trees: 20 Questions for Data

Linear regression predicts numbers. But what if you want to predict categories? Like "spam or not spam?" or "will this customer churn?" That's **classification**.

Decision trees work exactly like the game 20 Questions. "Is the email from a known contact? Yes. Does it contain the word 'lottery'? No. Does it have attachments? Yes..." The tree keeps asking questions until it reaches a conclusion.

```python
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd
import numpy as np

# Create sample data: predict if someone will buy a product
np.random.seed(42)
n = 300

data = pd.DataFrame({
    "age": np.random.randint(18, 70, n),
    "income": np.random.randint(20000, 120000, n),
    "visits_per_month": np.random.randint(0, 30, n),
    "time_on_site_min": np.random.uniform(0.5, 45, n).round(1)
})

# Create target: bought or not (1 = yes, 0 = no)
buy_probability = (
    (data["income"] > 50000).astype(int) * 0.3 +
    (data["visits_per_month"] > 10).astype(int) * 0.3 +
    (data["time_on_site_min"] > 15).astype(int) * 0.3 +
    np.random.uniform(0, 0.3, n)
)
data["bought"] = (buy_probability > 0.5).astype(int)

print(f"Buyers: {data['bought'].sum()} / {len(data)}")

# Split
X = data[["age", "income", "visits_per_month", "time_on_site_min"]]
y = data["bought"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Decision Tree
tree = DecisionTreeClassifier(max_depth=4, random_state=42)
tree.fit(X_train, y_train)

# Predict
predictions = tree.predict(X_test)

# Evaluate
print(f"\nAccuracy: {accuracy_score(y_test, predictions):.1%}")
print(f"\nDetailed Report:")
print(classification_report(y_test, predictions, target_names=["Didn't Buy", "Bought"]))
```

Output:

```
Accuracy: 86.7%

Detailed Report:
              precision    recall  f1-score   support
 Didn't Buy       0.83      0.80      0.82        25
     Bought       0.89      0.91      0.90        35
   accuracy                           0.87        60
```

86.7% accuracy. The model learned who's likely to buy a product just from age, income, visits, and time on site.

### Seeing What the Tree Learned

```python
# Feature importance - which features matter most?
importances = pd.Series(tree.feature_importances_, index=X.columns)
print(importances.sort_values(ascending=False))
# time_on_site_min     0.38
# visits_per_month     0.27
# income               0.25
# age                  0.10
```

Time on site is the most important predictor. Makes sense - people who spend more time browsing are more likely to buy.

```python
# Visualize the tree (optional but cool)
from sklearn.tree import export_text

tree_rules = export_text(tree, feature_names=list(X.columns))
print(tree_rules)
# |-- time_on_site_min <= 15.35
# |   |-- visits_per_month <= 10.50
# |   |   |-- income <= 49721.50
# |   |   |   |-- class: 0
# |   |   |-- income > 49721.50
# |   |   |   |-- class: 0
# |   |-- visits_per_month > 10.50
# |   |   |-- ...
```

You can literally read the decision logic. "If time on site is less than 15 minutes AND visits are less than 11 AND income is under $50K, predict they won't buy." This interpretability is why decision trees are so popular in business.

## Trying Different Models

The beauty of scikit-learn is that every model has the exact same interface. Swap in a different model and the rest of your code stays identical:

```python
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier

models = {
    "Decision Tree": DecisionTreeClassifier(max_depth=4, random_state=42),
    "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42),
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "K-Nearest Neighbors": KNeighborsClassifier(n_neighbors=5)
}

for name, model in models.items():
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)
    print(f"{name}: {acc:.1%}")

# Decision Tree:        86.7%
# Random Forest:        90.0%
# Logistic Regression:  85.0%
# K-Nearest Neighbors:  83.3%
```

Same three lines for every model: `.fit()`, `.predict()`, evaluate. Random Forest wins here because it's like a committee of decision trees voting together. But the point is: **you can swap models like swapping batteries.** Learn the scikit-learn API once, use any model.

> **Don't Panic:** Machine learning sounds like sci-fi. But the code is literally the same pattern every time: create model, `.fit(X_train, y_train)`, `.predict(X_test)`, check accuracy. The math inside the models is complex. The code to use them is not. You don't need to understand how an engine works to drive a car.

## Your Turn: Spam Classifier

Build a spam classifier. Create `spam_classifier.py`:

```python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Create sample email data
np.random.seed(42)
n = 500

data = pd.DataFrame({
    "word_count": np.random.randint(5, 500, n),
    "contains_free": np.random.choice([0, 1], n, p=[0.7, 0.3]),
    "contains_winner": np.random.choice([0, 1], n, p=[0.85, 0.15]),
    "num_exclamation": np.random.randint(0, 20, n),
    "num_links": np.random.randint(0, 10, n),
    "from_contact": np.random.choice([0, 1], n, p=[0.4, 0.6]),
    "has_unsubscribe": np.random.choice([0, 1], n, p=[0.6, 0.4])
})

# Create target: is_spam
spam_score = (
    data["contains_free"] * 2 +
    data["contains_winner"] * 3 +
    data["num_exclamation"] * 0.2 +
    data["num_links"] * 0.3 -
    data["from_contact"] * 2 -
    (data["word_count"] > 50).astype(int) * 0.5 +
    np.random.normal(0, 1, n)
)
data["is_spam"] = (spam_score > 2).astype(int)

# 1. Split features (X) and target (y)

# 2. Do a train/test split (80/20)

# 3. Train a DecisionTreeClassifier

# 4. Print accuracy

# 5. Print the full classification report

# 6. Which features are most important for detecting spam?

# 7. BONUS: Try a RandomForestClassifier. Is it better?
```

Expected results:
- Decision Tree accuracy: around 85-90%
- Random Forest accuracy: around 88-93%
- Top spam indicators: "contains_winner", "contains_free", "from_contact" (negative)

## TL;DR

- Machine learning = computers learning patterns from data instead of following explicit rules
- **Supervised learning**: give it examples with answers; it learns to predict on new data
- The scikit-learn workflow: load data, split (train/test), create model, `.fit()`, `.predict()`, evaluate
- **Train/test split** prevents overfitting - always test on data the model hasn't seen
- **Linear Regression** predicts numbers; **Decision Trees** and others predict categories
- **Accuracy** = percentage correct; **Precision** = "when I said yes, was I right?"; **Recall** = "of all the yeses, did I catch them?"
- **Feature importance** tells you which inputs matter most
- scikit-learn's API is consistent: every model uses `.fit()` and `.predict()` - learn one, know them all
- The ML code itself is 5 lines. The hard part is preparing good data and choosing what to predict
- You just built machine learning models. You. This chapter. Right now. Let that sink in.

---

# Chapter 30: AI APIs & LLMs: Building with OpenAI, Gemini & More

> **Sprint 5, Chapter 30** | **12 min read** | **Code: [github link](https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/sprint-5-ai/chapter-30-ai-apis/)**

LLMs are like having a very smart intern. They can write, summarize, translate, and answer questions - but they need clear instructions and sometimes make stuff up with total confidence. Sound like anyone you know from college group projects? The key difference: this intern works 24/7, never complains, and you can build an entire product around them.

You're about to build apps that use the same technology behind ChatGPT. Take a moment. This is genuinely cool.

## What You'll Learn
- What LLMs are (simple, no PhD required)
- OpenAI API setup and your first API call
- Chat completions - the core of everything
- System, user, and assistant messages
- Temperature - the creativity dial
- Tokens - how AI measures text
- Streaming responses
- Google Gemini API basics
- Prompt engineering fundamentals

## Why Should I Care?

ChatGPT, Gemini, Claude - you've used them. Now you're going to build with them. This is the most in-demand skill in tech right now. Job postings that mention "LLM" or "AI integration" have exploded. Companies are building AI features into everything: customer support bots, content generators, code assistants, data analyzers. And the developers building these features? They're using the exact APIs you're about to learn.

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
5. Copy it immediately - you won't see it again

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

> **Don't Panic:** The API is literally just sending text and getting text back. If you've used the `requests` library (Chapter 21), this is the same concept - you send data to a server, it sends data back. The OpenAI library just wraps that into a clean interface.

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

LLMs don't read words - they read **tokens**. A token is roughly 3/4 of a word. "Hello, world!" is about 3 tokens. A page of text is around 500-700 tokens.

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

> **Pro Tip:** `gpt-4o-mini` is cheap and fast - perfect for learning and most applications. `gpt-4o` is more capable but costs more. Start with mini, upgrade only if you need better quality.

## Streaming Responses

Instead of waiting for the entire response, you can stream it word by word - just like ChatGPT does:

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

> **Pro Tip:** You don't have to pick one. Many production apps use multiple LLMs - OpenAI for some tasks, Gemini for others, Claude for yet others. The APIs are similar enough that switching is easy.

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

Let's put it all together - a command-line chatbot:

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

- LLMs are sophisticated text predictors trained on massive amounts of data - not magic, not thinking
- **OpenAI API**: `pip install openai`, set `OPENAI_API_KEY`, call `client.chat.completions.create()`
- Messages have roles: **system** (personality), **user** (you), **assistant** (AI's responses)
- **Temperature**: 0 = focused/consistent, 1 = creative/varied
- **Tokens**: how AI measures text (~4 characters per token); you're billed per token
- **Streaming**: `stream=True` gives you the typing effect
- **Gemini** works similarly: `pip install google-generativeai`, same concepts
- **Prompt engineering** matters: be specific, give roles, show examples, specify format
- The API is just sending text and getting text back - you already know how to do this
- You're building AI-powered applications now. This is not a drill.

---

# Chapter 31: LangChain & AI Agents: The Next Level

> **Sprint 5, Chapter 31** | **12 min read** | **Code: [github link](https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/sprint-5-ai/chapter-31-langchain/)**

If the OpenAI API is a smart employee, LangChain is the project manager that organizes their work, gives them memory, and lets them use tools. In Chapter 30, you learned to have a conversation with an AI. In this chapter, you'll learn to give that AI access to your own data, remember past conversations, and chain multiple steps together. This is what companies are building RIGHT NOW.

## What You'll Learn
- What LangChain is and why it exists
- ChatOpenAI setup
- PromptTemplates - reusable instructions
- Chains - connecting the dots
- Memory - AI that remembers
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
- `langchain` - the core framework
- `langchain-openai` - OpenAI integration
- `langchain-community` - community integrations (document loaders, etc.)
- `chromadb` - a vector database (more on this soon)

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

# Conversation - the AI remembers!
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

Why overlap? Because if a sentence gets cut in half, the overlap ensures both chunks contain the complete thought. It's like how book pages overlap topics - you don't want to lose context at the break point.

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

Now connect everything - user asks a question, relevant chunks are retrieved, and the LLM answers:

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

Notice that last answer. The AI correctly says it doesn't know because the information isn't in the documents. That's the power of RAG - the AI stays grounded in your data instead of making things up.

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
- **Embeddings** turn text into numbers that capture meaning - similar meanings get similar numbers
- **Vector stores** (Chroma) are search engines for meaning, not just keywords
- The RAG workflow: `TextLoader` -> `TextSplitter` -> `Embeddings` -> `Chroma` -> `RetrievalChain`
- RAG keeps AI grounded - it answers from YOUR data and says "I don't know" when the answer isn't there
- This is what companies are building right now: chatbots with memory, document Q&A, AI agents with tools
- You just learned the hottest technology in tech. Seriously. Go update your resume.

---

# Chapter 32: Automation with Python: Let the Computer Do the Work

> **Sprint 5, Chapter 32** | **12 min read** | **Code: [github link](https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/sprint-5-ai/chapter-32-automation/)**

Why spend 10 minutes doing something manually when you can spend 2 hours automating it? ...Wait, actually that math checks out over time. If you automate a 10-minute daily task, you save 40+ hours a year. Automate five tasks and you've saved an entire work week. This is the chapter where Python starts doing your job while you get coffee.

## What You'll Learn
- File operations with os, shutil, pathlib
- Bulk file renaming
- Email automation with smtplib
- Scheduling tasks with the schedule library
- Selenium - browser automation basics
- Three practical recipes you can use immediately

## Why Should I Care?

Automate reports. Organize a messy Downloads folder. Send emails at 9 AM without being awake at 9 AM. Scrape data on a schedule. Fill out web forms. Rename 500 files in 2 seconds. Every office worker has repetitive computer tasks that eat hours every week. Python can do all of them. While you sleep.

The irony of automation: you feel guilty the first time your script does in 3 seconds what used to take you 20 minutes. Then you feel like a genius. Then you automate everything.

## File Operations: os, shutil, pathlib

### pathlib: The Modern Way

`pathlib` is the best way to work with files and folders in Python. It's clean, readable, and cross-platform.

```python
from pathlib import Path

# Current directory
here = Path(".")
print(here.resolve())  # Full path: C:\Users\you\projects

# Home directory
home = Path.home()
print(home)  # C:\Users\you (Windows) or /home/you (Linux)

# Build paths (no more string concatenation!)
downloads = Path.home() / "Downloads"
print(downloads)  # C:\Users\you\Downloads

# Check if a path exists
print(downloads.exists())  # True
print(downloads.is_dir())  # True

# List all files in a directory
for item in downloads.iterdir():
    print(item.name)

# Find specific files (glob patterns)
for pdf in downloads.glob("*.pdf"):
    print(f"Found PDF: {pdf.name}")

# Recursive search (all subdirectories too)
for py_file in Path(".").rglob("*.py"):
    print(f"Python file: {py_file}")
```

### File Information

```python
from pathlib import Path
import os

file = Path("example.txt")

# Create a test file
file.write_text("Hello, automation!")

# File info
print(f"Name: {file.name}")           # example.txt
print(f"Extension: {file.suffix}")     # .txt
print(f"Stem (no ext): {file.stem}")   # example
print(f"Size: {file.stat().st_size} bytes")
print(f"Exists: {file.exists()}")

# Read content
content = file.read_text()
print(content)  # Hello, automation!
```

### Creating, Moving, Copying, Deleting

```python
from pathlib import Path
import shutil

# Create directories
Path("organized/reports").mkdir(parents=True, exist_ok=True)
Path("organized/images").mkdir(parents=True, exist_ok=True)
Path("organized/data").mkdir(parents=True, exist_ok=True)

# Move a file
source = Path("report.pdf")
destination = Path("organized/reports/report.pdf")
if source.exists():
    shutil.move(str(source), str(destination))

# Copy a file
shutil.copy2("original.txt", "backup.txt")  # copy2 preserves metadata

# Copy entire directory
shutil.copytree("my_project", "my_project_backup")

# Delete a file
Path("temp_file.txt").unlink(missing_ok=True)

# Delete an empty directory
Path("empty_folder").rmdir()

# Delete a directory with contents (careful!)
shutil.rmtree("old_project")  # Gone forever. No recycle bin. Be careful.
```

> **Warning:** `shutil.rmtree()` permanently deletes a folder and everything in it. No undo. No recycle bin. Triple-check your path before running this. Seriously.

## Practical Recipe 1: File Organizer

Your Downloads folder is chaos. Let's fix that:

```python
from pathlib import Path
import shutil

def organize_downloads():
    """Sort files in Downloads folder by type."""

    downloads = Path.home() / "Downloads"

    # Map extensions to folder names
    categories = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".svg", ".webp", ".ico"],
        "Documents": [".pdf", ".doc", ".docx", ".txt", ".xlsx", ".csv", ".pptx"],
        "Videos": [".mp4", ".avi", ".mkv", ".mov", ".wmv"],
        "Audio": [".mp3", ".wav", ".flac", ".aac"],
        "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
        "Code": [".py", ".js", ".html", ".css", ".json", ".xml"],
        "Installers": [".exe", ".msi", ".dmg"],
    }

    moved_count = 0

    for file in downloads.iterdir():
        if file.is_dir():
            continue  # Skip folders

        # Find which category this file belongs to
        ext = file.suffix.lower()
        target_folder = "Other"  # Default

        for category, extensions in categories.items():
            if ext in extensions:
                target_folder = category
                break

        # Create target folder if it doesn't exist
        target_path = downloads / target_folder
        target_path.mkdir(exist_ok=True)

        # Move the file
        destination = target_path / file.name

        # Handle duplicates
        if destination.exists():
            destination = target_path / f"{file.stem}_copy{file.suffix}"

        shutil.move(str(file), str(destination))
        moved_count += 1
        print(f"  {file.name} -> {target_folder}/")

    print(f"\nDone! Organized {moved_count} files.")

# Run it!
organize_downloads()
```

Run this once and your Downloads folder goes from chaos to organized folders. Run it weekly (or schedule it - we'll get there) and it stays clean forever.

## Bulk File Renaming

Got 200 photos named `IMG_20240315_001.jpg`? Let's fix that:

```python
from pathlib import Path

def rename_photos(folder, prefix="vacation"):
    """Rename all images in a folder with a clean pattern."""

    folder = Path(folder)
    image_extensions = {".jpg", ".jpeg", ".png"}

    # Get all images, sorted by name
    images = sorted(
        f for f in folder.iterdir()
        if f.suffix.lower() in image_extensions
    )

    print(f"Found {len(images)} images")

    for i, image in enumerate(images, 1):
        new_name = f"{prefix}_{i:03d}{image.suffix.lower()}"
        new_path = folder / new_name

        image.rename(new_path)
        print(f"  {image.name} -> {new_name}")

    print(f"\nRenamed {len(images)} files!")

# Example usage:
# rename_photos("C:/Users/you/Photos/Beach Trip", prefix="beach_2024")
# Result: beach_2024_001.jpg, beach_2024_002.jpg, beach_2024_003.jpg...
```

Another common pattern - removing spaces from filenames:

```python
from pathlib import Path

def clean_filenames(folder):
    """Replace spaces and special chars in filenames."""
    folder = Path(folder)

    for file in folder.iterdir():
        if file.is_file():
            clean_name = file.name.replace(" ", "_").replace("(", "").replace(")", "")
            clean_name = clean_name.lower()

            if clean_name != file.name:
                file.rename(folder / clean_name)
                print(f"  '{file.name}' -> '{clean_name}'")
```

## Email Automation

Send emails from Python. Perfect for automated reports, alerts, or notifications.

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(to_email, subject, body):
    """Send an email using Gmail."""

    # Your email credentials
    sender_email = "your_email@gmail.com"
    app_password = "your-app-password"  # NOT your regular password!

    # Create the email
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "html"))

    # Send it
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()  # Encrypt the connection
        server.login(sender_email, app_password)
        server.send_message(msg)

    print(f"Email sent to {to_email}!")

# Usage:
send_email(
    to_email="colleague@example.com",
    subject="Weekly Report - Auto-generated",
    body="""
    <h2>Weekly Sales Report</h2>
    <p>Total sales: <b>$45,230</b></p>
    <p>Growth: <b>+12%</b> vs last week</p>
    <p><i>This report was generated automatically by Python.</i></p>
    """
)
```

> **Important - App Passwords:** Gmail doesn't let you use your regular password with smtplib. You need an **App Password**:
> 1. Go to your Google Account settings
> 2. Security -> 2-Step Verification (enable it if you haven't)
> 3. Search for "App passwords"
> 4. Generate a new app password for "Mail"
> 5. Use that 16-character password in your code
>
> Never hardcode the password. Use environment variables or a `.env` file, just like with API keys.

### Sending Emails with Attachments

```python
from email.mime.base import MIMEBase
from email import encoders
from pathlib import Path

def send_report_with_attachment(to_email, subject, body, attachment_path):
    """Send an email with a file attachment."""

    sender_email = "your_email@gmail.com"
    app_password = "your-app-password"

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "html"))

    # Attach the file
    file_path = Path(attachment_path)
    with open(file_path, "rb") as f:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(f.read())
        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition",
            f"attachment; filename={file_path.name}"
        )
        msg.attach(part)

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, app_password)
        server.send_message(msg)

    print(f"Email with attachment sent to {to_email}!")

# send_report_with_attachment(
#     "boss@company.com",
#     "Monthly Report",
#     "<p>Please find the report attached.</p>",
#     "reports/monthly_report.pdf"
# )
```

## Scheduling Tasks

The `schedule` library makes it easy to run Python functions at specific times:

```bash
pip install schedule
```

```python
import schedule
import time

def morning_report():
    print("Generating morning report...")
    # Your report logic here

def organize_files():
    print("Organizing downloads folder...")
    # Your file organizer logic here

def backup_data():
    print("Backing up data...")
    # Your backup logic here

# Schedule tasks
schedule.every().day.at("09:00").do(morning_report)
schedule.every().friday.at("17:00").do(organize_files)
schedule.every().hour.do(backup_data)

# More scheduling options:
schedule.every(10).minutes.do(lambda: print("Still running!"))
schedule.every().monday.do(lambda: print("Happy Monday!"))
schedule.every().day.at("23:59").do(lambda: print("End of day"))

print("Scheduler running. Press Ctrl+C to stop.")

while True:
    schedule.run_pending()
    time.sleep(60)  # Check every minute
```

The `while True` loop keeps the script running. It checks every 60 seconds if any scheduled task is due. Run this script in the background and your tasks execute automatically.

> **Pro Tip:** For production scheduling on a server, use `cron` (Linux/Mac) or Task Scheduler (Windows) to run your Python scripts. The `schedule` library is great for development and simple automation, but OS-level schedulers are more reliable for 24/7 operation.

## Selenium: Browser Automation

Selenium controls a web browser programmatically. It can click buttons, fill forms, navigate pages, and scrape dynamic content.

```bash
pip install selenium webdriver-manager
```

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up Chrome browser
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Navigate to a website
driver.get("https://www.python.org")

# Find elements and interact
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("list comprehension")
search_box.send_keys(Keys.RETURN)

time.sleep(2)  # Wait for results to load

# Get results
results = driver.find_elements(By.CSS_SELECTOR, ".list-recent-events li")
for result in results[:5]:
    print(result.text)

# Take a screenshot
driver.save_screenshot("python_search.png")

# Close the browser
driver.quit()
```

### Practical Example: Automated Form Filler

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

def fill_form(data):
    """Fill out a web form automatically."""

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        driver.get("https://example.com/form")

        # Wait for the form to load
        wait = WebDriverWait(driver, 10)

        # Fill in fields
        name_field = wait.until(EC.presence_of_element_located((By.ID, "name")))
        name_field.send_keys(data["name"])

        email_field = driver.find_element(By.ID, "email")
        email_field.send_keys(data["email"])

        message_field = driver.find_element(By.ID, "message")
        message_field.send_keys(data["message"])

        # Click submit
        submit_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        submit_btn.click()

        time.sleep(2)
        print("Form submitted successfully!")

    finally:
        driver.quit()

# fill_form({
#     "name": "Alex Smith",
#     "email": "alex@example.com",
#     "message": "This was submitted by a Python script!"
# })
```

> **Pro Tip:** Selenium is powerful but slow compared to `requests`. Use `requests` for APIs and simple page scraping (Chapter 21). Use Selenium only when you need to interact with JavaScript-heavy pages, click buttons, or fill forms.

## Practical Recipe 2: Automated Report Generator

Combine pandas, matplotlib, and email into one automated workflow:

```python
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from datetime import datetime

def generate_weekly_report():
    """Generate a sales report with chart and summary."""

    # Step 1: Load/generate data
    data = pd.DataFrame({
        "day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
        "sales": [1200, 1450, 1380, 1560, 1890, 2100, 1750],
        "visitors": [450, 520, 490, 580, 620, 710, 590]
    })

    # Step 2: Calculate stats
    total_sales = data["sales"].sum()
    avg_sales = data["sales"].mean()
    best_day = data.loc[data["sales"].idxmax(), "day"]
    conversion_rate = (data["sales"].sum() / data["visitors"].sum() * 100)

    # Step 3: Create chart
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    ax1.bar(data["day"], data["sales"], color="steelblue", edgecolor="black")
    ax1.set_title("Daily Sales", fontweight="bold")
    ax1.set_ylabel("Sales ($)")

    ax2.plot(data["day"], data["visitors"], marker="o", color="coral", linewidth=2)
    ax2.set_title("Daily Visitors", fontweight="bold")
    ax2.set_ylabel("Visitors")
    ax2.grid(True, alpha=0.3)

    fig.suptitle(f"Weekly Report - {datetime.now().strftime('%B %d, %Y')}",
                 fontsize=14, fontweight="bold")
    plt.tight_layout()

    chart_path = Path("weekly_report.png")
    plt.savefig(chart_path, dpi=150, bbox_inches="tight")
    plt.close()

    # Step 4: Create email body
    report_html = f"""
    <h2>Weekly Sales Report</h2>
    <p>Generated: {datetime.now().strftime('%B %d, %Y at %I:%M %p')}</p>
    <table border="1" cellpadding="8" style="border-collapse: collapse;">
        <tr><td><b>Total Sales</b></td><td>${total_sales:,}</td></tr>
        <tr><td><b>Daily Average</b></td><td>${avg_sales:,.0f}</td></tr>
        <tr><td><b>Best Day</b></td><td>{best_day}</td></tr>
        <tr><td><b>Conversion Rate</b></td><td>{conversion_rate:.1f}%</td></tr>
    </table>
    <p><i>Chart attached. This report was auto-generated with Python.</i></p>
    """

    print(f"Report generated!")
    print(f"Total Sales: ${total_sales:,}")
    print(f"Best Day: {best_day}")
    print(f"Chart saved: {chart_path}")

    # Step 5: Send email (uncomment when ready)
    # send_report_with_attachment(
    #     "boss@company.com",
    #     f"Weekly Sales Report - {datetime.now().strftime('%B %d')}",
    #     report_html,
    #     str(chart_path)
    # )

    return report_html

generate_weekly_report()
```

## Practical Recipe 3: Watchdog - Monitor a Folder for Changes

```python
# pip install watchdog
from pathlib import Path
import time
import shutil

def watch_folder(watch_path, process_func, check_interval=5):
    """Watch a folder and process new files."""

    watch_path = Path(watch_path)
    seen_files = set(f.name for f in watch_path.iterdir() if f.is_file())

    print(f"Watching {watch_path} for new files...")
    print(f"Currently {len(seen_files)} files. Waiting for new ones...")

    try:
        while True:
            current_files = set(f.name for f in watch_path.iterdir() if f.is_file())
            new_files = current_files - seen_files

            for filename in new_files:
                filepath = watch_path / filename
                print(f"\nNew file detected: {filename}")
                process_func(filepath)

            seen_files = current_files
            time.sleep(check_interval)

    except KeyboardInterrupt:
        print("\nStopped watching.")

def process_new_file(filepath):
    """What to do when a new file appears."""
    print(f"  Processing: {filepath.name}")
    print(f"  Size: {filepath.stat().st_size} bytes")
    print(f"  Type: {filepath.suffix}")

    # Example: move PDFs to a reports folder
    if filepath.suffix.lower() == ".pdf":
        dest = Path.home() / "Documents" / "AutoReports" / filepath.name
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(str(filepath), str(dest))
        print(f"  Copied to: {dest}")

# watch_folder(Path.home() / "Downloads", process_new_file)
```

> **Fun Fact:** The original name for Python came from Monty Python's Flying Circus, not the snake. Guido van Rossum, Python's creator, was a fan of the show and wanted a name that was "short, unique, and slightly mysterious." The snake imagery came later, but the language was named after a bunch of British comedians doing silly sketches. Which honestly explains a lot about Python's personality.

## Putting It All Together

Here's the ultimate automation combo - a scheduled script that:
1. Organizes your Downloads folder
2. Generates a report
3. Emails it to you

```python
import schedule
import time

def daily_automation():
    """Run all daily automation tasks."""
    print("\n-- Running Daily Automation --")

    # 1. Organize downloads
    print("\n1. Organizing files...")
    # organize_downloads()  # From earlier in this chapter

    # 2. Generate report
    print("\n2. Generating report...")
    # generate_weekly_report()  # From earlier in this chapter

    # 3. Send email
    print("\n3. Sending report...")
    # send_email(...)  # From earlier in this chapter

    print("\n-- Daily Automation Complete --")

# Run every weekday at 9 AM
schedule.every().monday.at("09:00").do(daily_automation)
schedule.every().tuesday.at("09:00").do(daily_automation)
schedule.every().wednesday.at("09:00").do(daily_automation)
schedule.every().thursday.at("09:00").do(daily_automation)
schedule.every().friday.at("09:00").do(daily_automation)

print("Automation scheduler running...")
print("Tasks scheduled for weekdays at 9:00 AM")
print("Press Ctrl+C to stop\n")

while True:
    schedule.run_pending()
    time.sleep(60)
```

## Your Turn: Automated Report Emailer

Create `auto_report.py` that combines everything from this chapter:

```python
# 1. Create a function that scans a folder and counts files by type
#    (how many PDFs, images, CSVs, etc.)

# 2. Create a function that generates a bar chart of the file counts

# 3. Create a function that formats the results as an HTML email body

# 4. (Optional) Set up email sending with smtplib

# 5. (Optional) Schedule it to run every Friday at 5 PM

# Starter code:
from pathlib import Path
import matplotlib.pyplot as plt
from collections import Counter
from datetime import datetime

def scan_folder(folder_path):
    """Count files by extension in a folder."""
    folder = Path(folder_path)
    extensions = Counter()

    for file in folder.iterdir():
        if file.is_file():
            ext = file.suffix.lower() if file.suffix else "no extension"
            extensions[ext] += 1

    return dict(extensions.most_common(10))  # Top 10 types

def create_chart(file_counts, output_path="folder_report.png"):
    """Create a bar chart of file types."""
    # Your code here: plt.bar(), labels, title, save
    pass

def create_email_body(folder_path, file_counts):
    """Generate an HTML email with the report."""
    # Your code here: HTML table with file counts
    pass

# Test it
counts = scan_folder(Path.home() / "Downloads")
print(counts)
# {'.pdf': 23, '.jpg': 45, '.xlsx': 12, ...}
```

## TL;DR

- **pathlib** is the modern way to work with files: `Path.home() / "Downloads"`, `path.glob("*.pdf")`
- **shutil** handles moving, copying, and deleting files and folders
- Bulk rename files with loops: `path.rename(new_path)`
- **smtplib** sends emails from Python - use App Passwords for Gmail, never hardcode credentials
- **schedule** runs functions at specific times: `schedule.every().day.at("09:00").do(task)`
- **Selenium** automates web browsers: clicking, typing, filling forms, taking screenshots
- Combine pandas + matplotlib + email for automated reporting pipelines
- Automation gets better over time - start with one annoying task, automate it, then add more
- Be careful with `shutil.rmtree()` - it permanently deletes folders with no undo
- You just learned to make your computer work while you sleep. Welcome to the good life.

---

# Sprint 5 Checkpoint: AI-Powered Resume Analyzer

> **Sprint 5 Project** | **60-90 min build** | **Code: [github link](https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/sprint-5-ai/sprint-5-checkpoint/)**

Sprint 5 COMPLETE. All 5 Sprints DONE.

You went from `print("Hello, World!")` to building AI applications. Read that sentence again. Let it sink in. You started this book not knowing what a variable was. Now you're using NumPy, pandas, machine learning, and large language models. You're analyzing data, making predictions, and building AI-powered tools.

Most people who start learning to code quit in week one. You didn't. Most people who make it past the basics never touch AI. You just finished an entire sprint on it. You're not a beginner. You're not even intermediate. You're someone who can build real things with Python AND AI.

Now let's prove it. One final sprint project. Then you're ready for the Final Projects.

## The Project: AI-Powered Resume Analyzer

You're going to build an application that:
1. Reads a resume (text file or PDF)
2. Analyzes it with pandas and basic NLP
3. Visualizes the findings with matplotlib
4. Uses an LLM to provide feedback and suggestions
5. Generates an automated report

This project uses skills from every chapter in Sprint 5.

## Skills Used

| Chapter | Skill | How It's Used |
|-----|----|--------|
| 26 - NumPy | Array operations | Scoring calculations, statistics |
| 27 - Pandas | Data analysis | Structuring resume data, analysis |
| 28 - Visualization | Charts | Skills chart, experience timeline |
| 29 - ML | Classification | Categorizing skills, job matching |
| 30 - AI APIs | LLM integration | Resume feedback, improvement tips |
| 31 - LangChain | RAG | Comparing resume against job descriptions |
| 32 - Automation | File handling, reporting | Reading files, generating report |

## Step-by-Step Build Guide

### Step 1: Set Up the Project

```python
# resume_analyzer.py
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import json
import re

# Optional (if you have API keys set up):
# from openai import OpenAI
# client = OpenAI()
```

Create a sample resume to work with:

```python
sample_resume = """
ALEX JOHNSON
Software Developer | alex.johnson@email.com | San Francisco, CA

SUMMARY
Passionate software developer with 4 years of experience in full-stack
web development. Skilled in Python, JavaScript, and cloud technologies.
Looking for a senior developer role at a forward-thinking company.

EXPERIENCE

Software Developer - TechCorp Inc. (2022-Present)
- Built REST APIs using Python and Flask serving 10,000+ daily users
- Implemented CI/CD pipelines with GitHub Actions reducing deploy time by 60%
- Led migration from monolith to microservices architecture
- Mentored 3 junior developers

Junior Developer - StartupXYZ (2020-2022)
- Developed front-end features using React and TypeScript
- Built automated testing suite increasing code coverage from 40% to 85%
- Collaborated with design team on UI/UX improvements
- Participated in agile sprints and code reviews

EDUCATION
B.S. Computer Science - UC Berkeley (2020)
Relevant coursework: Data Structures, Algorithms, Machine Learning, Databases

SKILLS
Python, JavaScript, TypeScript, React, Flask, Django, PostgreSQL, MongoDB,
Docker, Kubernetes, AWS, Git, CI/CD, REST APIs, GraphQL, Agile, Scrum

CERTIFICATIONS
- AWS Solutions Architect Associate (2023)
- Google Professional Cloud Developer (2022)
"""

# Save it
Path("sample_resume.txt").write_text(sample_resume)
print("Sample resume saved!")
```

### Step 2: Parse the Resume (Chapter 32 - File Handling)

```python
def load_resume(file_path):
    """Load a resume from a text file."""
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Resume not found: {file_path}")

    content = path.read_text(encoding="utf-8")
    print(f"Loaded resume: {path.name} ({len(content)} characters)")
    return content

def extract_sections(resume_text):
    """Split resume into sections based on headers."""
    sections = {}
    current_section = "HEADER"
    current_content = []

    for line in resume_text.strip().split("\n"):
        # Check if line is a section header (all caps, short)
        if line.strip().isupper() and len(line.strip()) < 30 and len(line.strip()) > 2:
            if current_content:
                sections[current_section] = "\n".join(current_content).strip()
            current_section = line.strip()
            current_content = []
        else:
            current_content.append(line)

    # Don't forget the last section
    if current_content:
        sections[current_section] = "\n".join(current_content).strip()

    return sections

# Test it
resume = load_resume("sample_resume.txt")
sections = extract_sections(resume)
for section, content in sections.items():
    print(f"\n-- {section} --")
    print(content[:100] + "..." if len(content) > 100 else content)
```

### Step 3: Analyze Skills (Chapters 26 & 27 - NumPy & Pandas)

```python
def analyze_skills(resume_text):
    """Extract and categorize skills from a resume."""

    # Define skill categories
    skill_categories = {
        "Programming Languages": ["python", "javascript", "typescript", "java",
                                   "c++", "go", "rust", "ruby", "php", "swift"],
        "Frontend": ["react", "angular", "vue", "html", "css", "tailwind",
                      "next.js", "svelte"],
        "Backend": ["flask", "django", "fastapi", "node.js", "express",
                     "spring", "rest apis", "graphql"],
        "Databases": ["postgresql", "mysql", "mongodb", "redis", "sqlite",
                       "dynamodb", "elasticsearch"],
        "Cloud & DevOps": ["aws", "gcp", "azure", "docker", "kubernetes",
                           "ci/cd", "terraform", "github actions"],
        "Data & AI": ["machine learning", "pandas", "numpy", "tensorflow",
                       "pytorch", "scikit-learn", "data analysis"],
        "Soft Skills": ["agile", "scrum", "mentoring", "leadership",
                         "collaboration", "communication"]
    }

    resume_lower = resume_text.lower()
    found_skills = {}
    all_found = []

    for category, skills in skill_categories.items():
        matches = [s for s in skills if s in resume_lower]
        if matches:
            found_skills[category] = matches
            all_found.extend(matches)

    # Create a DataFrame
    skill_data = []
    for category, skills in found_skills.items():
        for skill in skills:
            skill_data.append({"category": category, "skill": skill})

    df = pd.DataFrame(skill_data)

    # Calculate scores using NumPy
    category_counts = df["category"].value_counts()
    scores = np.array(category_counts.values)
    total_skills = scores.sum()
    percentages = (scores / total_skills * 100).round(1)

    print(f"\nTotal skills found: {total_skills}")
    print(f"\nSkills by category:")
    for cat, count, pct in zip(category_counts.index, scores, percentages):
        print(f"  {cat}: {count} skills ({pct}%)")

    return df, found_skills

skills_df, found_skills = analyze_skills(resume)
```

### Step 4: Visualize the Analysis (Chapter 28 - Visualization)

```python
def create_resume_dashboard(skills_df, sections, output_path="resume_dashboard.png"):
    """Create a visual dashboard for the resume analysis."""

    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # 1. Skills by Category (Bar Chart)
    category_counts = skills_df["category"].value_counts()
    colors = plt.cm.Set3(np.linspace(0, 1, len(category_counts)))
    axes[0, 0].barh(category_counts.index, category_counts.values, color=colors)
    axes[0, 0].set_title("Skills by Category", fontsize=13, fontweight="bold")
    axes[0, 0].set_xlabel("Number of Skills")

    # 2. Skills Distribution (Pie Chart)
    axes[0, 1].pie(category_counts.values, labels=category_counts.index,
                    autopct="%1.0f%%", colors=colors, startangle=90)
    axes[0, 1].set_title("Skills Distribution", fontsize=13, fontweight="bold")

    # 3. Resume Section Lengths (Bar Chart)
    section_lengths = {k: len(v.split()) for k, v in sections.items()}
    section_df = pd.Series(section_lengths).sort_values(ascending=True)
    axes[1, 0].barh(section_df.index, section_df.values, color="steelblue")
    axes[1, 0].set_title("Words per Section", fontsize=13, fontweight="bold")
    axes[1, 0].set_xlabel("Word Count")

    # 4. Resume Stats Summary
    total_words = sum(section_lengths.values())
    total_skills = len(skills_df)
    num_sections = len(sections)
    has_summary = "SUMMARY" in sections
    has_education = "EDUCATION" in sections

    stats_text = (
        f"Total Words: {total_words}\n"
        f"Total Skills: {total_skills}\n"
        f"Sections: {num_sections}\n"
        f"Has Summary: {'Yes' if has_summary else 'NO - Add one!'}\n"
        f"Has Education: {'Yes' if has_education else 'NO - Add one!'}\n"
        f"\nSkill Categories: {len(skills_df['category'].unique())}\n"
        f"Top Category: {skills_df['category'].value_counts().index[0]}"
    )
    axes[1, 1].text(0.1, 0.5, stats_text, fontsize=12, fontfamily="monospace",
                     verticalalignment="center", transform=axes[1, 1].transAxes,
                     bbox=dict(boxstyle="round", facecolor="lightyellow", alpha=0.8))
    axes[1, 1].set_title("Resume Stats", fontsize=13, fontweight="bold")
    axes[1, 1].axis("off")

    fig.suptitle("Resume Analysis Dashboard", fontsize=16, fontweight="bold")
    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"\nDashboard saved: {output_path}")

create_resume_dashboard(skills_df, sections)
```

### Step 5: Score the Resume (Chapter 29 - ML Concepts)

```python
def score_resume(resume_text, sections, skills_df):
    """Score a resume based on common best practices."""

    scores = {}

    # Length score (300-800 words is ideal for a 1-page resume)
    word_count = len(resume_text.split())
    if 300 <= word_count <= 800:
        scores["length"] = 10
    elif 200 <= word_count <= 1000:
        scores["length"] = 7
    else:
        scores["length"] = 4

    # Section completeness
    important_sections = ["SUMMARY", "EXPERIENCE", "EDUCATION", "SKILLS"]
    found_sections = sum(1 for s in important_sections if s in sections)
    scores["sections"] = round((found_sections / len(important_sections)) * 10)

    # Skills diversity
    num_categories = skills_df["category"].nunique()
    scores["skill_diversity"] = min(10, num_categories * 2)

    # Technical skills count
    total_skills = len(skills_df)
    scores["skill_count"] = min(10, total_skills)

    # Action verbs in experience
    action_verbs = ["built", "led", "developed", "implemented", "created",
                     "designed", "managed", "improved", "increased", "reduced",
                     "launched", "mentored", "collaborated", "automated"]
    experience_text = sections.get("EXPERIENCE", "").lower()
    verbs_found = sum(1 for v in action_verbs if v in experience_text)
    scores["action_verbs"] = min(10, verbs_found * 2)

    # Quantified achievements (numbers in experience section)
    numbers = re.findall(r'\d+', sections.get("EXPERIENCE", ""))
    scores["quantified"] = min(10, len(numbers) * 2)

    # Calculate overall score using NumPy
    weights = np.array([0.10, 0.15, 0.15, 0.15, 0.20, 0.25])
    score_values = np.array(list(scores.values()))
    overall = np.average(score_values, weights=weights)

    print("\n=== Resume Score ===")
    for criterion, score in scores.items():
        bar = "=" * score + "-" * (10 - score)
        print(f"  {criterion:20s} [{bar}] {score}/10")

    print(f"\n  {'OVERALL':20s} [{('=' * round(overall)) + ('-' * (10 - round(overall))))}] {overall:.1f}/10")

    return scores, overall

scores, overall = score_resume(resume, sections, skills_df)
```

### Step 6: AI Feedback (Chapter 30 - AI APIs)

```python
def get_ai_feedback(resume_text, scores):
    """Get AI-powered feedback on the resume."""

    # If you have an OpenAI API key:
    try:
        from openai import OpenAI
        client = OpenAI()

        score_summary = "\n".join(f"- {k}: {v}/10" for k, v in scores.items())

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "You are a professional resume reviewer. "
                               "Give specific, actionable feedback. "
                               "Be encouraging but honest. "
                               "Limit to 5 bullet points."
                },
                {
                    "role": "user",
                    "content": f"Review this resume and give improvement suggestions.\n\n"
                               f"Resume:\n{resume_text}\n\n"
                               f"Automated scores:\n{score_summary}"
                }
            ],
            temperature=0.7,
            max_tokens=500
        )

        feedback = response.choices[0].message.content
        print("\n=== AI Feedback ===")
        print(feedback)
        return feedback

    except Exception as e:
        print(f"\n=== AI Feedback (Offline Mode) ===")
        feedback = generate_offline_feedback(scores)
        print(feedback)
        return feedback

def generate_offline_feedback(scores):
    """Generate basic feedback without AI API."""
    tips = []

    if scores.get("quantified", 0) < 6:
        tips.append("Add more numbers! '10,000+ users' is better than 'many users'.")
    if scores.get("action_verbs", 0) < 6:
        tips.append("Start bullet points with strong action verbs: Built, Led, Designed, Launched.")
    if scores.get("skill_diversity", 0) < 6:
        tips.append("Diversify your skills across more categories (frontend, backend, cloud, etc.).")
    if scores.get("sections", 0) < 10:
        tips.append("Make sure you have all key sections: Summary, Experience, Education, Skills.")
    if scores.get("length", 0) < 7:
        tips.append("Aim for 300-800 words. Concise but comprehensive.")

    if not tips:
        tips.append("Your resume looks strong! Consider tailoring it for specific job descriptions.")

    return "\n".join(f"- {tip}" for tip in tips)

feedback = get_ai_feedback(resume, scores)
```

### Step 7: Generate the Final Report (Chapter 32 - Automation)

```python
def generate_report(resume_path, output_dir="resume_report"):
    """Run the complete analysis and generate a report."""

    output_dir = Path(output_dir)
    output_dir.mkdir(exist_ok=True)

    print("=" * 50)
    print("  AI-POWERED RESUME ANALYZER")
    print("=" * 50)

    # Load
    resume = load_resume(resume_path)
    sections = extract_sections(resume)

    # Analyze
    skills_df, found_skills = analyze_skills(resume)

    # Visualize
    dashboard_path = output_dir / "dashboard.png"
    create_resume_dashboard(skills_df, sections, str(dashboard_path))

    # Score
    scores, overall = score_resume(resume, sections, skills_df)

    # AI Feedback
    feedback = get_ai_feedback(resume, scores)

    # Save text report
    report_path = output_dir / "analysis_report.txt"
    with open(report_path, "w") as f:
        f.write("RESUME ANALYSIS REPORT\n")
        f.write(f"{'=' * 40}\n\n")
        f.write(f"Overall Score: {overall:.1f}/10\n\n")
        f.write("Scores:\n")
        for k, v in scores.items():
            f.write(f"  {k}: {v}/10\n")
        f.write(f"\nSkills Found: {len(skills_df)}\n")
        f.write(f"Skill Categories: {skills_df['category'].nunique()}\n\n")
        f.write("Feedback:\n")
        f.write(feedback)

    print(f"\n{'=' * 50}")
    print(f"  Report saved to: {output_dir}/")
    print(f"  - dashboard.png")
    print(f"  - analysis_report.txt")
    print(f"  Overall Score: {overall:.1f}/10")
    print(f"{'=' * 50}")

# Run the full analysis!
generate_report("sample_resume.txt")
```

### Running the Complete Project

```bash
python resume_analyzer.py
```

Expected output:

```
==================================================
  AI-POWERED RESUME ANALYZER
==================================================
Loaded resume: sample_resume.txt (1247 characters)

Total skills found: 14

Skills by category:
  Cloud & DevOps: 4 skills (28.6%)
  Programming Languages: 3 skills (21.4%)
  Backend: 3 skills (21.4%)
  Databases: 2 skills (14.3%)
  Soft Skills: 2 skills (14.3%)

Dashboard saved: resume_report/dashboard.png

=== Resume Score ===
  length               [==========] 10/10
  sections             [==========] 10/10
  skill_diversity      [==========] 10/10
  skill_count          [==========] 10/10
  action_verbs         [==========] 10/10
  quantified           [========-] 8/10

  OVERALL              [==========] 9.7/10

==================================================
  Report saved to: resume_report/
  Overall Score: 9.7/10
==================================================
```

## Stretch Goals

Already done? Try these enhancements:

1. **PDF Support**: Use `PyPDFLoader` from LangChain to read PDF resumes
2. **Job Match**: Compare the resume against a job description using RAG (Chapter 31)
3. **Multiple Resumes**: Analyze a folder of resumes and rank them
4. **Web Interface**: Use Streamlit (`pip install streamlit`) to create a drag-and-drop UI
5. **Email the Report**: Automatically email the analysis using smtplib (Chapter 32)

## Starter and Solution Code

- **Starter code:** [github link](https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/sprint-5-ai/sprint-5-checkpoint/starter/)
- **Solution code:** [github link](https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/sprint-5-ai/sprint-5-checkpoint/solution/)

## You Did It.

Sprint 5. Complete. All five sprints. Done.

Think about where you started:
- **Sprint 1**: `print("Hello, World!")` - variables, lists, loops
- **Sprint 2**: Dictionaries, functions, file I/O, error handling
- **Sprint 3**: OOP, APIs, web scraping, databases
- **Sprint 4**: Virtual environments, testing, Flask, deployment
- **Sprint 5**: NumPy, pandas, visualization, machine learning, AI APIs, LangChain, automation

That's not a "crash course." That's a transformation. You went from zero to someone who can build real, useful, AI-powered applications.

You're not a beginner. You're not even intermediate. You're someone who can build real things with Python AND AI. The gap between you and a "professional developer" is now just practice and projects - not knowledge.

Now it's time to prove it with the Final Projects. Let's go.

---

# Welcome to The Final Zone

You made it.

If you're reading this, you've gone from zero - knowing nothing about Python - to understanding variables, loops, functions, classes, APIs, databases, web frameworks, and even artificial intelligence. That's not a small thing. That's a genuinely impressive thing.

Now it's time to prove it.

## Ten Projects. Ten Portfolio Pieces.

This section contains ten final projects, arranged from beginner-friendly to advanced. Each one builds on the skills you've learned throughout this book, and each one produces something real - something that works, something you can show off, something you can talk about.

**Every project you complete here is something you can show to employers, put on GitHub, and talk about in interviews.**

That's not a throwaway line. Hiring managers don't want to hear "I read a book about Python." They want to see what you built. These projects give you that answer.

## How the Projects Work

Each project guide includes:

- **Difficulty rating** (1 to 5 stars) so you know what you're getting into
- **Time estimate** so you can plan your session
- **Skills list** linking back to where you learned each concept
- **Step-by-step build guide** with actual code, not just hand-waving
- **Extension challenges** to push yourself further
- **Portfolio tips** for presenting your work professionally

## The Progression

The projects are ordered intentionally. Start wherever your comfort level is, but if you can, work through them in order:

| # | Project | Difficulty | Time |
|--|-----|------|---|
| 1 | The Quiz Game | 1/5 | ~1 hour |
| 2 | Personal Budget Tracker | 2/5 | ~1.5 hours |
| 3 | To-Do App (CLI) | 2/5 | ~2 hours |
| 4 | Hangman Game | 2/5 | ~1.5 hours |
| 5 | Weather Dashboard | 3/5 | ~2 hours |
| 6 | Web Scraper & Data Analyzer | 3/5 | ~2.5 hours |
| 7 | Chat Application (CLI) | 4/5 | ~3 hours |
| 8 | Blog REST API | 4/5 | ~3 hours |
| 9 | ML Prediction App | 4/5 | ~3 hours |
| 10 | AI-Powered Study Buddy | 5/5 | ~4 hours |

Projects 1-4 use only Python's built-in features. Projects 5-6 introduce third-party libraries. Projects 7-10 tackle real-world engineering challenges: networking, web APIs, machine learning, and AI.

## Ground Rules

1. **Type every line yourself.** Don't copy-paste. Muscle memory matters.
2. **Break things on purpose.** Change a variable. Remove a line. See what happens.
3. **Do at least one extension challenge per project.** That's where the real learning lives.
4. **Push everything to GitHub.** Start building your public portfolio today.

## One More Thing

You will get stuck. You will see error messages. You will spend twenty minutes hunting a bug that turns out to be a missing colon. That's not failure - that's programming. Every working developer on the planet has been exactly where you are right now.

The difference between someone who "tried to learn Python" and someone who "knows Python" is simply this: they kept going.

So keep going. You've got ten projects ahead of you, and every single one of them is within your reach.

Let's build.

---

# Project 1: The Quiz Game

> **Difficulty:** 1/5 | **Time:** ~1 hour | **Skills:** variables, loops, conditions, lists, input
> **Code:** https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/final-projects/project-01-quiz-game/

## What You'll Build

A terminal-based quiz game with three categories (Science, History, and Geography), five questions each, score tracking, and a results summary at the end. When running, the player picks a category, answers multiple-choice questions, gets instant feedback on each answer, and sees a final scorecard showing how they did.

It looks like this when running:

```
=== THE QUIZ GAME ===

Choose a category:
1. Science
2. History
3. Geography
4. All Categories

Your choice: 1

-- Science --

Q1: What planet is known as the Red Planet?
  a) Venus
  b) Mars
  c) Jupiter
  d) Saturn
Your answer: b
Correct!

...

=== RESULTS ===
You scored 4/5 (80%)
Rating: Great job!
```

## Skills You'll Use

- Variables and data types (learned in Chapter 2)
- Lists and dictionaries (learned in Chapter 4)
- Conditional statements (learned in Chapter 3)
- Loops (learned in Chapter 3)
- User input and string methods (learned in Chapter 2)
- Functions (learned in Chapter 5)

## Step-by-Step Build Guide

### Step 1: Set Up the Question Data

The foundation of any quiz game is its questions. We'll store them as a list of dictionaries - each dictionary holds the question text, the answer choices, and the correct answer.

```python
# quiz_game.py

# Each question is a dictionary with question text, options, and correct answer
science_questions = [
    {
        "question": "What planet is known as the Red Planet?",
        "options": ["a) Venus", "b) Mars", "c) Jupiter", "d) Saturn"],
        "answer": "b"
    },
    {
        "question": "What gas do plants absorb from the atmosphere?",
        "options": ["a) Oxygen", "b) Nitrogen", "c) Carbon Dioxide", "d) Hydrogen"],
        "answer": "c"
    },
    {
        "question": "What is the chemical symbol for water?",
        "options": ["a) O2", "b) CO2", "c) NaCl", "d) H2O"],
        "answer": "d"
    },
    {
        "question": "How many bones are in the adult human body?",
        "options": ["a) 106", "b) 206", "c) 306", "d) 156"],
        "answer": "b"
    },
    {
        "question": "What force keeps us on the ground?",
        "options": ["a) Magnetism", "b) Friction", "c) Gravity", "d) Inertia"],
        "answer": "c"
    }
]

history_questions = [
    {
        "question": "In what year did World War II end?",
        "options": ["a) 1943", "b) 1944", "c) 1945", "d) 1946"],
        "answer": "c"
    },
    {
        "question": "Who was the first President of the United States?",
        "options": ["a) John Adams", "b) Thomas Jefferson",
                    "c) Benjamin Franklin", "d) George Washington"],
        "answer": "d"
    },
    {
        "question": "The ancient city of Rome is in which modern country?",
        "options": ["a) Greece", "b) Italy", "c) Spain", "d) Turkey"],
        "answer": "b"
    },
    {
        "question": "Who wrote the Declaration of Independence?",
        "options": ["a) George Washington", "b) Benjamin Franklin",
                    "c) Thomas Jefferson", "d) John Adams"],
        "answer": "c"
    },
    {
        "question": "The Great Wall was built primarily to protect which country?",
        "options": ["a) Japan", "b) India", "c) China", "d) Mongolia"],
        "answer": "c"
    }
]

geography_questions = [
    {
        "question": "What is the largest continent by area?",
        "options": ["a) Africa", "b) North America", "c) Europe", "d) Asia"],
        "answer": "d"
    },
    {
        "question": "Which river is the longest in the world?",
        "options": ["a) Amazon", "b) Nile", "c) Mississippi", "d) Yangtze"],
        "answer": "b"
    },
    {
        "question": "What is the smallest country in the world?",
        "options": ["a) Monaco", "b) Nauru", "c) Vatican City", "d) San Marino"],
        "answer": "c"
    },
    {
        "question": "Mount Everest is located in which mountain range?",
        "options": ["a) Andes", "b) Alps", "c) Rockies", "d) Himalayas"],
        "answer": "d"
    },
    {
        "question": "Which ocean is the largest?",
        "options": ["a) Atlantic", "b) Indian", "c) Pacific", "d) Arctic"],
        "answer": "c"
    }
]
```

### Step 2: Build the Category Selection

Now let's write a function that lets the player choose what they want to be quizzed on. We use a dictionary to map choices to question lists.

```python
def choose_category():
    """Let the player pick a quiz category."""
    categories = {
        "1": ("Science", science_questions),
        "2": ("History", history_questions),
        "3": ("Geography", geography_questions),
        "4": ("All Categories",
              science_questions + history_questions + geography_questions)
    }

    print("\nChoose a category:")
    print("1. Science")
    print("2. History")
    print("3. Geography")
    print("4. All Categories")

    while True:
        choice = input("\nYour choice: ").strip()
        if choice in categories:
            name, questions = categories[choice]
            print(f"\n-- {name} --")
            return name, questions
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")
```

### Step 3: Create the Quiz Runner

This function takes a list of questions, presents them one at a time, validates the player's input, and tracks the score.

```python
def run_quiz(questions):
    """Run through questions and return the score."""
    score = 0
    total = len(questions)
    results = []  # Track each answer for the summary

    for i, q in enumerate(questions, 1):
        print(f"\nQ{i}: {q['question']}")
        for option in q["options"]:
            print(f"  {option}")

        # Get valid input
        while True:
            answer = input("Your answer: ").strip().lower()
            if answer in ["a", "b", "c", "d"]:
                break
            print("Please enter a, b, c, or d.")

        # Check the answer
        if answer == q["answer"]:
            print("Correct!")
            score += 1
            results.append((q["question"], True))
        else:
            correct_letter = q["answer"]
            # Find the full text of the correct answer
            correct_text = [opt for opt in q["options"]
                           if opt.startswith(correct_letter)][0]
            print(f"Wrong! The correct answer was: {correct_text}")
            results.append((q["question"], False))

    return score, total, results
```

### Step 4: Build the Results Summary

After the quiz, show a detailed breakdown. A nice touch is giving the player a rating based on their percentage.

```python
def show_results(score, total, results, category_name):
    """Display the final results summary."""
    percentage = (score / total) * 100

    print("\n" + "=" * 40)
    print(f"  RESULTS - {category_name}")
    print("=" * 40)
    print(f"\n  You scored {score}/{total} ({percentage:.0f}%)")

    # Give a rating
    if percentage == 100:
        rating = "Perfect score! You're a genius!"
    elif percentage >= 80:
        rating = "Great job! Really impressive!"
    elif percentage >= 60:
        rating = "Good effort! Keep studying!"
    elif percentage >= 40:
        rating = "Not bad, but there's room to grow."
    else:
        rating = "Keep learning - you'll get there!"

    print(f"  Rating: {rating}")

    # Show question-by-question breakdown
    print(f"\n  Breakdown:")
    for question, correct in results:
        status = "+" if correct else "X"
        # Truncate long questions for clean display
        short_q = question if len(question) <= 45 else question[:42] + "..."
        print(f"    [{status}] {short_q}")

    print("\n" + "=" * 40)
```

### Step 5: Add the Play Again Loop

Wrap everything in a main function with a loop so the player can keep playing.

```python
def main():
    """Main game loop."""
    print("=" * 40)
    print("       THE QUIZ GAME")
    print("=" * 40)
    print("Test your knowledge across 3 categories!")

    while True:
        category_name, questions = choose_category()
        score, total, results = run_quiz(questions)
        show_results(score, total, results, category_name)

        # Ask to play again
        print()
        again = input("Play again? (yes/no): ").strip().lower()
        if again not in ["yes", "y"]:
            print("\nThanks for playing! See you next time.")
            break


if __name__ == "__main__":
    main()
```

### Step 6: Run and Test

Save your file as `quiz_game.py` and run it:

```
python quiz_game.py
```

Test each category, try invalid inputs (like entering "z" when it expects a-d), and make sure the score tallies correctly. Try the "All Categories" option to confirm questions from all three sets appear.

## Challenges (Level Up!)

1. **Randomize questions:** Import the `random` module and use `random.shuffle(questions)` to present questions in a different order each time. This makes the game replayable.

2. **Add a timer:** Use `time.time()` to track how long the player takes per question and display the total time in the results. Bonus: give a speed bonus for fast answers.

3. **High score persistence:** Save the top 5 scores to a text file so they persist between sessions. Display a "New High Score!" message when the player beats an existing record.

## Portfolio Tips

This is your "Hello World on steroids" - it shows you can structure data, handle user input, and build a complete program with a clear beginning, middle, and end. When presenting this project:

- **GitHub:** Include a clear README with a screenshot of the game running in the terminal. Mention the categories and how to add new questions.
- **Resume:** "Built a terminal-based quiz game with multiple categories, input validation, and score tracking using Python."
- **Interview talking point:** Discuss how you structured the question data (list of dictionaries) and why that choice made the code easy to extend with new categories.

---

# Project 2: Personal Budget Tracker

> **Difficulty:** 2/5 | **Time:** ~1.5 hours | **Skills:** file I/O, functions, error handling, CSV
> **Code:** https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/final-projects/project-02-budget-tracker/

## What You'll Build

A command-line budget tracker that lets you log income and expenses with categories, view monthly reports, and persist all data to a CSV file. Every time you open the app, your previous transactions are right where you left them.

Here's what it looks like:

```
=== PERSONAL BUDGET TRACKER ===

1. Add Income
2. Add Expense
3. View Summary
4. View Monthly Report
5. Search Transactions
6. Exit

Choice: 3

-- Financial Summary --
Total Income:   $3,250.00
Total Expenses: $1,847.50
Balance:        $1,402.50

Top Expense Categories:
  Rent:       $1,200.00 (64.9%)
  Groceries:    $347.50 (18.8%)
  Transport:    $300.00 (16.2%)
```

## Skills You'll Use

- Functions and program structure (learned in Chapter 5)
- File I/O and CSV module (learned in Chapter 7)
- Error handling with try/except (learned in Chapter 8)
- String formatting and f-strings (learned in Chapter 2)
- Dictionaries for aggregation (learned in Chapter 4)
- The `datetime` module (learned in Chapter 6)

## Step-by-Step Build Guide

### Step 1: Project Setup and Imports

Create the file and import everything you'll need. The `csv` and `datetime` modules are built into Python - no installs required.

```python
# budget_tracker.py

import csv
import os
from datetime import datetime

DATA_FILE = "budget_data.csv"
```

### Step 2: Build the CSV Persistence Layer

These two functions handle saving and loading data. If the CSV file doesn't exist yet, we create it with headers.

```python
def load_transactions():
    """Load all transactions from the CSV file."""
    transactions = []
    if not os.path.exists(DATA_FILE):
        return transactions

    try:
        with open(DATA_FILE, "r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                row["amount"] = float(row["amount"])
                transactions.append(row)
    except (csv.Error, ValueError) as e:
        print(f"Warning: Error reading data file: {e}")
        print("Starting with empty transaction list.")

    return transactions


def save_transactions(transactions):
    """Save all transactions to the CSV file."""
    fieldnames = ["date", "type", "category", "description", "amount"]

    try:
        with open(DATA_FILE, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(transactions)
    except IOError as e:
        print(f"Error saving data: {e}")
```

### Step 3: Add Transaction Input Functions

These functions collect transaction details from the user with proper input validation. Notice how we validate the amount to ensure it's a positive number.

```python
INCOME_CATEGORIES = ["Salary", "Freelance", "Investment", "Gift", "Other"]
EXPENSE_CATEGORIES = ["Rent", "Groceries", "Transport", "Utilities",
                      "Entertainment", "Healthcare", "Education", "Other"]


def get_amount(prompt="Amount: $"):
    """Get a valid positive dollar amount from the user."""
    while True:
        try:
            amount = float(input(prompt))
            if amount <= 0:
                print("Amount must be positive.")
                continue
            return round(amount, 2)
        except ValueError:
            print("Invalid amount. Please enter a number (e.g., 42.50).")


def choose_category(categories):
    """Let the user pick from a list of categories."""
    print("\nCategories:")
    for i, cat in enumerate(categories, 1):
        print(f"  {i}. {cat}")

    while True:
        try:
            choice = int(input("Choose category number: "))
            if 1 <= choice <= len(categories):
                return categories[choice - 1]
            print(f"Please enter a number between 1 and {len(categories)}.")
        except ValueError:
            print("Please enter a valid number.")


def add_transaction(transactions, trans_type):
    """Add an income or expense transaction."""
    print(f"\n-- Add {trans_type} --")

    if trans_type == "Income":
        category = choose_category(INCOME_CATEGORIES)
    else:
        category = choose_category(EXPENSE_CATEGORIES)

    amount = get_amount()
    description = input("Description (optional): ").strip() or "No description"
    date_str = datetime.now().strftime("%Y-%m-%d")

    transaction = {
        "date": date_str,
        "type": trans_type,
        "category": category,
        "description": description,
        "amount": amount
    }

    transactions.append(transaction)
    save_transactions(transactions)

    print(f"\n  Added: {trans_type} - {category} - ${amount:,.2f}")
    print(f"  Saved to {DATA_FILE}")
```

### Step 4: Build the Summary View

This function aggregates all transactions to show totals, balance, and a breakdown of spending by category.

```python
def view_summary(transactions):
    """Display overall financial summary."""
    if not transactions:
        print("\nNo transactions recorded yet.")
        return

    total_income = sum(t["amount"] for t in transactions
                       if t["type"] == "Income")
    total_expenses = sum(t["amount"] for t in transactions
                         if t["type"] == "Expense")
    balance = total_income - total_expenses

    print("\n-- Financial Summary --")
    print(f"  Total Income:   ${total_income:>10,.2f}")
    print(f"  Total Expenses: ${total_expenses:>10,.2f}")
    print(f"  Balance:        ${balance:>10,.2f}")

    if balance < 0:
        print("  ** Warning: You're spending more than you earn! **")

    # Category breakdown for expenses
    expense_by_category = {}
    for t in transactions:
        if t["type"] == "Expense":
            cat = t["category"]
            expense_by_category[cat] = expense_by_category.get(cat, 0) + t["amount"]

    if expense_by_category:
        print("\n  Top Expense Categories:")
        sorted_cats = sorted(expense_by_category.items(),
                             key=lambda x: x[1], reverse=True)
        for cat, amount in sorted_cats:
            pct = (amount / total_expenses * 100) if total_expenses > 0 else 0
            print(f"    {cat:<15} ${amount:>8,.2f} ({pct:.1f}%)")
```

### Step 5: Add Monthly Reports

Filter transactions by month and year to show period-specific breakdowns.

```python
def view_monthly_report(transactions):
    """Show a report for a specific month."""
    if not transactions:
        print("\nNo transactions recorded yet.")
        return

    # Get available months
    months = set()
    for t in transactions:
        month_key = t["date"][:7]  # "YYYY-MM"
        months.add(month_key)

    sorted_months = sorted(months, reverse=True)
    print("\nAvailable months:")
    for i, m in enumerate(sorted_months, 1):
        print(f"  {i}. {m}")

    while True:
        try:
            choice = int(input("Choose month number: "))
            if 1 <= choice <= len(sorted_months):
                selected = sorted_months[choice - 1]
                break
            print("Invalid choice.")
        except ValueError:
            print("Please enter a number.")

    # Filter transactions for selected month
    monthly = [t for t in transactions if t["date"].startswith(selected)]

    income = sum(t["amount"] for t in monthly if t["type"] == "Income")
    expenses = sum(t["amount"] for t in monthly if t["type"] == "Expense")

    print(f"\n-- Report for {selected} --")
    print(f"  Income:   ${income:>10,.2f}")
    print(f"  Expenses: ${expenses:>10,.2f}")
    print(f"  Net:      ${income - expenses:>10,.2f}")

    print(f"\n  Transactions:")
    for t in monthly:
        sign = "+" if t["type"] == "Income" else "-"
        print(f"    {t['date']}  {sign}${t['amount']:>8,.2f}  "
              f"{t['category']:<12} {t['description']}")


def search_transactions(transactions):
    """Search transactions by keyword."""
    if not transactions:
        print("\nNo transactions recorded yet.")
        return

    keyword = input("\nSearch keyword: ").strip().lower()
    if not keyword:
        print("No keyword entered.")
        return

    matches = [t for t in transactions
               if keyword in t["category"].lower()
               or keyword in t["description"].lower()]

    if not matches:
        print(f"No transactions matching '{keyword}'.")
        return

    print(f"\n  Found {len(matches)} transaction(s):")
    total = 0
    for t in matches:
        sign = "+" if t["type"] == "Income" else "-"
        print(f"    {t['date']}  {sign}${t['amount']:>8,.2f}  "
              f"{t['category']:<12} {t['description']}")
        if t["type"] == "Income":
            total += t["amount"]
        else:
            total -= t["amount"]
    print(f"  Net total: ${total:,.2f}")
```

### Step 6: Wire Up the Main Menu

Connect everything with a main menu loop that loads data on start and keeps running until the user exits.

```python
def main():
    """Main application loop."""
    print("=" * 40)
    print("   PERSONAL BUDGET TRACKER")
    print("=" * 40)

    transactions = load_transactions()
    print(f"Loaded {len(transactions)} existing transaction(s).")

    while True:
        print("\n1. Add Income")
        print("2. Add Expense")
        print("3. View Summary")
        print("4. View Monthly Report")
        print("5. Search Transactions")
        print("6. Exit")

        choice = input("\nChoice: ").strip()

        if choice == "1":
            add_transaction(transactions, "Income")
        elif choice == "2":
            add_transaction(transactions, "Expense")
        elif choice == "3":
            view_summary(transactions)
        elif choice == "4":
            view_monthly_report(transactions)
        elif choice == "5":
            search_transactions(transactions)
        elif choice == "6":
            print("\nGoodbye! Keep tracking those finances.")
            break
        else:
            print("Invalid choice. Please enter 1-6.")


if __name__ == "__main__":
    main()
```

## Challenges (Level Up!)

1. **Budget limits:** Let the user set monthly spending limits per category. When they add an expense that pushes a category over its limit, display a warning. Store limits in a separate CSV or JSON file.

2. **Export to formatted report:** Generate a nicely formatted text file report that summarizes a month's finances - something you could print or email to yourself.

3. **Recurring transactions:** Add support for recurring monthly transactions (like rent or salary) that auto-populate when you start a new month.

## Portfolio Tips

A budget tracker shows you understand data persistence, input validation, and practical problem-solving. When presenting this project:

- **GitHub:** Include sample CSV data so reviewers can see the app in action immediately. Add screenshots of the summary and monthly report output.
- **Resume:** "Developed a CLI budget tracker with CSV persistence, category-based analytics, and monthly reporting using Python."
- **Interview talking point:** Discuss your choice of CSV format for storage (human-readable, easily opened in Excel) and how you handled edge cases like empty files and invalid input. Mention how you'd evolve it - perhaps adding a SQLite database if the data grew large.

---

# Project 3: To-Do App (CLI)

> **Difficulty:** 2/5 | **Time:** ~2 hours | **Skills:** OOP, CRUD, JSON persistence
> **Code:** https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/final-projects/project-03-todo-app/

## What You'll Build

A full-featured command-line to-do application built with object-oriented programming. You'll create a `Task` class, implement all four CRUD operations (Create, Read, Update, Delete), add priority levels and filtering, and persist everything to a JSON file.

Here's what it looks like when running:

```
=== TO-DO APP ===

1. Add Task       4. Complete Task
2. View Tasks     5. Delete Task
3. Edit Task      6. Exit

Choice: 2

-- Your Tasks --
  ID  Priority  Status      Task                    Due Date
  1   [!!!]     [ ]         Buy groceries           2026-04-05
  2   [!! ]     [x]         Finish Python project   2026-04-01
  3   [!  ]     [ ]         Call dentist             2026-04-10

Showing 3 task(s). Filter: all
```

## Skills You'll Use

- Classes and OOP (learned in Chapter 9)
- JSON file I/O (learned in Chapter 7)
- List comprehensions (learned in Chapter 4)
- Error handling (learned in Chapter 8)
- String formatting (learned in Chapter 2)
- Functions and program design (learned in Chapter 5)

## Step-by-Step Build Guide

### Step 1: Define the Task Class

This is the core of your application. Each task is an object with properties like title, priority, completion status, and a due date. We include methods to convert the task to and from a dictionary for JSON storage.

```python
# todo_app.py

import json
import os
from datetime import datetime

DATA_FILE = "tasks.json"


class Task:
    """Represents a single to-do task."""

    # Class variable to track the next available ID
    _next_id = 1

    def __init__(self, title, priority="medium", due_date=None,
                 completed=False, task_id=None):
        if task_id is not None:
            self.id = task_id
            # Keep _next_id ahead of any loaded IDs
            Task._next_id = max(Task._next_id, task_id + 1)
        else:
            self.id = Task._next_id
            Task._next_id += 1

        self.title = title
        self.priority = priority  # "high", "medium", "low"
        self.due_date = due_date  # "YYYY-MM-DD" string or None
        self.completed = completed
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M")

    def to_dict(self):
        """Convert task to a dictionary for JSON storage."""
        return {
            "id": self.id,
            "title": self.title,
            "priority": self.priority,
            "due_date": self.due_date,
            "completed": self.completed,
            "created_at": self.created_at
        }

    @classmethod
    def from_dict(cls, data):
        """Create a Task from a dictionary (loaded from JSON)."""
        task = cls(
            title=data["title"],
            priority=data.get("priority", "medium"),
            due_date=data.get("due_date"),
            completed=data.get("completed", False),
            task_id=data["id"]
        )
        task.created_at = data.get("created_at", "Unknown")
        return task

    def priority_display(self):
        """Return a visual priority indicator."""
        indicators = {"high": "[!!!]", "medium": "[!! ]", "low": "[!  ]"}
        return indicators.get(self.priority, "[?  ]")

    def status_display(self):
        """Return a checkbox-style status."""
        return "[x]" if self.completed else "[ ]"

    def __str__(self):
        status = self.status_display()
        priority = self.priority_display()
        due = self.due_date or "No date"
        return (f"  {self.id:<4}{priority:<10}{status:<12}"
                f"{self.title:<24}{due}")
```

### Step 2: Build the TaskManager Class

The `TaskManager` handles the collection of tasks, including loading, saving, and all CRUD operations. This keeps your data management logic organized in one place.

```python
class TaskManager:
    """Manages a collection of tasks with CRUD operations."""

    def __init__(self, data_file=DATA_FILE):
        self.data_file = data_file
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        """Load tasks from the JSON file."""
        if not os.path.exists(self.data_file):
            self.tasks = []
            return

        try:
            with open(self.data_file, "r") as f:
                data = json.load(f)
                self.tasks = [Task.from_dict(item) for item in data]
        except (json.JSONDecodeError, KeyError) as e:
            print(f"Warning: Could not load tasks ({e}). Starting fresh.")
            self.tasks = []

    def save_tasks(self):
        """Save all tasks to the JSON file."""
        data = [task.to_dict() for task in self.tasks]
        with open(self.data_file, "w") as f:
            json.dump(data, f, indent=2)

    def add_task(self, title, priority="medium", due_date=None):
        """Create and add a new task."""
        task = Task(title, priority, due_date)
        self.tasks.append(task)
        self.save_tasks()
        return task

    def get_task(self, task_id):
        """Find a task by its ID."""
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def update_task(self, task_id, **kwargs):
        """Update task properties."""
        task = self.get_task(task_id)
        if task is None:
            return None

        for key, value in kwargs.items():
            if hasattr(task, key):
                setattr(task, key, value)

        self.save_tasks()
        return task

    def delete_task(self, task_id):
        """Delete a task by ID."""
        task = self.get_task(task_id)
        if task:
            self.tasks.remove(task)
            self.save_tasks()
            return True
        return False

    def complete_task(self, task_id):
        """Mark a task as completed."""
        return self.update_task(task_id, completed=True)

    def get_filtered(self, filter_type="all"):
        """Return tasks filtered by status or priority."""
        if filter_type == "active":
            return [t for t in self.tasks if not t.completed]
        elif filter_type == "completed":
            return [t for t in self.tasks if t.completed]
        elif filter_type == "high":
            return [t for t in self.tasks if t.priority == "high"]
        return self.tasks

    def get_sorted(self, tasks=None, sort_by="priority"):
        """Sort tasks by priority or due date."""
        if tasks is None:
            tasks = self.tasks

        if sort_by == "priority":
            order = {"high": 0, "medium": 1, "low": 2}
            return sorted(tasks, key=lambda t: order.get(t.priority, 1))
        elif sort_by == "due_date":
            return sorted(tasks,
                          key=lambda t: t.due_date or "9999-12-31")
        elif sort_by == "id":
            return sorted(tasks, key=lambda t: t.id)
        return tasks
```

### Step 3: Build the User Interface Functions

Now create the interactive functions that collect user input and call the TaskManager methods.

```python
def get_priority():
    """Ask the user to choose a priority level."""
    print("  Priority: 1=High, 2=Medium, 3=Low")
    mapping = {"1": "high", "2": "medium", "3": "low"}
    while True:
        choice = input("  Choose (1/2/3): ").strip()
        if choice in mapping:
            return mapping[choice]
        print("  Please enter 1, 2, or 3.")


def get_due_date():
    """Ask the user for an optional due date."""
    while True:
        date_str = input("  Due date (YYYY-MM-DD, or press Enter to skip): ").strip()
        if not date_str:
            return None
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return date_str
        except ValueError:
            print("  Invalid date format. Use YYYY-MM-DD.")


def get_task_id(prompt="Task ID: "):
    """Get a valid task ID from the user."""
    while True:
        try:
            return int(input(prompt).strip())
        except ValueError:
            print("  Please enter a number.")


def display_tasks(tasks, filter_name="all"):
    """Display tasks in a formatted table."""
    if not tasks:
        print("\n  No tasks found.")
        return

    print(f"\n  {'ID':<4}{'Priority':<10}{'Status':<12}"
          f"{'Task':<24}{'Due Date'}")
    print("  " + "-" * 64)
    for task in tasks:
        print(task)
    print(f"\n  Showing {len(tasks)} task(s). Filter: {filter_name}")
```

### Step 4: Implement Each Menu Action

```python
def add_task_ui(manager):
    """Interactive UI for adding a task."""
    print("\n-- Add Task --")
    title = input("  Task title: ").strip()
    if not title:
        print("  Title cannot be empty.")
        return

    priority = get_priority()
    due_date = get_due_date()

    task = manager.add_task(title, priority, due_date)
    print(f"\n  Added task #{task.id}: {task.title}")


def view_tasks_ui(manager):
    """Interactive UI for viewing tasks with filter/sort options."""
    print("\n-- Your Tasks --")
    print("  Filter: 1=All  2=Active  3=Completed  4=High Priority")
    choice = input("  Choose (or Enter for all): ").strip()

    filter_map = {"1": "all", "2": "active", "3": "completed", "4": "high"}
    filter_type = filter_map.get(choice, "all")

    tasks = manager.get_filtered(filter_type)
    tasks = manager.get_sorted(tasks, sort_by="priority")
    display_tasks(tasks, filter_type)


def edit_task_ui(manager):
    """Interactive UI for editing a task."""
    print("\n-- Edit Task --")
    display_tasks(manager.tasks)
    task_id = get_task_id("\n  Task ID to edit: ")

    task = manager.get_task(task_id)
    if not task:
        print(f"  Task #{task_id} not found.")
        return

    print(f"  Editing: {task.title}")
    new_title = input(f"  New title (Enter to keep '{task.title}'): ").strip()
    if new_title:
        manager.update_task(task_id, title=new_title)

    change_priority = input("  Change priority? (y/n): ").strip().lower()
    if change_priority == "y":
        new_priority = get_priority()
        manager.update_task(task_id, priority=new_priority)

    change_date = input("  Change due date? (y/n): ").strip().lower()
    if change_date == "y":
        new_date = get_due_date()
        manager.update_task(task_id, due_date=new_date)

    print("  Task updated!")


def complete_task_ui(manager):
    """Interactive UI for completing a task."""
    print("\n-- Complete Task --")
    active = [t for t in manager.tasks if not t.completed]
    display_tasks(active, "active")

    if not active:
        return

    task_id = get_task_id("\n  Task ID to complete: ")
    result = manager.complete_task(task_id)
    if result:
        print(f"  Task #{task_id} marked as complete!")
    else:
        print(f"  Task #{task_id} not found.")


def delete_task_ui(manager):
    """Interactive UI for deleting a task."""
    print("\n-- Delete Task --")
    display_tasks(manager.tasks)

    if not manager.tasks:
        return

    task_id = get_task_id("\n  Task ID to delete: ")
    task = manager.get_task(task_id)
    if not task:
        print(f"  Task #{task_id} not found.")
        return

    confirm = input(f"  Delete '{task.title}'? (y/n): ").strip().lower()
    if confirm == "y":
        manager.delete_task(task_id)
        print("  Task deleted.")
    else:
        print("  Cancelled.")
```

### Step 5: Build the Main Menu

```python
def main():
    """Main application loop."""
    print("=" * 35)
    print("       TO-DO APP")
    print("=" * 35)

    manager = TaskManager()
    print(f"Loaded {len(manager.tasks)} task(s).")

    while True:
        print("\n1. Add Task       4. Complete Task")
        print("2. View Tasks     5. Delete Task")
        print("3. Edit Task      6. Exit")

        choice = input("\nChoice: ").strip()

        actions = {
            "1": lambda: add_task_ui(manager),
            "2": lambda: view_tasks_ui(manager),
            "3": lambda: edit_task_ui(manager),
            "4": lambda: complete_task_ui(manager),
            "5": lambda: delete_task_ui(manager),
        }

        if choice == "6":
            print("\nGoodbye! Stay productive.")
            break
        elif choice in actions:
            actions[choice]()
        else:
            print("Invalid choice. Please enter 1-6.")


if __name__ == "__main__":
    main()
```

## Challenges (Level Up!)

1. **Subtasks:** Add the ability to create subtasks under a parent task. A parent task automatically completes when all its subtasks are done. This will stretch your OOP skills with composition.

2. **Color-coded output:** Use ANSI escape codes to make high-priority tasks appear in red, completed tasks in green, and overdue tasks flash a warning. (Search for "ANSI color codes Python" to learn how.)

3. **Undo/Redo:** Implement an undo stack that lets the user reverse their last action. Every time a task is added, deleted, or modified, push the previous state onto the stack.

## Portfolio Tips

This project demonstrates OOP, data persistence, and clean architecture - three things every employer cares about. When presenting it:

- **GitHub:** Structure your repo cleanly. Put the code in a `/src` folder, include sample data, and write a README that shows the app in action.
- **Resume:** "Built an OOP-based CLI task manager with CRUD operations, JSON persistence, and priority-based filtering using Python."
- **Interview talking point:** Explain your class design decisions. Why did you separate `Task` from `TaskManager`? How does `to_dict` / `from_dict` enable persistence? This shows you think about software architecture, not just "making it work."

---

# Project 4: Hangman Game

> **Difficulty:** 2/5 | **Time:** ~1.5 hours | **Skills:** strings, game logic, ASCII art, loops
> **Code:** https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/final-projects/project-04-hangman/

## What You'll Build

A classic Hangman game in the terminal with word categories, difficulty levels, ASCII art that updates with each wrong guess, and score tracking across rounds. It's polished, fun, and surprisingly satisfying to build.

Here's what it looks like:

```
=== HANGMAN ===

Category: Animals | Difficulty: Medium | Lives: 6

   ---
   |    |
   |    O
   |   /|
   |
   |
  --

Word: _ _ _ _ _ _ _

Guessed: a, e, r, t
Remaining: 3 lives

Guess a letter: s
Correct! The 's' appears 1 time(s).

Word: _ _ _ s _ e r
```

## Skills You'll Use

- String manipulation and methods (learned in Chapter 2)
- Loops and conditionals (learned in Chapter 3)
- Lists and random selection (learned in Chapter 4)
- Functions and modular design (learned in Chapter 5)
- Sets for tracking guesses (learned in Chapter 4)

## Step-by-Step Build Guide

### Step 1: Define the Word Bank and ASCII Art

Start with the word bank organized by category and difficulty, and the hangman stages as ASCII art strings.

```python
# hangman.py

import random

# Word bank organized by category
WORD_BANK = {
    "Animals": {
        "easy": ["cat", "dog", "bird", "fish", "frog"],
        "medium": ["dolphin", "giraffe", "penguin", "hamster", "lobster"],
        "hard": ["chameleon", "rhinoceros", "hippopotamus", "chinchilla"]
    },
    "Countries": {
        "easy": ["india", "china", "japan", "italy", "spain"],
        "medium": ["germany", "australia", "thailand", "portugal", "morocco"],
        "hard": ["mozambique", "kazakhstan", "afghanistan", "liechtenstein"]
    },
    "Technology": {
        "easy": ["code", "data", "wifi", "byte", "chip"],
        "medium": ["python", "server", "docker", "github", "laptop"],
        "hard": ["kubernetes", "javascript", "blockchain", "tensorflow"]
    }
}

# Each stage is one more body part - 7 stages (0 = no parts, 6 = full body)
HANGMAN_STAGES = [
    """
   ---
   |    |
   |
   |
   |
   |
  --""",
    """
   ---
   |    |
   |    O
   |
   |
   |
  --""",
    """
   ---
   |    |
   |    O
   |    |
   |
   |
  --""",
    """
   ---
   |    |
   |    O
   |   /|
   |
   |
  --""",
    """
   ---
   |    |
   |    O
   |   /|\\
   |
   |
  --""",
    """
   ---
   |    |
   |    O
   |   /|\\
   |   /
   |
  --""",
    """
   ---
   |    |
   |    O
   |   /|\\
   |   / \\
   |
  --"""
]
```

### Step 2: Build the Setup Functions

Let the player choose their category and difficulty before each round.

```python
def choose_category():
    """Let the player choose a word category."""
    categories = list(WORD_BANK.keys())
    print("\nCategories:")
    for i, cat in enumerate(categories, 1):
        print(f"  {i}. {cat}")

    while True:
        try:
            choice = int(input("Choose a category: "))
            if 1 <= choice <= len(categories):
                return categories[choice - 1]
        except ValueError:
            pass
        print(f"Please enter a number between 1 and {len(categories)}.")


def choose_difficulty():
    """Let the player choose difficulty level."""
    print("\nDifficulty:")
    print("  1. Easy   (short words, 8 lives)")
    print("  2. Medium (longer words, 6 lives)")
    print("  3. Hard   (longest words, 5 lives)")

    lives_map = {"1": ("easy", 8), "2": ("medium", 6), "3": ("hard", 5)}

    while True:
        choice = input("Choose difficulty: ").strip()
        if choice in lives_map:
            return lives_map[choice]
        print("Please enter 1, 2, or 3.")


def get_random_word(category, difficulty):
    """Pick a random word from the selected category and difficulty."""
    words = WORD_BANK[category][difficulty]
    return random.choice(words).lower()
```

### Step 3: Create the Display Function

This function renders the current game state: the hangman figure, the partially revealed word, and the guessed letters.

```python
def display_state(word, guessed_letters, wrong_guesses, max_lives,
                  category, difficulty):
    """Display the current game state."""
    # Clear some space
    print("\n" * 2)

    lives_remaining = max_lives - wrong_guesses
    stage_index = min(wrong_guesses, len(HANGMAN_STAGES) - 1)

    # Header
    print(f"Category: {category} | Difficulty: {difficulty.title()} "
          f"| Lives: {max_lives}")

    # Hangman figure
    print(HANGMAN_STAGES[stage_index])

    # Word display (show guessed letters, hide others)
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print(f"\nWord: {display_word.strip()}")

    # Guessed letters
    if guessed_letters:
        sorted_guesses = sorted(guessed_letters)
        print(f"\nGuessed: {', '.join(sorted_guesses)}")

    print(f"Remaining: {lives_remaining} lives")

    return lives_remaining
```

### Step 4: Build the Core Game Loop

This is the heart of the game. Each iteration gets a guess, validates it, checks if it's correct, and determines win/loss.

```python
def play_round(category, difficulty, max_lives):
    """Play a single round of hangman. Returns True if player wins."""
    word = get_random_word(category, difficulty)
    guessed_letters = set()
    wrong_guesses = 0

    while True:
        lives = display_state(word, guessed_letters, wrong_guesses,
                              max_lives, category, difficulty)

        # Check win condition
        if all(letter in guessed_letters for letter in word):
            print(f"\n  YOU WIN! The word was: {word}")
            return True

        # Check lose condition
        if lives <= 0:
            print(f"\n  GAME OVER! The word was: {word}")
            return False

        # Get player's guess
        while True:
            guess = input("\nGuess a letter: ").strip().lower()

            if len(guess) != 1 or not guess.isalpha():
                print("Please enter a single letter.")
                continue
            if guess in guessed_letters:
                print(f"You already guessed '{guess}'. Try another.")
                continue
            break

        guessed_letters.add(guess)

        # Check if correct
        if guess in word:
            count = word.count(guess)
            print(f"Correct! The '{guess}' appears {count} time(s).")
        else:
            wrong_guesses += 1
            print(f"Wrong! '{guess}' is not in the word.")
```

### Step 5: Add Score Tracking and the Main Loop

Keep a running score across multiple rounds and display a session summary at the end.

```python
def show_scoreboard(wins, losses):
    """Display the current score."""
    total = wins + losses
    if total == 0:
        return

    win_rate = (wins / total) * 100
    print("\n-- Scoreboard --")
    print(f"  Wins: {wins}  |  Losses: {losses}  |  "
          f"Win Rate: {win_rate:.0f}%")

    # Visual bar
    bar_width = 20
    filled = int((wins / total) * bar_width) if total > 0 else 0
    bar = "#" * filled + "-" * (bar_width - filled)
    print(f"  [{bar}]")


def main():
    """Main game loop with score tracking."""
    print("=" * 30)
    print("      HANGMAN")
    print("=" * 30)
    print("Guess the word before")
    print("the hangman is complete!")

    wins = 0
    losses = 0

    while True:
        category = choose_category()
        difficulty, max_lives = choose_difficulty()

        won = play_round(category, difficulty, max_lives)

        if won:
            wins += 1
        else:
            losses += 1

        show_scoreboard(wins, losses)

        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("\n-- Final Results --")
            show_scoreboard(wins, losses)
            print("\nThanks for playing!")
            break


if __name__ == "__main__":
    main()
```

## Challenges (Level Up!)

1. **Hint system:** Give the player one free hint per round that reveals a random unguessed letter. Deduct half a life as the cost. This requires tracking which letters are still hidden.

2. **Two-player mode:** Let one player enter a custom word (hiding the input with `getpass.getpass()`) and the other player guesses. Add a competitive scoreboard.

3. **Word bank from file:** Move the word bank to an external text file (one word per line, organized by headers like `[Animals:easy]`). Write code to parse this file, making it easy for anyone to add new words without touching the Python code.

## Portfolio Tips

Hangman is a game most people know instantly, which makes it a great demo piece. When presenting this project:

- **GitHub:** Create an animated GIF of gameplay for your README. Tools like `asciinema` can record terminal sessions beautifully.
- **Resume:** "Built a terminal Hangman game with multiple categories, difficulty scaling, ASCII art rendering, and session score tracking in Python."
- **Interview talking point:** Talk about how you used sets to efficiently track guessed letters (O(1) lookup vs. searching a list). Discuss the state machine pattern: every round moves through a clear sequence of states (setup, playing, won/lost).

---

# Project 5: Weather Dashboard

> **Difficulty:** 3/5 | **Time:** ~2 hours | **Skills:** APIs, JSON parsing, formatted output, file I/O
> **Code:** https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/final-projects/project-05-weather-dashboard/

## What You'll Build

A command-line weather dashboard that fetches real weather data from the wttr.in API, displays current conditions and a multi-day forecast with formatted output, and lets you save favorite cities for quick access. No API key required.

Here's what it looks like:

```
=== WEATHER DASHBOARD ===

1. Check Weather     4. Remove Favorite
2. 3-Day Forecast    5. View Favorites
3. Add Favorite      6. Exit

Choice: 1
City: London

-- Current Weather: London --
  Condition:   Partly cloudy
  Temperature: 15C (59F)
  Feels Like:  13C (55F)
  Humidity:    72%
  Wind:        14 km/h SW
  UV Index:    3

  Last updated: 2026-04-01 14:00
```

## Skills You'll Use

- HTTP requests with `urllib` (learned in Chapter 12)
- JSON parsing (learned in Chapter 7)
- String formatting and f-strings (learned in Chapter 2)
- File I/O for favorites (learned in Chapter 7)
- Error handling (learned in Chapter 8)
- Functions and modular design (learned in Chapter 5)

## Step-by-Step Build Guide

### Step 1: Set Up and Fetch Weather Data

The wttr.in API is a free weather service that requires no API key. We'll use Python's built-in `urllib` module so there's nothing to install.

```python
# weather_dashboard.py

import json
import os
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError

FAVORITES_FILE = "favorite_cities.json"


def fetch_weather(city):
    """Fetch weather data from wttr.in API.
    Returns parsed JSON or None on failure."""
    # wttr.in returns JSON when you add ?format=j1
    url = f"https://wttr.in/{city}?format=j1"

    try:
        request = Request(url, headers={"User-Agent": "Python-Weather-App"})
        with urlopen(request, timeout=10) as response:
            data = json.loads(response.read().decode())
            return data
    except HTTPError as e:
        print(f"  HTTP Error: {e.code} - Could not find city '{city}'.")
    except URLError as e:
        print(f"  Connection Error: {e.reason}")
        print("  Check your internet connection.")
    except json.JSONDecodeError:
        print("  Error: Could not parse weather data.")

    return None
```

### Step 2: Parse and Display Current Conditions

The wttr.in JSON response has a specific structure. We'll extract the key fields and display them in a clean, readable format.

```python
def display_current_weather(data, city):
    """Parse and display current weather conditions."""
    try:
        current = data["current_condition"][0]

        temp_c = current["temp_C"]
        temp_f = current["temp_F"]
        feels_c = current["FeelsLikeC"]
        feels_f = current["FeelsLikeF"]
        humidity = current["humidity"]
        description = current["weatherDesc"][0]["value"]
        wind_speed = current["windspeedKmph"]
        wind_dir = current["winddir16Point"]
        uv_index = current["uvIndex"]
        observation_time = current.get("observation_time", "N/A")

        # Area name from the API
        area = data.get("nearest_area", [{}])[0]
        area_name = area.get("areaName", [{}])[0].get("value", city)
        country = area.get("country", [{}])[0].get("value", "")

        print(f"\n-- Current Weather: {area_name}, {country} --")
        print(f"  Condition:   {description}")
        print(f"  Temperature: {temp_c}C ({temp_f}F)")
        print(f"  Feels Like:  {feels_c}C ({feels_f}F)")
        print(f"  Humidity:    {humidity}%")
        print(f"  Wind:        {wind_speed} km/h {wind_dir}")
        print(f"  UV Index:    {uv_index}")
        print(f"\n  Observation time: {observation_time}")

    except (KeyError, IndexError) as e:
        print(f"  Error parsing weather data: {e}")
```

### Step 3: Build the Forecast Display

The API provides multi-day forecast data. We'll parse it and show a clean 3-day outlook with high/low temperatures and conditions.

```python
def display_forecast(data, city):
    """Display a 3-day weather forecast."""
    try:
        forecasts = data.get("weather", [])

        if not forecasts:
            print("  No forecast data available.")
            return

        area = data.get("nearest_area", [{}])[0]
        area_name = area.get("areaName", [{}])[0].get("value", city)

        print(f"\n-- 3-Day Forecast: {area_name} --")
        print(f"  {'Date':<14}{'Condition':<22}{'High':<10}{'Low':<10}{'Rain %'}")
        print("  " + "-" * 60)

        for day in forecasts[:3]:
            date = day["date"]
            max_c = day["maxtempC"]
            min_c = day["mintempC"]
            max_f = day["maxtempF"]
            min_f = day["mintempF"]

            # Get midday weather for the description
            hourly = day.get("hourly", [])
            # Use the noon entry (index 4 out of 8 three-hour blocks)
            midday = hourly[4] if len(hourly) > 4 else hourly[0]
            desc = midday["weatherDesc"][0]["value"]
            chance_rain = midday.get("chanceofrain", "?")

            print(f"  {date:<14}{desc:<22}"
                  f"{max_c}C({max_f}F)  {min_c}C({min_f}F)  {chance_rain}%")

        # Simple visual bar for temperature trend
        print(f"\n  Temperature trend:")
        for day in forecasts[:3]:
            max_c = int(day["maxtempC"])
            bar = "#" * max(1, max_c // 2)
            print(f"    {day['date']}: {bar} {max_c}C")

    except (KeyError, IndexError) as e:
        print(f"  Error parsing forecast data: {e}")
```

### Step 4: Implement Favorite Cities

Let users save their frequently checked cities to a JSON file for quick access.

```python
def load_favorites():
    """Load favorite cities from JSON file."""
    if not os.path.exists(FAVORITES_FILE):
        return []
    try:
        with open(FAVORITES_FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []


def save_favorites(favorites):
    """Save favorite cities to JSON file."""
    with open(FAVORITES_FILE, "w") as f:
        json.dump(favorites, f, indent=2)


def add_favorite(favorites):
    """Add a city to favorites."""
    city = input("\nCity to add: ").strip()
    if not city:
        print("  No city entered.")
        return favorites

    # Verify the city exists by fetching weather
    print(f"  Verifying '{city}'...")
    data = fetch_weather(city)
    if data:
        # Use the canonical name from the API
        area = data.get("nearest_area", [{}])[0]
        canonical = area.get("areaName", [{}])[0].get("value", city)

        if canonical.lower() not in [f.lower() for f in favorites]:
            favorites.append(canonical)
            save_favorites(favorites)
            print(f"  Added '{canonical}' to favorites!")
        else:
            print(f"  '{canonical}' is already in your favorites.")
    else:
        print("  Could not verify city. Not added.")

    return favorites


def remove_favorite(favorites):
    """Remove a city from favorites."""
    if not favorites:
        print("\n  No favorites saved yet.")
        return favorites

    print("\nYour favorites:")
    for i, city in enumerate(favorites, 1):
        print(f"  {i}. {city}")

    try:
        choice = int(input("Number to remove: "))
        if 1 <= choice <= len(favorites):
            removed = favorites.pop(choice - 1)
            save_favorites(favorites)
            print(f"  Removed '{removed}'.")
        else:
            print("  Invalid number.")
    except ValueError:
        print("  Please enter a number.")

    return favorites


def view_favorites(favorites):
    """Display favorites with a quick weather summary."""
    if not favorites:
        print("\n  No favorites saved yet. Add some with option 3!")
        return

    print("\n-- Favorite Cities --")
    for city in favorites:
        data = fetch_weather(city)
        if data:
            current = data["current_condition"][0]
            temp = current["temp_C"]
            desc = current["weatherDesc"][0]["value"]
            print(f"  {city:<20} {temp}C  {desc}")
        else:
            print(f"  {city:<20} (could not fetch)")
```

### Step 5: Build the Main Application

```python
def check_weather():
    """Prompt for a city and show current weather."""
    city = input("\nCity: ").strip()
    if not city:
        print("  No city entered.")
        return

    print(f"  Fetching weather for '{city}'...")
    data = fetch_weather(city)
    if data:
        display_current_weather(data, city)


def check_forecast():
    """Prompt for a city and show 3-day forecast."""
    city = input("\nCity: ").strip()
    if not city:
        print("  No city entered.")
        return

    print(f"  Fetching forecast for '{city}'...")
    data = fetch_weather(city)
    if data:
        display_forecast(data, city)


def main():
    """Main application loop."""
    print("=" * 35)
    print("    WEATHER DASHBOARD")
    print("=" * 35)

    favorites = load_favorites()
    if favorites:
        print(f"Loaded {len(favorites)} favorite city/cities.")

    while True:
        print("\n1. Check Weather     4. Remove Favorite")
        print("2. 3-Day Forecast    5. View Favorites")
        print("3. Add Favorite      6. Exit")

        choice = input("\nChoice: ").strip()

        if choice == "1":
            check_weather()
        elif choice == "2":
            check_forecast()
        elif choice == "3":
            favorites = add_favorite(favorites)
        elif choice == "4":
            favorites = remove_favorite(favorites)
        elif choice == "5":
            view_favorites(favorites)
        elif choice == "6":
            print("\nStay dry out there!")
            break
        else:
            print("Invalid choice. Please enter 1-6.")


if __name__ == "__main__":
    main()
```

## Challenges (Level Up!)

1. **Weather alerts:** Compare the forecast against configurable thresholds (e.g., temperature below 0, rain chance above 80%) and display alerts. Store thresholds in a config JSON file.

2. **Historical comparison:** Cache each day's weather to a CSV file. After a week of data, show trends like "Today is 5 degrees warmer than the weekly average."

3. **Multiple API support:** Add a fallback API (like Open-Meteo, also free and keyless) so if wttr.in is down, the app still works. Abstract the API call behind a common interface.

## Portfolio Tips

This project shows you can work with real external APIs, handle network errors gracefully, and build data-rich displays. When presenting it:

- **GitHub:** Include screenshots showing both current weather and forecast output. Mention that it requires no API key (lowers the barrier for anyone trying your code).
- **Resume:** "Built a CLI weather dashboard consuming the wttr.in REST API with JSON parsing, multi-day forecasting, and persistent favorite cities."
- **Interview talking point:** Discuss how you handled network failures (timeouts, bad city names, no internet). Talk about your choice to use `urllib` over `requests` for zero dependencies, and how you'd refactor to use `requests` in a production setting.

---

# Project 6: Web Scraper & Data Analyzer

> **Difficulty:** 3/5 | **Time:** ~2.5 hours | **Skills:** BeautifulSoup, pandas, data analysis
> **Code:** https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/final-projects/project-06-web-scraper/

## What You'll Build

A web scraper that collects quotes from quotes.toscrape.com (a site built specifically for practicing scraping), stores the data in a structured format, and then analyzes it - finding the most prolific authors, the most popular tags, and generating text-based visualizations.

Here's what the output looks like:

```
=== WEB SCRAPER & DATA ANALYZER ===

Scraping page 1... found 10 quotes
Scraping page 2... found 10 quotes
...
Scraping page 10... found 10 quotes

Total quotes collected: 100

-- Analysis Menu --
1. Top Authors
2. Tag Analysis
3. Longest/Shortest Quotes
4. Search Quotes
5. Export to CSV
6. Exit

Choice: 1

-- Top 10 Authors --
  Albert Einstein      ################  10 quotes
  J.K. Rowling         ############      6 quotes
  Steve Martin         ######            3 quotes
  ...
```

## Skills You'll Use

- Web scraping with BeautifulSoup (learned in Chapter 13)
- Data structures (lists, dicts) (learned in Chapter 4)
- File I/O and CSV (learned in Chapter 7)
- String manipulation (learned in Chapter 2)
- Functions and program design (learned in Chapter 5)
- List comprehensions (learned in Chapter 4)

## Step-by-Step Build Guide

### Step 1: Install Dependencies and Set Up

First, install the required library. BeautifulSoup is the go-to Python library for parsing HTML.

```bash
pip install beautifulsoup4
```

Now set up the project file:

```python
# web_scraper.py

import csv
import json
from urllib.request import urlopen, Request
from urllib.error import URLError
from collections import Counter

try:
    from bs4 import BeautifulSoup
except ImportError:
    print("Please install beautifulsoup4: pip install beautifulsoup4")
    exit(1)

BASE_URL = "https://quotes.toscrape.com"
```

### Step 2: Build the Scraper

This function scrapes one page at a time, extracting the quote text, author, and tags. We then loop through all pages.

```python
def scrape_page(url):
    """Scrape a single page and return a list of quote dictionaries."""
    quotes = []

    try:
        request = Request(url, headers={"User-Agent": "Python-Scraper-Project"})
        with urlopen(request, timeout=10) as response:
            html = response.read().decode()
    except URLError as e:
        print(f"  Error fetching {url}: {e}")
        return quotes, None

    soup = BeautifulSoup(html, "html.parser")

    # Each quote is in a div with class "quote"
    for quote_div in soup.find_all("div", class_="quote"):
        text_span = quote_div.find("span", class_="text")
        author_span = quote_div.find("small", class_="author")
        tag_elements = quote_div.find_all("a", class_="tag")

        if text_span and author_span:
            quote = {
                "text": text_span.get_text().strip("\u201c\u201d"),
                "author": author_span.get_text(),
                "tags": [tag.get_text() for tag in tag_elements]
            }
            quotes.append(quote)

    # Check if there's a next page
    next_btn = soup.find("li", class_="next")
    next_url = None
    if next_btn:
        next_link = next_btn.find("a")
        if next_link:
            next_url = BASE_URL + next_link["href"]

    return quotes, next_url


def scrape_all_quotes():
    """Scrape all pages and return the complete list of quotes."""
    all_quotes = []
    url = BASE_URL
    page = 1

    while url:
        print(f"  Scraping page {page}...", end=" ")
        quotes, next_url = scrape_page(url)
        print(f"found {len(quotes)} quotes")

        all_quotes.extend(quotes)
        url = next_url
        page += 1

    print(f"\n  Total quotes collected: {len(all_quotes)}")
    return all_quotes
```

### Step 3: Build the Analysis Functions

Now the fun part - turning raw data into insights. We'll analyze authors, tags, and quote characteristics.

```python
def analyze_top_authors(quotes, limit=10):
    """Find and display the most quoted authors."""
    author_counts = Counter(q["author"] for q in quotes)
    top = author_counts.most_common(limit)

    print(f"\n-- Top {limit} Authors --")
    if not top:
        print("  No data to analyze.")
        return

    max_count = top[0][1]
    for author, count in top:
        bar_length = int((count / max_count) * 20)
        bar = "#" * bar_length
        print(f"  {author:<25}{bar:<22}{count} quotes")

    return author_counts


def analyze_tags(quotes, limit=15):
    """Analyze and display the most popular tags."""
    all_tags = []
    for q in quotes:
        all_tags.extend(q["tags"])

    tag_counts = Counter(all_tags)
    top = tag_counts.most_common(limit)

    print(f"\n-- Top {limit} Tags --")
    if not top:
        print("  No tags found.")
        return

    max_count = top[0][1]
    for tag, count in top:
        bar_length = int((count / max_count) * 20)
        bar = "#" * bar_length
        print(f"  {tag:<20}{bar:<22}{count}")

    # Tag cloud style display
    print("\n  Tag cloud (by frequency):")
    cloud_tags = tag_counts.most_common(20)
    line = "  "
    for tag, count in cloud_tags:
        entry = f"[{tag}:{count}] "
        if len(line) + len(entry) > 70:
            print(line)
            line = "  "
        line += entry
    if line.strip():
        print(line)

    return tag_counts


def analyze_quote_lengths(quotes):
    """Analyze quote lengths and show extremes."""
    if not quotes:
        print("  No quotes to analyze.")
        return

    lengths = [(len(q["text"]), q) for q in quotes]
    lengths.sort(key=lambda x: x[0])

    avg_length = sum(l for l, _ in lengths) / len(lengths)

    print("\n-- Quote Length Analysis --")
    print(f"  Total quotes: {len(quotes)}")
    print(f"  Average length: {avg_length:.0f} characters")
    print(f"  Shortest: {lengths[0][0]} characters")
    print(f"  Longest: {lengths[-1][0]} characters")

    # Distribution
    short = sum(1 for l, _ in lengths if l < 50)
    medium = sum(1 for l, _ in lengths if 50 <= l < 150)
    long_q = sum(1 for l, _ in lengths if l >= 150)

    print(f"\n  Distribution:")
    print(f"    Short  (<50 chars):  {'#' * short} ({short})")
    print(f"    Medium (50-150):     {'#' * medium} ({medium})")
    print(f"    Long   (>150):       {'#' * long_q} ({long_q})")

    print(f"\n  Shortest quote:")
    print(f'    "{lengths[0][1]["text"][:80]}..."')
    print(f'    - {lengths[0][1]["author"]}')

    print(f"\n  Longest quote:")
    text = lengths[-1][1]["text"]
    preview = text[:100] + "..." if len(text) > 100 else text
    print(f'    "{preview}"')
    print(f'    - {lengths[-1][1]["author"]}')
```

### Step 4: Add Search and Export

```python
def search_quotes(quotes):
    """Search quotes by keyword, author, or tag."""
    print("\n-- Search Quotes --")
    print("  Search by: 1=Keyword  2=Author  3=Tag")
    search_type = input("  Choice: ").strip()

    query = input("  Search term: ").strip().lower()
    if not query:
        print("  No search term entered.")
        return

    results = []
    if search_type == "1":
        results = [q for q in quotes if query in q["text"].lower()]
    elif search_type == "2":
        results = [q for q in quotes if query in q["author"].lower()]
    elif search_type == "3":
        results = [q for q in quotes
                   if any(query in tag.lower() for tag in q["tags"])]
    else:
        results = [q for q in quotes
                   if query in q["text"].lower()
                   or query in q["author"].lower()]

    print(f"\n  Found {len(results)} result(s):")
    for i, q in enumerate(results[:10], 1):
        text = q["text"][:80] + "..." if len(q["text"]) > 80 else q["text"]
        print(f'\n  {i}. "{text}"')
        print(f'     - {q["author"]}')
        if q["tags"]:
            print(f'     Tags: {", ".join(q["tags"])}')

    if len(results) > 10:
        print(f"\n  ... and {len(results) - 10} more.")


def export_to_csv(quotes):
    """Export all quotes to a CSV file."""
    filename = "quotes_data.csv"

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Author", "Quote", "Tags", "Length"])

        for q in quotes:
            writer.writerow([
                q["author"],
                q["text"],
                "; ".join(q["tags"]),
                len(q["text"])
            ])

    print(f"\n  Exported {len(quotes)} quotes to {filename}")

    # Also save as JSON for good measure
    json_file = "quotes_data.json"
    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(quotes, f, indent=2, ensure_ascii=False)

    print(f"  Also saved to {json_file}")
```

### Step 5: Wire Up the Main Application

```python
def main():
    """Main application."""
    print("=" * 40)
    print("  WEB SCRAPER & DATA ANALYZER")
    print("=" * 40)
    print("\nScraping quotes from quotes.toscrape.com...")

    quotes = scrape_all_quotes()

    if not quotes:
        print("No quotes collected. Check your internet connection.")
        return

    while True:
        print("\n-- Analysis Menu --")
        print("1. Top Authors")
        print("2. Tag Analysis")
        print("3. Quote Length Analysis")
        print("4. Search Quotes")
        print("5. Export to CSV")
        print("6. Exit")

        choice = input("\nChoice: ").strip()

        if choice == "1":
            analyze_top_authors(quotes)
        elif choice == "2":
            analyze_tags(quotes)
        elif choice == "3":
            analyze_quote_lengths(quotes)
        elif choice == "4":
            search_quotes(quotes)
        elif choice == "5":
            export_to_csv(quotes)
        elif choice == "6":
            print("\nHappy analyzing!")
            break
        else:
            print("Invalid choice. Please enter 1-6.")


if __name__ == "__main__":
    main()
```

## Challenges (Level Up!)

1. **Scrape author details:** Each author name on the site links to a bio page. Follow those links and scrape the author's birth date, birthplace, and description. Add an "Author Profile" option to your menu.

2. **Visualization upgrade:** Use the `matplotlib` library to generate actual bar charts and pie charts of your data. Save them as PNG files. This is a great preview of data science skills.

3. **Scheduled scraping:** Use Python's `schedule` or `time` module to re-scrape daily and track how the site changes. Store snapshots with timestamps and show a diff between runs.

## Portfolio Tips

This project combines web scraping, data analysis, and data export - skills that data science and backend employers look for. When presenting it:

- **GitHub:** Include sample output files (CSV, JSON) and screenshots of the analysis. Note that you scrape a practice site designed for this purpose (shows ethical awareness).
- **Resume:** "Built a web scraper using BeautifulSoup to collect and analyze 100+ data points, with statistical analysis, search, and CSV/JSON export capabilities."
- **Interview talking point:** Discuss the ethics of web scraping (robots.txt, rate limiting, terms of service). Explain how you structured the data for analysis and why you chose Counter for aggregation. Mention how this pattern could scale to scrape job boards, product prices, or news sites.

---

# Project 7: Chat Application (CLI)

> **Difficulty:** 4/5 | **Time:** ~3 hours | **Skills:** sockets, threading, networking
> **Code:** https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/final-projects/project-07-chat-app/

## What You'll Build

A real-time multi-user chat application with a server and client, built using Python's `socket` and `threading` modules. The server handles multiple connected clients simultaneously, broadcasting messages to all participants. Each client gets a username and can send messages that appear instantly on every other client's screen.

Here's what it looks like:

```
=== CHAT CLIENT ===
Connected to server at localhost:5555
Enter your username: alice

[Server] alice has joined the chat!
[bob] Hey alice, welcome!
[alice] Thanks! What are we talking about?
[charlie] Python sockets. This is pretty cool.
[alice] Agreed!
```

## Skills You'll Use

- Socket programming (learned in Chapter 14)
- Threading for concurrency (learned in Chapter 14)
- Error handling (learned in Chapter 8)
- String encoding/decoding (learned in Chapter 2)
- Object-oriented design (learned in Chapter 9)

## Step-by-Step Build Guide

### Step 1: Build the Chat Server

The server listens for incoming connections, assigns each client to a separate thread, and broadcasts messages to all connected clients. This is the backbone of the application.

```python
# chat_server.py

import socket
import threading
from datetime import datetime

HOST = "127.0.0.1"  # localhost
PORT = 5555
BUFFER_SIZE = 1024
ENCODING = "utf-8"


class ChatServer:
    """Multi-client chat server using TCP sockets."""

    def __init__(self, host=HOST, port=PORT):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET,
                                       socket.SO_REUSEADDR, 1)
        self.clients = {}  # {client_socket: username}
        self.lock = threading.Lock()  # Thread-safe client management

    def start(self):
        """Start the server and listen for connections."""
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print(f"[SERVER] Running on {self.host}:{self.port}")
        print("[SERVER] Waiting for connections...")

        try:
            while True:
                client_socket, address = self.server_socket.accept()
                print(f"[SERVER] Connection from {address}")

                # Start a new thread for each client
                thread = threading.Thread(
                    target=self.handle_client,
                    args=(client_socket, address),
                    daemon=True
                )
                thread.start()

                with self.lock:
                    active = len(self.clients)
                print(f"[SERVER] Active connections: {active + 1}")

        except KeyboardInterrupt:
            print("\n[SERVER] Shutting down...")
        finally:
            self.shutdown()

    def handle_client(self, client_socket, address):
        """Handle communication with a single client."""
        username = None

        try:
            # First message from client is their username
            client_socket.send("USERNAME".encode(ENCODING))
            username = client_socket.recv(BUFFER_SIZE).decode(ENCODING).strip()

            if not username:
                username = f"User-{address[1]}"

            with self.lock:
                self.clients[client_socket] = username

            # Announce the new user
            join_msg = f"[Server] {username} has joined the chat!"
            print(f"[SERVER] {username} connected from {address}")
            self.broadcast(join_msg, exclude=client_socket)
            client_socket.send(f"[Server] Welcome, {username}!".encode(ENCODING))

            # Listen for messages
            while True:
                message = client_socket.recv(BUFFER_SIZE).decode(ENCODING)
                if not message:
                    break

                # Handle special commands
                if message.startswith("/"):
                    self.handle_command(message, client_socket, username)
                else:
                    timestamp = datetime.now().strftime("%H:%M")
                    formatted = f"[{username} {timestamp}] {message}"
                    print(formatted)
                    self.broadcast(formatted, exclude=client_socket)

        except (ConnectionResetError, ConnectionAbortedError, OSError):
            pass
        finally:
            self.disconnect_client(client_socket, username)

    def handle_command(self, message, client_socket, username):
        """Handle chat commands like /users, /quit, /help."""
        command = message.strip().lower()

        if command == "/users":
            with self.lock:
                user_list = ", ".join(self.clients.values())
            client_socket.send(
                f"[Server] Online users: {user_list}".encode(ENCODING)
            )
        elif command == "/help":
            help_text = (
                "[Server] Commands: /users (list online), "
                "/quit (disconnect), /help (this message)"
            )
            client_socket.send(help_text.encode(ENCODING))
        elif command == "/quit":
            client_socket.send("[Server] Goodbye!".encode(ENCODING))
            raise ConnectionResetError("User quit")

    def broadcast(self, message, exclude=None):
        """Send a message to all connected clients."""
        with self.lock:
            disconnected = []
            for client_socket in self.clients:
                if client_socket != exclude:
                    try:
                        client_socket.send(message.encode(ENCODING))
                    except (BrokenPipeError, OSError):
                        disconnected.append(client_socket)

            # Clean up any broken connections
            for sock in disconnected:
                self.disconnect_client(sock, self.clients.get(sock))

    def disconnect_client(self, client_socket, username):
        """Remove a client and notify others."""
        with self.lock:
            if client_socket in self.clients:
                del self.clients[client_socket]

        try:
            client_socket.close()
        except OSError:
            pass

        if username:
            leave_msg = f"[Server] {username} has left the chat."
            print(f"[SERVER] {username} disconnected")
            self.broadcast(leave_msg)

    def shutdown(self):
        """Shut down the server gracefully."""
        print("[SERVER] Closing all connections...")
        with self.lock:
            for client_socket in list(self.clients.keys()):
                try:
                    client_socket.send(
                        "[Server] Server is shutting down.".encode(ENCODING)
                    )
                    client_socket.close()
                except OSError:
                    pass
            self.clients.clear()
        self.server_socket.close()
        print("[SERVER] Server stopped.")


if __name__ == "__main__":
    server = ChatServer()
    server.start()
```

### Step 2: Build the Chat Client

The client connects to the server, sends a username, then runs two threads: one for receiving messages (so they appear in real time) and one for reading user input.

```python
# chat_client.py

import socket
import threading
import sys

HOST = "127.0.0.1"
PORT = 5555
BUFFER_SIZE = 1024
ENCODING = "utf-8"


class ChatClient:
    """Chat client that connects to the ChatServer."""

    def __init__(self, host=HOST, port=PORT):
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.running = True
        self.username = None

    def connect(self):
        """Connect to the server and start chatting."""
        try:
            self.client_socket.connect((self.host, self.port))
            print(f"Connected to server at {self.host}:{self.port}")
        except ConnectionRefusedError:
            print(f"Could not connect to {self.host}:{self.port}")
            print("Make sure the server is running first.")
            return

        # Wait for username request
        response = self.client_socket.recv(BUFFER_SIZE).decode(ENCODING)
        if response == "USERNAME":
            self.username = input("Enter your username: ").strip()
            if not self.username:
                self.username = "Anonymous"
            self.client_socket.send(self.username.encode(ENCODING))

        # Start the receive thread
        receive_thread = threading.Thread(
            target=self.receive_messages,
            daemon=True
        )
        receive_thread.start()

        # Main thread handles sending
        self.send_messages()

    def receive_messages(self):
        """Continuously receive and display messages from the server."""
        while self.running:
            try:
                message = self.client_socket.recv(BUFFER_SIZE).decode(ENCODING)
                if not message:
                    print("\nDisconnected from server.")
                    self.running = False
                    break
                print(f"\r{message}")
                # Re-show the input prompt
                print(f"[{self.username}] ", end="", flush=True)
            except (ConnectionResetError, OSError):
                if self.running:
                    print("\nLost connection to server.")
                    self.running = False
                break

    def send_messages(self):
        """Read user input and send messages to the server."""
        print("\nType your messages (or /help for commands, /quit to exit):\n")

        while self.running:
            try:
                message = input(f"[{self.username}] ")
                if not message:
                    continue

                if message.strip().lower() == "/quit":
                    self.client_socket.send(message.encode(ENCODING))
                    print("Disconnecting...")
                    self.running = False
                    break

                self.client_socket.send(message.encode(ENCODING))

            except (EOFError, KeyboardInterrupt):
                print("\nDisconnecting...")
                self.running = False
                break

        self.disconnect()

    def disconnect(self):
        """Close the connection."""
        self.running = False
        try:
            self.client_socket.close()
        except OSError:
            pass
        print("Disconnected.")


def main():
    print("=" * 30)
    print("     CHAT CLIENT")
    print("=" * 30)

    # Allow custom host/port from command line
    host = sys.argv[1] if len(sys.argv) > 1 else HOST
    port = int(sys.argv[2]) if len(sys.argv) > 2 else PORT

    client = ChatClient(host, port)
    client.connect()


if __name__ == "__main__":
    main()
```

### Step 3: Test the Application

Open three terminal windows. In the first, start the server:

```bash
python chat_server.py
```

In the second and third terminals, start clients:

```bash
python chat_client.py
```

Give each client a different username. Type messages in one client and watch them appear in the other. Try the `/users` and `/help` commands.

### Step 4: Understanding the Architecture

Take a moment to understand what's happening under the hood:

1. The **server** creates a TCP socket and listens on port 5555
2. When a client connects, the server spawns a **new thread** to handle that client
3. Each client thread listens for incoming messages in an infinite loop
4. When a message arrives, the server **broadcasts** it to all other clients
5. The **lock** (`threading.Lock`) prevents race conditions when multiple threads modify the client list simultaneously
6. The **client** uses two threads: one for receiving (background) and one for sending (foreground/input)

This is the same fundamental pattern used by real chat systems, just simplified.

## Challenges (Level Up!)

1. **Private messages:** Implement a `/dm username message` command that sends a message only to a specific user. The server needs to look up the recipient's socket by username.

2. **Chat rooms:** Add support for multiple rooms with `/join roomname` and `/leave` commands. Only broadcast messages to users in the same room. Track room membership in a dictionary.

3. **Message history:** Store the last 50 messages on the server. When a new client connects, send them the recent history so they can catch up on the conversation.

## Portfolio Tips

A networking project is a standout on any junior developer's portfolio. When presenting this:

- **GitHub:** Include clear instructions for running the server and client. Add a diagram showing the client-server architecture. Mention the threading model.
- **Resume:** "Built a multi-user CLI chat application using TCP sockets and threading with broadcast messaging, user commands, and graceful disconnection handling."
- **Interview talking point:** Explain the threading model and why you used a lock for the client dictionary. Discuss the difference between TCP and UDP and why TCP is appropriate for chat (reliable, ordered delivery). Mention how you'd scale this - an event loop with `asyncio` or a message broker like Redis Pub/Sub.

---

# Project 8: Blog REST API

> **Difficulty:** 4/5 | **Time:** ~3 hours | **Skills:** Flask, SQLite, CRUD, authentication
> **Code:** https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/final-projects/project-08-blog-api/

## What You'll Build

A fully functional REST API for a blog application using Flask and SQLite. It includes user registration and login with token-based authentication, full CRUD operations for blog posts, and proper HTTP status codes. You can test it with `curl` or any API testing tool.

Here's what interacting with it looks like:

```bash
# Register a user
$ curl -X POST http://localhost:5000/api/register \
    -H "Content-Type: application/json" \
    -d '{"username": "alice", "password": "secret123"}'

{"message": "User created successfully", "user_id": 1}

# Login and get a token
$ curl -X POST http://localhost:5000/api/login \
    -H "Content-Type: application/json" \
    -d '{"username": "alice", "password": "secret123"}'

{"token": "abc123xyz...", "username": "alice"}

# Create a blog post
$ curl -X POST http://localhost:5000/api/posts \
    -H "Authorization: Bearer abc123xyz..." \
    -H "Content-Type: application/json" \
    -d '{"title": "My First Post", "content": "Hello, world!"}'

{"id": 1, "title": "My First Post", "author": "alice", "created_at": "..."}
```

## Skills You'll Use

- Flask web framework (learned in Chapter 15)
- SQLite database (learned in Chapter 11)
- REST API design (learned in Chapter 15)
- Password hashing (learned in Chapter 15)
- Error handling (learned in Chapter 8)
- JSON (learned in Chapter 7)

## Step-by-Step Build Guide

### Step 1: Install Dependencies and Set Up

```bash
pip install flask
```

Create the project structure:

```python
# blog_api.py

import sqlite3
import hashlib
import secrets
import os
from datetime import datetime
from functools import wraps
from flask import Flask, request, jsonify, g

app = Flask(__name__)
app.config["DATABASE"] = "blog.db"
```

### Step 2: Set Up the Database Layer

We'll use SQLite with a helper pattern that gives each request its own database connection.

```python
def get_db():
    """Get a database connection for the current request."""
    if "db" not in g:
        g.db = sqlite3.connect(app.config["DATABASE"])
        g.db.row_factory = sqlite3.Row  # Return rows as dictionaries
        g.db.execute("PRAGMA foreign_keys = ON")
    return g.db


@app.teardown_appcontext
def close_db(exception):
    """Close database connection when request ends."""
    db = g.pop("db", None)
    if db is not None:
        db.close()


def init_db():
    """Create database tables if they don't exist."""
    db = sqlite3.connect(app.config["DATABASE"])
    db.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            token TEXT UNIQUE,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """)
    db.execute("""
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            author_id INTEGER NOT NULL,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            updated_at TEXT DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (author_id) REFERENCES users (id)
        )
    """)
    db.commit()
    db.close()
```

### Step 3: Build Authentication

We need three pieces: password hashing, token generation, and a decorator to protect routes.

```python
def hash_password(password):
    """Hash a password with a salt using SHA-256."""
    salt = secrets.token_hex(16)
    hash_value = hashlib.sha256((salt + password).encode()).hexdigest()
    return f"{salt}:{hash_value}"


def verify_password(stored_hash, password):
    """Verify a password against a stored hash."""
    salt, hash_value = stored_hash.split(":")
    check = hashlib.sha256((salt + password).encode()).hexdigest()
    return check == hash_value


def generate_token():
    """Generate a secure random token."""
    return secrets.token_hex(32)


def login_required(f):
    """Decorator to require authentication on a route."""
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get("Authorization")

        if not auth_header or not auth_header.startswith("Bearer "):
            return jsonify({"error": "Missing or invalid token"}), 401

        token = auth_header.split(" ")[1]

        db = get_db()
        user = db.execute(
            "SELECT * FROM users WHERE token = ?", (token,)
        ).fetchone()

        if not user:
            return jsonify({"error": "Invalid or expired token"}), 401

        # Attach user info to the request context
        g.current_user = dict(user)
        return f(*args, **kwargs)

    return decorated
```

### Step 4: Create Auth Endpoints

```python
@app.route("/api/register", methods=["POST"])
def register():
    """Register a new user."""
    data = request.get_json()

    if not data or not data.get("username") or not data.get("password"):
        return jsonify({"error": "Username and password are required"}), 400

    username = data["username"].strip()
    password = data["password"]

    if len(username) < 3:
        return jsonify({"error": "Username must be at least 3 characters"}), 400
    if len(password) < 6:
        return jsonify({"error": "Password must be at least 6 characters"}), 400

    db = get_db()

    # Check if username exists
    existing = db.execute(
        "SELECT id FROM users WHERE username = ?", (username,)
    ).fetchone()

    if existing:
        return jsonify({"error": "Username already taken"}), 409

    password_hash = hash_password(password)

    cursor = db.execute(
        "INSERT INTO users (username, password_hash) VALUES (?, ?)",
        (username, password_hash)
    )
    db.commit()

    return jsonify({
        "message": "User created successfully",
        "user_id": cursor.lastrowid
    }), 201


@app.route("/api/login", methods=["POST"])
def login():
    """Login and receive an auth token."""
    data = request.get_json()

    if not data or not data.get("username") or not data.get("password"):
        return jsonify({"error": "Username and password are required"}), 400

    db = get_db()
    user = db.execute(
        "SELECT * FROM users WHERE username = ?", (data["username"],)
    ).fetchone()

    if not user or not verify_password(user["password_hash"], data["password"]):
        return jsonify({"error": "Invalid username or password"}), 401

    # Generate and store a new token
    token = generate_token()
    db.execute(
        "UPDATE users SET token = ? WHERE id = ?", (token, user["id"])
    )
    db.commit()

    return jsonify({
        "token": token,
        "username": user["username"],
        "message": "Login successful"
    })
```

### Step 5: Build the Blog Post CRUD Endpoints

These are the core of the API - creating, reading, updating, and deleting blog posts.

```python
@app.route("/api/posts", methods=["GET"])
def get_posts():
    """Get all posts (public, no auth required)."""
    db = get_db()

    # Support optional query parameters
    author = request.args.get("author")
    limit = request.args.get("limit", 20, type=int)
    offset = request.args.get("offset", 0, type=int)

    if author:
        rows = db.execute("""
            SELECT p.*, u.username as author_name
            FROM posts p JOIN users u ON p.author_id = u.id
            WHERE u.username = ?
            ORDER BY p.created_at DESC
            LIMIT ? OFFSET ?
        """, (author, limit, offset)).fetchall()
    else:
        rows = db.execute("""
            SELECT p.*, u.username as author_name
            FROM posts p JOIN users u ON p.author_id = u.id
            ORDER BY p.created_at DESC
            LIMIT ? OFFSET ?
        """, (limit, offset)).fetchall()

    posts = []
    for row in rows:
        posts.append({
            "id": row["id"],
            "title": row["title"],
            "content": row["content"],
            "author": row["author_name"],
            "created_at": row["created_at"],
            "updated_at": row["updated_at"]
        })

    return jsonify({"posts": posts, "count": len(posts)})


@app.route("/api/posts/<int:post_id>", methods=["GET"])
def get_post(post_id):
    """Get a single post by ID."""
    db = get_db()
    row = db.execute("""
        SELECT p.*, u.username as author_name
        FROM posts p JOIN users u ON p.author_id = u.id
        WHERE p.id = ?
    """, (post_id,)).fetchone()

    if not row:
        return jsonify({"error": "Post not found"}), 404

    return jsonify({
        "id": row["id"],
        "title": row["title"],
        "content": row["content"],
        "author": row["author_name"],
        "created_at": row["created_at"],
        "updated_at": row["updated_at"]
    })


@app.route("/api/posts", methods=["POST"])
@login_required
def create_post():
    """Create a new blog post (auth required)."""
    data = request.get_json()

    if not data or not data.get("title") or not data.get("content"):
        return jsonify({"error": "Title and content are required"}), 400

    title = data["title"].strip()
    content = data["content"].strip()

    if len(title) > 200:
        return jsonify({"error": "Title must be under 200 characters"}), 400

    db = get_db()
    now = datetime.now().isoformat()

    cursor = db.execute(
        """INSERT INTO posts (title, content, author_id, created_at, updated_at)
           VALUES (?, ?, ?, ?, ?)""",
        (title, content, g.current_user["id"], now, now)
    )
    db.commit()

    return jsonify({
        "id": cursor.lastrowid,
        "title": title,
        "content": content,
        "author": g.current_user["username"],
        "created_at": now
    }), 201


@app.route("/api/posts/<int:post_id>", methods=["PUT"])
@login_required
def update_post(post_id):
    """Update a blog post (only the author can update)."""
    db = get_db()
    post = db.execute("SELECT * FROM posts WHERE id = ?", (post_id,)).fetchone()

    if not post:
        return jsonify({"error": "Post not found"}), 404
    if post["author_id"] != g.current_user["id"]:
        return jsonify({"error": "You can only edit your own posts"}), 403

    data = request.get_json()
    title = data.get("title", post["title"]).strip()
    content = data.get("content", post["content"]).strip()
    now = datetime.now().isoformat()

    db.execute(
        "UPDATE posts SET title = ?, content = ?, updated_at = ? WHERE id = ?",
        (title, content, now, post_id)
    )
    db.commit()

    return jsonify({
        "id": post_id,
        "title": title,
        "content": content,
        "updated_at": now,
        "message": "Post updated"
    })


@app.route("/api/posts/<int:post_id>", methods=["DELETE"])
@login_required
def delete_post(post_id):
    """Delete a blog post (only the author can delete)."""
    db = get_db()
    post = db.execute("SELECT * FROM posts WHERE id = ?", (post_id,)).fetchone()

    if not post:
        return jsonify({"error": "Post not found"}), 404
    if post["author_id"] != g.current_user["id"]:
        return jsonify({"error": "You can only delete your own posts"}), 403

    db.execute("DELETE FROM posts WHERE id = ?", (post_id,))
    db.commit()

    return jsonify({"message": "Post deleted", "id": post_id})
```

### Step 6: Add Error Handlers and Run

```python
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Endpoint not found"}), 404


@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify({"error": "Method not allowed"}), 405


@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500


if __name__ == "__main__":
    init_db()
    print("Blog API running at http://localhost:5000")
    print("\nEndpoints:")
    print("  POST   /api/register     - Register a new user")
    print("  POST   /api/login        - Login and get token")
    print("  GET    /api/posts        - List all posts")
    print("  GET    /api/posts/<id>   - Get a single post")
    print("  POST   /api/posts        - Create a post (auth)")
    print("  PUT    /api/posts/<id>   - Update a post (auth)")
    print("  DELETE /api/posts/<id>   - Delete a post (auth)")
    app.run(debug=True)
```

### Step 7: Test Your API

Start the server and test with `curl` commands:

```bash
# Start the server
python blog_api.py

# In another terminal:

# Register
curl -X POST http://localhost:5000/api/register \
  -H "Content-Type: application/json" \
  -d '{"username": "alice", "password": "secret123"}'

# Login (copy the token from the response)
curl -X POST http://localhost:5000/api/login \
  -H "Content-Type: application/json" \
  -d '{"username": "alice", "password": "secret123"}'

# Create a post (replace YOUR_TOKEN)
curl -X POST http://localhost:5000/api/posts \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"title": "Hello World", "content": "My first blog post!"}'

# Get all posts
curl http://localhost:5000/api/posts

# Update a post
curl -X PUT http://localhost:5000/api/posts/1 \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"title": "Hello World (Updated)"}'

# Delete a post
curl -X DELETE http://localhost:5000/api/posts/1 \
  -H "Authorization: Bearer YOUR_TOKEN"
```

## Challenges (Level Up!)

1. **Comments system:** Add a comments table linked to posts. Create endpoints for adding, listing, and deleting comments. Comments should require authentication, and only the comment author or the post author can delete a comment.

2. **Pagination and search:** Add proper pagination with `page` and `per_page` query parameters, returning total count and page info. Add a `/api/posts/search?q=keyword` endpoint that searches titles and content.

3. **Rate limiting:** Implement simple rate limiting that allows only 30 requests per minute per token. Track request timestamps in memory and return a 429 status when the limit is exceeded.

## Portfolio Tips

A REST API is one of the most valuable portfolio pieces you can have - it's the backbone of modern web applications. When presenting this:

- **GitHub:** Include a comprehensive README with all endpoints documented, example `curl` commands, and setup instructions. Consider adding a Postman collection file.
- **Resume:** "Built a RESTful blog API with Flask featuring token-based authentication, SQLite persistence, full CRUD operations, and authorization controls."
- **Interview talking point:** Discuss your authentication approach (token-based vs. session-based), why you check authorization on update/delete (only the author can modify their own posts), and how you'd improve security for production (HTTPS, JWT with expiration, password complexity rules, input sanitization).

---

# Project 9: ML Prediction App

> **Difficulty:** 4/5 | **Time:** ~3 hours | **Skills:** scikit-learn, Flask, model training
> **Code:** https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/final-projects/project-09-ml-prediction/

## What You'll Build

A machine learning application that predicts house prices based on features like square footage, number of bedrooms, and location. You'll generate a realistic training dataset, train a model using scikit-learn, evaluate its performance, save the trained model, and serve predictions through a Flask API.

Here's what using it looks like:

```bash
# Train the model
$ python train_model.py

Training house price prediction model...
Dataset: 1000 samples, 6 features
Training set: 800 samples
Test set: 200 samples

Model Performance:
  R2 Score:           0.92
  Mean Absolute Error: $18,432
  Root Mean Sq Error:  $24,891

Model saved to house_price_model.pkl

# Start the prediction API
$ python prediction_api.py

# Make a prediction
$ curl -X POST http://localhost:5000/predict \
    -H "Content-Type: application/json" \
    -d '{"sqft": 2000, "bedrooms": 3, "bathrooms": 2,
         "age": 10, "garage": 1, "location": "suburban"}'

{"predicted_price": "$342,150", "confidence_range": "$317,718 - $366,582"}
```

## Skills You'll Use

- scikit-learn for ML (learned in Chapter 17)
- Data generation and preprocessing (learned in Chapter 16)
- Flask API (learned in Chapter 15)
- File I/O with pickle (learned in Chapter 7)
- NumPy basics (learned in Chapter 16)
- Error handling (learned in Chapter 8)

## Step-by-Step Build Guide

### Step 1: Install Dependencies

```bash
pip install scikit-learn flask numpy
```

### Step 2: Generate the Training Dataset

Since we don't have a real housing dataset, we'll generate a realistic synthetic one. This is actually a common technique in ML when real data is scarce or proprietary.

```python
# generate_data.py

import csv
import random
import numpy as np

def generate_housing_data(n_samples=1000):
    """Generate a realistic synthetic housing dataset."""
    random.seed(42)
    np.random.seed(42)

    locations = ["urban", "suburban", "rural"]
    location_multiplier = {"urban": 1.4, "suburban": 1.0, "rural": 0.7}

    data = []
    for _ in range(n_samples):
        # Generate correlated features
        sqft = random.randint(600, 5000)
        bedrooms = max(1, min(6, int(sqft / 600) + random.randint(-1, 1)))
        bathrooms = max(1, min(bedrooms, random.randint(1, bedrooms + 1)))
        age = random.randint(0, 80)
        garage = random.choice([0, 1, 2])
        location = random.choice(locations)

        # Calculate price based on realistic-ish formula + noise
        base_price = 50000
        price = base_price
        price += sqft * 150                      # price per sqft
        price += bedrooms * 15000                 # bedroom premium
        price += bathrooms * 12000                # bathroom premium
        price -= age * 1200                       # depreciation
        price += garage * 25000                   # garage value
        price *= location_multiplier[location]    # location factor

        # Add realistic noise (10% standard deviation)
        noise = np.random.normal(0, price * 0.10)
        price = max(50000, price + noise)

        data.append({
            "sqft": sqft,
            "bedrooms": bedrooms,
            "bathrooms": bathrooms,
            "age": age,
            "garage": garage,
            "location": location,
            "price": round(price, 2)
        })

    return data


def save_dataset(data, filename="housing_data.csv"):
    """Save dataset to CSV."""
    fieldnames = ["sqft", "bedrooms", "bathrooms", "age",
                  "garage", "location", "price"]

    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

    print(f"Generated {len(data)} samples -> {filename}")


if __name__ == "__main__":
    data = generate_housing_data(1000)
    save_dataset(data)

    # Quick stats
    prices = [d["price"] for d in data]
    print(f"Price range: ${min(prices):,.0f} - ${max(prices):,.0f}")
    print(f"Average price: ${sum(prices)/len(prices):,.0f}")
```

### Step 3: Train the Model

This is where the ML magic happens. We'll load the data, preprocess it (encoding the location category), split it into training and test sets, train a Random Forest model, and evaluate its performance.

```python
# train_model.py

import csv
import pickle
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_absolute_error, r2_score

MODEL_FILE = "house_price_model.pkl"
ENCODER_FILE = "location_encoder.pkl"


def load_data(filename="housing_data.csv"):
    """Load the housing dataset from CSV."""
    data = []
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)

    # Convert to numpy arrays
    locations = [row["location"] for row in data]

    # Encode location strings as numbers
    encoder = LabelEncoder()
    location_encoded = encoder.fit_transform(locations)

    features = []
    prices = []
    for i, row in enumerate(data):
        features.append([
            float(row["sqft"]),
            int(row["bedrooms"]),
            int(row["bathrooms"]),
            int(row["age"]),
            int(row["garage"]),
            location_encoded[i]
        ])
        prices.append(float(row["price"]))

    X = np.array(features)
    y = np.array(prices)

    return X, y, encoder


def train_and_evaluate():
    """Train the model and print evaluation metrics."""
    print("Training house price prediction model...")
    print()

    # Load data
    X, y, encoder = load_data()
    print(f"Dataset: {X.shape[0]} samples, {X.shape[1]} features")

    # Split into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    print(f"Training set: {len(X_train)} samples")
    print(f"Test set: {len(X_test)} samples")

    # Train Random Forest model
    model = RandomForestRegressor(
        n_estimators=100,
        max_depth=15,
        random_state=42,
        n_jobs=-1  # Use all CPU cores
    )
    model.fit(X_train, y_train)

    # Evaluate
    y_pred = model.predict(X_test)
    r2 = r2_score(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    rmse = np.sqrt(np.mean((y_test - y_pred) ** 2))

    print(f"\nModel Performance:")
    print(f"  R2 Score:            {r2:.3f}")
    print(f"  Mean Absolute Error: ${mae:,.0f}")
    print(f"  Root Mean Sq Error:  ${rmse:,.0f}")

    # Feature importance
    feature_names = ["sqft", "bedrooms", "bathrooms",
                     "age", "garage", "location"]
    importances = model.feature_importances_
    sorted_idx = np.argsort(importances)[::-1]

    print(f"\nFeature Importance:")
    for idx in sorted_idx:
        bar = "#" * int(importances[idx] * 40)
        print(f"  {feature_names[idx]:<12} {bar} ({importances[idx]:.3f})")

    # Save the model and encoder
    with open(MODEL_FILE, "wb") as f:
        pickle.dump(model, f)
    print(f"\nModel saved to {MODEL_FILE}")

    with open(ENCODER_FILE, "wb") as f:
        pickle.dump(encoder, f)
    print(f"Encoder saved to {ENCODER_FILE}")

    return model, encoder


if __name__ == "__main__":
    train_and_evaluate()
```

### Step 4: Build the Prediction API

Now wrap the trained model in a Flask API so anyone can get predictions by sending a JSON request.

```python
# prediction_api.py

import pickle
import numpy as np
from flask import Flask, request, jsonify

app = Flask(__name__)

MODEL_FILE = "house_price_model.pkl"
ENCODER_FILE = "location_encoder.pkl"

# Load model and encoder at startup
try:
    with open(MODEL_FILE, "rb") as f:
        model = pickle.load(f)
    with open(ENCODER_FILE, "rb") as f:
        encoder = pickle.load(f)
    print("Model loaded successfully!")
except FileNotFoundError:
    print("ERROR: Model files not found. Run train_model.py first.")
    exit(1)

VALID_LOCATIONS = list(encoder.classes_)


@app.route("/predict", methods=["POST"])
def predict():
    """Predict house price from features."""
    data = request.get_json()

    if not data:
        return jsonify({"error": "No JSON data provided"}), 400

    # Validate required fields
    required = ["sqft", "bedrooms", "bathrooms", "age", "garage", "location"]
    missing = [f for f in required if f not in data]
    if missing:
        return jsonify({
            "error": f"Missing fields: {', '.join(missing)}",
            "required": required
        }), 400

    # Validate values
    try:
        sqft = float(data["sqft"])
        bedrooms = int(data["bedrooms"])
        bathrooms = int(data["bathrooms"])
        age = int(data["age"])
        garage = int(data["garage"])
        location = data["location"].lower()
    except (ValueError, TypeError) as e:
        return jsonify({"error": f"Invalid value: {e}"}), 400

    if location not in VALID_LOCATIONS:
        return jsonify({
            "error": f"Invalid location. Choose from: {VALID_LOCATIONS}"
        }), 400

    if sqft <= 0 or bedrooms <= 0 or bathrooms <= 0:
        return jsonify({"error": "Values must be positive"}), 400

    # Encode location and create feature array
    location_encoded = encoder.transform([location])[0]
    features = np.array([[sqft, bedrooms, bathrooms, age,
                          garage, location_encoded]])

    # Make prediction
    predicted_price = model.predict(features)[0]

    # Calculate confidence range (rough estimate based on model error)
    margin = predicted_price * 0.07  # ~7% margin
    low = predicted_price - margin
    high = predicted_price + margin

    return jsonify({
        "predicted_price": f"${predicted_price:,.0f}",
        "confidence_range": f"${low:,.0f} - ${high:,.0f}",
        "input": {
            "sqft": sqft,
            "bedrooms": bedrooms,
            "bathrooms": bathrooms,
            "age": age,
            "garage": garage,
            "location": location
        }
    })


@app.route("/model-info", methods=["GET"])
def model_info():
    """Return information about the loaded model."""
    feature_names = ["sqft", "bedrooms", "bathrooms",
                     "age", "garage", "location"]
    importances = model.feature_importances_

    features_info = {}
    for name, imp in zip(feature_names, importances):
        features_info[name] = round(float(imp), 4)

    return jsonify({
        "model_type": "RandomForestRegressor",
        "n_estimators": model.n_estimators,
        "valid_locations": VALID_LOCATIONS,
        "feature_importances": features_info,
        "input_format": {
            "sqft": "int (square footage, e.g., 2000)",
            "bedrooms": "int (1-6)",
            "bathrooms": "int (1-6)",
            "age": "int (years, 0-80)",
            "garage": "int (0, 1, or 2 cars)",
            "location": f"string ({', '.join(VALID_LOCATIONS)})"
        }
    })


@app.route("/", methods=["GET"])
def home():
    """API documentation."""
    return jsonify({
        "name": "House Price Prediction API",
        "endpoints": {
            "POST /predict": "Predict house price from features",
            "GET /model-info": "Get model information",
            "GET /": "This documentation"
        },
        "example_request": {
            "sqft": 2000,
            "bedrooms": 3,
            "bathrooms": 2,
            "age": 10,
            "garage": 1,
            "location": "suburban"
        }
    })


if __name__ == "__main__":
    print("House Price Prediction API")
    print("Endpoints:")
    print("  POST /predict     - Get a price prediction")
    print("  GET  /model-info  - Model details")
    print("  GET  /            - API docs")
    print()
    app.run(debug=True)
```

### Step 5: Run the Full Pipeline

Execute these commands in order:

```bash
# Step 1: Generate the dataset
python generate_data.py

# Step 2: Train the model
python train_model.py

# Step 3: Start the API
python prediction_api.py

# Step 4: Test (in another terminal)
curl http://localhost:5000/

curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"sqft": 2000, "bedrooms": 3, "bathrooms": 2,
       "age": 10, "garage": 1, "location": "suburban"}'

curl http://localhost:5000/model-info
```

## Challenges (Level Up!)

1. **Model comparison:** Train multiple models (Linear Regression, Gradient Boosting, and Random Forest) and compare their performance. Add an endpoint that returns predictions from all three models with their confidence scores.

2. **Input validation and feature engineering:** Add derived features like price-per-sqft from the training data, bed-to-bath ratio, and age categories (new/moderate/old). Retrain and see if performance improves.

3. **Batch predictions:** Add a `/predict/batch` endpoint that accepts a JSON array of houses and returns predictions for all of them at once, along with summary statistics (average predicted price, range).

## Portfolio Tips

An ML project that goes from data to trained model to serving API is exactly what employers want to see. When presenting this:

- **GitHub:** Include all three scripts with clear naming. Add a README that explains the ML pipeline (data generation, training, evaluation, serving). Include the model performance metrics.
- **Resume:** "Built an end-to-end ML pipeline: synthetic data generation, Random Forest model training (R2=0.92), and a Flask REST API serving real-time house price predictions."
- **Interview talking point:** Discuss why you chose Random Forest (handles non-linear relationships, built-in feature importance, robust to outliers). Explain the train/test split and why it matters (preventing overfitting). Talk about how you'd deploy this in production (Docker, cloud hosting, model versioning).

---

# Project 10: AI-Powered Study Buddy

> **Difficulty:** 5/5 | **Time:** ~4 hours | **Skills:** OpenAI API, LangChain, RAG, conversation memory
> **Code:** https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/final-projects/project-10-study-buddy/

## What You'll Build

An intelligent study assistant that loads your study materials (text files, notes, PDFs), lets you ask questions about them using AI, generates quizzes based on the content, and maintains conversation history so it remembers context. This is a real-world application of Retrieval-Augmented Generation (RAG) - the same pattern used in enterprise AI tools.

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

        return "\n\n--\n\n".join(context_parts)

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

        print(f"\n-- Conversation History ({len(self.messages)} messages) --")
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

This is the main class that ties everything together - document context, conversation memory, and AI responses.

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
    print("\n-- Commands --")
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
            # It's a question - ask the study buddy
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

This is your capstone project - the one that makes hiring managers sit up. AI-powered applications are the hottest thing in tech right now. When presenting this:

- **GitHub:** Write an excellent README with screenshots, architecture explanation (document loading, chunking, retrieval, generation), and clear setup instructions. Include sample study materials.
- **Resume:** "Built an AI-powered study assistant using OpenAI's API with RAG (Retrieval-Augmented Generation), document chunking, context-aware Q&A, quiz generation, and persistent conversation memory."
- **Interview talking point:** Explain what RAG is and why it matters (the AI answers from YOUR documents, not just its training data). Discuss the chunking strategy and why you limit context size (token costs, relevance). Talk about how you'd improve retrieval with embeddings and vector databases (Pinecone, ChromaDB). This demonstrates that you understand the architecture behind tools like ChatGPT plugins, Copilot, and enterprise AI assistants.

---

# Appendix A: Python Cheat Sheet

A quick-reference guide to Python syntax and common patterns. Bookmark this page - you'll come back to it constantly.

---

## Variables and Data Types

| Syntax | Example | Notes |
|----|-----|----|
| Integer | `x = 42` | Whole numbers, no size limit |
| Float | `pi = 3.14` | Decimal numbers |
| String | `name = "Alice"` | Text, single or double quotes |
| Boolean | `done = True` | `True` or `False` (capitalized) |
| None | `result = None` | Represents "no value" |
| Type check | `type(x)` | Returns `<class 'int'>` etc. |
| Type convert | `int("42")`, `str(42)`, `float("3.14")` | Can raise ValueError |

## Strings

| Operation | Syntax | Result |
|------|----|----|
| Concatenation | `"Hello" + " " + "World"` | `"Hello World"` |
| Repetition | `"ha" * 3` | `"hahaha"` |
| f-string | `f"Hello, {name}!"` | `"Hello, Alice!"` |
| Length | `len("hello")` | `5` |
| Index | `"hello"[0]` | `"h"` |
| Slice | `"hello"[1:4]` | `"ell"` |
| Upper/Lower | `"hi".upper()`, `"HI".lower()` | `"HI"`, `"hi"` |
| Strip | `" hi ".strip()` | `"hi"` |
| Split | `"a,b,c".split(",")` | `["a", "b", "c"]` |
| Join | `", ".join(["a", "b"])` | `"a, b"` |
| Replace | `"hello".replace("l", "L")` | `"heLLo"` |
| Find | `"hello".find("ll")` | `2` (-1 if not found) |
| Startswith | `"hello".startswith("he")` | `True` |
| Contains | `"ll" in "hello"` | `True` |

## f-String Formatting

| Syntax | Example | Result |
|----|-----|----|
| Variable | `f"{name}"` | Value of `name` |
| Expression | `f"{2 + 3}"` | `"5"` |
| Decimal places | `f"{3.14159:.2f}"` | `"3.14"` |
| Comma separator | `f"{1000000:,}"` | `"1,000,000"` |
| Percentage | `f"{0.85:.1%}"` | `"85.0%"` |
| Padding | `f"{'hi':<10}"` | `"hi        "` |
| Right align | `f"{'hi':>10}"` | `"        hi"` |
| Center | `f"{'hi':^10}"` | `"    hi    "` |
| Zero pad | `f"{42:05d}"` | `"00042"` |

## Lists

| Operation | Syntax | Result/Effect |
|------|----|--------|
| Create | `nums = [1, 2, 3]` | |
| Empty list | `items = []` | |
| Access | `nums[0]`, `nums[-1]` | `1`, `3` |
| Slice | `nums[1:3]` | `[2, 3]` |
| Append | `nums.append(4)` | `[1, 2, 3, 4]` |
| Insert | `nums.insert(0, 0)` | `[0, 1, 2, 3]` |
| Remove | `nums.remove(2)` | Removes first `2` |
| Pop | `nums.pop()` | Removes and returns last |
| Pop at index | `nums.pop(0)` | Removes and returns first |
| Sort | `nums.sort()` | In-place sort |
| Reverse | `nums.reverse()` | In-place reverse |
| Length | `len(nums)` | Number of items |
| Contains | `2 in nums` | `True` |
| Index of | `nums.index(2)` | `1` |
| Count | `nums.count(2)` | Number of occurrences |
| Copy | `nums.copy()` or `nums[:]` | Shallow copy |
| Extend | `nums.extend([4, 5])` | Adds all items |

## List Comprehensions

```python
# Basic
squares = [x**2 for x in range(10)]

# With condition
evens = [x for x in range(20) if x % 2 == 0]

# With transformation
upper = [s.upper() for s in names]

# Nested
flat = [x for row in matrix for x in row]
```

## Dictionaries

| Operation | Syntax | Result/Effect |
|------|----|--------|
| Create | `d = {"name": "Alice", "age": 30}` | |
| Empty dict | `d = {}` | |
| Access | `d["name"]` | `"Alice"` (KeyError if missing) |
| Safe access | `d.get("name", "default")` | `"Alice"` or `"default"` |
| Set | `d["email"] = "a@b.com"` | Adds or updates |
| Delete | `del d["age"]` | Removes key |
| Pop | `d.pop("age", None)` | Removes and returns value |
| Keys | `d.keys()` | Dict keys view |
| Values | `d.values()` | Dict values view |
| Items | `d.items()` | Key-value pairs |
| Contains | `"name" in d` | `True` |
| Length | `len(d)` | Number of key-value pairs |
| Update | `d.update({"age": 31})` | Merge another dict |
| Comprehension | `{k: v for k, v in items}` | |

## Sets

| Operation | Syntax | Result |
|------|----|----|
| Create | `s = {1, 2, 3}` | |
| Empty set | `s = set()` | NOT `{}` (that's a dict) |
| Add | `s.add(4)` | |
| Remove | `s.remove(2)` | KeyError if missing |
| Discard | `s.discard(2)` | No error if missing |
| Union | `s1 \| s2` or `s1.union(s2)` | All items from both |
| Intersection | `s1 & s2` | Items in both |
| Difference | `s1 - s2` | Items in s1 but not s2 |
| Contains | `2 in s` | `True` |

## Tuples

| Operation | Syntax | Notes |
|------|----|----|
| Create | `t = (1, 2, 3)` | Immutable (can't change) |
| Single item | `t = (1,)` | Comma required |
| Unpack | `a, b, c = t` | `a=1, b=2, c=3` |
| Access | `t[0]` | `1` |
| Contains | `2 in t` | `True` |

## Conditionals

```python
# if / elif / else
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

# Ternary (one-line if)
status = "pass" if score >= 60 else "fail"

# Multiple conditions
if age >= 18 and has_id:
    print("Allowed")

if day == "Saturday" or day == "Sunday":
    print("Weekend")

# Membership check
if name in ["Alice", "Bob", "Charlie"]:
    print("Known user")
```

## Loops

```python
# for loop with range
for i in range(5):           # 0, 1, 2, 3, 4
    print(i)

for i in range(2, 10, 2):   # 2, 4, 6, 8
    print(i)

# for loop with list
for item in my_list:
    print(item)

# for loop with index
for i, item in enumerate(my_list):
    print(f"{i}: {item}")

# for loop with dictionary
for key, value in my_dict.items():
    print(f"{key}: {value}")

# while loop
while count < 10:
    count += 1

# break and continue
for item in items:
    if item == "stop":
        break        # Exit the loop entirely
    if item == "skip":
        continue     # Skip to next iteration
    print(item)
```

## Functions

```python
# Basic function
def greet(name):
    return f"Hello, {name}!"

# Default parameters
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

# Multiple return values
def get_min_max(numbers):
    return min(numbers), max(numbers)

lo, hi = get_min_max([3, 1, 4, 1, 5])

# *args (variable positional arguments)
def total(*numbers):
    return sum(numbers)

total(1, 2, 3)  # 6

# **kwargs (variable keyword arguments)
def create_user(**kwargs):
    return kwargs

create_user(name="Alice", age=30)  # {"name": "Alice", "age": 30}

# Lambda (anonymous function)
square = lambda x: x ** 2
sorted_list = sorted(items, key=lambda x: x["name"])
```

## Classes

```python
class Dog:
    # Class variable (shared by all instances)
    species = "Canis familiaris"

    # Constructor
    def __init__(self, name, age):
        self.name = name      # Instance variable
        self.age = age

    # Method
    def bark(self):
        return f"{self.name} says Woof!"

    # String representation
    def __str__(self):
        return f"{self.name}, age {self.age}"

# Inheritance
class Puppy(Dog):
    def __init__(self, name, age, toy):
        super().__init__(name, age)
        self.toy = toy

    def play(self):
        return f"{self.name} plays with {self.toy}"

# Usage
dog = Dog("Rex", 5)
print(dog.bark())
print(dog)
```

## File I/O

```python
# Read entire file
with open("file.txt", "r") as f:
    content = f.read()

# Read lines
with open("file.txt", "r") as f:
    lines = f.readlines()      # List of lines

# Read line by line (memory efficient)
with open("file.txt", "r") as f:
    for line in f:
        print(line.strip())

# Write (overwrites)
with open("file.txt", "w") as f:
    f.write("Hello, World!\n")

# Append
with open("file.txt", "a") as f:
    f.write("Another line\n")

# JSON
import json
with open("data.json", "w") as f:
    json.dump(my_dict, f, indent=2)

with open("data.json", "r") as f:
    data = json.load(f)

# CSV
import csv
with open("data.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
```

## Error Handling

```python
# Basic try/except
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Multiple exceptions
try:
    value = int(input("Number: "))
    result = 10 / value
except ValueError:
    print("Not a valid number")
except ZeroDivisionError:
    print("Cannot divide by zero")

# Catch-all with details
try:
    risky_operation()
except Exception as e:
    print(f"Error: {e}")

# Finally (always runs)
try:
    f = open("file.txt")
    data = f.read()
except FileNotFoundError:
    print("File not found")
finally:
    f.close()

# Raise your own exceptions
if age < 0:
    raise ValueError("Age cannot be negative")
```

## Common Built-in Functions

| Function | Example | Result |
|-----|-----|----|
| `print()` | `print("hi", end="")` | Output to console |
| `input()` | `name = input("Name: ")` | Read from user |
| `len()` | `len([1, 2, 3])` | `3` |
| `range()` | `range(5)` | `0, 1, 2, 3, 4` |
| `type()` | `type(42)` | `<class 'int'>` |
| `int()` | `int("42")` | `42` |
| `str()` | `str(42)` | `"42"` |
| `float()` | `float("3.14")` | `3.14` |
| `bool()` | `bool(0)` | `False` |
| `list()` | `list(range(3))` | `[0, 1, 2]` |
| `dict()` | `dict(a=1, b=2)` | `{"a": 1, "b": 2}` |
| `sorted()` | `sorted([3, 1, 2])` | `[1, 2, 3]` |
| `reversed()` | `list(reversed([1, 2, 3]))` | `[3, 2, 1]` |
| `enumerate()` | `list(enumerate(["a", "b"]))` | `[(0, "a"), (1, "b")]` |
| `zip()` | `list(zip([1, 2], ["a", "b"]))` | `[(1, "a"), (2, "b")]` |
| `map()` | `list(map(str, [1, 2, 3]))` | `["1", "2", "3"]` |
| `filter()` | `list(filter(bool, [0, 1, "", "hi"]))` | `[1, "hi"]` |
| `sum()` | `sum([1, 2, 3])` | `6` |
| `min()` / `max()` | `min(3, 1, 4)` | `1` |
| `abs()` | `abs(-5)` | `5` |
| `round()` | `round(3.14159, 2)` | `3.14` |
| `isinstance()` | `isinstance(42, int)` | `True` |

## Common Imports

```python
import os                  # File/directory operations
import sys                 # System-specific parameters
import json                # JSON encoding/decoding
import csv                 # CSV file handling
import datetime            # Date and time
import random              # Random numbers
import math                # Mathematical functions
import re                  # Regular expressions
import collections         # Specialized containers
from pathlib import Path   # Modern file paths
```

---

# Appendix B: Top 20 Python Errors (and How to Fix Them)

Every Python developer - from complete beginner to seasoned professional - has seen these errors. The difference between a beginner and an expert isn't that experts don't get errors; it's that experts read the error message, nod, and fix it in thirty seconds. By the end of this appendix, you'll do the same.

---

## 1. SyntaxError: invalid syntax

**We've ALL seen this one.** It means Python can't even understand your code enough to run it.

```python
# This causes the error
if x == 5
    print("hello")
```

```
SyntaxError: invalid syntax
```

**What it means:** You have a typo or missing punctuation. Python's parser choked.

**Common causes:** Missing colon after `if`, `for`, `while`, `def`, or `class`. Mismatched parentheses. Using `=` instead of `==`.

**Fix:** Add the missing colon:
```python
if x == 5:
    print("hello")
```

---

## 2. IndentationError: unexpected indent

```python
x = 5
    y = 10  # This line is randomly indented
```

**What it means:** A line is indented when it shouldn't be, or indented to the wrong level.

**Fix:** Make sure indentation is consistent. Use 4 spaces per level (never mix tabs and spaces). Most editors have a "convert tabs to spaces" setting - turn it on.

---

## 3. NameError: name 'variable' is not defined

```python
print(message)  # 'message' was never created
```

**What it means:** You're trying to use a variable or function that doesn't exist yet.

**Common causes:** Typo in the variable name. Using a variable before assigning it. Forgetting to import a module.

**Fix:** Check spelling carefully. Make sure the variable is assigned before you use it. Variable names are case-sensitive (`Name` is not `name`).

---

## 4. TypeError: unsupported operand type(s)

```python
result = "age: " + 25
```

```
TypeError: can only concatenate str (not "int") to str
```

**What it means:** You're trying to combine two types that don't work together.

**Fix:** Convert to the same type:
```python
result = "age: " + str(25)
# Or better, use an f-string:
result = f"age: {25}"
```

---

## 5. TypeError: function() takes X positional arguments but Y were given

```python
def greet(name):
    print(f"Hello, {name}")

greet("Alice", "Bob")  # Too many arguments
```

**What it means:** You called a function with the wrong number of arguments.

**Fix:** Check the function definition and match the number of arguments. If you forgot `self` in a class method, that's often the culprit.

---

## 6. IndexError: list index out of range

```python
fruits = ["apple", "banana", "cherry"]
print(fruits[3])  # Only indices 0, 1, 2 exist
```

**What it means:** You're trying to access a list position that doesn't exist.

**Fix:** Remember that list indices start at 0. A list with 3 items has indices 0, 1, and 2. Use `len(fruits) - 1` for the last index, or just `fruits[-1]`.

---

## 7. KeyError: 'key'

```python
user = {"name": "Alice", "age": 30}
print(user["email"])  # 'email' doesn't exist
```

**What it means:** You're trying to access a dictionary key that doesn't exist.

**Fix:** Use `.get()` for safe access:
```python
email = user.get("email", "not provided")
```
Or check first: `if "email" in user:`

---

## 8. ValueError: invalid literal for int()

```python
number = int("hello")
```

**What it means:** You tried to convert a string to a number, but the string isn't a valid number.

**Fix:** Validate input before converting, or use try/except:
```python
try:
    number = int(user_input)
except ValueError:
    print("Please enter a valid number.")
```

---

## 9. AttributeError: 'type' object has no attribute 'method'

```python
name = "Alice"
name.push("!")  # Strings don't have a 'push' method
```

**What it means:** You're calling a method that doesn't exist on that type.

**Fix:** Check the documentation for available methods. For strings, it's `name + "!"` or `name.replace(...)`. For lists, `append()` not `push()`.

---

## 10. FileNotFoundError: No such file or directory

```python
with open("data.txt") as f:
    content = f.read()
```

**What it means:** The file you're trying to open doesn't exist at that path.

**Fix:** Check the file path. Use `os.path.exists("data.txt")` to verify. Remember that the path is relative to where you RUN the script, not where the script file lives.

---

## 11. ModuleNotFoundError: No module named 'module'

```python
import pandas  # Not installed
```

**What it means:** The module isn't installed or doesn't exist.

**Fix:** Install it with pip:
```bash
pip install pandas
```
If it IS installed, check you're using the right Python environment (virtual environments are a common gotcha).

---

## 12. ZeroDivisionError: division by zero

```python
average = total / count  # count is 0
```

**What it means:** Exactly what it says - you divided by zero.

**Fix:** Check for zero before dividing:
```python
average = total / count if count != 0 else 0
```

---

## 13. TypeError: 'NoneType' object is not subscriptable

```python
result = some_function()
print(result[0])  # some_function() returned None
```

**What it means:** You're trying to index or slice something that is `None`.

**Common cause:** A function that doesn't explicitly return a value returns `None` by default. Methods like `list.sort()` and `list.append()` return `None` (they modify the list in place).

**Fix:**
```python
# Wrong: sort() returns None
sorted_list = my_list.sort()

# Right: sort in place, then use the list
my_list.sort()
sorted_list = my_list

# Or: use sorted() which returns a new list
sorted_list = sorted(my_list)
```

---

## 14. RecursionError: maximum recursion depth exceeded

```python
def countdown(n):
    print(n)
    countdown(n - 1)  # No base case!

countdown(10)
```

**What it means:** A function calls itself forever without stopping.

**Fix:** Add a base case:
```python
def countdown(n):
    if n <= 0:     # Base case
        return
    print(n)
    countdown(n - 1)
```

---

## 15. TypeError: 'int' object is not iterable

```python
for digit in 12345:
    print(digit)
```

**What it means:** You're trying to loop over something that isn't a sequence (like a number).

**Fix:** Convert to an iterable:
```python
for digit in str(12345):
    print(digit)

# Or use range for counting:
for i in range(5):
    print(i)
```

---

## 16. UnboundLocalError: local variable referenced before assignment

```python
count = 10

def increment():
    count = count + 1  # Python sees 'count =' and treats it as local
    return count
```

**What it means:** Inside a function, Python sees an assignment to `count` and treats it as a local variable, but you're trying to read it before the assignment happens.

**Fix:** Use the `global` keyword (sparingly) or pass the value as a parameter:
```python
def increment(count):
    return count + 1

count = increment(count)
```

---

## 17. StopIteration

```python
my_iter = iter([1, 2, 3])
next(my_iter)  # 1
next(my_iter)  # 2
next(my_iter)  # 3
next(my_iter)  # StopIteration!
```

**What it means:** You called `next()` on an iterator that has no more items.

**Fix:** Use a for loop instead (it handles StopIteration automatically), or provide a default:
```python
value = next(my_iter, None)  # Returns None instead of raising error
```

---

## 18. ImportError: cannot import name 'X' from 'Y'

```python
from math import squareroot  # Wrong name
```

**What it means:** The name you're trying to import doesn't exist in that module.

**Fix:** Check the correct name. For math, it's `sqrt`, not `squareroot`:
```python
from math import sqrt
```

---

## 19. PermissionError: Permission denied

```python
with open("/etc/passwd", "w") as f:  # Can't write to system files
    f.write("oops")
```

**What it means:** You don't have permission to read or write that file.

**Fix:** Check file permissions. On Windows, make sure the file isn't open in another program. Write to locations you own (your home directory, your project folder).

---

## 20. JSONDecodeError: Expecting value

```python
import json
data = json.loads("")  # Empty string isn't valid JSON
```

**What it means:** You tried to parse something as JSON, but it's not valid JSON.

**Common causes:** Empty string, HTML instead of JSON (API returned an error page), file path instead of file contents.

**Fix:** Validate before parsing:
```python
import json

text = response.read()
if text:
    try:
        data = json.loads(text)
    except json.JSONDecodeError as e:
        print(f"Invalid JSON: {e}")
        print(f"Received: {text[:100]}")
```

---

## How to Read Any Error Message

Every Python error message follows this pattern:

```
Traceback (most recent call last):
  File "script.py", line 15, in main
    result = process(data)
  File "script.py", line 8, in process
    return data[key]
KeyError: 'missing_key'
```

Read it from **bottom to top**:
1. **Last line** = the actual error (KeyError: 'missing_key')
2. **Line above** = the exact code that failed (`return data[key]`)
3. **File and line number** = where to look (`script.py, line 8`)
4. **The chain** = how you got there (main called process)

The error message is your friend. Read it carefully, and it will tell you exactly what went wrong and where.

---

# Appendix C: What Next? Career Paths After This Book

You've finished the book. You can write Python. But "I know Python" isn't a job title - so where do you go from here?

This appendix maps out five career paths you can pursue with Python as your foundation. Each path includes what to learn next, in what order, and what job titles to search for when you're ready.

Pick the one that excites you most. You don't have to choose forever - many developers switch paths or combine them. But having a direction beats wandering.

---

## Path 1: Web Development

**The path:** Build websites and web applications that people use in their browsers.

Python is one of the most popular languages for backend web development. You'll build the servers, APIs, and databases that power everything from small business sites to platforms serving millions of users.

### What to Learn Next (in order)

1. **Django or Flask (deeper)** - You touched Flask in this book. Django is the "batteries-included" framework used by Instagram, Spotify, and Mozilla. Learn one deeply before the other.
2. **HTML, CSS, JavaScript basics** - You don't need to become a frontend expert, but you need to understand what the browser does with what your server sends.
3. **SQL and PostgreSQL** - Move beyond SQLite to a production database. Learn JOINs, indexes, and query optimization.
4. **REST API design** - Learn to design clean, consistent APIs. Study authentication patterns (OAuth, JWT).
5. **Deployment** - Learn to deploy with Docker, Heroku, or AWS. Understand Linux servers, NGINX, and HTTPS.
6. **Frontend framework (optional)** - React or Vue.js to become full-stack.

### Recommended Resources

- Django official tutorial (djangoproject.com) - free, thorough, and well-written
- "Django for Beginners" by William S. Vincent
- MDN Web Docs for HTML/CSS/JS fundamentals

### Job Titles to Search For

- Junior Python Developer
- Backend Developer (Python)
- Django Developer
- Full-Stack Python Developer
- API Developer

### Typical Salary Range (US, entry-level)

$60,000 - $90,000, scaling to $120,000+ with experience.

---

## Path 2: Data Science

**The path:** Turn data into insights, reports, and business decisions.

Data scientists are the detectives of the tech world. You'll clean messy datasets, find patterns, build visualizations, and tell stories with numbers. Python is THE dominant language in data science.

### What to Learn Next (in order)

1. **pandas (deep dive)** - You've seen the basics. Now learn groupby, merge, pivot tables, and time series handling. This is your most-used tool.
2. **Data visualization** - Matplotlib, Seaborn, and Plotly. Learn to make charts that communicate clearly.
3. **SQL** - Most real-world data lives in databases. Learn to query, join, and aggregate.
4. **Statistics fundamentals** - Mean, median, standard deviation, distributions, hypothesis testing, correlation. You don't need a math degree, but you need the basics.
5. **Jupyter Notebooks** - The standard environment for data exploration. Interactive, visual, shareable.
6. **Machine learning basics** - scikit-learn for classification, regression, and clustering. Understand when to use what.
7. **A specialization** - Natural language processing (NLP), computer vision, time series forecasting, or recommendation systems.

### Recommended Resources

- "Python for Data Analysis" by Wes McKinney (the creator of pandas)
- Kaggle.com - free datasets and competitions to practice on
- Khan Academy for statistics fundamentals (free)

### Job Titles to Search For

- Junior Data Analyst
- Data Analyst (Python)
- Junior Data Scientist
- Business Intelligence Analyst
- Analytics Engineer

### Typical Salary Range (US, entry-level)

$65,000 - $95,000, scaling to $130,000+ for senior data scientists.

---

## Path 3: AI/ML Engineering

**The path:** Build intelligent systems that learn from data.

This is the cutting edge. AI/ML engineers build the models and systems behind recommendation engines, self-driving cars, chatbots, image recognition, and everything in between. This book gave you the foundation - now you go deep.

### What to Learn Next (in order)

1. **Mathematics** - Linear algebra (vectors, matrices), calculus (derivatives, gradients), and probability. Khan Academy and 3Blue1Brown make these accessible.
2. **scikit-learn (mastery)** - Classification, regression, clustering, cross-validation, hyperparameter tuning, pipelines.
3. **Deep learning** - Neural networks, CNNs (for images), RNNs and Transformers (for text). Start with PyTorch or TensorFlow.
4. **Natural Language Processing** - Tokenization, embeddings, transformer models, fine-tuning. Hugging Face is the go-to library.
5. **MLOps** - Model versioning (MLflow), deployment (Docker, FastAPI), monitoring, and CI/CD for ML pipelines.
6. **Large Language Models** - Prompt engineering, fine-tuning, RAG architectures, LangChain, vector databases.

### Recommended Resources

- Fast.ai course (free, practical, top-down approach)
- "Hands-On Machine Learning" by Aurelien Geron
- Andrew Ng's Machine Learning course on Coursera
- Hugging Face documentation and tutorials

### Job Titles to Search For

- Junior ML Engineer
- AI Engineer
- Machine Learning Developer
- NLP Engineer
- MLOps Engineer
- AI/ML Research Assistant

### Typical Salary Range (US, entry-level)

$80,000 - $120,000, scaling to $180,000+ for senior ML engineers at top companies.

---

## Path 4: DevOps & Automation

**The path:** Automate everything. Build the systems that build the systems.

DevOps engineers are the invisible heroes who keep software running smoothly. You'll write scripts that automate deployments, monitor systems, manage cloud infrastructure, and ensure teams can ship code reliably. Python is the scripting language of choice in this world.

### What to Learn Next (in order)

1. **Linux command line** - Become comfortable in a terminal. Learn bash scripting, file permissions, process management, and SSH.
2. **Git (advanced)** - Branching strategies, rebasing, cherry-picking, hooks. You'll manage complex workflows.
3. **Docker** - Containerize applications. Learn Dockerfiles, docker-compose, and container networking.
4. **CI/CD pipelines** - GitHub Actions, Jenkins, or GitLab CI. Automate testing and deployment.
5. **Cloud platforms** - AWS, Google Cloud, or Azure. Start with one. Learn compute (EC2/VMs), storage (S3), and networking basics.
6. **Infrastructure as Code** - Terraform or Ansible. Define your infrastructure in files, not click-ops.
7. **Monitoring** - Prometheus, Grafana, or cloud-native monitoring. Know when things break before users notice.

### Recommended Resources

- "The Linux Command Line" by William Shotts (free online)
- Docker official getting started guide
- AWS Free Tier (12 months of free access to core services)
- "The Phoenix Project" (novel about DevOps culture)

### Job Titles to Search For

- Junior DevOps Engineer
- Site Reliability Engineer (SRE)
- Platform Engineer
- Automation Engineer
- Cloud Engineer
- Build & Release Engineer

### Typical Salary Range (US, entry-level)

$70,000 - $100,000, scaling to $150,000+ for senior SREs.

---

## Path 5: Game Development

**The path:** Build games, from simple 2D to complex simulations.

Game development combines programming, art, math, and storytelling. Python is a great starting point with Pygame, and the skills transfer directly to industry-standard engines.

### What to Learn Next (in order)

1. **Pygame** - Build 2D games from scratch. Learn game loops, sprite management, collision detection, and audio.
2. **Game design fundamentals** - Game mechanics, level design, player psychology, balancing. Read "The Art of Game Design" by Jesse Schell.
3. **Object-oriented patterns** - State machines, entity-component systems, observer pattern. Games rely heavily on design patterns.
4. **Math for games** - Vectors, trigonometry, physics simulation (gravity, momentum, collision).
5. **A game engine** - Godot (uses GDScript, similar to Python) or Unity (uses C#, but your programming fundamentals transfer). Pick one and build several small games.
6. **3D basics (optional)** - If you want to go beyond 2D, learn 3D coordinate systems, cameras, lighting, and shaders.

### Recommended Resources

- Pygame official documentation and tutorials
- "Invent Your Own Computer Games with Python" by Al Sweigart (free online)
- Godot Engine documentation (free, open-source game engine)
- Game jams on itch.io (build a game in 48 hours - incredibly educational)

### Job Titles to Search For

- Junior Game Developer
- Gameplay Programmer
- Tools Programmer
- Technical Designer
- Indie Game Developer (freelance/self-published)

### Typical Salary Range (US, entry-level)

$50,000 - $80,000 at studios, scaling to $120,000+ for senior gameplay programmers. Indie developers have unlimited upside (and risk).

---

## The Universal Advice

Regardless of which path you choose:

1. **Build projects.** The projects in this book are a start. Keep building. Every project teaches you something a tutorial can't.

2. **Contribute to open source.** Find a project on GitHub that interests you, read the code, fix a bug, submit a pull request. It's the fastest way to learn professional practices.

3. **Network.** Join Python communities online. Attend local meetups. Follow developers on social media. Most jobs come through connections, not applications.

4. **Never stop learning.** Technology changes fast. The developers who thrive are the ones who stay curious and keep adding new tools to their belt.

You have the foundation. Now go build something amazing.

---

# Appendix D: Recommended Resources

A curated collection of the best places to keep learning after this book. Everything listed here has been vetted for quality, accessibility, and relevance to the skills you've built.

---

## YouTube Channels

**Corey Schafer**
The gold standard for Python tutorials on YouTube. Clear explanations, practical examples, and thorough coverage of everything from basics to advanced topics like decorators, generators, and virtual environments. His Flask and Django series are particularly excellent.

**Sentdex (Harrison Kinsley)**
Focuses on Python for machine learning, data analysis, and AI. His series on building neural networks from scratch is legendary. Great for when you're ready to go deeper into the ML path.

**Tech With Tim**
Beginner-friendly Python content with a focus on projects. Game development with Pygame, web development, and automation. His project-based tutorials help you build real things.

**ArjanCodes**
Software design and architecture in Python. Once you've learned the basics, Arjan teaches you how to write CLEAN Python - design patterns, SOLID principles, and professional code structure. This is what takes you from "knows Python" to "writes good Python."

**Fireship**
Not Python-specific, but outstanding for understanding technology concepts quickly. His "100 seconds of X" series gives you rapid overviews of frameworks, languages, and tools. Great for exploring different career paths.

**freeCodeCamp**
Long-form, comprehensive tutorials on every topic imaginable. Their Python courses are 4-12 hours each and cover topics from the absolute basics to data science and web development. All free.

**3Blue1Brown**
The best math visualizations on the internet. Essential viewing if you're heading toward data science or ML. His series on linear algebra and neural networks will make abstract concepts click.

---

## Websites

**Real Python (realpython.com)**
The best written Python tutorials on the web. Every article is thorough, well-edited, and packed with practical examples. Their learning paths organize content by topic and skill level. Some content is behind a paywall, but most is free.

**Python.org Official Documentation**
The official source of truth. It's more reference material than tutorial, but learning to read official docs is a critical professional skill. Start with the Tutorial section.

**W3Schools Python (w3schools.com/python)**
Simple, interactive examples for quick reference. Not as deep as Real Python, but great for looking up syntax quickly. Includes a "Try it Yourself" editor in every lesson.

**LeetCode (leetcode.com)**
Practice coding challenges organized by difficulty and topic. Start with "Easy" problems and work up. Many companies use LeetCode-style questions in interviews. The "Top Interview 150" collection is a great starting point.

**Kaggle (kaggle.com)**
Free datasets, competitions, and notebooks for data science practice. Their "Learn" section has short, interactive courses on pandas, SQL, ML, and more. The competitions (even beginner-level ones) are excellent for building your data science portfolio.

**Stack Overflow (stackoverflow.com)**
The world's largest programming Q&A site. Nearly every error message you'll encounter has already been asked and answered here. Learn to search effectively: include the error message, the language, and the library name.

**GitHub (github.com)**
Not just for hosting your code - it's the world's largest library of open-source projects. Read other people's code. Study how popular Python projects are structured. Star repos you find useful.

---

## Online Courses

**CS50's Introduction to Computer Science (Harvard, free on edX)**
The best introductory computer science course in the world. It starts with C, moves to Python, and covers algorithms, data structures, and web programming. The production quality is unmatched, and it's completely free.

**100 Days of Code: Python (Udemy, Angela Yu)**
A comprehensive, project-based Python course that takes you from beginner to advanced over 100 days. Each day is a new project. It's paid, but Udemy frequently runs sales where courses drop to $10-15.

**Fast.ai Practical Deep Learning (free)**
If you're heading into AI/ML, this is the course. It takes a top-down, practical approach: you build working ML models on day one, then gradually understand the theory behind them. No math prerequisites. Free.

**MIT 6.0001 Introduction to CS with Python (MIT OpenCourseWare, free)**
MIT's actual introductory CS course, recorded and published for free. More academic than other options, but gives you a rigorous foundation in computational thinking.

**freeCodeCamp's Scientific Computing with Python (free)**
A structured, certification-track course covering Python from basics through data structures and algorithms. Earn a free certificate by completing all the projects.

---

## Communities

**r/learnpython (Reddit)**
The most welcoming programming community on Reddit. Ask any question, no matter how basic, and get helpful answers. Read the FAQ first, search before posting, and include your code when asking for help.

**r/Python (Reddit)**
More advanced than r/learnpython. News about the Python ecosystem, library announcements, and discussions about best practices. Great for staying current on what's happening in the Python world.

**Python Discord (pythondiscord.com)**
A large, active Discord server with channels organized by topic (help, career advice, project showcase). Real-time help from experienced developers. Includes regular coding challenges and events.

**Stack Overflow**
Listed under websites too, but it deserves mention as a community. Once you're experienced enough, answering other people's questions is one of the best ways to solidify your own knowledge.

**Dev.to (dev.to)**
A blogging platform for developers. Read articles, follow Python tags, and when you're ready, start writing your own posts. Writing about what you've learned is a powerful way to reinforce it - and it builds your professional presence.

---

## Books to Read Next

**"Automate the Boring Stuff with Python" by Al Sweigart**
Free online at automatetheboringstuff.com. Focuses on practical automation: working with spreadsheets, PDFs, emails, web scraping, and file management. Perfect for immediately applying Python to your daily life.

**"Fluent Python" by Luciano Ramalho**
The book that takes you from "knows Python" to "thinks in Python." Covers the language's most powerful features in depth: data models, iterators, generators, concurrency, and metaprogramming. Read this when you're comfortable with the basics and want to level up.

**"Clean Code" by Robert C. Martin**
Not Python-specific, but essential reading for any developer. Teaches you how to write code that humans can read and maintain. The principles apply to every language.

**"Designing Data-Intensive Applications" by Martin Kleppmann**
For when you're building systems that handle real data at scale. Covers databases, distributed systems, and data processing. More advanced, but incredibly valuable for backend and data engineering roles.

**"Python Tricks" by Dan Bader**
A collection of Python patterns, tips, and best practices organized as short, digestible chapters. Great for filling in gaps and discovering features you didn't know existed.

---

## Podcasts

**Talk Python to Me**
The premier Python podcast. Interviews with Python library creators, core developers, and community members. Each episode focuses on a specific topic or project. Hosted by Michael Kennedy, who has a gift for making technical conversations accessible.

**Python Bytes**
A weekly, bite-sized podcast (20-30 minutes) covering the latest Python news, tools, and libraries. Co-hosted by Michael Kennedy and Brian Okken. Great for staying current without a huge time commitment.

**Real Python Podcast**
Companion to the Real Python website. Deep dives into Python topics with interviews and tutorials. Well-produced and consistently valuable.

**Lex Fridman Podcast**
Not Python-specific, but features some of the most fascinating conversations in technology, AI, and computer science. Interviews with researchers, engineers, and thinkers at the frontier. Long-form (2-4 hours), but deeply engaging.

---

## Final Note

You don't need all of these. Pick one resource from each category that resonates with you and dive in. You can always come back to this list when you're ready for more.

The most important resource is the one you actually use. Consistency beats variety every time.

---

# About the Author

[Author Name] is a software developer, educator, and firm believer that programming should be fun, accessible, and free of unnecessary jargon.

After spending years watching talented people bounce off dry textbooks and confusing tutorials, they decided to write the book they wished they'd had when starting out - one that treats readers like intelligent adults, explains things in plain language, and builds toward real projects instead of endless toy examples.

They've worked across the software industry, from scrappy startups to established companies, and have taught Python to beginners in classrooms, workshops, and late-night debugging sessions over coffee. The common thread in all of it: the moment when something clicks for someone who thought they "weren't a tech person." That moment never gets old.

Their philosophy is simple: you don't need a computer science degree to write great code. You need curiosity, persistence, and a guide who respects your time. This book aims to be that guide.

When not coding, they can be found hiking trails with a slightly overenthusiastic dog, experimenting with recipes that have too many ingredients, and collecting programming books they swear they'll finish someday.

*Python Crash Course: From Zero to AI* is their first book, but probably not their last.

---

**Connect:**
- GitHub: [github.com/author-handle]
- Twitter/X: [@author-handle]
- Website: [author-website.com]
- Email: hello@author-website.com

If this book helped you, leaving a review on Amazon means the world. It helps other learners find the book and tells the author that the late nights were worth it.

---

