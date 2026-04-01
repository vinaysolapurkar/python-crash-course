# Chapter 27: Pandas: Data Analysis Like a Boss

> **Sprint 5, Chapter 27** | **12 min read** | **Code: [github link](https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/sprint-5-ai/chapter-27-pandas/)**

If Excel and Python had a baby, it would be pandas. All the spreadsheet power, none of the mouse clicking. No more dragging formulas across 10,000 rows. No more accidentally sorting one column and scrambling all your data. Pandas does what Excel does -- but in code, which means it's reproducible, automatable, and infinitely more powerful.

## What You'll Learn
- Series (one column) and DataFrame (the whole spreadsheet)
- Reading CSV files into pandas
- Selecting columns and rows
- Filtering data with conditions
- Sorting and groupby (pivot table vibes)
- Handling missing data
- `describe()` -- instant statistics

## Why Should I Care?

Data science, business analytics, machine learning prep, financial analysis, marketing reports -- they all start with pandas. If data is the new oil, pandas is the refinery. Every data science job listing mentions it. Every machine learning project starts by loading data into a pandas DataFrame. If you plan to work with data in any capacity, pandas is non-negotiable.

## Installing Pandas

```bash
pip install pandas
```

```python
import pandas as pd
```

Just like NumPy has `np`, pandas has `pd`. It's the law. Nobody will arrest you for writing `import pandas`, but other programmers will give you a look.

## Series: One Column of Data

A **Series** is a single column of data with labels. Think of it as a labeled list.

```python
import pandas as pd

# Create a Series from a list
scores = pd.Series([85, 92, 78, 95, 88])
print(scores)
# 0    85
# 1    92
# 2    78
# 3    95
# 4    88
# dtype: int64
```

Notice the numbers on the left? That's the **index** -- automatic labels. You can set your own:

```python
scores = pd.Series(
    [85, 92, 78, 95, 88],
    index=["Alice", "Bob", "Charlie", "Diana", "Eve"]
)
print(scores)
# Alice      85
# Bob        92
# Charlie    78
# Diana      95
# Eve        88
# dtype: int64

# Access by label
print(scores["Diana"])    # 95

# Access by position
print(scores.iloc[0])     # 85
```

> **Remember When?** Remember dictionaries from Chapter 9? A Series is basically a dictionary with superpowers. Keys become the index, values become the data. And you get all of NumPy's math for free.

## DataFrame: The Whole Spreadsheet

A **DataFrame** is the star of the show. It's a table -- rows and columns, just like a spreadsheet. Each column is a Series.

```python
import pandas as pd

# Create a DataFrame from a dictionary
data = {
    "name": ["Alice", "Bob", "Charlie", "Diana", "Eve"],
    "age": [25, 30, 35, 28, 32],
    "city": ["New York", "London", "Tokyo", "Paris", "Sydney"],
    "salary": [70000, 85000, 90000, 75000, 88000]
}

df = pd.DataFrame(data)
print(df)
#       name  age      city  salary
# 0    Alice   25  New York   70000
# 1      Bob   30    London   85000
# 2  Charlie   35     Tokyo   90000
# 3    Diana   28     Paris   75000
# 4      Eve   32    Sydney   88000
```

That's it. Dictionary keys become column names. Lists become the data. You just created a spreadsheet in three lines of code.

```python
# Quick info about your DataFrame
print(df.shape)     # (5, 4) -- 5 rows, 4 columns
print(df.columns)   # Index(['name', 'age', 'city', 'salary'], dtype='object')
print(df.dtypes)
# name      object
# age        int64
# city      object
# salary     int64
```

## Reading Data from CSV

In the real world, you rarely type in data manually. You read it from files. The most common format is CSV (Comma-Separated Values).

```python
# Reading a CSV file
df = pd.read_csv("movies.csv")

# First 5 rows (always do this first!)
print(df.head())

# Last 5 rows
print(df.tail())

# How big is it?
print(df.shape)  # (1000, 8) -- 1000 movies, 8 columns
```

Let's create a sample CSV to work with throughout this chapter:

