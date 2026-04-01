"""
Chapter 23 Exercise: Quote Scraper
====================================

Scrape quotes from http://quotes.toscrape.com and display them nicely!

Requirements:

1. Scrape quotes from at least the first 3 pages
2. Store each quote as a dict: {"text": ..., "author": ..., "tags": [...]}
3. Display all quotes in a nice format
4. Show statistics:
   - Total quotes scraped
   - Number of unique authors
   - Most quoted author
   - Most common tags

Bonus:
   - Save quotes to a JSON file
   - Filter quotes by tag (let user pick a tag)
   - Search quotes by keyword

Starter code below:
"""

import requests
from bs4 import BeautifulSoup
import time
import json


def scrape_page(url):
    """
    Scrape a single page of quotes.

    Args:
        url: The URL to scrape

    Returns:
        tuple: (list of quote dicts, next page URL or None)
    """
    # TODO: Fetch the page
    # TODO: Parse with BeautifulSoup
    # TODO: Find all quote divs
    # TODO: Extract text, author, tags from each
    # TODO: Find the "Next" button URL
    # TODO: Return (quotes_list, next_url)
    pass


def scrape_all_quotes(max_pages=5):
    """
    Scrape multiple pages of quotes.

    Args:
        max_pages: Maximum number of pages to scrape

    Returns:
        list of quote dicts
    """
    # TODO: Start at page 1
    # TODO: Loop through pages, calling scrape_page()
    # TODO: Be polite — add time.sleep(1) between requests!
    # TODO: Stop when no next page or max_pages reached
    pass


def display_quotes(quotes):
    """Display all quotes in a nice format."""
    # TODO: Loop through quotes and print them nicely
    pass


def show_statistics(quotes):
    """Show interesting statistics about the scraped quotes."""
    # TODO: Total quotes, unique authors, most quoted author, top tags
    pass


def save_to_json(quotes, filename="quotes.json"):
    """Save quotes to a JSON file."""
    # TODO: Use json.dump() to save quotes
    pass


def search_quotes(quotes, keyword):
    """Search quotes containing a keyword."""
    # TODO: Filter quotes where keyword is in text or author
    pass


def filter_by_tag(quotes, tag):
    """Filter quotes by a specific tag."""
    # TODO: Filter quotes where tag is in the tags list
    pass


def main():
    """Main function."""
    print("=" * 40)
    print("  QUOTE SCRAPER")
    print("  Source: quotes.toscrape.com")
    print("=" * 40)

    # TODO: Scrape quotes
    # TODO: Display them
    # TODO: Show statistics
    # TODO: Menu for search/filter/save
    pass


if __name__ == "__main__":
    main()
