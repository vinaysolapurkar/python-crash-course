"""
=============================================================
  PROJECT 6: WEB SCRAPER & DATA ANALYZER
=============================================================

Build a web scraper that collects data from a website and
then analyzes it! We'll scrape quotes from the practice
site quotes.toscrape.com (it's made for learning scraping).

WHAT YOU'LL PRACTICE:
  - Web scraping with BeautifulSoup
  - Pagination (scraping multiple pages)
  - Data storage with pandas DataFrames
  - Data analysis and aggregation
  - CSV file export
  - Text-based data visualization

DEPENDENCIES:
  pip install requests beautifulsoup4 pandas

REQUIREMENTS:
  1. Scrape quotes from quotes.toscrape.com
     (at least 3 pages)
  2. Extract: quote text, author, tags
  3. Store in a pandas DataFrame
  4. Analysis:
     - Most quoted authors (top 10)
     - Most common tags (top 10)
     - Longest and shortest quotes
  5. Save scraped data to CSV
  6. Generate text-based bar charts of results

TARGET WEBSITE:
  https://quotes.toscrape.com/
  Each page has ~10 quotes with author and tags.
  Pagination: /page/1/, /page/2/, etc.

EXAMPLE OUTPUT:
  Scraping page 1... found 10 quotes
  Scraping page 2... found 10 quotes
  ...
  Total quotes scraped: 50

  TOP 10 AUTHORS:
  Albert Einstein    ████████████ 5
  J.K. Rowling       ████████     4
  Steve Martin       ██████       3
  ...

  MOST COMMON TAGS:
  love               ████████████████ 14
  inspirational      ████████████     10
  life               ██████████       8
  ...

  Data saved to quotes_data.csv

HINTS:
  - Use requests.get(url) to fetch pages
  - BeautifulSoup(html, 'html.parser') to parse
  - Quotes are in <div class="quote"> elements
  - Author is in <small class="author">
  - Tags are in <a class="tag">
  - Use pd.DataFrame(list_of_dicts) to create DataFrame
  - df.groupby('author').size() for counting

Good luck!
=============================================================
"""

import csv

# You'll need to install these:
# pip install requests beautifulsoup4 pandas
try:
    import requests
    from bs4 import BeautifulSoup
    import pandas as pd
except ImportError as e:
    print(f"Missing dependency: {e}")
    print("Run: pip install requests beautifulsoup4 pandas")
    exit(1)


BASE_URL = "https://quotes.toscrape.com"


def scrape_page(page_number):
    """Scrape a single page and return a list of quote dicts."""
    # TODO: Build URL for the page
    # TODO: Fetch the page with requests
    # TODO: Parse with BeautifulSoup
    # TODO: Find all quote elements
    # TODO: Extract text, author, tags from each
    # TODO: Return list of dicts
    pass


def scrape_all_pages(max_pages=5):
    """Scrape multiple pages and return all quotes."""
    # TODO: Loop through pages
    # TODO: Stop if a page has no quotes (end of pages)
    # TODO: Return combined list of all quotes
    pass


def analyze_authors(df):
    """Find and display the most quoted authors."""
    # TODO: Group by author, count quotes
    # TODO: Show top 10 with a bar chart
    pass


def analyze_tags(df):
    """Find and display the most common tags."""
    # TODO: Explode tags column (if stored as lists)
    # TODO: Count tag frequencies
    # TODO: Show top 10 with a bar chart
    pass


def text_bar_chart(data, title, max_bar_length=30):
    """Display a horizontal text-based bar chart."""
    # TODO: Print title
    # TODO: Calculate bar lengths proportionally
    # TODO: Print each bar with label and count
    pass


def save_to_csv(df, filename="quotes_data.csv"):
    """Save the DataFrame to a CSV file."""
    # TODO: Use df.to_csv()
    pass


def main():
    """Scrape, analyze, and save."""
    # TODO: Scrape quotes
    # TODO: Create DataFrame
    # TODO: Run analyses
    # TODO: Save to CSV
    pass


if __name__ == "__main__":
    main()
