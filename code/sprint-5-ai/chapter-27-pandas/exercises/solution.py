"""
Chapter 27: Pandas — SOLUTION
===============================

Movie analysis complete! Your boss is going to be impressed.
This is basically what real data analysts do (with bigger datasets).
"""

import pandas as pd
import numpy as np

# Movie dataset
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
        8.5, 8.4, 8.4, None
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
        1000000, 800000, 700000, None,
        850000, 1300000, 1100000, 900000
    ]
}

# TASK 1: Create the DataFrame
movies = pd.DataFrame(movie_data)
print("MOVIE DATABASE")
print("=" * 70)
print(movies.to_string(index=False))
print()

# TASK 2: Basic info
print("BASIC INFO")
print("=" * 70)
print(f"Shape: {movies.shape} ({movies.shape[0]} movies, {movies.shape[1]} columns)")
print(f"\nData types:\n{movies.dtypes}")
print(f"\nFirst 3 rows:\n{movies.head(3)}")
print()

# TASK 3: Movies rated 8.0 or higher
print("MOVIES RATED 8.0+")
print("=" * 70)
top_rated = movies[movies["rating"] >= 8.0]
print(top_rated[["title", "rating"]].to_string(index=False))
print(f"({len(top_rated)} movies)\n")

# TASK 4: Action movies from 2020 or later
print("ACTION MOVIES (2020+)")
print("=" * 70)
recent_action = movies[(movies["genre"] == "Action") & (movies["year"] >= 2020)]
if len(recent_action) > 0:
    print(recent_action[["title", "year"]].to_string(index=False))
else:
    print("No action movies from 2020 or later in this dataset!")
print()

# TASK 5: Sort by rating (descending)
print("ALL MOVIES SORTED BY RATING")
print("=" * 70)
sorted_movies = movies.sort_values("rating", ascending=False)
print(sorted_movies[["title", "rating"]].to_string(index=False))
print()

# TASK 6: Average rating per genre
print("AVERAGE RATING BY GENRE")
print("=" * 70)
avg_by_genre = movies.groupby("genre")["rating"].mean().sort_values(ascending=False)
for genre, rating in avg_by_genre.items():
    print(f"  {genre:12s} {rating:.2f}")
print()

# TASK 7: Genre with the most movies
print("GENRE COUNTS")
print("=" * 70)
genre_counts = movies["genre"].value_counts()
print(genre_counts)
print(f"\nMost common genre: {genre_counts.index[0]} ({genre_counts.iloc[0]} movies)")
print()

# TASK 8: Movie with the most votes
print("MOST POPULAR MOVIE (by votes)")
print("=" * 70)
# dropna for votes since one is missing
valid_votes = movies.dropna(subset=["votes"])
most_popular_idx = valid_votes["votes"].idxmax()
most_popular = movies.loc[most_popular_idx]
print(f"  {most_popular['title']} — {most_popular['votes']:,.0f} votes")
print()

# TASK 9: Handle missing data
print("MISSING DATA")
print("=" * 70)
print(f"Missing values per column:\n{movies.isna().sum()}\n")

# Fill missing rating with the mean
mean_rating = movies["rating"].mean()
movies["rating"] = movies["rating"].fillna(mean_rating)
print(f"Filled missing rating with mean: {mean_rating:.2f}")

# Fill missing votes with 0
movies["votes"] = movies["votes"].fillna(0)
print(f"Filled missing votes with 0")
print(f"\nMissing values now:\n{movies.isna().sum()}\n")

# TASK 10 (BONUS): Add popularity column
movies["popularity"] = (movies["votes"] / 1000).round(1)
print("WITH POPULARITY COLUMN")
print("=" * 70)
print(movies[["title", "votes", "popularity"]].to_string(index=False))
print()

# EXTRA: Quick describe
print("DATASET SUMMARY")
print("=" * 70)
print(movies.describe())