```python
import pandas as pd

# Creating our sample movie dataset
movies_data = {
    "title": ["The Matrix", "Inception", "Interstellar", "The Dark Knight",
              "Pulp Fiction", "Forrest Gump", "The Godfather", "Parasite",
              "Get Out", "Mad Max: Fury Road"],
    "year": [1999, 2010, 2014, 2008, 1994, 1994, 1972, 2019, 2017, 2015],
    "genre": ["Sci-Fi", "Sci-Fi", "Sci-Fi", "Action", "Crime", "Drama",
              "Crime", "Thriller", "Horror", "Action"],
    "rating": [8.7, 8.8, 8.6, 9.0, 8.9, 8.8, 9.2, 8.5, 7.7, 8.1],
    "votes": [1900000, 2300000, 1800000, 2700000, 2100000, 2000000,
              1900000, 800000, 600000, 1000000],
    "runtime_min": [136, 148, 169, 152, 154, 142, 175, 132, 104, 120],
    "budget_millions": [63, 160, 165, 185, 8, 55, 6, 11, 5, 150],
    "revenue_millions": [467, 836, 701, 1005, 214, 678, 287, 266, 255, 375]
}

movies = pd.DataFrame(movies_data)
movies.to_csv("movies.csv", index=False)
print(movies.head())
```

## Selecting Columns and Rows

### Selecting Columns

```python
# Single column (returns a Series)
titles = movies["title"]
print(titles)
# 0          The Matrix
# 1           Inception
# 2        Interstellar
# ...

# Multiple columns (returns a DataFrame)
subset = movies[["title", "rating", "year"]]
print(subset.head())
#              title  rating  year
# 0       The Matrix     8.7  1999
# 1        Inception     8.8  2010
# 2     Interstellar     8.6  2014
```

### Selecting Rows

```python
# By position (iloc = integer location)
first_movie = movies.iloc[0]     # First row
print(first_movie)
# title             The Matrix
# year                    1999
# genre                 Sci-Fi
# rating                   8.7
# ...

# Slice of rows
first_three = movies.iloc[0:3]
print(first_three)

# Specific rows and columns
print(movies.iloc[0:3, [0, 3]])  # First 3 rows, title and rating columns

# By label (loc)
# (Our index is numbers, so loc and iloc look similar here)
print(movies.loc[0, "title"])  # "The Matrix"
```

> **Pro Tip:** `iloc` uses integer positions (like list indexing). `loc` uses labels (like dictionary keys). When your index is just numbers 0, 1, 2..., they look the same. But when your index is custom labels (like dates or names), `loc` is what you want.

## Filtering with Conditions

This is where pandas really starts to flex. Want to find all movies rated above 8.5? One line:

```python
# Movies rated above 8.5
great_movies = movies[movies["rating"] > 8.5]
print(great_movies[["title", "rating"]])
#              title  rating
# 0       The Matrix     8.7
# 1        Inception     8.8
# 2     Interstellar     8.6
# 3   The Dark Knight    9.0
# 4    Pulp Fiction      8.9
# 5    Forrest Gump      8.8
# 6    The Godfather     9.2

# Sci-Fi movies only
scifi = movies[movies["genre"] == "Sci-Fi"]
print(scifi["title"])
# 0      The Matrix
# 1       Inception
# 2    Interstellar

# Combine conditions with & (and) or | (or)
scifi_great = movies[(movies["genre"] == "Sci-Fi") & (movies["rating"] > 8.7)]
print(scifi_great[["title", "rating"]])
#        title  rating
# 1  Inception     8.8

# Movies from the 90s or rated above 9.0
classic_or_great = movies[(movies["year"] < 2000) | (movies["rating"] > 9.0)]
print(classic_or_great[["title", "year", "rating"]])
```

Notice the pattern: `df[condition]`. The condition creates a True/False mask (just like NumPy boolean indexing from Chapter 26), and pandas returns only the rows where it's True.

```python
# Check what values exist in a column
print(movies["genre"].unique())     # ['Sci-Fi' 'Action' 'Crime' 'Drama' 'Thriller' 'Horror']
print(movies["genre"].nunique())    # 6 unique genres
print(movies["genre"].value_counts())
# Sci-Fi      3
# Action      2
# Crime       2
# Drama       1
# Thriller    1
# Horror      1
```

## Sorting and Groupby

### Sorting

