"""
Chapter 28: Data Visualization — YOUR TURN!
=============================================

Remember that movie dataset from Chapter 27? Your boss loved the
analysis. Now she wants CHARTS. "Make it visual," she says.
"Something I can put in a presentation."

You've got the data. Time to make it pretty!

TASKS:
1. Create a bar chart of average rating by genre
2. Create a histogram of ratings distribution
3. Create a scatter plot of votes vs rating
4. BONUS: Combine all three into one figure using subplots

Charts will be saved as PNG files in a "movie_charts" folder.
"""

import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

# Movie dataset (same as Chapter 27)
movies = pd.DataFrame({
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
    "rating": [8.7, 8.8, 8.6, 9.0, 8.9, 8.8, 8.8, 8.5,
               8.1, 7.4, 8.0, 8.4, 8.5, 8.4, 8.4, 8.3],
    "year": [1999, 2010, 2014, 2008, 1994, 1999, 1994, 2000,
             2015, 2014, 2021, 2018, 2019, 2019, 2019, 2023],
    "votes": [1900, 2300, 1800, 2700, 2100, 2100, 2000, 1500,
              1000, 800, 700, 600, 850, 1300, 1100, 900]
})

# Output directory for charts
output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "movie_charts")
os.makedirs(output_dir, exist_ok=True)


# TODO 1: Bar chart — Average rating by genre
# Steps:
# - Group movies by genre, calculate mean rating
# - Create a bar chart with genre on x-axis, avg rating on y-axis
# - Add a title, axis labels, and value labels on top of each bar
# - Save as "genre_ratings.png"

# Your code here...


# TODO 2: Histogram — Ratings distribution
# Steps:
# - Create a histogram of all ratings
# - Use 8-10 bins
# - Add a vertical line for the mean rating
# - Add title, axis labels, legend
# - Save as "ratings_distribution.png"

# Your code here...


# TODO 3: Scatter plot — Votes vs Rating
# Steps:
# - Scatter plot with votes on x-axis, rating on y-axis
# - Color dots by genre (hint: loop through genres, plot each separately)
# - Add title, axis labels, legend
# - Save as "votes_vs_rating.png"

# Your code here...


# TODO 4 (BONUS): Dashboard — All three charts in one figure
# Steps:
# - Create a 2x2 subplot figure (leave one spot empty or add another chart)
# - Put charts 1-3 in the grid
# - Add a main title with plt.suptitle()
# - Save as "movie_dashboard.png"

# Your code here...


print(f"Charts saved to: {output_dir}")
