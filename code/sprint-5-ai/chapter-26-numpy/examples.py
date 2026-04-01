"""
Chapter 26: NumPy — The Backbone of Python Data Science
========================================================

You know how a regular Python list is like a Swiss Army knife?
It does everything okay, but nothing FAST. NumPy arrays are like
a laser-guided missile: they do math BLAZINGLY fast.

Why? Because under the hood, NumPy is written in C. Your Python
code sends the instructions, and C does the heavy lifting.
It's like having a Formula 1 engine in your Honda Civic.

Let's see what all the fuss is about!
"""

import numpy as np
import time

# ============================================================
# 1. WHY NUMPY? (Speed Comparison)
# ============================================================
# Let's race: Python list vs NumPy array
# Think of it like a bicycle vs a jet engine

print("=" * 60)
print("SPEED TEST: Python List vs NumPy Array")
print("=" * 60)

size = 1_000_000  # One million numbers. No big deal for NumPy.

# --- Python list approach ---
python_list = list(range(size))
start = time.time()
python_result = [x * 2 for x in python_list]
python_time = time.time() - start
print(f"Python list: {python_time:.4f} seconds")

# --- NumPy approach ---
numpy_array = np.arange(size)
start = time.time()
numpy_result = numpy_array * 2  # Look ma, no loop!
numpy_time = time.time() - start
print(f"NumPy array: {numpy_time:.4f} seconds")

# How much faster?
if numpy_time > 0:
    print(f"NumPy was ~{python_time / numpy_time:.0f}x faster!")
print("(Your mileage may vary, but NumPy usually wins by 10-100x)\n")


# ============================================================
# 2. CREATING ARRAYS
# ============================================================
# There are more ways to create arrays than there are ways
# to order coffee at Starbucks. Here are the essential ones:

print("=" * 60)
print("CREATING ARRAYS")
print("=" * 60)

# From a regular Python list — the classic conversion
grades = np.array([85, 92, 78, 95, 88])
print(f"From list:    {grades}")

# 2D array — like a spreadsheet / table
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
print(f"2D array:\n{matrix}\n")

# zeros — when you need a blank canvas
blank = np.zeros(5)
print(f"zeros(5):     {blank}")

# ones — like zeros but... one-sier
all_ones = np.ones((2, 3))  # 2 rows, 3 columns
print(f"ones(2,3):\n{all_ones}\n")

# arange — like range() but returns an array (and works with floats!)
counting = np.arange(0, 10, 2)  # start, stop, step
print(f"arange(0,10,2): {counting}")

# linspace — "give me exactly N evenly spaced numbers between A and B"
# Super useful for plotting graphs later!
smooth = np.linspace(0, 1, 5)  # 5 numbers from 0 to 1
print(f"linspace(0,1,5): {smooth}")

# Random arrays — because sometimes you need chaos
random_arr = np.random.rand(3, 3)  # 3x3 of random floats [0, 1)
print(f"Random 3x3:\n{random_arr}\n")

random_ints = np.random.randint(1, 100, size=5)  # 5 random ints from 1-99
print(f"Random ints: {random_ints}\n")


# ============================================================
# 3. SHAPE AND DTYPE — Know Your Array
# ============================================================
# Shape tells you the dimensions, dtype tells you the data type.
# Think of shape as "how many rows and columns" and dtype as
# "what kind of stuff is stored here."

print("=" * 60)
print("SHAPE AND DTYPE")
print("=" * 60)

data = np.array([[1.5, 2.7, 3.1],
                 [4.0, 5.5, 6.2]])

print(f"Array:\n{data}")
print(f"Shape: {data.shape}")       # (2, 3) — 2 rows, 3 columns
print(f"Dtype: {data.dtype}")       # float64
print(f"Size:  {data.size}")        # 6 total elements
print(f"Ndim:  {data.ndim}")        # 2 dimensions
print()

# You can force a dtype
integers = np.array([1.7, 2.3, 3.9], dtype=int)  # Truncates decimals!
print(f"Forced int dtype: {integers}")  # [1, 2, 3] — no rounding, just chop!
print()


# ============================================================
# 4. INDEXING AND SLICING
# ============================================================
# Works like Python lists, but with superpowers for 2D+ arrays.
# Think of it like GPS coordinates: [row, column]

print("=" * 60)
print("INDEXING AND SLICING")
print("=" * 60)

arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90])
print(f"Array:     {arr}")
print(f"arr[0]:    {arr[0]}")       # 10 — first element
print(f"arr[-1]:   {arr[-1]}")      # 90 — last element
print(f"arr[2:5]:  {arr[2:5]}")     # [30, 40, 50] — slice
print(f"arr[::2]:  {arr[::2]}")     # [10, 30, 50, 70, 90] — every other
print()

# 2D indexing — this is where it gets cool
grid = np.array([[1,  2,  3,  4],
                 [5,  6,  7,  8],
                 [9, 10, 11, 12]])

print(f"Grid:\n{grid}")
print(f"grid[0, 0]:   {grid[0, 0]}")        # 1 — top-left corner
print(f"grid[2, 3]:   {grid[2, 3]}")        # 12 — bottom-right corner
print(f"grid[1, :]:   {grid[1, :]}")        # [5, 6, 7, 8] — entire row 1
print(f"grid[:, 2]:   {grid[:, 2]}")        # [3, 7, 11] — entire column 2
print(f"grid[0:2, 1:3]:\n{grid[0:2, 1:3]}") # Sub-matrix!
print()

# Boolean indexing — "give me everything that matches this condition"
# This is like asking the array: "who among you is greater than 6?"
print(f"Elements > 6: {grid[grid > 6]}")
print()


