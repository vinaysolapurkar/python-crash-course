# Chapter 28: Data Visualization: Making Data Beautiful

> **Sprint 5, Chapter 28** | **12 min read** | **Code: [github link](https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/sprint-5-ai/chapter-28-data-visualization/)**

Data without visualization is like a movie without pictures. Technically the story is there, but nobody's paying attention. You could hand your boss a spreadsheet with 10,000 rows and say "the numbers are good." Or you could show them one chart that makes their eyebrows go up. Guess which one gets you the raise.

## What You'll Learn
- Matplotlib basics: line, scatter, bar, histogram, pie charts
- Making charts not ugly: labels, titles, colors, legends
- Subplots -- multiple charts in one figure
- Seaborn -- matplotlib but prettier
- Plotly -- interactive charts that move
- Choosing the right chart for your data

## Why Should I Care?

Presentations. Reports. Dashboards. Job interviews. Blog posts. Every time you need to communicate something about data, you need a chart. Data visualization is the difference between "I analyzed the data" and "let me show you what I found." One gets a nod. The other gets attention.

Also, you'll use visualization constantly when building machine learning models. Plotting your data before feeding it to an algorithm is like reading the recipe before you start cooking. Highly recommended.

## Installing the Libraries

```bash
pip install matplotlib seaborn plotly
```

```python
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
```

That `matplotlib.pyplot as plt` is another one of those universal conventions. Every tutorial, every textbook, every notebook. Just `plt`.

## Matplotlib: The Foundation

Matplotlib is the original Python plotting library. It's not the prettiest out of the box, but it's the most flexible and everything else is built on top of it.

### Your First Chart: Line Plot

```python
import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [120, 135, 148, 162, 155, 178]

plt.plot(months, sales)
plt.title("Monthly Sales 2024")
plt.xlabel("Month")
plt.ylabel("Sales ($K)")
plt.show()
```

That's it. Five lines. You've got a chart.

Let's make it look better:

```python
plt.plot(months, sales, color="royalblue", marker="o", linewidth=2, markersize=8)
plt.title("Monthly Sales 2024", fontsize=16, fontweight="bold")
plt.xlabel("Month", fontsize=12)
plt.ylabel("Sales ($K)", fontsize=12)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

Now it looks like something you'd actually put in a presentation.

### Multiple Lines on One Chart

```python
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
product_a = [120, 135, 148, 162, 155, 178]
product_b = [90, 105, 112, 130, 142, 151]
product_c = [75, 80, 95, 88, 102, 110]

plt.plot(months, product_a, marker="o", label="Product A")
plt.plot(months, product_b, marker="s", label="Product B")
plt.plot(months, product_c, marker="^", label="Product C")

plt.title("Sales by Product", fontsize=14, fontweight="bold")
plt.xlabel("Month")
plt.ylabel("Sales ($K)")
plt.legend()  # Shows the labels
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

### Scatter Plot: Seeing Relationships

```python
import numpy as np

# Movie data
budgets = [63, 160, 165, 185, 8, 55, 6, 11, 5, 150]
revenues = [467, 836, 701, 1005, 214, 678, 287, 266, 255, 375]
ratings = [8.7, 8.8, 8.6, 9.0, 8.9, 8.8, 9.2, 8.5, 7.7, 8.1]

# Size of dots based on rating, color based on rating
plt.scatter(budgets, revenues, s=[r * 30 for r in ratings],
            c=ratings, cmap="coolwarm", alpha=0.7, edgecolors="black")

plt.colorbar(label="Rating")
plt.title("Budget vs Revenue", fontsize=14, fontweight="bold")
plt.xlabel("Budget ($M)")
plt.ylabel("Revenue ($M)")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

Scatter plots are perfect for answering "Is there a relationship between X and Y?" In this case: does spending more on a movie mean making more money? (Spoiler: sort of, but Pulp Fiction says otherwise.)

### Bar Chart: Comparing Categories

```python
genres = ["Sci-Fi", "Action", "Crime", "Drama", "Thriller", "Horror"]
avg_ratings = [8.70, 8.55, 9.05, 8.80, 8.50, 7.70]

colors = ["#2196F3", "#FF5722", "#4CAF50", "#FF9800", "#9C27B0", "#F44336"]

