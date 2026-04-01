"""
Chapter 28: Data Visualization — SOLUTION
===========================================

Your movie dashboard is ready for the boss's presentation!
These charts tell the story of the data — which genres dominate,
how ratings are distributed, and whether more votes mean better ratings.
"""

import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

# Movie dataset
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

# Output directory
output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "movie_charts")
os.makedirs(output_dir, exist_ok=True)

# Color palette for genres
genre_colors = {
    "Action": "#e15759",
    "Sci-Fi": "#4e79a7",
    "Drama": "#76b7b2",
    "Crime": "#f28e2b",
    "Animation": "#59a14f",
    "Thriller": "#b07aa1"
}


# ============================================================
# TASK 1: Bar chart — Average rating by genre
# ============================================================
avg_by_genre = movies.groupby("genre")["rating"].mean().sort_values(ascending=False)

plt.figure(figsize=(9, 5))
colors = [genre_colors.get(g, "#999999") for g in avg_by_genre.index]
bars = plt.bar(avg_by_genre.index, avg_by_genre.values, color=colors,
               edgecolor="white", linewidth=1.5)

# Value labels on top of bars
for bar, val in zip(bars, avg_by_genre.values):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.02,
             f"{val:.2f}", ha="center", va="bottom", fontweight="bold", fontsize=11)

plt.title("Average Movie Rating by Genre", fontsize=16, fontweight="bold")
plt.ylabel("Average Rating", fontsize=12)
plt.ylim(7.0, 9.5)  # Zoom in on the relevant range
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()

chart_path = os.path.join(output_dir, "genre_ratings.png")
plt.savefig(chart_path, dpi=150)
plt.close()
print(f"Saved: {chart_path}")


# ============================================================
# TASK 2: Histogram — Ratings distribution
# ============================================================
plt.figure(figsize=(9, 5))
plt.hist(movies["rating"], bins=10, color="mediumseagreen",
         edgecolor="white", alpha=0.85)

# Mean line
mean_rating = movies["rating"].mean()
plt.axvline(mean_rating, color="red", linestyle="--", linewidth=2,
            label=f"Mean: {mean_rating:.2f}")

# Median line
median_rating = movies["rating"].median()
plt.axvline(median_rating, color="orange", linestyle=":", linewidth=2,
            label=f"Median: {median_rating:.2f}")

plt.title("Distribution of Movie Ratings", fontsize=16, fontweight="bold")
plt.xlabel("Rating", fontsize=12)
plt.ylabel("Number of Movies", fontsize=12)
plt.legend(fontsize=11)
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()

chart_path = os.path.join(output_dir, "ratings_distribution.png")
plt.savefig(chart_path, dpi=150)
plt.close()
print(f"Saved: {chart_path}")


# ============================================================
# TASK 3: Scatter plot — Votes vs Rating
# ============================================================
plt.figure(figsize=(9, 6))

# Plot each genre separately so they get different colors + legend entries
for genre in movies["genre"].unique():
    genre_data = movies[movies["genre"] == genre]
    plt.scatter(genre_data["votes"], genre_data["rating"],
                color=genre_colors.get(genre, "#999"),
                s=100, alpha=0.8, edgecolors="white", linewidth=0.5,
                label=genre)

# Annotate some interesting movies
for _, row in movies.iterrows():
    if row["rating"] >= 8.9 or row["votes"] >= 2500:
        plt.annotate(row["title"],
                     (row["votes"], row["rating"]),
                     textcoords="offset points",
                     xytext=(5, 5), fontsize=8, alpha=0.8)

plt.title("Votes vs Rating — Do Popular Movies Rate Higher?",
          fontsize=14, fontweight="bold")
plt.xlabel("Votes (thousands)", fontsize=12)
plt.ylabel("Rating", fontsize=12)
plt.legend(loc="lower right", fontsize=10)
plt.grid(True, alpha=0.3)
plt.tight_layout()

chart_path = os.path.join(output_dir, "votes_vs_rating.png")
plt.savefig(chart_path, dpi=150)
plt.close()
print(f"Saved: {chart_path}")


# ============================================================
# TASK 4 (BONUS): Dashboard — All three in one figure
# ============================================================
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# --- Top-left: Bar chart of avg rating by genre ---
colors = [genre_colors.get(g, "#999") for g in avg_by_genre.index]
bars = axes[0][0].bar(avg_by_genre.index, avg_by_genre.values,
                       color=colors, edgecolor="white")
for bar, val in zip(bars, avg_by_genre.values):
    axes[0][0].text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.02,
                    f"{val:.1f}", ha="center", va="bottom", fontsize=9, fontweight="bold")
axes[0][0].set_title("Avg Rating by Genre", fontweight="bold")
axes[0][0].set_ylim(7.0, 9.5)
axes[0][0].grid(axis="y", alpha=0.3)
axes[0][0].tick_params(axis='x', rotation=30)

# --- Top-right: Histogram ---
axes[0][1].hist(movies["rating"], bins=10, color="mediumseagreen",
                edgecolor="white", alpha=0.85)
axes[0][1].axvline(mean_rating, color="red", linestyle="--", linewidth=2,
                   label=f"Mean: {mean_rating:.2f}")
axes[0][1].set_title("Ratings Distribution", fontweight="bold")
axes[0][1].set_xlabel("Rating")
axes[0][1].legend(fontsize=9)
axes[0][1].grid(axis="y", alpha=0.3)

# --- Bottom-left: Scatter plot ---
for genre in movies["genre"].unique():
    genre_data = movies[movies["genre"] == genre]
    axes[1][0].scatter(genre_data["votes"], genre_data["rating"],
                       color=genre_colors.get(genre, "#999"),
                       s=80, alpha=0.8, label=genre)
axes[1][0].set_title("Votes vs Rating", fontweight="bold")
axes[1][0].set_xlabel("Votes (K)")
axes[1][0].set_ylabel("Rating")
axes[1][0].legend(fontsize=8, loc="lower right")
axes[1][0].grid(True, alpha=0.3)

# --- Bottom-right: Horizontal bar of movie count per genre ---
genre_counts = movies["genre"].value_counts()
bar_colors = [genre_colors.get(g, "#999") for g in genre_counts.index]
axes[1][1].barh(genre_counts.index, genre_counts.values, color=bar_colors,
                edgecolor="white")
axes[1][1].set_title("Movies per Genre", fontweight="bold")
axes[1][1].set_xlabel("Count")
axes[1][1].grid(axis="x", alpha=0.3)

plt.suptitle("Movie Ratings Dashboard", fontsize=18, fontweight="bold", y=1.01)
plt.tight_layout()

chart_path = os.path.join(output_dir, "movie_dashboard.png")
plt.savefig(chart_path, dpi=150, bbox_inches="tight")
plt.close()
print(f"Saved: {chart_path}")

print(f"\nAll charts saved to: {output_dir}")
print("Great job! Your boss is going to love these visuals!")
