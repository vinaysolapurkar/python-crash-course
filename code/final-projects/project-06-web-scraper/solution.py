"""
=============================================================
  PROJECT 6: WEB SCRAPER & DATA ANALYZER - SOLUTION
=============================================================
  Scrapes quotes from quotes.toscrape.com, analyzes the data
  with pandas, and generates text-based visualizations.

  Dependencies:
    pip install requests beautifulsoup4 pandas

  Run:  python solution.py
=============================================================
"""

try:
    import requests
    from bs4 import BeautifulSoup
    import pandas as pd
except ImportError as e:
    print(f"Missing dependency: {e}")
    print("Run: pip install requests beautifulsoup4 pandas")
    exit(1)


BASE_URL = "https://quotes.toscrape.com"


# ── Scraping Functions ─────────────────────────────────────

def scrape_page(page_number):
    """
    Scrape a single page of quotes.
    Returns a list of dicts with keys: text, author, tags.
    """
    url = f"{BASE_URL}/page/{page_number}/"
    quotes = []

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"  Error fetching page {page_number}: {e}")
        return quotes

    soup = BeautifulSoup(response.text, "html.parser")

    # Each quote lives in a <div class="quote">
    quote_elements = soup.find_all("div", class_="quote")

    for element in quote_elements:
        # The quote text is in <span class="text">
        text_tag = element.find("span", class_="text")
        text = text_tag.get_text() if text_tag else ""

        # Strip the curly quotes that wrap each quote
        text = text.strip("\u201c\u201d")

        # Author is in <small class="author">
        author_tag = element.find("small", class_="author")
        author = author_tag.get_text() if author_tag else "Unknown"

        # Tags are in <a class="tag">
        tag_elements = element.find_all("a", class_="tag")
        tags = [tag.get_text() for tag in tag_elements]

        quotes.append({
            "text": text,
            "author": author,
            "tags": tags,
        })

    return quotes


def scrape_all_pages(max_pages=5):
    """
    Scrape multiple pages of quotes.
    Stops early if we reach a page with no quotes.
    """
    all_quotes = []

    for page_num in range(1, max_pages + 1):
        print(f"  Scraping page {page_num}...", end=" ")
        page_quotes = scrape_page(page_num)

        if not page_quotes:
            print("no quotes found (end of pages)")
            break

        print(f"found {len(page_quotes)} quotes")
        all_quotes.extend(page_quotes)

    return all_quotes


# ── Analysis Functions ─────────────────────────────────────

def text_bar_chart(labels, values, title, max_bar=30):
    """
    Print a horizontal bar chart using block characters.

    labels: list of label strings
    values: list of numeric values
    title: chart title
    max_bar: maximum bar width in characters
    """
    if not values:
        return

    max_val = max(values)
    max_label_len = max(len(str(label)) for label in labels)

    print(f"\n  {title}")
    print(f"  {'─' * (max_label_len + max_bar + 10)}")

    for label, value in zip(labels, values):
        # Scale bar length proportionally
        if max_val > 0:
            bar_len = int(value / max_val * max_bar)
        else:
            bar_len = 0

        bar = "█" * bar_len
        print(f"  {label:<{max_label_len}}  {bar} {value}")

    print()


def analyze_authors(df):
    """Show the most prolific authors."""
    author_counts = df["author"].value_counts().head(10)

    text_bar_chart(
        labels=author_counts.index.tolist(),
        values=author_counts.values.tolist(),
        title="TOP 10 MOST QUOTED AUTHORS",
    )

    return author_counts


def analyze_tags(df):
    """Show the most common tags across all quotes."""
    # Explode the tags list so each tag gets its own row
    all_tags = df["tags"].explode()
    tag_counts = all_tags.value_counts().head(10)

    text_bar_chart(
        labels=tag_counts.index.tolist(),
        values=tag_counts.values.tolist(),
        title="TOP 10 MOST COMMON TAGS",
    )

    return tag_counts


def analyze_quote_lengths(df):
    """Find the longest and shortest quotes."""
    df["length"] = df["text"].str.len()

    longest_idx = df["length"].idxmax()
    shortest_idx = df["length"].idxmin()

    longest = df.loc[longest_idx]
    shortest = df.loc[shortest_idx]

    print("  QUOTE LENGTH ANALYSIS")
    print("  " + "─" * 50)

    print(f"\n  Longest quote ({longest['length']} chars):")
    # Truncate if super long
    display_text = longest["text"][:100] + "..." if len(longest["text"]) > 100 else longest["text"]
    print(f'  "{display_text}"')
    print(f"  - {longest['author']}")

    print(f"\n  Shortest quote ({shortest['length']} chars):")
    print(f'  "{shortest["text"]}"')
    print(f"  - {shortest['author']}")

    print(f"\n  Average quote length: {df['length'].mean():.0f} characters")
    print()


def save_to_csv(df, filename="quotes_data.csv"):
    """Save the DataFrame to a CSV file."""
    # Convert tags list to a semicolon-separated string for CSV
    df_copy = df.copy()
    df_copy["tags"] = df_copy["tags"].apply(lambda x: "; ".join(x))

    df_copy.to_csv(filename, index=False, encoding="utf-8")
    print(f"  Data saved to {filename}")


# ── Main ───────────────────────────────────────────────────

def main():
    """Scrape, analyze, visualize, and save!"""
    print()
    print("=" * 50)
    print("  WEB SCRAPER & DATA ANALYZER")
    print("  Source: quotes.toscrape.com")
    print("=" * 50)
    print()

    # Step 1: Scrape
    print("  SCRAPING QUOTES...")
    print("  " + "─" * 40)
    quotes = scrape_all_pages(max_pages=5)

    if not quotes:
        print("\n  No quotes scraped. Check your internet connection.")
        return

    print(f"\n  Total quotes scraped: {len(quotes)}")
    print(f"  Unique authors: {len(set(q['author'] for q in quotes))}")

    # Step 2: Create DataFrame
    df = pd.DataFrame(quotes)

    # Step 3: Analyze
    print()
    print("=" * 50)
    print("  ANALYSIS RESULTS")
    print("=" * 50)

    analyze_authors(df)
    analyze_tags(df)
    analyze_quote_lengths(df)

    # Step 4: Save to CSV
    print("  " + "─" * 40)
    save_to_csv(df)

    print()
    print("=" * 50)
    print("  Done! Check quotes_data.csv for the full dataset.")
    print("=" * 50)


if __name__ == "__main__":
    main()