plt.bar(genres, avg_ratings, color=colors, edgecolor="black", linewidth=0.5)
plt.title("Average Rating by Genre", fontsize=14, fontweight="bold")
plt.xlabel("Genre")
plt.ylabel("Average Rating")
plt.ylim(7, 10)  # Start y-axis at 7 to show differences better
plt.tight_layout()
plt.show()
```

Horizontal bars work better when you have long category names:

```python
movies = ["The Godfather", "The Dark Knight", "Pulp Fiction",
          "Inception", "Forrest Gump", "The Matrix"]
ratings = [9.2, 9.0, 8.9, 8.8, 8.8, 8.7]

plt.barh(movies, ratings, color="steelblue", edgecolor="black")
plt.title("Top 6 Movies by Rating", fontsize=14, fontweight="bold")
plt.xlabel("Rating")
plt.xlim(8.5, 9.5)
plt.tight_layout()
plt.show()
```

### Histogram: Distribution of Data

```python
import numpy as np

# Generate 1000 random test scores
np.random.seed(42)
scores = np.random.normal(loc=75, scale=12, size=1000)

plt.hist(scores, bins=25, color="steelblue", edgecolor="black", alpha=0.7)
plt.title("Distribution of Test Scores", fontsize=14, fontweight="bold")
plt.xlabel("Score")
plt.ylabel("Number of Students")
plt.axvline(np.mean(scores), color="red", linestyle="--", label=f"Mean: {np.mean(scores):.1f}")
plt.legend()
plt.tight_layout()
plt.show()
```

Histograms answer the question: "What does the spread of my data look like?" The bell curve shape means most students scored near the average, with fewer at the extremes. You'll see this shape everywhere in statistics and ML.

### Pie Chart: Parts of a Whole

```python
genres = ["Sci-Fi", "Action", "Crime", "Drama", "Thriller", "Horror"]
counts = [3, 2, 2, 1, 1, 1]

colors = ["#2196F3", "#FF5722", "#4CAF50", "#FF9800", "#9C27B0", "#F44336"]

plt.pie(counts, labels=genres, colors=colors, autopct="%1.0f%%",
        startangle=90, explode=[0.05] * 6)
plt.title("Movies by Genre", fontsize=14, fontweight="bold")
plt.tight_layout()
plt.show()
```

> **Pro Tip:** Pie charts get a bad reputation in data science. They're fine for showing simple proportions (like budget breakdown), but bar charts are almost always easier to read when comparing values. Use pie charts sparingly.

## Making Charts Not Ugly

Here's the cheat sheet for going from "default matplotlib" to "actually presentable":

```python
import matplotlib.pyplot as plt
import numpy as np

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [120, 135, 148, 162, 155, 178]

# Set a style -- this changes everything
plt.style.use("seaborn-v0_8-whitegrid")  # Clean, modern look

fig, ax = plt.subplots(figsize=(10, 6))  # Control the size

ax.plot(months, sales, color="#2196F3", marker="o", linewidth=2.5,
        markersize=8, markerfacecolor="white", markeredgewidth=2)

ax.set_title("Monthly Sales 2024", fontsize=18, fontweight="bold", pad=20)
ax.set_xlabel("Month", fontsize=13)
ax.set_ylabel("Sales ($K)", fontsize=13)
ax.set_ylim(100, 200)

# Add value labels on each point
for i, (month, sale) in enumerate(zip(months, sales)):
    ax.annotate(f"${sale}K", (month, sale), textcoords="offset points",
                xytext=(0, 12), ha="center", fontsize=10)

ax.grid(True, alpha=0.3)
fig.tight_layout()
plt.show()
```

Key upgrades:
- `plt.style.use()` -- sets a global style theme
- `figsize=(10, 6)` -- control the chart size
- `tight_layout()` -- prevents labels from getting cut off
- Annotations -- add data labels directly on the chart
- Custom colors with hex codes -- no more default blue

Available styles you can try:

```python
# See all available styles
print(plt.style.available)

# Some good ones:
# "seaborn-v0_8-whitegrid" -- clean and modern
# "ggplot" -- R-inspired
# "fivethirtyeight" -- news/data journalism style
# "dark_background" -- dark mode
```

### Saving Charts

```python
# Save to file instead of displaying
plt.savefig("sales_chart.png", dpi=150, bbox_inches="tight")

