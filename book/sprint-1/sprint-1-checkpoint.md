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
