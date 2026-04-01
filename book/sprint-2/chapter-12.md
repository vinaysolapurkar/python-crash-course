# Chapter 12: File Handling: Reading & Writing Like a Pro

> **Sprint 2, Chapter 12** | **Estimated Time: 12-15 minutes** | **Difficulty: Intermediate**

So far, everything we've built disappears when the program stops. That's like writing a novel and forgetting to hit save. Your contact book? Gone. Your quiz scores? Poof. Your user data? Vanished into the void.

Let's fix that. This chapter is about making your data *survive*.

## Writing Files: The with Statement

The safest way to write to a file in Python is the `with` statement. It opens the file, lets you do your thing, and then automatically closes it when you're done -- even if something goes wrong.

```python
# Write to a file
with open("hello.txt", "w") as f:
    f.write("Hello, world!\n")
    f.write("This is my first file.\n")
    f.write("Python is awesome.\n")
```

Let's break that down:
- `open("hello.txt", "w")` -- opens (or creates) a file called `hello.txt` in **write** mode
- `as f` -- gives us a variable `f` to work with (short for "file")
- `f.write()` -- writes text to the file
- `\n` -- newline character (hit Enter)

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
|------|-------------|---------------|-------------|
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
# Method 2: csv.DictReader (gives you dictionaries -- way better)
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

You met `json` briefly in Chapter 11. Now let's use it with files. JSON is perfect for storing structured data -- dictionaries, lists, nested data. It's what every web API speaks.

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
- `json.dump()` / `json.load()` -- work with **files**
- `json.dumps()` / `json.loads()` -- work with **strings**

The 's' stands for 'string'. Dump to string, load from string.

## Practical Example: Settings Manager

Here's a real-world pattern -- loading and saving app settings:

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
        f.write(f"\n--- {timestamp} ---\n")
        f.write(f"{entry}\n")

    print("Entry saved!")

def read_entries():
    # Your code here -- read and display the diary file
    pass

# Main loop
while True:
    print("\n--- My Diary ---")
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

- **Always use `with open()`** -- it handles closing the file automatically.
- **Write mode (`"w"`)** creates or overwrites. **Append mode (`"a"`)** adds without destroying. **Read mode (`"r"`)** is the default.
- For large files, read **line by line** with a for loop instead of `.read()`.
- **CSV**: Use `csv.DictReader` and `csv.DictWriter` for readable, maintainable code.
- **JSON**: Use `json.dump()`/`json.load()` for files, `json.dumps()`/`json.loads()` for strings.
- `newline=""` in your `open()` call prevents double-spacing in CSV files on Windows.
- Your programs can finally remember things between runs. That's a superpower.
