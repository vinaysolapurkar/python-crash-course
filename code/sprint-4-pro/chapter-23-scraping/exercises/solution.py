"""
Chapter 23 Exercise SOLUTION: Quote Scraper
=============================================
Scraping wisdom from the internet, one quote at a time.
Because who doesn't need more inspirational quotes in their life?

Run it: python solution.py
"""

import requests
from bs4 import BeautifulSoup
import time
import json
import os

BASE_URL = "http://quotes.toscrape.com"


def scrape_page(url):
    """
    Scrape a single page of quotes.
    Returns (list of quote dicts, next page URL or None).
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.exceptions.ConnectionError:
        print("  Cannot connect. Check your internet!")
        return [], None
    except Exception as e:
        print(f"  Error: {e}")
        return [], None

    soup = BeautifulSoup(response.text, "html.parser")
    quotes = []

    for quote_div in soup.find_all("div", class_="quote"):
        text_elem = quote_div.find("span", class_="text")
        author_elem = quote_div.find("small", class_="author")
        tag_elems = quote_div.find_all("a", class_="tag")

        if text_elem and author_elem:
            quotes.append({
                "text": text_elem.text.strip("\u201c\u201d"),  # remove curly quotes
                "author": author_elem.text,
                "tags": [t.text for t in tag_elems],
            })

    # Find next page
    next_btn = soup.find("li", class_="next")
    next_url = None
    if next_btn:
        link = next_btn.find("a")
        if link and link.get("href"):
            next_url = BASE_URL + link["href"]

    return quotes, next_url


def scrape_all_quotes(max_pages=10):
    """Scrape multiple pages of quotes."""
    all_quotes = []
    current_url = BASE_URL + "/"

    for page_num in range(1, max_pages + 1):
        if current_url is None:
            print(f"  No more pages! Stopped at page {page_num - 1}.")
            break

        print(f"  Scraping page {page_num}...")
        quotes, next_url = scrape_page(current_url)

        if not quotes:
            print(f"  No quotes found on page {page_num}. Stopping.")
            break

        all_quotes.extend(quotes)
        current_url = next_url

        # Be a good internet citizen
        if current_url:
            time.sleep(1)

    return all_quotes


def display_quotes(quotes, limit=None):
    """Display quotes in a nice format."""
    display = quotes[:limit] if limit else quotes

    for i, q in enumerate(display, 1):
        tags = ", ".join(f"#{t}" for t in q["tags"])
        print(f"\n  {i}. {q['text']}")
        print(f"     -- {q['author']}")
        if tags:
            print(f"     [{tags}]")

    if limit and len(quotes) > limit:
        print(f"\n  ... and {len(quotes) - limit} more quotes")


def show_statistics(quotes):
    """Show interesting statistics about scraped quotes."""
    print(f"\n  {'=' * 45}")
    print(f"  STATISTICS")
    print(f"  {'=' * 45}")

    # Total quotes
    print(f"  Total quotes: {len(quotes)}")

    # Unique authors
    authors = {}
    for q in quotes:
        authors[q["author"]] = authors.get(q["author"], 0) + 1

    print(f"  Unique authors: {len(authors)}")

    # Most quoted authors
    print(f"\n  Top 5 Most Quoted Authors:")
    for author, count in sorted(authors.items(), key=lambda x: -x[1])[:5]:
        bar = "#" * count
        print(f"    {author:<30} {count:>3} {bar}")

    # Tag statistics
    all_tags = {}
    for q in quotes:
        for tag in q["tags"]:
            all_tags[tag] = all_tags.get(tag, 0) + 1

    print(f"\n  Top 10 Tags:")
    for tag, count in sorted(all_tags.items(), key=lambda x: -x[1])[:10]:
        bar = "#" * count
        print(f"    #{tag:<20} {count:>3} {bar}")

    # Average tags per quote
    total_tags = sum(len(q["tags"]) for q in quotes)
    avg_tags = total_tags / len(quotes) if quotes else 0
    print(f"\n  Average tags per quote: {avg_tags:.1f}")

    # Longest and shortest quotes
    if quotes:
        longest = max(quotes, key=lambda q: len(q["text"]))
        shortest = min(quotes, key=lambda q: len(q["text"]))
        print(f"\n  Longest quote: {len(longest['text'])} chars by {longest['author']}")
        print(f"  Shortest quote: {len(shortest['text'])} chars by {shortest['author']}")

    print(f"  {'=' * 45}")


def save_to_json(quotes, filename="scraped_quotes.json"):
    """Save quotes to a JSON file."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(quotes, f, indent=2, ensure_ascii=False)
    print(f"  Saved {len(quotes)} quotes to '{filename}'")


