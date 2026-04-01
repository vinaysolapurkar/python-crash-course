"""
Chapter 27: Pandas — Data Analysis with Superpowers
=====================================================

If NumPy is like a spreadsheet of numbers, Pandas is like Excel
on steroids. It gives you LABELS for your data — column names,
row names, and a ton of built-in analysis tools.

The name "Pandas" comes from "Panel Data" (an economics term),
NOT the cute bear. Sorry to disappoint.

The two main objects:
  - Series: A labeled 1D array (like a single column)
  - DataFrame: A labeled 2D table (like a spreadsheet)
"""

import pandas as pd
import numpy as np
from io import StringIO  # To create CSV data without actual files

# ============================================================
# 1. SERIES — A Labeled 1D Array
# ============================================================
# Think of a Series as a single column in a spreadsheet,
# where each cell has a label (index).

print("=" * 60)
print("SERIES")
print("=" * 60)

# Create from a list
temps = pd.Series([72, 68, 75, 81, 79],
                  index=["Mon", "Tue", "Wed", "Thu", "Fri"],
                  name="Temperature")
print(f"Temperature Series:\n{temps}\n")

# Access by label or position
print(f"Wednesday temp: {temps['Wed']}")
print(f"First temp:     {temps.iloc[0]}")  # iloc = integer location
print(f"Mean temp:      {temps.mean():.1f}")
print()

# Create from a dictionary — super common!
scores = pd.Series({"Alice": 95, "Bob": 82, "Charlie": 91, "Diana": 88})
print(f"Scores:\n{scores}\n")


# ============================================================
# 2. DATAFRAME — The Star of the Show
# ============================================================
# A DataFrame is basically a table. Each column is a Series.
# Think of it as a dictionary of lists that all have the same length.

print("=" * 60)
print("DATAFRAME CREATION")
print("=" * 60)

# Method 1: From a dictionary (most common)
data = {
    "name": ["Alice", "Bob", "Charlie", "Diana", "Eve"],
    "age": [25, 30, 35, 28, 22],
    "city": ["NYC", "LA", "NYC", "Chicago", "LA"],
    "salary": [70000, 85000, 92000, 65000, 55000]
}
df = pd.DataFrame(data)
print(f"DataFrame from dict:\n{df}\n")

# Method 2: From a list of dictionaries
people = [
    {"name": "Frank", "age": 40, "hobby": "chess"},
    {"name": "Grace", "age": 33, "hobby": "hiking"},
]
df2 = pd.DataFrame(people)
print(f"From list of dicts:\n{df2}\n")


# ============================================================
# 3. READING CSV DATA
# ============================================================
# In real life, you'd use pd.read_csv("filename.csv")
# Here we'll use StringIO to simulate a CSV file in memory.

print("=" * 60)
print("READING CSV DATA")
print("=" * 60)

csv_data = """name,department,salary,years
Alice,Engineering,95000,5
Bob,Marketing,72000,3
Charlie,Engineering,105000,8
Diana,HR,68000,2
Eve,Marketing,78000,4
Frank,Engineering,88000,6
Grace,HR,72000,3
"""

# StringIO makes a string act like a file — super handy for demos!
df = pd.read_csv(StringIO(csv_data))
print(f"Employee data:\n{df}\n")

# Quick overview of the data
print(f"Shape: {df.shape}")          # (rows, columns)
print(f"Columns: {list(df.columns)}")
print(f"Data types:\n{df.dtypes}\n")

# First/last few rows
print(f"First 3 rows:\n{df.head(3)}\n")
print(f"Last 2 rows:\n{df.tail(2)}\n")


# ============================================================
# 4. SELECTING COLUMNS AND ROWS
# ============================================================
# Think of [] as "give me this column" and .loc/.iloc as
# "give me this row."

print("=" * 60)
print("SELECTING DATA")
print("=" * 60)

# Select a single column (returns a Series)
names = df["name"]
print(f"Names column:\n{names}\n")

# Select multiple columns (returns a DataFrame)
subset = df[["name", "salary"]]
print(f"Name and salary:\n{subset}\n")

# Select rows by index number with iloc
print(f"Row 0 (iloc):\n{df.iloc[0]}\n")

# Select rows by label with loc
# First, let's set name as the index
df_indexed = df.set_index("name")
print(f"Alice's data (loc):\n{df_indexed.loc['Alice']}\n")

# Slice of rows
print(f"Rows 1-3:\n{df.iloc[1:4]}\n")


# ============================================================
# 5. FILTERING WITH CONDITIONS
# ============================================================
# This is where Pandas gets REALLY powerful.
# You can ask questions about your data in plain logic!

print("=" * 60)
print("FILTERING")
print("=" * 60)