# Other formats
plt.savefig("sales_chart.pdf")
plt.savefig("sales_chart.svg")  # Vector format -- scales perfectly
```

## Subplots: Multiple Charts in One Figure

Sometimes one chart isn't enough. You want to show several views of the same data side by side.

```python
import matplotlib.pyplot as plt
import numpy as np

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Top-left: Line chart
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [120, 135, 148, 162, 155, 178]
axes[0, 0].plot(months, sales, marker="o", color="steelblue")
axes[0, 0].set_title("Monthly Sales", fontweight="bold")
axes[0, 0].set_ylabel("Sales ($K)")

# Top-right: Bar chart
genres = ["Sci-Fi", "Action", "Crime", "Drama"]
counts = [3, 2, 2, 1]
axes[0, 1].bar(genres, counts, color=["#2196F3", "#FF5722", "#4CAF50", "#FF9800"])
axes[0, 1].set_title("Movies by Genre", fontweight="bold")

# Bottom-left: Scatter plot
np.random.seed(42)
x = np.random.randn(100)
y = x * 2 + np.random.randn(100) * 0.5
axes[1, 0].scatter(x, y, alpha=0.6, color="purple")
axes[1, 0].set_title("Correlation Example", fontweight="bold")
axes[1, 0].set_xlabel("X")
axes[1, 0].set_ylabel("Y")

# Bottom-right: Histogram
scores = np.random.normal(75, 12, 500)
axes[1, 1].hist(scores, bins=20, color="coral", edgecolor="black")
axes[1, 1].set_title("Score Distribution", fontweight="bold")
axes[1, 1].set_xlabel("Score")

fig.suptitle("Dashboard Example", fontsize=16, fontweight="bold", y=1.02)
plt.tight_layout()
plt.show()
```

`plt.subplots(2, 2)` gives you a 2x2 grid. Access each chart with `axes[row, col]`. Fill them in with whatever chart types you want. This is how dashboards are born.

## Seaborn: Matplotlib But Prettier

Seaborn is built on top of matplotlib and makes statistical charts gorgeous with almost no effort.

```python
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Using our movie data
movies = pd.DataFrame({
    "title": ["The Matrix", "Inception", "Interstellar", "The Dark Knight",
              "Pulp Fiction", "Forrest Gump", "The Godfather", "Parasite",
              "Get Out", "Mad Max: Fury Road"],
    "genre": ["Sci-Fi", "Sci-Fi", "Sci-Fi", "Action", "Crime", "Drama",
              "Crime", "Thriller", "Horror", "Action"],
    "rating": [8.7, 8.8, 8.6, 9.0, 8.9, 8.8, 9.2, 8.5, 7.7, 8.1],
    "budget_millions": [63, 160, 165, 185, 8, 55, 6, 11, 5, 150],
    "revenue_millions": [467, 836, 701, 1005, 214, 678, 287, 266, 255, 375]
})
```

### Bar Plot

```python
plt.figure(figsize=(10, 6))
sns.barplot(data=movies, x="genre", y="rating", palette="viridis")
plt.title("Average Rating by Genre", fontsize=14, fontweight="bold")
plt.tight_layout()
plt.show()
```

One line of seaborn replaces about ten lines of matplotlib. And it looks better. The bars automatically show confidence intervals (those little lines on top). Seaborn thinks statistically by default.

### Box Plot

```python
# Create a bigger dataset for box plots
import numpy as np
np.random.seed(42)

data = pd.DataFrame({
    "department": np.random.choice(["Engineering", "Marketing", "Sales", "HR"], 200),
    "salary": np.random.normal(75000, 15000, 200),
    "satisfaction": np.random.uniform(1, 10, 200)
})

plt.figure(figsize=(10, 6))
sns.boxplot(data=data, x="department", y="salary", palette="Set2")
plt.title("Salary Distribution by Department", fontsize=14, fontweight="bold")
plt.ylabel("Salary ($)")
plt.tight_layout()
plt.show()
```

Box plots show you the median, quartiles, and outliers at a glance. They're the "tell me everything about this distribution in one shape" chart.

### Heatmap

```python
# Correlation matrix -- how are variables related?
numeric_movies = movies[["rating", "budget_millions", "revenue_millions"]].copy()