```python
# Sort by rating (highest first)
best_first = movies.sort_values("rating", ascending=False)
print(best_first[["title", "rating"]].head())
#              title  rating
# 6    The Godfather     9.2
# 3  The Dark Knight     9.0
# 4    Pulp Fiction      8.9
# 1        Inception     8.8
# 5    Forrest Gump      8.8

# Sort by year, then by rating
sorted_movies = movies.sort_values(["year", "rating"], ascending=[True, False])
print(sorted_movies[["title", "year", "rating"]])
```

### Groupby: Pivot Table Vibes

Groupby is like Excel pivot tables, but cooler. "Group my data by [some column], then calculate [some statistic]."

```python
# Average rating by genre
genre_avg = movies.groupby("genre")["rating"].mean()
print(genre_avg)
# genre
# Action      8.55
# Crime       9.05
# Drama       8.80
# Horror      7.70
# Sci-Fi      8.70
# Thriller    8.50

# Multiple statistics at once
genre_stats = movies.groupby("genre")["rating"].agg(["mean", "min", "max", "count"])
print(genre_stats)
#           mean  min  max  count
# genre
# Action    8.55  8.1  9.0      2
# Crime     9.05  8.9  9.2      2
# Drama     8.80  8.8  8.8      1
# Horror    7.70  7.7  7.7      1
# Sci-Fi    8.70  8.6  8.8      3
# Thriller  8.50  8.5  8.5      1

# Average budget and revenue by genre
money = movies.groupby("genre")[["budget_millions", "revenue_millions"]].mean()
print(money)
```

Here's the Groupby pattern: `df.groupby("column_to_group_by")["column_to_calculate"].operation()`. You'll use this pattern hundreds of times.

## Adding and Modifying Columns

```python
# Add a new column: profit
movies["profit_millions"] = movies["revenue_millions"] - movies["budget_millions"]
print(movies[["title", "profit_millions"]].head())
#            title  profit_millions
# 0     The Matrix              404
# 1      Inception              676
# 2   Interstellar              536
# 3  The Dark Knight            820
# 4   Pulp Fiction              206

# Add a column based on a condition
movies["is_blockbuster"] = movies["revenue_millions"] > 500
print(movies[["title", "is_blockbuster"]])

# Add a column with a calculation
movies["roi"] = (movies["revenue_millions"] / movies["budget_millions"]).round(1)
print(movies[["title", "budget_millions", "revenue_millions", "roi"]])
# Pulp Fiction: ROI of 26.8x on an $8M budget. Not bad, Tarantino.
```

## Handling Missing Data

Real-world data is messy. Columns have missing values. Pandas handles this gracefully with `NaN` (Not a Number).

```python
import pandas as pd
import numpy as np

# Create data with missing values
data = {
    "name": ["Alice", "Bob", "Charlie", "Diana", "Eve"],
    "age": [25, np.nan, 35, 28, np.nan],
    "salary": [70000, 85000, np.nan, 75000, 88000],
    "city": ["New York", "London", None, "Paris", "Sydney"]
}

df = pd.DataFrame(data)
print(df)
#       name   age   salary      city
# 0    Alice  25.0  70000.0  New York
# 1      Bob   NaN  85000.0    London
# 2  Charlie  35.0      NaN      None
# 3    Diana  28.0  75000.0     Paris
# 4      Eve   NaN  88000.0    Sydney
```

Finding missing data:

```python
# Which values are missing?
print(df.isna())
#     name    age  salary   city
# 0  False  False   False  False
# 1  False   True   False  False
# 2  False  False    True   True
# 3  False  False   False  False
# 4  False   True   False  False

# How many missing per column?
print(df.isna().sum())
# name      0
# age       2
# salary    1
# city      1
```

Fixing missing data:

```python
# Option 1: Drop rows with any missing data
clean = df.dropna()
print(clean)  # Only Alice, Diana -- lost 3 rows!

# Option 2: Fill missing values with a specific value
filled = df.fillna({"age": df["age"].mean(), "salary": 0, "city": "Unknown"})
print(filled)
#       name   age   salary      city
# 0    Alice  25.0  70000.0  New York
# 1      Bob  29.3  85000.0    London
# 2  Charlie  35.0      0.0   Unknown
# 3    Diana  28.0  75000.0     Paris
# 4      Eve  29.3  88000.0    Sydney

# Option 3: Drop only rows where a specific column is missing
has_age = df.dropna(subset=["age"])
print(has_age)  # Keeps Alice, Charlie, Diana
```

