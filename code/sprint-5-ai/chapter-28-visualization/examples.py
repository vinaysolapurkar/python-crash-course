"""
Chapter 28: Data Visualization — Making Data Beautiful
========================================================

"A picture is worth a thousand rows of data."
    — Every data scientist, probably

Visualization turns boring numbers into stories your brain can
actually understand. We'll cover three libraries:

1. matplotlib — The OG. Like a manual transmission car: full control,
   but you do more work. Foundation for everything else.

2. seaborn — Built on matplotlib but prettier by default. Like
   matplotlib wearing a tuxedo.

3. plotly — Interactive charts that work in browsers. Like matplotlib
   that went to Silicon Valley and got funded.

NOTE: Running this file will generate chart images saved to disk.
      If you're in a Jupyter notebook, they'll display inline!
"""

import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend (works without display)
import matplotlib.pyplot as plt
import numpy as np
import os

# Try to import seaborn and plotly (optional)
try:
    import seaborn as sns
    HAS_SEABORN = True
except ImportError:
    HAS_SEABORN = False
    print("Note: seaborn not installed. Run: pip install seaborn")
    print("Skipping seaborn examples.\n")

try:
    import plotly.express as px
    HAS_PLOTLY = True
except ImportError:
    HAS_PLOTLY = False
    print("Note: plotly not installed. Run: pip install plotly")
    print("Skipping plotly examples.\n")

# Create output directory for saved figures
output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "charts")
os.makedirs(output_dir, exist_ok=True)


# ============================================================
# 1. MATPLOTLIB BASICS — Line Plot
# ============================================================
# plt.plot() is your bread and butter. It draws lines.
# Think of it as "connect the dots for adults."

print("=" * 60)
print("1. LINE PLOT")
print("=" * 60)

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [120, 135, 148, 162, 158, 175]

plt.figure(figsize=(8, 5))           # Set the canvas size
plt.plot(months, sales,
         color="royalblue",           # Line color
         marker="o",                   # Dot at each point
         linewidth=2,                  # Thicker line
         markersize=8,                 # Bigger dots
         label="2024 Sales")           # Legend label

plt.title("Monthly Sales", fontsize=16, fontweight="bold")
plt.xlabel("Month", fontsize=12)
plt.ylabel("Sales ($K)", fontsize=12)
plt.legend()                           # Show the legend
plt.grid(True, alpha=0.3)             # Subtle grid lines
plt.tight_layout()                     # Prevent label cutoff

chart_path = os.path.join(output_dir, "01_line_plot.png")
plt.savefig(chart_path, dpi=100)
plt.close()
print(f"Saved: {chart_path}")


# ============================================================
# 2. SCATTER PLOT
# ============================================================
# Perfect for showing relationships between two variables.
# "Does studying more = better grades?" Scatter plot will tell you!

print("\n2. SCATTER PLOT")
print("=" * 60)

np.random.seed(42)
study_hours = np.random.uniform(1, 10, 50)
exam_scores = study_hours * 8 + np.random.normal(0, 5, 50) + 20
exam_scores = np.clip(exam_scores, 0, 100)  # Keep scores in 0-100

plt.figure(figsize=(8, 5))
plt.scatter(study_hours, exam_scores,
            color="coral",
            alpha=0.7,                 # Slight transparency
            edgecolors="darkred",
            s=80)                      # Dot size

# Add a trend line
z = np.polyfit(study_hours, exam_scores, 1)
p = np.poly1d(z)
x_line = np.linspace(1, 10, 100)
plt.plot(x_line, p(x_line), "--", color="darkred", alpha=0.8, label="Trend")

plt.title("Study Hours vs Exam Scores", fontsize=16, fontweight="bold")
plt.xlabel("Hours Studied", fontsize=12)
plt.ylabel("Exam Score", fontsize=12)
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()

chart_path = os.path.join(output_dir, "02_scatter_plot.png")
plt.savefig(chart_path, dpi=100)
plt.close()
print(f"Saved: {chart_path}")


# ============================================================
# 3. BAR CHART
# ============================================================
# Bar charts compare categories. "Which programming language is
# most popular?" That's a bar chart question.

print("\n3. BAR CHART")
print("=" * 60)

languages = ["Python", "JavaScript", "Java", "C++", "Go", "Rust"]
popularity = [85, 78, 65, 55, 42, 38]
colors = ["#3776AB", "#F7DF1E", "#f89820", "#00599C", "#00ADD8", "#DEA584"]

plt.figure(figsize=(8, 5))
bars = plt.bar(languages, popularity, color=colors, edgecolor="white", linewidth=1.5)

# Add value labels on top of each bar (a nice touch!)
for bar, val in zip(bars, popularity):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 1,
             str(val), ha="center", va="bottom", fontweight="bold")

plt.title("Programming Language Popularity", fontsize=16, fontweight="bold")
plt.ylabel("Popularity Score", fontsize=12)
plt.ylim(0, 100)  # Give room for labels
plt.tight_layout()

chart_path = os.path.join(output_dir, "03_bar_chart.png")
plt.savefig(chart_path, dpi=100)
plt.close()
print(f"Saved: {chart_path}")