plt.figure(figsize=(8, 6))
sns.heatmap(numeric_movies.corr(), annot=True, cmap="coolwarm",
            center=0, fmt=".2f", linewidths=1)
plt.title("Correlation Heatmap", fontsize=14, fontweight="bold")
plt.tight_layout()
plt.show()
```

A heatmap of correlations instantly shows you which variables are related. Dark red = strong positive correlation. Dark blue = strong negative. This is one of the first things data scientists plot with a new dataset.

### Pairplot: The Kitchen Sink

```python
# This one chart shows every relationship between every numeric column
sns.pairplot(movies[["rating", "budget_millions", "revenue_millions"]],
             diag_kind="hist", plot_kws={"alpha": 0.6})
plt.suptitle("Relationships Between Movie Variables", y=1.02)
plt.show()
```

One line. You get scatter plots for every pair of variables and histograms on the diagonal. It's like x-ray vision for your dataset.

## Plotly: Interactive Charts That Move

Plotly creates charts you can hover over, zoom into, and interact with. Perfect for dashboards and web apps.

```python
import plotly.express as px
import pandas as pd

movies = pd.DataFrame({
    "title": ["The Matrix", "Inception", "Interstellar", "The Dark Knight",
              "Pulp Fiction", "Forrest Gump", "The Godfather", "Parasite",
              "Get Out", "Mad Max: Fury Road"],
    "genre": ["Sci-Fi", "Sci-Fi", "Sci-Fi", "Action", "Crime", "Drama",
              "Crime", "Thriller", "Horror", "Action"],
    "rating": [8.7, 8.8, 8.6, 9.0, 8.9, 8.8, 9.2, 8.5, 7.7, 8.1],
    "budget_millions": [63, 160, 165, 185, 8, 55, 6, 11, 5, 150],
    "revenue_millions": [467, 836, 701, 1005, 214, 678, 287, 266, 255, 375]
})

# Interactive scatter plot
fig = px.scatter(
    movies,
    x="budget_millions",
    y="revenue_millions",
    color="genre",
    size="rating",
    hover_name="title",
    title="Budget vs Revenue (Hover for Details!)",
    labels={"budget_millions": "Budget ($M)", "revenue_millions": "Revenue ($M)"}
)
fig.show()  # Opens in your browser!
```

When you run this, a chart opens in your browser. Hover over any dot to see the movie name, genre, budget, revenue, and rating. Zoom in by dragging. This is what modern dashboards look like.

```python
# Interactive bar chart
fig = px.bar(
    movies.sort_values("rating", ascending=True),
    x="rating",
    y="title",
    orientation="h",
    color="genre",
    title="Movie Ratings",
    labels={"rating": "IMDb Rating", "title": "Movie"}
)
fig.show()

# Interactive line chart with animation
# (Imagine monthly data over several years)
fig = px.scatter(
    movies,
    x="budget_millions",
    y="revenue_millions",
    color="genre",
    hover_name="title",
    size_max=15,
    title="Movie Economics"
)
fig.update_layout(template="plotly_white")
fig.show()
```

> **Pro Tip:** Plotly charts can be embedded directly in web apps (Flask, Streamlit, Dash). If you want to build data dashboards, Plotly + Dash is one of the most popular combinations in the industry.

## Choosing the Right Chart

Here's your decision guide:

| Question You're Asking | Chart Type | Library Call |
|---|---|---|
| How does something change over time? | **Line chart** | `plt.plot()` |
| How do categories compare? | **Bar chart** | `plt.bar()` or `sns.barplot()` |
| What's the relationship between X and Y? | **Scatter plot** | `plt.scatter()` or `px.scatter()` |
| What does the distribution look like? | **Histogram** | `plt.hist()` or `sns.histplot()` |
| What are the proportions? | **Pie chart** | `plt.pie()` |
| How are variables correlated? | **Heatmap** | `sns.heatmap()` |
| How is data distributed across groups? | **Box plot** | `sns.boxplot()` |
| I want to see EVERYTHING | **Pair plot** | `sns.pairplot()` |
| I need interactivity | **Any Plotly chart** | `px.scatter()`, `px.bar()`, etc. |

When in doubt, start with a bar chart (for categories) or scatter plot (for relationships). You can always change it later.

> **Fun Fact:** Matplotlib was created by John Hunter in 2003 to replicate MATLAB's plotting capabilities in Python. The name literally comes from "MATLAB plotting library." Hunter wanted scientists who were used to MATLAB to feel right at home. The project became one of the most-used Python libraries in history.

## Pandas + Matplotlib: The Quick Way

Pandas DataFrames have built-in plotting that uses matplotlib under the hood:

```python
import pandas as pd
import matplotlib.pyplot as plt

