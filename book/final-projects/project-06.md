# Project 6: Web Scraper & Data Analyzer

> **Difficulty:** 3/5 | **Time:** ~2.5 hours | **Skills:** BeautifulSoup, pandas, data analysis
> **Code:** https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/final-projects/project-06-web-scraper/

## What You'll Build

A web scraper that collects quotes from quotes.toscrape.com (a site built specifically for practicing scraping), stores the data in a structured format, and then analyzes it -- finding the most prolific authors, the most popular tags, and generating text-based visualizations.

Here's what the output looks like:

```
=== WEB SCRAPER & DATA ANALYZER ===

Scraping page 1... found 10 quotes
Scraping page 2... found 10 quotes
...
Scraping page 10... found 10 quotes

Total quotes collected: 100

--- Analysis Menu ---
1. Top Authors
2. Tag Analysis
3. Longest/Shortest Quotes
4. Search Quotes
5. Export to CSV
6. Exit

Choice: 1

--- Top 10 Authors ---
  Albert Einstein      ################  10 quotes
  J.K. Rowling         ############      6 quotes
  Steve Martin         ######            3 quotes
  ...
```

## Skills You'll Use

- Web scraping with BeautifulSoup (learned in Chapter 13)
- Data structures (lists, dicts) (learned in Chapter 4)
- File I/O and CSV (learned in Chapter 7)
- String manipulation (learned in Chapter 2)
- Functions and program design (learned in Chapter 5)
- List comprehensions (learned in Chapter 4)

## Step-by-Step Build Guide

### Step 1: Install Dependencies and Set Up

First, install the required library. BeautifulSoup is the go-to Python library for parsing HTML.

```bash
pip install beautifulsoup4
```

Now set up the project file:

```python
# web_scraper.py

import csv
import json
from urllib.request import urlopen, Request
from urllib.error import URLError
from collections import Counter

try:
    from bs4 import BeautifulSoup
except ImportError:
    print("Please install beautifulsoup4: pip install beautifulsoup4")
    exit(1)

BASE_URL = "https://quotes.toscrape.com"
```

### Step 2: Build the Scraper

This function scrapes one page at a time, extracting the quote text, author, and tags. We then loop through all pages.

```python
def scrape_page(url):
    """Scrape a single page and return a list of quote dictionaries."""
    quotes = []

    try:
        request = Request(url, headers={"User-Agent": "Python-Scraper-Project"})
        with urlopen(request, timeout=10) as response:
            html = response.read().decode()
    except URLError as e:
        print(f"  Error fetching {url}: {e}")
        return quotes, None

    soup = BeautifulSoup(html, "html.parser")

    # Each quote is in a div with class "quote"
    for quote_div in soup.find_all("div", class_="quote"):
        text_span = quote_div.find("span", class_="text")
        author_span = quote_div.find("small", class_="author")
        tag_elements = quote_div.find_all("a", class_="tag")

        if text_span and author_span:
            quote = {
                "text": text_span.get_text().strip("\u201c\u201d"),
                "author": author_span.get_text(),
                "tags": [tag.get_text() for tag in tag_elements]
            }
            quotes.append(quote)

    # Check if there's a next page
    next_btn = soup.find("li", class_="next")
    next_url = None
    if next_btn:
        next_link = next_btn.find("a")
        if next_link:
            next_url = BASE_URL + next_link["href"]

    return quotes, next_url


def scrape_all_quotes():
    """Scrape all pages and return the complete list of quotes."""
    all_quotes = []
    url = BASE_URL
    page = 1

    while url:
        print(f"  Scraping page {page}...", end=" ")
        quotes, next_url = scrape_page(url)
        print(f"found {len(quotes)} quotes")

        all_quotes.extend(quotes)
        url = next_url
        page += 1

    print(f"\n  Total quotes collected: {len(all_quotes)}")
    return all_quotes
```

### Step 3: Build the Analysis Functions

Now the fun part -- turning raw data into insights. We'll analyze authors, tags, and quote characteristics.

```python
def analyze_top_authors(quotes, limit=10):
    """Find and display the most quoted authors."""
    author_counts = Counter(q["author"] for q in quotes)
    top = author_counts.most_common(limit)

    print(f"\n--- Top {limit} Authors ---")
    if not top:
        print("  No data to analyze.")
        return

    max_count = top[0][1]
    for author, count in top:
        bar_length = int((count / max_count) * 20)
        bar = "#" * bar_length
        print(f"  {author:<25}{bar:<22}{count} quotes")

    return author_counts


def analyze_tags(quotes, limit=15):
    """Analyze and display the most popular tags."""
    all_tags = []
    for q in quotes:
        all_tags.extend(q["tags"])

    tag_counts = Counter(all_tags)
    top = tag_counts.most_common(limit)

    print(f"\n--- Top {limit} Tags ---")
    if not top:
        print("  No tags found.")
        return

    max_count = top[0][1]
    for tag, count in top:
        bar_length = int((count / max_count) * 20)
        bar = "#" * bar_length
        print(f"  {tag:<20}{bar:<22}{count}")

    # Tag cloud style display
    print("\n  Tag cloud (by frequency):")
    cloud_tags = tag_counts.most_common(20)
    line = "  "
    for tag, count in cloud_tags:
        entry = f"[{tag}:{count}] "
        if len(line) + len(entry) > 70:
            print(line)
            line = "  "
        line += entry
    if line.strip():
        print(line)

    return tag_counts


def analyze_quote_lengths(quotes):
    """Analyze quote lengths and show extremes."""
    if not quotes:
        print("  No quotes to analyze.")
        return

    lengths = [(len(q["text"]), q) for q in quotes]
    lengths.sort(key=lambda x: x[0])

    avg_length = sum(l for l, _ in lengths) / len(lengths)

    print("\n--- Quote Length Analysis ---")
    print(f"  Total quotes: {len(quotes)}")
    print(f"  Average length: {avg_length:.0f} characters")
    print(f"  Shortest: {lengths[0][0]} characters")
    print(f"  Longest: {lengths[-1][0]} characters")

    # Distribution
    short = sum(1 for l, _ in lengths if l < 50)
    medium = sum(1 for l, _ in lengths if 50 <= l < 150)
    long_q = sum(1 for l, _ in lengths if l >= 150)

    print(f"\n  Distribution:")
    print(f"    Short  (<50 chars):  {'#' * short} ({short})")
    print(f"    Medium (50-150):     {'#' * medium} ({medium})")
    print(f"    Long   (>150):       {'#' * long_q} ({long_q})")

    print(f"\n  Shortest quote:")
    print(f'    "{lengths[0][1]["text"][:80]}..."')
    print(f'    -- {lengths[0][1]["author"]}')

    print(f"\n  Longest quote:")
    text = lengths[-1][1]["text"]
    preview = text[:100] + "..." if len(text) > 100 else text
    print(f'    "{preview}"')
    print(f'    -- {lengths[-1][1]["author"]}')
```