> **Pro Tip:** `dropna()` is aggressive -- it can remove a lot of data. `fillna()` with the mean or median is usually a better first choice for numerical columns. For categorical columns (like city), `fillna("Unknown")` is a safe bet.

## describe(): Instant Statistics

One function to rule them all:

```python
print(movies.describe())
#            year     rating        votes  runtime_min  budget_millions  revenue_millions
# count  10.0000  10.000000  10000000.00    10.000000        10.000000         10.000000
# mean 2004.2000   8.630000  1710000.000   143.200000        80.800000        508.400000
# std    14.3900   0.440454   672309.450    21.606000        72.800000        263.600000
# min  1972.0000   7.700000   600000.000   104.000000         5.000000        214.000000
# 25%  1995.2500   8.525000  1225000.000   131.000000         9.250000        267.750000
# 50%  2009.0000   8.750000  1900000.000   145.000000        59.000000        376.500000
# 75%  2014.7500   8.825000  2075000.000   156.500000       162.500000        692.250000
# max  2019.0000   9.200000  2700000.000   175.000000       185.000000       1005.000000
```

Count, mean, standard deviation, min, max, and quartiles -- all in one call. This is the first thing every data scientist runs on a new dataset. Always.

```python
# describe() for a single column
print(movies["rating"].describe())

# For non-numeric columns
print(movies["genre"].describe())
# count        10
# unique        6
# top      Sci-Fi
# freq          3
```

> **Don't Panic:** Pandas has hundreds of methods. You need about 20 of them for 95% of your work. This chapter covers those 20. You can always look up the rest when you need them. The pandas documentation is excellent, and honestly, so is asking ChatGPT "how do I do X in pandas?"

## Useful Extras

A few more things you'll use constantly:

```python
# Rename columns
movies_clean = movies.rename(columns={"runtime_min": "runtime", "budget_millions": "budget"})

# Apply a function to every value in a column
movies["title_upper"] = movies["title"].apply(str.upper)

# String methods
movies["title_length"] = movies["title"].str.len()
short_titles = movies[movies["title"].str.contains("The")]

# Reset index after filtering
scifi = movies[movies["genre"] == "Sci-Fi"].reset_index(drop=True)
print(scifi)  # Index is now 0, 1, 2 instead of 0, 1, 2 (original positions)
```

## Your Turn: Movie Ratings Dataset Analysis

Create `movie_analysis.py` and work with the movie dataset we created above:

```python
import pandas as pd

# 1. Load the movies.csv file (or create the DataFrame from above)

# 2. Print the first 5 rows and the shape

# 3. What's the average rating across all movies?

# 4. Which movie has the highest rating? The lowest?

# 5. Filter: Find all movies made after 2010 with a rating above 8.0

# 6. Which genre has the highest average rating?

# 7. Which movie had the best ROI (revenue / budget)?

# 8. Add a "decade" column (1990s, 2000s, 2010s, etc.)
#    Hint: (movies["year"] // 10) * 10

# 9. What's the average budget by decade?

# 10. Sort movies by profit (revenue - budget) in descending order
```

Expected insights:
- The Godfather has the highest rating (9.2) and was made with just $6M
- Pulp Fiction has the best ROI: made $214M on just $8M (26.8x return)
- The 2010s had the highest average budgets
- Crime genre has the highest average rating

## TL;DR

- Pandas is Python's data analysis powerhouse -- think Excel but with code
- `import pandas as pd` -- the universal convention
- **Series** = one column; **DataFrame** = the whole table
- `pd.read_csv("file.csv")` loads data; `df.head()` previews it
- Select columns: `df["col"]` or `df[["col1", "col2"]]`
- Select rows: `df.iloc[0]` (by position) or `df.loc[0]` (by label)
- Filter: `df[df["col"] > value]` -- same boolean indexing pattern as NumPy
- Sort: `df.sort_values("col", ascending=False)`
- Groupby: `df.groupby("col")["other_col"].mean()` -- pivot table in one line
- Missing data: `df.isna().sum()` to find it, `df.fillna()` or `df.dropna()` to fix it
- `df.describe()` gives you instant statistics on every numeric column
- You only need about 20 pandas methods for 95% of your work -- this chapter covered them
