"""
Chapter 12: File Handling -- Teaching Python to Read and Write
==============================================================
So far, all our data disappears when the program ends.
That's like writing a novel on an Etch A Sketch.

File handling lets you SAVE data permanently and READ it back later.
This is how real apps work -- databases, configs, logs, save files.

Let's teach Python to be literate!
"""

import os
import csv
import json

# We'll create files in a 'demo_files' folder to keep things tidy
DEMO_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "demo_files")
os.makedirs(DEMO_DIR, exist_ok=True)

# =============================================================================
# 1. WRITING FILES -- The 'with' Statement
# =============================================================================
print("=== Writing Files ===")

# The 'with' statement automatically closes the file when done.
# This is the ONLY way you should open files. Seriously. No exceptions.
# (Well, except the kind Python throws when things go wrong.)

filepath = os.path.join(DEMO_DIR, "hello.txt")

# "w" mode = write (creates file or OVERWRITES existing!)
with open(filepath, "w") as f:
    f.write("Hello, File World!\n")
    f.write("This is line 2.\n")
    f.write("Python wrote this. How cool is that?\n")

print(f"Created: {filepath}")

# Write multiple lines at once with writelines()
filepath2 = os.path.join(DEMO_DIR, "heroes.txt")
heroes = ["Spider-Man\n", "Batman\n", "Wonder Woman\n", "Iron Man\n", "Thor\n"]

with open(filepath2, "w") as f:
    f.writelines(heroes)  # Note: doesn't add \n automatically!

print(f"Created: {filepath2}")

# =============================================================================
# 2. READING FILES
# =============================================================================
print("\n=== Reading Files ===")

# Method 1: read() -- reads the ENTIRE file as one big string
with open(filepath, "r") as f:
    content = f.read()
print(f"--- Full content ---\n{content}")

# Method 2: readline() -- reads ONE line at a time
with open(filepath, "r") as f:
    first_line = f.readline()  # Reads line 1
    second_line = f.readline()  # Reads line 2
print(f"First line: {first_line.strip()}")
print(f"Second line: {second_line.strip()}")

# Method 3: readlines() -- reads ALL lines into a LIST
with open(filepath, "r") as f:
    lines = f.readlines()
print(f"\nAll lines as list: {lines}")
print(f"Number of lines: {len(lines)}")

# Method 4: Loop line by line (BEST for large files -- memory efficient!)
print("\n--- Line by line ---")
with open(filepath2, "r") as f:
    for i, line in enumerate(f, 1):
        print(f"  Hero #{i}: {line.strip()}")

# =============================================================================
# 3. APPENDING TO FILES
# =============================================================================
print("\n=== Appending ===")

# "a" mode = append (adds to end, doesn't overwrite!)
with open(filepath2, "a") as f:
    f.write("Black Panther\n")
    f.write("Captain Marvel\n")

# Verify the append worked
with open(filepath2, "r") as f:
    print(f"Heroes after append ({sum(1 for _ in f)} lines):")

with open(filepath2, "r") as f:
    for line in f:
        print(f"  - {line.strip()}")

# =============================================================================
# 4. CSV FILES -- Spreadsheet Data
# =============================================================================
print("\n=== CSV Files (Comma Separated Values) ===")

# CSV is the universal language of spreadsheets and data.
# Python's csv module makes it easy.

csv_path = os.path.join(DEMO_DIR, "students.csv")

# Writing CSV with csv.writer
with open(csv_path, "w", newline="") as f:
    writer = csv.writer(f)
    # Write header row
    writer.writerow(["Name", "Subject", "Grade"])
    # Write data rows
    writer.writerow(["Hermione", "Potions", 99])
    writer.writerow(["Harry", "Defense", 100])
    writer.writerow(["Ron", "Charms", 72])
    writer.writerow(["Draco", "Potions", 88])

print(f"Created CSV: {csv_path}")

# Reading CSV with csv.reader
print("\n--- Reading CSV ---")
with open(csv_path, "r") as f:
    reader = csv.reader(f)
    header = next(reader)  # Skip/read the header row
    print(f"  Columns: {header}")
    for row in reader:
        name, subject, grade = row
        print(f"  {name}: {grade} in {subject}")

