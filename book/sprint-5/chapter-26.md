# Chapter 26: NumPy: The Foundation of Everything AI

> **Sprint 5, Chapter 26** | **10 min read** | **Code: [github link](https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/sprint-5-ai/chapter-26-numpy/)**

If Python lists are a bicycle, NumPy arrays are a Tesla. Same job -- getting you from A to B. Wildly different speed. And once you drive the Tesla, you're never going back to pedaling.

## What You'll Learn
- Creating NumPy arrays (multiple ways)
- Shape and dtype -- understanding your data's structure
- Indexing and slicing (you already know most of this)
- Element-wise math operations (no loops!)
- Broadcasting -- NumPy's mind-reading trick
- Essential functions: mean, std, max, min, sum, reshape
- Why NumPy is dramatically faster than regular Python lists

## Why Should I Care?

Every single AI and machine learning library in Python -- TensorFlow, PyTorch, scikit-learn, pandas -- is built on top of NumPy. It's not optional. It's not a "nice to have." It's the foundation. Learning AI without NumPy is like learning to cook without knowing what a stove is.

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
print(scores.shape)  # (5,)     -- 1D array with 5 elements
print(scores.dtype)  # int64    -- 64-bit integers

grades = np.array([
    [85, 92, 78],
    [95, 88, 76],
    [90, 85, 92]
])
print(grades.shape)  # (3, 3)   -- 3 rows, 3 columns
print(grades.dtype)  # int64

# You can also check other properties
print(scores.ndim)   # 1  -- one dimension
print(grades.ndim)   # 2  -- two dimensions
print(grades.size)   # 9  -- total number of elements
```

Think of `shape` as the dimensions of a spreadsheet. `(3, 3)` means 3 rows and 3 columns. `(5,)` means just a single row of 5 items. When you start doing machine learning, you'll check `.shape` constantly. It's the first thing you look at when something goes wrong.

```python
# You can specify the data type
precise = np.array([1, 2, 3], dtype=np.float64)
print(precise)       # [1. 2. 3.]
print(precise.dtype)  # float64

small = np.array([1, 2, 3], dtype=np.int8)
print(small.dtype)    # int8 -- uses less memory
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
print(scores[::2])   # [85 78 88 91] -- every other element
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

Fancy indexing -- selecting specific elements by condition:

```python
scores = np.array([85, 92, 78, 95, 88, 76, 91])

# Boolean indexing -- this is incredibly powerful
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
# Regular Python -- requires a loop
scores_list = [85, 92, 78, 95, 88]
curved_list = []
for s in scores_list:
    curved_list.append(s + 5)

# NumPy -- one line
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

# Broadcasting: (3, 3) * (3,) -- NumPy applies weights to each row
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
print(np.mean(scores))    # 86.0    -- average
print(np.median(scores))  # 86.5    -- middle value
print(np.std(scores))     # 6.265   -- standard deviation
print(np.max(scores))     # 95      -- highest
print(np.min(scores))     # 76      -- lowest
print(np.sum(scores))     # 688     -- total

# Position finders
print(np.argmax(scores))  # 3  -- index of the highest score
print(np.argmin(scores))  # 5  -- index of the lowest score

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

> **Don't Panic:** NumPy looks like a lot of new stuff, but 80% of it works exactly like lists. Indexing? Same as lists. Slicing? Same as lists. The main difference is that math operations work on the entire array at once instead of needing loops. You already know this stuff -- NumPy just makes it faster.

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
- `import numpy as np` -- the universal convention
- Create arrays with `np.array()`, `np.zeros()`, `np.ones()`, `np.arange()`, `np.linspace()`
- `.shape` tells you dimensions, `.dtype` tells you data type
- Indexing and slicing work just like lists, plus `[row, col]` for 2D
- Boolean indexing: `arr[arr > 90]` gives you all elements matching the condition
- Math operations work element-wise -- no loops needed
- Broadcasting lets NumPy do math between arrays of different sizes
- Key functions: `np.mean()`, `np.std()`, `np.max()`, `np.min()`, `np.sum()`, `np.sort()`
- `.reshape()` changes the shape of your data
- NumPy is 50-100x faster than regular Python lists for numerical operations
- Every AI/ML library is built on NumPy -- this is the foundation of everything that follows