# Who earns more than 80k?
high_earners = df[df["salary"] > 80000]
print(f"Salary > 80k:\n{high_earners}\n")

# Who's in Engineering?
engineers = df[df["department"] == "Engineering"]
print(f"Engineers:\n{engineers}\n")

# Multiple conditions — use & (and), | (or), ~ (not)
# IMPORTANT: Each condition needs parentheses!
senior_engineers = df[(df["department"] == "Engineering") & (df["years"] > 5)]
print(f"Senior engineers (>5 years):\n{senior_engineers}\n")

# Using .isin() for multiple values
marketing_or_hr = df[df["department"].isin(["Marketing", "HR"])]
print(f"Marketing or HR:\n{marketing_or_hr}\n")


# ============================================================
# 6. SORTING
# ============================================================
print("=" * 60)
print("SORTING")
print("=" * 60)

# Sort by salary (ascending)
by_salary = df.sort_values("salary")
print(f"By salary (ascending):\n{by_salary}\n")

# Sort by salary (descending)
by_salary_desc = df.sort_values("salary", ascending=False)
print(f"By salary (descending):\n{by_salary_desc}\n")

# Sort by multiple columns
by_dept_salary = df.sort_values(["department", "salary"], ascending=[True, False])
print(f"By department, then salary (desc):\n{by_dept_salary}\n")


# ============================================================
# 7. GROUPBY — Split, Apply, Combine
# ============================================================
# groupby is like saying "for each department, calculate..."
# It's the SQL GROUP BY equivalent.
# Think of it as sorting papers into piles, then analyzing each pile.

print("=" * 60)
print("GROUPBY")
print("=" * 60)

# Average salary by department
avg_by_dept = df.groupby("department")["salary"].mean()
print(f"Average salary by department:\n{avg_by_dept}\n")

# Multiple aggregations at once
dept_stats = df.groupby("department").agg({
    "salary": ["mean", "max", "min"],
    "years": "mean"
})
print(f"Department stats:\n{dept_stats}\n")

# Count per department
dept_counts = df.groupby("department").size()
print(f"Employees per department:\n{dept_counts}\n")


# ============================================================
# 8. HANDLING MISSING DATA
# ============================================================
# Real-world data is messy. Missing values happen ALL THE TIME.
# Pandas uses NaN (Not a Number) to represent missing data.

print("=" * 60)
print("MISSING DATA")
print("=" * 60)

messy_data = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie", "Diana"],
    "age": [25, None, 35, 28],
    "score": [90, 85, None, None],
    "city": ["NYC", "LA", None, "Chicago"]
})
print(f"Messy data:\n{messy_data}\n")

# Detect missing values
print(f"Is null?\n{messy_data.isna()}\n")
print(f"Null counts per column:\n{messy_data.isna().sum()}\n")

# Fill missing values
filled = messy_data.fillna({"age": messy_data["age"].mean(),
                             "score": 0,
                             "city": "Unknown"})
print(f"After fillna:\n{filled}\n")

# Drop rows with ANY missing value
dropped = messy_data.dropna()
print(f"After dropna:\n{dropped}\n")

# Drop rows only if a specific column is missing
dropped_score = messy_data.dropna(subset=["score"])
print(f"Dropped only if score is missing:\n{dropped_score}\n")


# ============================================================
# 9. DESCRIBE AND VALUE_COUNTS
# ============================================================
# describe() gives you instant stats. value_counts() is like
# a frequency table. These are your "quick look" tools.

print("=" * 60)
print("DESCRIBE & VALUE_COUNTS")
print("=" * 60)

print(f"df.describe() — stats for numeric columns:\n{df.describe()}\n")

print(f"Department value counts:\n{df['department'].value_counts()}\n")

# Adding new columns
df["bonus"] = df["salary"] * 0.10
print(f"With bonus column:\n{df}\n")

# Quick math on columns
print(f"Total compensation:\n{df['salary'] + df['bonus']}\n")


# ============================================================
# RECAP
# ============================================================
print("=" * 60)
print("CHAPTER 27 RECAP")
print("=" * 60)
print("""
Pandas gives you labeled, structured data analysis:

1. Series: Labeled 1D data (like a column)
2. DataFrame: Labeled 2D table (like a spreadsheet)
3. read_csv(): Load data from CSV files
4. Selecting: df['col'], df.iloc[], df.loc[]
5. Filtering: df[df['col'] > value] — query your data!
6. Sorting: sort_values() with ascending parameter
7. Groupby: Split data into groups and aggregate
8. Missing data: isna(), fillna(), dropna()
9. describe(): Instant statistical summary
10. value_counts(): Frequency of each value

Next up: Making beautiful charts with matplotlib and seaborn!
""")