def search_quotes(quotes, keyword):
    """Search quotes by keyword (in text or author)."""
    keyword_lower = keyword.lower()
    results = [
        q for q in quotes
        if keyword_lower in q["text"].lower() or keyword_lower in q["author"].lower()
    ]
    return results


def filter_by_tag(quotes, tag):
    """Filter quotes by a specific tag."""
    tag_lower = tag.lower()
    return [q for q in quotes if tag_lower in [t.lower() for t in q["tags"]]]


def get_all_tags(quotes):
    """Get all unique tags from quotes."""
    tags = set()
    for q in quotes:
        tags.update(q["tags"])
    return sorted(tags)


def main():
    """Main function with menu."""
    print("=" * 45)
    print("  QUOTE SCRAPER")
    print("  Source: quotes.toscrape.com")
    print("  (A scraping practice site)")
    print("=" * 45)

    # Check for cached data
    cache_file = "scraped_quotes.json"
    quotes = []

    if os.path.exists(cache_file):
        use_cache = input("\n  Found cached quotes. Use them? (y/n): ").strip().lower()
        if use_cache == "y":
            with open(cache_file, "r", encoding="utf-8") as f:
                quotes = json.load(f)
            print(f"  Loaded {len(quotes)} quotes from cache!")

    if not quotes:
        pages = input("\n  How many pages to scrape? (default 5): ").strip()
        max_pages = int(pages) if pages.isdigit() else 5

        print(f"\n  Scraping up to {max_pages} pages...")
        print("  (Adding 1-second delays between pages to be polite)\n")
        quotes = scrape_all_quotes(max_pages)

        if quotes:
            print(f"\n  Scraped {len(quotes)} quotes!")
            save_to_json(quotes, cache_file)
        else:
            print("\n  No quotes scraped. Check your internet connection!")
            return

    # Menu
    while True:
        print(f"\n{'=' * 40}")
        print(f"  QUOTE SCRAPER MENU ({len(quotes)} quotes loaded)")
        print(f"{'=' * 40}")
        print("  1. View all quotes")
        print("  2. View first 10 quotes")
        print("  3. Statistics")
        print("  4. Search by keyword")
        print("  5. Filter by tag")
        print("  6. Random quote")
        print("  7. Save to JSON")
        print("  8. Re-scrape")
        print("  0. Quit")
        print(f"{'=' * 40}")

        choice = input("\n  Choose: ").strip()

        if choice == "1":
            display_quotes(quotes)

        elif choice == "2":
            display_quotes(quotes, limit=10)

        elif choice == "3":
            show_statistics(quotes)

        elif choice == "4":
            keyword = input("  Search term: ").strip()
            if keyword:
                results = search_quotes(quotes, keyword)
                if results:
                    print(f"\n  Found {len(results)} quotes matching '{keyword}':")
                    display_quotes(results)
                else:
                    print(f"  No quotes matching '{keyword}'.")

        elif choice == "5":
            tags = get_all_tags(quotes)
            print(f"\n  Available tags ({len(tags)}):")
            print(f"  {', '.join(tags)}")
            tag = input("\n  Filter by tag: ").strip()
            if tag:
                results = filter_by_tag(quotes, tag)
                if results:
                    print(f"\n  Found {len(results)} quotes with tag '#{tag}':")
                    display_quotes(results)
                else:
                    print(f"  No quotes with tag '#{tag}'.")

        elif choice == "6":
            import random
            q = random.choice(quotes)
            print(f"\n  Random Quote:")
            print(f"  {q['text']}")
            print(f"  -- {q['author']}")

        elif choice == "7":
            filename = input("  Filename (default: scraped_quotes.json): ").strip()
            save_to_json(quotes, filename or "scraped_quotes.json")

        elif choice == "8":
            pages = input("  How many pages? (default 5): ").strip()
            max_pages = int(pages) if pages.isdigit() else 5
            print(f"\n  Re-scraping {max_pages} pages...")
            quotes = scrape_all_quotes(max_pages)
            if quotes:
                print(f"  Scraped {len(quotes)} quotes!")
                save_to_json(quotes, cache_file)

        elif choice == "0":
            print("\n  Stay inspired! Goodbye!")
            break

        else:
            print("  Invalid option!")


if __name__ == "__main__":
    main()