# ============================================================
# 5. ARITHMETIC OPERATIONS
# ============================================================
# Here's where NumPy really shines. Operations apply to EVERY
# element automatically. No loops needed!
# It's like having a whole army of calculators working at once.

print("=" * 60)
print("ARITHMETIC OPERATIONS")
print("=" * 60)

a = np.array([10, 20, 30, 40])
b = np.array([1, 2, 3, 4])

print(f"a = {a}")
print(f"b = {b}")
print(f"a + b = {a + b}")       # Element-wise addition
print(f"a - b = {a - b}")       # Element-wise subtraction
print(f"a * b = {a * b}")       # Element-wise multiplication (NOT matrix mult!)
print(f"a / b = {a / b}")       # Element-wise division
print(f"a ** 2 = {a ** 2}")     # Square every element
print(f"a % 3 = {a % 3}")       # Modulo every element
print()

# Comparison operations — returns boolean arrays
print(f"a > 20: {a > 20}")       # [False, False,  True,  True]
print(f"a == 30: {a == 30}")     # [False, False,  True, False]
print()


# ============================================================
# 6. BROADCASTING
# ============================================================
# Broadcasting is NumPy's secret sauce. It lets you do math between
# arrays of DIFFERENT shapes. Think of it like this:
#
# If you have a classroom of 30 students and you say "everyone add 10
# to your score," you don't need 30 copies of the number 10.
# NumPy "broadcasts" the 10 across all elements.

print("=" * 60)
print("BROADCASTING")
print("=" * 60)

scores = np.array([72, 85, 91, 68, 77])

# Scalar broadcasting — one number applies to all
curved_scores = scores + 5  # Add 5 to everyone's score
print(f"Original scores: {scores}")
print(f"After +5 curve:  {curved_scores}")
print()

# Broadcasting with different shapes
# A 3x3 matrix + a 1x3 array
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
row_add = np.array([10, 20, 30])

result = matrix + row_add  # row_add gets "stretched" to match matrix
print(f"Matrix:\n{matrix}")
print(f"Row to add: {row_add}")
print(f"After broadcasting add:\n{result}")
print()


# ============================================================
# 7. RESHAPE
# ============================================================
# Reshape lets you reorganize data without changing it.
# Like rearranging furniture — same stuff, different layout.

print("=" * 60)
print("RESHAPE")
print("=" * 60)

original = np.arange(1, 13)  # [1, 2, 3, ..., 12]
print(f"Original (flat): {original}")

# Reshape to 3 rows x 4 columns
reshaped_3x4 = original.reshape(3, 4)
print(f"Reshaped to 3x4:\n{reshaped_3x4}\n")

# Reshape to 4 rows x 3 columns
reshaped_4x3 = original.reshape(4, 3)
print(f"Reshaped to 4x3:\n{reshaped_4x3}\n")

# Use -1 to let NumPy figure out one dimension
# "I want 2 rows, you figure out the columns"
auto_shape = original.reshape(2, -1)
print(f"Reshaped to 2x?: \n{auto_shape}\n")

# Flatten — back to 1D
flat_again = reshaped_3x4.flatten()
print(f"Flattened: {flat_again}")
print()


# ============================================================
# 8. COMMON FUNCTIONS — Your Statistical Toolbox
# ============================================================
# These are the bread and butter of data analysis.
# If arrays are the ingredients, these functions are the recipes.

print("=" * 60)
print("COMMON FUNCTIONS")
print("=" * 60)

test_scores = np.array([85, 92, 78, 95, 88, 72, 91, 83, 97, 76])
print(f"Test scores: {test_scores}")
print(f"  Mean (average): {np.mean(test_scores):.1f}")
print(f"  Standard dev:   {np.std(test_scores):.1f}")
print(f"  Max score:      {np.max(test_scores)}")
print(f"  Min score:      {np.min(test_scores)}")
print(f"  Sum:            {np.sum(test_scores)}")
print(f"  Median:         {np.median(test_scores)}")
print()

# argmax / argmin — WHERE is the max/min?
print(f"  Index of max:   {np.argmax(test_scores)} (score: {test_scores[np.argmax(test_scores)]})")
print(f"  Index of min:   {np.argmin(test_scores)} (score: {test_scores[np.argmin(test_scores)]})")
print()

# Axis operations — per-row or per-column stats
# This is super useful for real data analysis!
student_scores = np.array([
    [85, 90, 78],  # Student 0: Math, Science, English
    [92, 88, 95],  # Student 1
    [76, 82, 89],  # Student 2
])
print(f"Student scores (rows=students, cols=subjects):")
print(f"{student_scores}")
print(f"  Mean per student (axis=1): {np.mean(student_scores, axis=1)}")
print(f"  Mean per subject (axis=0): {np.mean(student_scores, axis=0)}")
print()

# Sorting
unsorted = np.array([42, 17, 83, 5, 61])
print(f"Unsorted: {unsorted}")
print(f"Sorted:   {np.sort(unsorted)}")
print()

# Unique values
data = np.array([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
unique, counts = np.unique(data, return_counts=True)
print(f"Data:    {data}")
print(f"Unique:  {unique}")
print(f"Counts:  {counts}")
print()


# ============================================================
# RECAP
# ============================================================
print("=" * 60)
print("CHAPTER 26 RECAP")
print("=" * 60)
print("""
NumPy is your gateway to data science in Python:

1. Creating arrays: np.array(), zeros(), ones(), arange(), linspace()
2. Shape & dtype: Know your data's dimensions and type
3. Indexing: [row, col], slicing, boolean indexing
4. Arithmetic: +, -, *, / work element-wise (no loops!)
5. Broadcasting: Math between different-shaped arrays
6. Reshape: Reorganize without changing data
7. Functions: mean, std, max, min, sum, argmax, and more

Next up: Pandas — where we put LABELS on our data!
""")
