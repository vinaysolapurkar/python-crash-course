# ============================================================
# Chapter 4: Strings — Words, Words, Words
# ============================================================
# Strings are everywhere. Usernames, passwords, tweets, error
# messages that make you question your life choices...
# Let's master them.
# ============================================================

# ----------------------------------------------------------
# STRING METHODS — Transforming Text Like a Boss
# ----------------------------------------------------------
print("=== STRING METHODS ===")

movie = "  The Lord of the Rings  "

# Case methods
print(f"UPPER:  '{'hello world'.upper()}'")           # HELLO WORLD
print(f"lower:  '{'STOP YELLING'.lower()}'")           # stop yelling
print(f"Title:  '{'the dark knight'.title()}'")         # The Dark Knight
print(f"Capital:  '{'hello there'.capitalize()}'")      # Hello there
print(f"sWAP:   '{'Hello'.swapcase()}'")                # hELLO

# Stripping whitespace (like trimming the hedges)
print(f"\nBefore strip: '{movie}'")
print(f"After strip:  '{movie.strip()}'")           # removes both sides
print(f"Left strip:   '{movie.lstrip()}'")          # removes left only
print(f"Right strip:  '{movie.rstrip()}'")          # removes right only

# Replace — find and swap
quote = "I am Groot. I am Groot."
print(f"\nOriginal: {quote}")
print(f"Replace:  {quote.replace('Groot', 'Batman')}")
# Only replace first occurrence:
print(f"First only: {quote.replace('Groot', 'Batman', 1)}")

# Split — break a string into a list
csv_data = "red,green,blue,yellow"
colors = csv_data.split(",")
print(f"\nSplit '{csv_data}' -> {colors}")

sentence = "May the Force be with you"
words = sentence.split()    # splits on whitespace by default
print(f"Split '{sentence}' -> {words}")

# Join — the opposite of split (putting Humpty Dumpty back together)
print(f"Join with ' | ': {' | '.join(colors)}")
print(f"Join with '-':   {'-'.join(words)}")

# Count and Find
lyric = "na na na na na na na na Batman!"
print(f"\nLyric: '{lyric}'")
print(f"Count 'na': {lyric.count('na')}")        # 8
print(f"Find 'Batman': index {lyric.find('Batman')}")   # 24
print(f"Find 'Superman': {lyric.find('Superman')}")     # -1 (not found)

# Startswith / Endswith
url = "https://www.python.org"
print(f"\n'{url}'")
print(f"Starts with 'https': {url.startswith('https')}")   # True
print(f"Ends with '.org':    {url.endswith('.org')}")       # True
print(f"Ends with '.com':    {url.endswith('.com')}")       # False

# ----------------------------------------------------------
# METHOD CHAINING — Combo Moves!
# ----------------------------------------------------------
print("\n=== METHOD CHAINING ===")

messy_input = "   hElLo, WoRLd!   "
clean = messy_input.strip().lower().replace("!", "").title()
print(f"Before: '{messy_input}'")
print(f"After:  '{clean}'")
# Each method returns a new string, so you can chain them like a boss.

# Practical: cleaning user input
raw_email = "  User@Example.COM  "
clean_email = raw_email.strip().lower()
print(f"\nRaw email:   '{raw_email}'")
print(f"Clean email: '{clean_email}'")

# ----------------------------------------------------------
# STRING SLICING — Surgical Precision
# ----------------------------------------------------------
print("\n=== STRING SLICING ===")

#          0123456789...
text = "Hello, World!"
# Positive indices:  H=0, e=1, l=2, l=3, o=4, ,=5, ' '=6, W=7...
# Negative indices: !=−1, d=−2, l=−3, r=−4, o=−5, W=−6...

print(f"text = '{text}'")
print(f"text[0]     = '{text[0]}'")         # H (first character)
print(f"text[-1]    = '{text[-1]}'")        # ! (last character)
print(f"text[0:5]   = '{text[0:5]}'")      # Hello (start:stop, stop is EXCLUDED)
print(f"text[7:]    = '{text[7:]}'")        # World! (from index 7 to the end)
print(f"text[:5]    = '{text[:5]}'")        # Hello (from start to index 5)
print(f"text[-6:]   = '{text[-6:]}'")       # orld! (last 6 characters)
print(f"text[::2]   = '{text[::2]}'")      # Hlo ol! (every 2nd character)
print(f"text[::-1]  = '{text[::-1]}'")      # !dlroW ,olleH (REVERSED!)

