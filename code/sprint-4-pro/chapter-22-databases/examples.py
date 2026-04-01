"""
Chapter 22: Databases with SQLite — Persistent Data Storage
=============================================================

So far, all our data disappears when the program ends.
Variables? Poof. Lists? Gone. Dicts? Vanished into the void.

Databases are like a save file for your data.
SQLite is Python's built-in database — no installation needed!
It stores everything in a single file. Simple. Clean. Powerful.

Think of a database as a super-powered spreadsheet:
  - Tables = Sheets (one per topic)
  - Columns = Fields (what info to store)
  - Rows = Records (individual entries)
  - SQL = The language to talk to the database
"""

import sqlite3
import os

# Clean up from any previous runs
DB_FILE = "chapter22_demo.db"
if os.path.exists(DB_FILE):
    os.remove(DB_FILE)

# ============================================================
# 1. Connecting to SQLite — Opening the Save File
# ============================================================
print("=" * 50)
print("1. CONNECTING TO SQLITE")
print("=" * 50)

# sqlite3.connect() creates the file if it doesn't exist
conn = sqlite3.connect(DB_FILE)

# A cursor is like your pen — it writes and reads from the database
cursor = conn.cursor()

print(f"Connected to '{DB_FILE}'!")
print("(If the file didn't exist, SQLite just created it. Magic!)")


# ============================================================
# 2. CREATE TABLE — Setting Up Your Spreadsheet
# ============================================================
print("\n" + "=" * 50)
print("2. CREATE TABLE")
print("=" * 50)

# SQL (Structured Query Language) is the language databases speak
cursor.execute("""
    CREATE TABLE IF NOT EXISTS movies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        director TEXT NOT NULL,
        year INTEGER,
        rating REAL,
        genre TEXT
    )
""")

# Commit saves changes to the database file
conn.commit()

print("""
Created 'movies' table with columns:
  id       → auto-incrementing ID (database handles this)
  title    → text, required (NOT NULL)
  director → text, required
  year     → integer (release year)
  rating   → real number (decimal, like 8.5)
  genre    → text

Data types in SQLite:
  TEXT     → strings
  INTEGER  → whole numbers
  REAL     → decimal numbers
  BLOB     → binary data (images, files)
  NULL     → nothing (the void)
""")


# ============================================================
# 3. INSERT — Adding Data
# ============================================================
print("=" * 50)
print("3. INSERT — ADDING DATA")
print("=" * 50)

# Method 1: Single insert
cursor.execute("""
    INSERT INTO movies (title, director, year, rating, genre)
    VALUES (?, ?, ?, ?, ?)
""", ("The Shawshank Redemption", "Frank Darabont", 1994, 9.3, "Drama"))

# IMPORTANT: Use ? placeholders, NEVER f-strings!
# f-strings in SQL = SQL injection vulnerability = hackers' dream

# Method 2: Insert many at once (much faster for bulk data!)
movies = [
    ("The Dark Knight", "Christopher Nolan", 2008, 9.0, "Action"),
    ("Pulp Fiction", "Quentin Tarantino", 1994, 8.9, "Crime"),
    ("Forrest Gump", "Robert Zemeckis", 1994, 8.8, "Drama"),
    ("The Matrix", "The Wachowskis", 1999, 8.7, "Sci-Fi"),
    ("Inception", "Christopher Nolan", 2010, 8.8, "Sci-Fi"),
    ("Interstellar", "Christopher Nolan", 2014, 8.7, "Sci-Fi"),
    ("The Godfather", "Francis Ford Coppola", 1972, 9.2, "Crime"),
    ("Fight Club", "David Fincher", 1999, 8.8, "Drama"),
    ("The Lord of the Rings: The Return of the King", "Peter Jackson", 2003, 9.0, "Fantasy"),
    ("Spirited Away", "Hayao Miyazaki", 2001, 8.6, "Animation"),
]

cursor.executemany("""
    INSERT INTO movies (title, director, year, rating, genre)
    VALUES (?, ?, ?, ?, ?)
""", movies)

conn.commit()
print(f"Inserted {len(movies) + 1} movies into the database!")


# ============================================================
# 4. SELECT — Reading Data
# ============================================================
print("\n" + "=" * 50)
print("4. SELECT — READING DATA")
print("=" * 50)

# fetchall() gets ALL matching rows
cursor.execute("SELECT * FROM movies")
all_movies = cursor.fetchall()
print(f"All movies ({len(all_movies)}):")
for movie in all_movies[:5]:  # show first 5
    print(f"  {movie}")
print(f"  ... and {len(all_movies) - 5} more\n")

# Select specific columns
cursor.execute("SELECT title, rating FROM movies ORDER BY rating DESC")
print("Top movies by rating:")
for title, rating in cursor.fetchall():
    print(f"  {rating:.1f} - {title}")

# fetchone() gets just ONE row
print()
cursor.execute("SELECT title, year FROM movies WHERE year = 1994")
print("Movies from 1994:")
while True:
    row = cursor.fetchone()
    if row is None:
        break
    print(f"  {row[0]} ({row[1]})")


# ============================================================
# 5. WHERE — Filtering Results
# ============================================================
print("\n" + "=" * 50)
print("5. WHERE — FILTERING")
print("=" * 50)

# Filter with WHERE clause
print("Sci-Fi movies:")
cursor.execute("SELECT title, year, rating FROM movies WHERE genre = ?", ("Sci-Fi",))
for title, year, rating in cursor.fetchall():
    print(f"  {title} ({year}) - {rating}")

