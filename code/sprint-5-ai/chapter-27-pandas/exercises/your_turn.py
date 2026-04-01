"""
Chapter 27: Pandas — YOUR TURN!
=================================

You're a data analyst at a movie streaming company. You've got a
dataset of movie ratings and your boss wants insights. Time to flex
those Pandas muscles!

TASKS:
1. Create the movie DataFrame from the data below
2. Display basic info: shape, dtypes, first 3 rows
3. Find all movies with rating >= 8.0
4. Find all Action movies from 2020 or later
5. Sort movies by rating (descending)
6. Calculate average rating per genre
7. Find the genre with the most movies
8. Find the movie with the most votes
9. Handle the missing data (there are some NaN values!)
10. BONUS: Add a "popularity" column = votes / 1000, rounded to 1 decimal
"""

import pandas as pd
import numpy as np

# Here's your movie dataset — create the DataFrame from this dict
movie_data = {
    "title": [
        "The Matrix", "Inception", "Interstellar", "The Dark Knight",
        "Pulp Fiction", "Fight Club", "Forrest Gump", "Gladiator",
        "Mad Max: Fury Road", "John Wick", "Dune", "Spider-Verse",
        "Parasite", "Joker", "Avengers: Endgame", "Oppenheimer"
    ],
    "genre": [
        "Action", "Sci-Fi", "Sci-Fi", "Action",
        "Crime", "Drama", "Drama", "Action",
        "Action", "Action", "Sci-Fi", "Animation",
        "Thriller", "Drama", "Action", "Drama"
    ],
    "rating": [
        8.7, 8.8, 8.6, 9.0,
        8.9, 8.8, 8.8, 8.5,
        8.1, 7.4, 8.0, 8.4,
        8.5, 8.4, 8.4, None  # Missing rating!
    ],
    "year": [
        1999, 2010, 2014, 2008,
        1994, 1999, 1994, 2000,
        2015, 2014, 2021, 2018,
        2019, 2019, 2019, 2023
    ],
    "votes": [
        1900000, 2300000, 1800000, 2700000,
        2100000, 2100000, 2000000, 1500000,
        1000000, 800000, 700000, None,  # Missing votes!
        850000, 1300000, 1100000, 900000
    ]
}

# TODO 1: Create the DataFrame
movies = None

# TODO 2: Display basic info
# print shape, dtypes, and first 3 rows

# TODO 3: Find all movies rated 8.0 or higher
# Hint: movies[movies["rating"] >= 8.0]

# TODO 4: Find all Action movies from 2020 or later
# Hint: Use & with two conditions (both in parentheses)

# TODO 5: Sort by rating, highest first

# TODO 6: Average rating per genre
# Hint: groupby("genre")["rating"].mean()

# TODO 7: Genre with the most movies
# Hint: value_counts() on the genre column

# TODO 8: Movie with the most votes
# Hint: idxmax() or sort_values

# TODO 9: Handle missing data
# - How many missing values per column?
# - Fill missing rating with the mean rating
# - Fill missing votes with 0

# TODO 10 (BONUS): Add popularity column
# popularity = votes / 1000, rounded to 1 decimal