movies = pd.DataFrame({
    "title": ["The Matrix", "Inception", "The Dark Knight", "Pulp Fiction", "The Godfather"],
    "rating": [8.7, 8.8, 9.0, 8.9, 9.2],
    "budget_millions": [63, 160, 185, 8, 6],
    "revenue_millions": [467, 836, 1005, 214, 287]
})

# Plot directly from a DataFrame
movies.plot(x="title", y="rating", kind="bar", figsize=(10, 5),
            title="Movie Ratings", legend=False, color="steelblue")
plt.ylabel("Rating")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()

# Scatter plot from DataFrame
movies.plot(x="budget_millions", y="revenue_millions", kind="scatter",
            figsize=(8, 6), title="Budget vs Revenue")
plt.show()
```

This is great for quick exploration. You're already in pandas, so why switch? For polished charts, use matplotlib or seaborn directly. For quick "what does this data look like?" plots, pandas is the fastest path.

## Your Turn: Movie Ratings Visual Dashboard

Create `movie_dashboard.py` and build a 2x2 dashboard:

```python
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Movie dataset (use the one from Chapter 27 or create it fresh)
movies = pd.DataFrame({
    "title": ["The Matrix", "Inception", "Interstellar", "The Dark Knight",
              "Pulp Fiction", "Forrest Gump", "The Godfather", "Parasite",
              "Get Out", "Mad Max: Fury Road"],
    "year": [1999, 2010, 2014, 2008, 1994, 1994, 1972, 2019, 2017, 2015],
    "genre": ["Sci-Fi", "Sci-Fi", "Sci-Fi", "Action", "Crime", "Drama",
              "Crime", "Thriller", "Horror", "Action"],
    "rating": [8.7, 8.8, 8.6, 9.0, 8.9, 8.8, 9.2, 8.5, 7.7, 8.1],
    "budget_millions": [63, 160, 165, 185, 8, 55, 6, 11, 5, 150],
    "revenue_millions": [467, 836, 701, 1005, 214, 678, 287, 266, 255, 375]
})

movies["profit_millions"] = movies["revenue_millions"] - movies["budget_millions"]

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# 1. Top-left: Bar chart of ratings (sorted)

# 2. Top-right: Scatter plot of budget vs revenue, colored by genre

# 3. Bottom-left: Horizontal bar chart of profit by movie

# 4. Bottom-right: Pie chart of genre distribution

fig.suptitle("Movie Dashboard", fontsize=18, fontweight="bold")
plt.tight_layout()
plt.savefig("movie_dashboard.png", dpi=150, bbox_inches="tight")
plt.show()
```

Challenge: Also create one interactive Plotly chart showing budget vs revenue with hover labels.

## TL;DR

- **Matplotlib** is the foundation: `plt.plot()`, `plt.scatter()`, `plt.bar()`, `plt.hist()`, `plt.pie()`
- Make charts pretty with labels, titles, colors, grid, `tight_layout()`, and `plt.style.use()`
- **Subplots**: `fig, axes = plt.subplots(rows, cols)` for multi-chart dashboards
- **Seaborn** makes statistical charts beautiful with minimal code: `sns.barplot()`, `sns.heatmap()`, `sns.boxplot()`
- **Plotly** creates interactive, browser-based charts: `px.scatter()`, `px.bar()`
- Save charts with `plt.savefig("chart.png", dpi=150)`
- Use pandas `.plot()` for quick exploration, dedicated libraries for polished output
- When in doubt: bar chart for categories, scatter for relationships, histogram for distributions