print("\nMovies rated 9.0 or higher:")
cursor.execute("SELECT title, rating FROM movies WHERE rating >= ?", (9.0,))
for title, rating in cursor.fetchall():
    print(f"  {title} ({rating})")

print("\nChristopher Nolan movies:")
cursor.execute("""
    SELECT title, year, rating
    FROM movies
    WHERE director = ?
    ORDER BY year
""", ("Christopher Nolan",))
for title, year, rating in cursor.fetchall():
    print(f"  {title} ({year}) - {rating}")

# LIKE for pattern matching
print("\nMovies with 'The' in the title:")
cursor.execute("SELECT title FROM movies WHERE title LIKE ?", ("%The%",))
for (title,) in cursor.fetchall():
    print(f"  {title}")


# ============================================================
# 6. UPDATE — Changing Existing Data
# ============================================================
print("\n" + "=" * 50)
print("6. UPDATE")
print("=" * 50)

# Update a single record
cursor.execute("""
    UPDATE movies SET rating = ? WHERE title = ?
""", (9.5, "The Shawshank Redemption"))

conn.commit()

cursor.execute("SELECT title, rating FROM movies WHERE title = ?",
               ("The Shawshank Redemption",))
title, rating = cursor.fetchone()
print(f"Updated: {title} → rating {rating}")


# ============================================================
# 7. DELETE — Removing Data
# ============================================================
print("\n" + "=" * 50)
print("7. DELETE")
print("=" * 50)

# Count before
cursor.execute("SELECT COUNT(*) FROM movies")
count_before = cursor.fetchone()[0]

# Delete a specific movie
cursor.execute("DELETE FROM movies WHERE title = ?", ("Fight Club",))
conn.commit()

# Count after
cursor.execute("SELECT COUNT(*) FROM movies")
count_after = cursor.fetchone()[0]

print(f"Deleted 'Fight Club'. Movies: {count_before} → {count_after}")
print("(First rule of Fight Club: we just deleted Fight Club from the database)")


# ============================================================
# 8. Parameterized Queries — Stay Safe!
# ============================================================
print("\n" + "=" * 50)
print("8. PARAMETERIZED QUERIES — SECURITY!")
print("=" * 50)
print("""
NEVER do this:
  cursor.execute(f"SELECT * FROM users WHERE name = '{user_input}'")

WHY? SQL Injection! If user_input is:
  ' OR '1'='1' --
Then the query becomes:
  SELECT * FROM users WHERE name = '' OR '1'='1' --'
  ...which returns ALL users! A hacker's dream.

ALWAYS do this:
  cursor.execute("SELECT * FROM users WHERE name = ?", (user_input,))

The ? placeholder safely escapes the input. Hackers foiled!
""")


# ============================================================
# 9. Context Manager — The Right Way
# ============================================================
print("=" * 50)
print("9. CONTEXT MANAGER (BEST PRACTICE)")
print("=" * 50)

# Always use 'with' for database connections!
# It automatically handles commit/rollback and closing.

with sqlite3.connect(DB_FILE) as conn:
    # Row factory gives us dict-like access to columns by name!
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM movies WHERE genre = ?", ("Sci-Fi",))
    print("\nSci-Fi movies (using Row factory):")
    for row in cursor.fetchall():
        # Access columns by NAME instead of index — so much cleaner!
        print(f"  {row['title']} ({row['year']}) - Directed by {row['director']}")

    # Aggregation queries
    cursor.execute("""
        SELECT genre, COUNT(*) as count, AVG(rating) as avg_rating
        FROM movies
        GROUP BY genre
        ORDER BY avg_rating DESC
    """)
    print("\nGenre statistics:")
    print(f"  {'Genre':<12} {'Count':<8} {'Avg Rating':<10}")
    print(f"  {'-'*12} {'-'*8} {'-'*10}")
    for row in cursor.fetchall():
        print(f"  {row['genre']:<12} {row['count']:<8} {row['avg_rating']:.2f}")


# ============================================================
# Cleanup
# ============================================================
print(f"\nDatabase saved to: {os.path.abspath(DB_FILE)}")

# Clean up the demo database
if os.path.exists(DB_FILE):
    os.remove(DB_FILE)
    print(f"(Cleaned up {DB_FILE} for tidiness)")


# ============================================================
# Recap
# ============================================================
print("\n" + "=" * 50)
print("CHAPTER 22 RECAP")
print("=" * 50)
print("""
SQLite Cheat Sheet:
-----------------------------------------------------------------
CONNECT:     conn = sqlite3.connect("my_database.db")
CURSOR:      cursor = conn.cursor()
EXECUTE:     cursor.execute("SQL QUERY", (params,))
COMMIT:      conn.commit()   ← SAVE changes!
CLOSE:       conn.close()    ← or use 'with' statement

SQL BASICS:
  CREATE TABLE  → make a new table
  INSERT INTO   → add data
  SELECT        → read data
  UPDATE        → change data
  DELETE        → remove data
  WHERE         → filter results
  ORDER BY      → sort results
  GROUP BY      → aggregate results

SAFETY:
  Always use ? placeholders: cursor.execute("... WHERE x = ?", (val,))
  NEVER use f-strings in SQL queries!

BEST PRACTICE:
  with sqlite3.connect("db.db") as conn:
      cursor = conn.cursor()
      ...  # auto-commits on success, auto-rollback on error

ROW FACTORY:
  conn.row_factory = sqlite3.Row
  → Access columns by name: row['title'] instead of row[0]
-----------------------------------------------------------------
""")