# ============================================================
# 4. HISTOGRAM
# ============================================================
# Histograms show the DISTRIBUTION of data.
# "How are the scores spread out?" Histogram answers this.
# Not the same as a bar chart! Histograms show continuous data.

print("\n4. HISTOGRAM")
print("=" * 60)

np.random.seed(42)
test_scores = np.random.normal(75, 10, 200)  # Mean 75, std 10, 200 students

plt.figure(figsize=(8, 5))
plt.hist(test_scores, bins=20,
         color="mediumseagreen",
         edgecolor="white",
         alpha=0.8)

# Add a vertical line for the mean
mean_score = np.mean(test_scores)
plt.axvline(mean_score, color="red", linestyle="--", linewidth=2,
            label=f"Mean: {mean_score:.1f}")

plt.title("Test Score Distribution", fontsize=16, fontweight="bold")
plt.xlabel("Score", fontsize=12)
plt.ylabel("Number of Students", fontsize=12)
plt.legend()
plt.tight_layout()

chart_path = os.path.join(output_dir, "04_histogram.png")
plt.savefig(chart_path, dpi=100)
plt.close()
print(f"Saved: {chart_path}")


# ============================================================
# 5. PIE CHART
# ============================================================
# Pie charts show parts of a whole. Use sparingly!
# They're the "comic sans" of data viz — popular but often misused.
# Rule of thumb: if you have more than 5 slices, use a bar chart instead.

print("\n5. PIE CHART")
print("=" * 60)

activities = ["Sleep", "Work", "Commute", "Leisure", "Meals"]
hours = [8, 8, 2, 4, 2]
colors = ["#4e79a7", "#f28e2b", "#e15759", "#76b7b2", "#59a14f"]

plt.figure(figsize=(7, 7))
wedges, texts, autotexts = plt.pie(
    hours,
    labels=activities,
    colors=colors,
    autopct="%1.0f%%",      # Show percentages
    startangle=90,            # Start from the top
    explode=[0, 0, 0, 0.1, 0],  # "Explode" leisure slice
    shadow=True,
    textprops={"fontsize": 12}
)
# Make percentage text bold
for autotext in autotexts:
    autotext.set_fontweight("bold")

plt.title("How I Spend My Day (24 hours)", fontsize=16, fontweight="bold")
plt.tight_layout()

chart_path = os.path.join(output_dir, "05_pie_chart.png")
plt.savefig(chart_path, dpi=100)
plt.close()
print(f"Saved: {chart_path}")


# ============================================================
# 6. SUBPLOTS — Multiple Charts in One Figure
# ============================================================
# Subplots are like having multiple TV screens on one wall.
# Great for comparing related data side by side.

print("\n6. SUBPLOTS")
print("=" * 60)

fig, axes = plt.subplots(2, 2, figsize=(12, 10))
# axes is a 2D array: axes[row][col]

# Top-left: Line chart
x = np.linspace(0, 10, 100)
axes[0][0].plot(x, np.sin(x), color="royalblue", linewidth=2)
axes[0][0].set_title("Sine Wave")
axes[0][0].grid(True, alpha=0.3)

# Top-right: Scatter
np.random.seed(42)
axes[0][1].scatter(np.random.rand(30), np.random.rand(30),
                   color="coral", s=60, alpha=0.7)
axes[0][1].set_title("Random Scatter")

# Bottom-left: Bar
categories = ["A", "B", "C", "D"]
values = [25, 40, 30, 55]
axes[1][0].bar(categories, values, color="mediumseagreen")
axes[1][0].set_title("Category Values")

# Bottom-right: Histogram
data = np.random.normal(0, 1, 500)
axes[1][1].hist(data, bins=25, color="mediumpurple", edgecolor="white")
axes[1][1].set_title("Normal Distribution")

plt.suptitle("Four Charts, One Figure!", fontsize=18, fontweight="bold")
plt.tight_layout()

chart_path = os.path.join(output_dir, "06_subplots.png")
plt.savefig(chart_path, dpi=100)
plt.close()
print(f"Saved: {chart_path}")


# ============================================================
# 7. SEABORN — Statistical Visualization
# ============================================================
# Seaborn makes matplotlib prettier with less code.
# It also has chart types built specifically for stats.