# Reading CSV with csv.DictReader -- each row becomes a dictionary!
print("\n--- DictReader (rows as dicts -- super useful!) ---")
with open(csv_path, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        # row is a dict: {"Name": "Hermione", "Subject": "Potions", "Grade": "99"}
        print(f"  {row['Name']} got {row['Grade']} in {row['Subject']}")

# Writing CSV with csv.DictWriter
csv_path2 = os.path.join(DEMO_DIR, "scores.csv")
scores = [
    {"player": "Mario", "level": 10, "coins": 245},
    {"player": "Luigi", "level": 8, "coins": 180},
    {"player": "Peach", "level": 12, "coins": 310},
]

with open(csv_path2, "w", newline="") as f:
    fieldnames = ["player", "level", "coins"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()       # Write the header row
    writer.writerows(scores)   # Write all data rows at once!

print(f"\nCreated: {csv_path2}")

# =============================================================================
# 5. JSON FILES -- Structured Data
# =============================================================================
print("\n=== JSON Files ===")

json_path = os.path.join(DEMO_DIR, "game_save.json")

# Save data to JSON file with json.dump()
game_state = {
    "player": "Link",
    "health": 80,
    "inventory": ["Master Sword", "Hylian Shield", "Bow"],
    "location": {"x": 142, "y": 58, "zone": "Hyrule Field"},
    "quest_complete": False,
    "playtime_hours": 47.5
}

with open(json_path, "w") as f:
    json.dump(game_state, f, indent=2)  # indent=2 makes it pretty!

print(f"Saved game state to: {json_path}")

# Load data from JSON file with json.load()
with open(json_path, "r") as f:
    loaded_state = json.load(f)

print(f"\nLoaded game state:")
print(f"  Player: {loaded_state['player']}")
print(f"  Health: {loaded_state['health']}")
print(f"  Inventory: {loaded_state['inventory']}")
print(f"  Location: {loaded_state['location']['zone']}")
print(f"  Playtime: {loaded_state['playtime_hours']} hours")

# Quick reminder:
# json.dump() / json.load()   -> work with FILES
# json.dumps() / json.loads() -> work with STRINGS
# The 's' stands for 'string'. Easy to remember!

# =============================================================================
# 6. CHECKING IF FILES EXIST
# =============================================================================
print("\n=== Checking File Existence ===")

# Always check before reading -- avoid crashes!
files_to_check = [
    json_path,
    csv_path,
    os.path.join(DEMO_DIR, "definitely_not_real.txt"),
]

for fpath in files_to_check:
    filename = os.path.basename(fpath)
    if os.path.exists(fpath):
        size = os.path.getsize(fpath)
        print(f"  {filename}: EXISTS ({size} bytes)")
    else:
        print(f"  {filename}: DOES NOT EXIST")

# Check if something is a file vs directory
print(f"\n  Is demo_files a directory? {os.path.isdir(DEMO_DIR)}")
print(f"  Is hello.txt a file? {os.path.isfile(filepath)}")

# =============================================================================
# 7. FILE MODES REFERENCE
# =============================================================================
print("\n=== File Modes Reference ===")
print("""
  Mode  | Description
  ------+------------------------------------------
  "r"   | Read only (default). File must exist.
  "w"   | Write only. Creates file or OVERWRITES.
  "a"   | Append only. Creates file or adds to end.
  "r+"  | Read AND write. File must exist.
  "w+"  | Write AND read. Creates/overwrites.
  "a+"  | Append AND read. Creates or adds to end.
  "rb"  | Read binary (images, PDFs, etc.)
  "wb"  | Write binary

  PRO TIP: Always use 'with open()' to auto-close files.
  Forgetting to close files is like leaving the fridge open.
""")

# =============================================================================
# 8. CLEANUP -- Remove Demo Files (Comment Out to Keep Them)
# =============================================================================
print("=== Cleanup ===")

# Let's clean up our demo files so we don't leave a mess.
# Comment this section out if you want to inspect the files!

import shutil

if os.path.exists(DEMO_DIR):
    shutil.rmtree(DEMO_DIR)
    print(f"Cleaned up {DEMO_DIR} -- no trace left, like a ninja.")
else:
    print("Nothing to clean up!")

# =============================================================================
# RECAP
# =============================================================================
print("\n" + "=" * 50)
print("CHAPTER 12 RECAP -- File Handling")
print("=" * 50)
print("""
- ALWAYS use 'with open(path, mode) as f:' -- auto-closes!
- Writing: f.write(), f.writelines()
- Reading: f.read(), f.readline(), f.readlines(), or loop
- Appending: open with "a" mode
- CSV: csv.writer/reader for lists, DictWriter/DictReader for dicts
- JSON: json.dump/load for files, json.dumps/loads for strings
- os.path: exists(), isfile(), isdir(), getsize(), join()

Files are how your programs remember things between runs.
Master file I/O and your programs go from goldfish memory
to elephant memory. Save early, save often!
""")
