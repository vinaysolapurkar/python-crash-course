"""
Chapter 17: Magic Methods — Making Your Classes Pythonic ✨
============================================================

Magic methods (aka "dunder methods" because of __double_underscores__)
let your objects work with Python's built-in operations.

Want to use + on your objects? __add__
Want print() to show something nice? __str__
Want len() to work? __len__

They're called "magic" because Python calls them automatically
behind the scenes. You never call obj.__str__() directly —
you just call str(obj) or print(obj) and Python does the magic.

It's like being a puppeteer — you pull strings behind the curtain
and the audience sees a great show.
"""

# ============================================================
# 1. __str__ and __repr__ — How Your Object Introduces Itself
# ============================================================
print("=" * 50)
print("1. __str__ and __repr__")
print("=" * 50)


class Book:
    """A book class to demonstrate __str__ and __repr__."""

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        """
        Called by print() and str().
        This is for HUMANS — make it pretty and readable.
        Think: "How would I describe this to my grandma?"
        """
        return f"'{self.title}' by {self.author} ({self.pages} pages)"

    def __repr__(self):
        """
        Called in the REPL and by repr().
        This is for DEVELOPERS — make it unambiguous.
        Ideally, it should look like code to recreate the object.
        Think: "How would I recreate this object?"
        """
        return f"Book('{self.title}', '{self.author}', {self.pages})"


book = Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", 224)

# __str__ is used by print()
print(book)  # 'The Hitchhiker's Guide...' by Douglas Adams (224 pages)

# __repr__ is used in the REPL and for debugging
print(repr(book))  # Book('The Hitchhiker's Guide...', 'Douglas Adams', 224)

# Without __str__, print() would show something like:
# <__main__.Book object at 0x7f2a3c4d5e60>  ← Not helpful at all!


# ============================================================
# 2. __len__ and __getitem__ — Making Your Object a Collection
# ============================================================
print("\n" + "=" * 50)
print("2. __len__ and __getitem__")
print("=" * 50)


class Playlist:
    """A music playlist that acts like a Python collection."""

    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)
        print(f"Added '{song}' to {self.name}")

    def __len__(self):
        """Now len(playlist) works!"""
        return len(self.songs)

    def __getitem__(self, index):
        """
        Now playlist[0] works! And slicing too!
        This also makes the object ITERABLE (you can loop over it).
        """
        return self.songs[index]

    def __str__(self):
        song_list = "\n  ".join(f"{i+1}. {s}" for i, s in enumerate(self.songs))
        return f"🎵 {self.name} ({len(self)} songs):\n  {song_list}"


# Build a playlist
vibes = Playlist("Coding Vibes")
vibes.add_song("Bohemian Rhapsody - Queen")
vibes.add_song("Lose Yourself - Eminem")
vibes.add_song("Eye of the Tiger - Survivor")
vibes.add_song("Don't Stop Me Now - Queen")
vibes.add_song("Harder Better Faster Stronger - Daft Punk")

print(f"\nPlaylist length: {len(vibes)}")  # uses __len__
print(f"First song: {vibes[0]}")           # uses __getitem__
print(f"Last song: {vibes[-1]}")           # negative indexing works too!

# Slicing works because of __getitem__!
print(f"First 3: {vibes[:3]}")

# Looping works because of __getitem__!
print("\nPlaying all songs:")
for song in vibes:
    print(f"  🎶 Now playing: {song}")

print()
print(vibes)  # uses __str__


# ============================================================
# 3. __add__ — Teaching Your Objects to Use +
# ============================================================
print("\n" + "=" * 50)
print("3. __add__ — THE PLUS OPERATOR")
print("=" * 50)


