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