if HAS_SEABORN:
    print("\n7. SEABORN")
    print("=" * 60)

    import pandas as pd

    # Create sample data
    np.random.seed(42)
    df = pd.DataFrame({
        "department": np.random.choice(["Engineering", "Marketing", "Sales", "HR"], 100),
        "salary": np.random.normal(75000, 15000, 100),
        "satisfaction": np.random.uniform(3, 10, 100),
        "experience": np.random.randint(1, 20, 100)
    })

    # --- Seaborn Bar Plot ---
    fig, axes = plt.subplots(1, 3, figsize=(16, 5))

    sns.barplot(data=df, x="department", y="salary", ax=axes[0],
                palette="viridis", errorbar="sd")
    axes[0].set_title("Avg Salary by Department")
    axes[0].tick_params(axis='x', rotation=30)

    # --- Seaborn Box Plot ---
    # Box plots show distribution: median, quartiles, outliers
    # Think of it as a "summary of the spread"
    sns.boxplot(data=df, x="department", y="satisfaction", ax=axes[1],
                palette="Set2")
    axes[1].set_title("Satisfaction by Department")
    axes[1].tick_params(axis='x', rotation=30)

    # --- Seaborn Heatmap ---
    # Heatmaps show correlations or 2D data with colors
    numeric_df = df[["salary", "satisfaction", "experience"]]
    corr_matrix = numeric_df.corr()
    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", center=0,
                fmt=".2f", ax=axes[2])
    axes[2].set_title("Correlation Heatmap")

    plt.suptitle("Seaborn Gallery", fontsize=16, fontweight="bold")
    plt.tight_layout()

    chart_path = os.path.join(output_dir, "07_seaborn.png")
    plt.savefig(chart_path, dpi=100)
    plt.close()
    print(f"Saved: {chart_path}")


# ============================================================
# 8. PLOTLY — Interactive Charts
# ============================================================
# Plotly charts are interactive — you can hover, zoom, and pan.
# They render in your browser as HTML. Perfect for dashboards!

if HAS_PLOTLY:
    print("\n8. PLOTLY")
    print("=" * 60)

    import pandas as pd

    # Sample data
    countries = pd.DataFrame({
        "country": ["USA", "China", "Japan", "Germany", "India",
                     "UK", "France", "Brazil", "Canada", "Australia"],
        "gdp_trillion": [25.5, 18.3, 4.2, 4.1, 3.7,
                          3.1, 2.8, 1.9, 2.1, 1.7],
        "population_m": [331, 1412, 125, 84, 1408,
                          67, 67, 215, 38, 26],
        "continent": ["N. America", "Asia", "Asia", "Europe", "Asia",
                       "Europe", "Europe", "S. America", "N. America", "Oceania"]
    })

    # Interactive bar chart
    fig = px.bar(countries, x="country", y="gdp_trillion",
                 color="continent",
                 title="GDP by Country (Trillion USD)",
                 labels={"gdp_trillion": "GDP (Trillion $)",
                          "country": "Country"})
    chart_path = os.path.join(output_dir, "08_plotly_bar.html")
    fig.write_html(chart_path)
    print(f"Saved: {chart_path}")

    # Interactive scatter
    fig = px.scatter(countries, x="population_m", y="gdp_trillion",
                     size="gdp_trillion", color="continent",
                     hover_name="country",
                     title="Population vs GDP",
                     labels={"population_m": "Population (Millions)",
                              "gdp_trillion": "GDP (Trillion $)"})
    chart_path = os.path.join(output_dir, "08_plotly_scatter.html")
    fig.write_html(chart_path)
    print(f"Saved: {chart_path}")
    print("(Open the HTML files in a browser for interactive charts!)")


# ============================================================
# 9. CHOOSING THE RIGHT CHART
# ============================================================
print("\n" + "=" * 60)
print("CHOOSING THE RIGHT CHART")
print("=" * 60)
print("""
Quick reference guide — what chart for what question:

  QUESTION                          CHART TYPE
  -------------------------------------------
  How does Y change over time?      Line chart
  Is there a relationship?          Scatter plot
  Compare categories?               Bar chart
  What's the distribution?          Histogram
  Parts of a whole?                 Pie chart (max 5 slices!)
  Compare distributions?            Box plot
  Show correlation matrix?          Heatmap
  Need interactivity?               Plotly!

Pro tips:
  - Always label your axes!
  - Choose colorblind-friendly palettes
  - Less is more — don't over-decorate
  - Title should tell the STORY, not describe the chart type
    Bad:  "Bar Chart of Sales"
    Good: "Q4 Sales Outperformed All Other Quarters"
""")


# ============================================================
# 10. SAVING FIGURES
# ============================================================
print("=" * 60)
print("SAVING FIGURES")
print("=" * 60)
print(f"""
Saving is easy with matplotlib:

  plt.savefig("chart.png")           # PNG (good for web)
  plt.savefig("chart.png", dpi=300)  # High resolution
  plt.savefig("chart.pdf")           # PDF (good for papers)
  plt.savefig("chart.svg")           # SVG (scalable, good for web)

All example charts were saved to: {output_dir}
""")


# ============================================================
# RECAP
# ============================================================
print("=" * 60)
print("CHAPTER 28 RECAP")
print("=" * 60)
print("""
You now have THREE visualization libraries in your toolkit:

1. matplotlib: Full control, foundation for everything
   - plt.plot(), plt.scatter(), plt.bar(), plt.hist(), plt.pie()
   - plt.subplots() for multi-chart layouts
   - Always: plt.title(), plt.xlabel(), plt.ylabel(), plt.legend()

2. seaborn: Statistical charts made beautiful
   - sns.barplot(), sns.boxplot(), sns.heatmap()
   - Works great with Pandas DataFrames

3. plotly: Interactive browser-based charts
   - px.bar(), px.scatter() with hover and zoom
   - Saves as HTML files

Next up: Machine Learning — teaching computers to learn from data!
""")