### Step 4: Add Search and Export

```python
def search_quotes(quotes):
    """Search quotes by keyword, author, or tag."""
    print("\n--- Search Quotes ---")
    print("  Search by: 1=Keyword  2=Author  3=Tag")
    search_type = input("  Choice: ").strip()

    query = input("  Search term: ").strip().lower()
    if not query:
        print("  No search term entered.")
        return

    results = []
    if search_type == "1":
        results = [q for q in quotes if query in q["text"].lower()]
    elif search_type == "2":
        results = [q for q in quotes if query in q["author"].lower()]
    elif search_type == "3":
        results = [q for q in quotes
                   if any(query in tag.lower() for tag in q["tags"])]
    else:
        results = [q for q in quotes
                   if query in q["text"].lower()
                   or query in q["author"].lower()]

    print(f"\n  Found {len(results)} result(s):")
    for i, q in enumerate(results[:10], 1):
        text = q["text"][:80] + "..." if len(q["text"]) > 80 else q["text"]
        print(f'\n  {i}. "{text}"')
        print(f'     -- {q["author"]}')
        if q["tags"]:
            print(f'     Tags: {", ".join(q["tags"])}')

    if len(results) > 10:
        print(f"\n  ... and {len(results) - 10} more.")


def export_to_csv(quotes):
    """Export all quotes to a CSV file."""
    filename = "quotes_data.csv"

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Author", "Quote", "Tags", "Length"])

        for q in quotes:
            writer.writerow([
                q["author"],
                q["text"],
                "; ".join(q["tags"]),
                len(q["text"])
            ])

    print(f"\n  Exported {len(quotes)} quotes to {filename}")

    # Also save as JSON for good measure
    json_file = "quotes_data.json"
    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(quotes, f, indent=2, ensure_ascii=False)

    print(f"  Also saved to {json_file}")
```

### Step 5: Wire Up the Main Application

```python
def main():
    """Main application."""
    print("=" * 40)
    print("  WEB SCRAPER & DATA ANALYZER")
    print("=" * 40)
    print("\nScraping quotes from quotes.toscrape.com...")

    quotes = scrape_all_quotes()

    if not quotes:
        print("No quotes collected. Check your internet connection.")
        return

    while True:
        print("\n--- Analysis Menu ---")
        print("1. Top Authors")
        print("2. Tag Analysis")
        print("3. Quote Length Analysis")
        print("4. Search Quotes")
        print("5. Export to CSV")
        print("6. Exit")

        choice = input("\nChoice: ").strip()

        if choice == "1":
            analyze_top_authors(quotes)
        elif choice == "2":
            analyze_tags(quotes)
        elif choice == "3":
            analyze_quote_lengths(quotes)
        elif choice == "4":
            search_quotes(quotes)
        elif choice == "5":
            export_to_csv(quotes)
        elif choice == "6":
            print("\nHappy analyzing!")
            break
        else:
            print("Invalid choice. Please enter 1-6.")


if __name__ == "__main__":
    main()
```

## Challenges (Level Up!)

1. **Scrape author details:** Each author name on the site links to a bio page. Follow those links and scrape the author's birth date, birthplace, and description. Add an "Author Profile" option to your menu.

2. **Visualization upgrade:** Use the `matplotlib` library to generate actual bar charts and pie charts of your data. Save them as PNG files. This is a great preview of data science skills.

3. **Scheduled scraping:** Use Python's `schedule` or `time` module to re-scrape daily and track how the site changes. Store snapshots with timestamps and show a diff between runs.

## Portfolio Tips

This project combines web scraping, data analysis, and data export -- skills that data science and backend employers look for. When presenting it:

- **GitHub:** Include sample output files (CSV, JSON) and screenshots of the analysis. Note that you scrape a practice site designed for this purpose (shows ethical awareness).
- **Resume:** "Built a web scraper using BeautifulSoup to collect and analyze 100+ data points, with statistical analysis, search, and CSV/JSON export capabilities."
- **Interview talking point:** Discuss the ethics of web scraping (robots.txt, rate limiting, terms of service). Explain how you structured the data for analysis and why you chose Counter for aggregation. Mention how this pattern could scale to scrape job boards, product prices, or news sites.