# The classic palindrome check
word = "racecar"
is_palindrome = word == word[::-1]
print(f"\nIs '{word}' a palindrome? {is_palindrome}")   # True

word2 = "python"
print(f"Is '{word2}' a palindrome? {word2 == word2[::-1]}")   # False

# ----------------------------------------------------------
# ESCAPE CHARACTERS — The Backslash Gang
# ----------------------------------------------------------
print("\n=== ESCAPE CHARACTERS ===")

print("Line 1\nLine 2")          # \n = newline
print("Column1\tColumn2")        # \t = tab
print("She said \"hello\"")      # \" = literal quote
print('It\'s a beautiful day')   # \' = literal apostrophe
print("Backslash: \\")           # \\ = literal backslash

# Multi-line strings with triple quotes (way cleaner)
haiku = """
    Code flows like water,
    Bugs appear, then disappear—
    Stack Overflow saves.
"""
print(haiku)

# ----------------------------------------------------------
# RAW STRINGS — When You Don't Want Escaping
# ----------------------------------------------------------
print("=== RAW STRINGS ===")

# Normal string: backslashes are escape characters
print("Normal: C:\\Users\\new_folder\\test")

# Raw string: backslashes are just backslashes
print(r"Raw:    C:\Users\new_folder\test")

# Super useful for file paths and regex patterns!

# ----------------------------------------------------------
# F-STRING FORMATTING — The Power Tools
# ----------------------------------------------------------
print("\n=== F-STRING FORMATTING ===")

# Padding and alignment
name = "Yoda"
print(f"Left:   '{name:<20}'")     # 'Yoda                '
print(f"Right:  '{name:>20}'")     # '                Yoda'
print(f"Center: '{name:^20}'")     # '        Yoda        '
print(f"Fill:   '{name:*^20}'")    # '********Yoda********'

# Number formatting
pi = 3.14159265
big = 1234567890
percent = 0.856

print(f"\n2 decimals:    {pi:.2f}")          # 3.14
print(f"6 decimals:    {pi:.6f}")            # 3.141593
print(f"Comma sep:     {big:,}")             # 1,234,567,890
print(f"Percentage:    {percent:.1%}")       # 85.6%
print(f"Padded int:    {42:05d}")            # 00042 (zero-padded, 5 wide)

# Combining alignment and formatting
print("\n--- Scoreboard ---")
players = [("Mario", 9850), ("Luigi", 7200), ("Peach", 12400)]
for player_name, score in players:
    print(f"  {player_name:<10} {score:>8,} pts")

# ----------------------------------------------------------
# USEFUL STRING CHECKS
# ----------------------------------------------------------
print("\n=== STRING CHECKS ===")

print(f"'hello'.isalpha()   = {'hello'.isalpha()}")     # True (only letters)
print(f"'123'.isdigit()     = {'123'.isdigit()}")       # True (only digits)
print(f"'hello1'.isalnum()  = {'hello1'.isalnum()}")    # True (letters or digits)
print(f"'  '.isspace()      = {'  '.isspace()}")        # True (only whitespace)
print(f"'Hello'.istitle()   = {'Hello'.istitle()}")     # True (title case)

# ----------------------------------------------------------
# QUICK RECAP
# ----------------------------------------------------------
print("\n=== CHAPTER 4 RECAP ===")
print("1. String methods: .upper(), .lower(), .strip(), .replace(), .split()")
print("2. .count(), .find(), .startswith(), .endswith() for searching")
print("3. Chain methods: text.strip().lower().replace(...)")
print("4. Slicing: text[start:stop:step], text[::-1] to reverse")
print("5. Escape chars: \\n \\t \\\" \\\\ — or use raw strings r'...'")
print("6. f-string formatting: alignment, decimals, commas, percentages")
print("\nStrings are immutable — methods return NEW strings, not modify old ones!")