class Vector:
    """A 2D vector. Math class meets Python class."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        """Defines what happens when you do: vector1 + vector2"""
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented  # let Python handle the error

    def __mul__(self, scalar):
        """Defines what happens when you do: vector * number"""
        if isinstance(scalar, (int, float)):
            return Vector(self.x * scalar, self.y * scalar)
        return NotImplemented

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"


v1 = Vector(3, 4)
v2 = Vector(1, 2)

v3 = v1 + v2  # calls v1.__add__(v2)
print(f"{v1} + {v2} = {v3}")

v4 = v1 * 3   # calls v1.__mul__(3)
print(f"{v1} * 3 = {v4}")


# ============================================================
# 4. __eq__ and __lt__ — Comparison Magic
# ============================================================
print("\n" + "=" * 50)
print("4. __eq__ and __lt__ — COMPARISON OPERATORS")
print("=" * 50)


class Student:
    """A student with a GPA, for comparison demos."""

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa

    def __eq__(self, other):
        """Defines ==. Two students are 'equal' if same GPA."""
        if isinstance(other, Student):
            return self.gpa == other.gpa
        return NotImplemented

    def __lt__(self, other):
        """
        Defines <. Lower GPA = 'less than'.
        Fun fact: if you define __lt__, Python can use it for sorting!
        """
        if isinstance(other, Student):
            return self.gpa < other.gpa
        return NotImplemented

    def __le__(self, other):
        """Defines <="""
        if isinstance(other, Student):
            return self.gpa <= other.gpa
        return NotImplemented

    def __str__(self):
        return f"{self.name} (GPA: {self.gpa})"

    def __repr__(self):
        return f"Student('{self.name}', {self.gpa})"


alice = Student("Alice", 3.9)
bob = Student("Bob", 3.5)
charlie = Student("Charlie", 3.9)

print(f"{alice} == {charlie}? {alice == charlie}")  # True (same GPA)
print(f"{alice} == {bob}?     {alice == bob}")      # False
print(f"{bob} < {alice}?      {bob < alice}")       # True

# Because we defined __lt__, sorting works!
students = [alice, bob, charlie, Student("Diana", 4.0), Student("Eve", 3.2)]
sorted_students = sorted(students)  # uses __lt__ to compare
print("\nStudents sorted by GPA:")
for s in sorted_students:
    print(f"  {s}")


# ============================================================
# 5. __enter__ and __exit__ — Context Managers
# ============================================================
print("\n" + "=" * 50)
print("5. CONTEXT MANAGERS (__enter__ / __exit__)")
print("=" * 50)


class Timer:
    """
    A context manager that times how long a block of code takes.

    Usage:
        with Timer("my operation"):
            # do something slow
            ...

    __enter__ runs at the start of 'with'
    __exit__ runs at the end of 'with' (even if there's an error!)
    """

    import time

    def __init__(self, label="Timer"):
        self.label = label
        self.start_time = None

    def __enter__(self):
        """Called when entering the 'with' block."""
        import time
        self.start_time = time.time()
        print(f"⏱️  [{self.label}] Started...")
        return self  # this is what gets assigned to the 'as' variable

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Called when leaving the 'with' block.
        exc_type, exc_val, exc_tb contain exception info if one occurred.
        Return True to suppress the exception, False to let it propagate.
        """
        import time
        elapsed = time.time() - self.start_time
        print(f"⏱️  [{self.label}] Finished in {elapsed:.4f} seconds")
        return False  # don't suppress exceptions


# Use our Timer context manager
import time

with Timer("counting"):
    total = sum(range(1_000_000))
    print(f"Sum of 0 to 999,999 = {total:,}")

print()

with Timer("sleeping"):
    time.sleep(0.5)
    print("Done sleeping!")


# Another practical example: a file-like resource manager
class DatabaseConnection:
    """Fake database connection to show context manager pattern."""

    def __init__(self, db_name):
        self.db_name = db_name
        self.connected = False

    def __enter__(self):
        self.connected = True
        print(f"📦 Connected to '{self.db_name}' database")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connected = False
        print(f"📦 Disconnected from '{self.db_name}' database")
        if exc_type:
            print(f"   (An error occurred: {exc_val})")
        return False

    def query(self, sql):
        if not self.connected:
            raise RuntimeError("Not connected!")
        print(f"   Executing: {sql}")
        return [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]


# The connection is automatically closed when the 'with' block ends
with DatabaseConnection("users_db") as db:
    results = db.query("SELECT * FROM users")
    print(f"   Got {len(results)} results")
# db.__exit__() is called here automatically — even if there's an error!


# ============================================================
# 6. All Magic Methods at a Glance
# ============================================================
print("\n" + "=" * 50)
print("MAGIC METHODS CHEAT SHEET")
print("=" * 50)
print("""
 Method          Triggered By        Example
 ──────────────────────────────────────────────────
 __init__        Creating object     obj = MyClass()
 __str__         print(obj), str()   print(book)
 __repr__        repr(), REPL        repr(book)
 __len__         len(obj)            len(playlist)
 __getitem__     obj[key]            playlist[0]
 __setitem__     obj[key] = val      playlist[0] = "new"
 __add__         obj + other         v1 + v2
 __sub__         obj - other         v1 - v2
 __mul__         obj * other         v1 * 3
 __eq__          obj == other        s1 == s2
 __lt__          obj < other         s1 < s2
 __le__          obj <= other        s1 <= s2
 __gt__          obj > other         s1 > s2
 __ge__          obj >= other        s1 >= s2
 __contains__    item in obj         "song" in playlist
 __bool__        bool(obj), if obj   if playlist:
 __enter__       with obj:           with Timer():
 __exit__        end of with block   (auto-called)
 __call__        obj()               timer()
 ──────────────────────────────────────────────────

Pro tip: You don't need ALL of these. Implement the ones
that make your class intuitive to use!
""")
