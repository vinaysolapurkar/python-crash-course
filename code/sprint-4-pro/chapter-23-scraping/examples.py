"""
Chapter 23: Web Scraping — Teaching Python to Read Websites
=============================================================

Web scraping is extracting data from websites.
Think of it as teaching Python to read a webpage like a human would,
but faster, and without getting distracted by cat videos.

How it works:
  1. requests gets the raw HTML of a webpage
  2. BeautifulSoup parses the HTML (like a translator)
  3. You find the data you want using tags, classes, or CSS selectors

IMPORTANT ETHICS NOTE:
  - Check the website's robots.txt (e.g., example.com/robots.txt)
  - Don't scrape too fast (add delays between requests)
  - Respect Terms of Service
  - Don't scrape personal/private data
  - If they have an API, use that instead!
  - When in doubt, ask permission

Install required packages:
  pip install requests beautifulsoup4

We'll use http://quotes.toscrape.com — a site MADE for practicing scraping!
"""

# ============================================================
# 0. Setup
# ============================================================
try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    print("Install required packages:")
    print("  pip install requests beautifulsoup4")
    exit(1)

import time

# ============================================================
# 1. HTML Basics — What Websites Are Made Of
# ============================================================
print("=" * 50)
print("1. HTML BASICS")
print("=" * 50)
print("""
HTML (HyperText Markup Language) is the structure of every webpage.
Think of it as the skeleton — CSS is the skin, JavaScript is the muscles.

Key concepts:
  <tag>content</tag>           → an HTML element
  <tag class="name">           → class attribute (for styling)
  <tag id="unique">            → id attribute (unique identifier)
  <a href="url">link text</a>  → a hyperlink
  <div>, <span>, <p>           → containers for content
  <h1> to <h6>                 → headings
  <ul><li>item</li></ul>       → lists

Example:
  <div class="quote">
      <span class="text">"Be yourself; everyone else is taken."</span>
      <small class="author">Oscar Wilde</small>
  </div>
""")

# Let's parse some sample HTML first
sample_html = """
<html>
<body>
    <h1>My Favorite Movies</h1>
    <ul class="movie-list">
        <li class="movie" data-year="1994">
            <span class="title">The Shawshank Redemption</span>
            <span class="rating">9.3</span>
        </li>
        <li class="movie" data-year="2008">
            <span class="title">The Dark Knight</span>
            <span class="rating">9.0</span>
        </li>
        <li class="movie" data-year="2010">
            <span class="title">Inception</span>
            <span class="rating">8.8</span>
        </li>
    </ul>
</body>
</html>
"""

# Parse with BeautifulSoup
soup = BeautifulSoup(sample_html, "html.parser")

# Find elements
title = soup.find("h1")
print(f"Page title: {title.text}")

# Find all movies
movies = soup.find_all("li", class_="movie")
print(f"\nFound {len(movies)} movies:")
for movie in movies:
    name = movie.find("span", class_="title").text
    rating = movie.find("span", class_="rating").text
    year = movie.get("data-year")  # get attribute value
    print(f"  {name} ({year}) - Rating: {rating}")


# ============================================================
# 2. Fetching a Real Webpage
# ============================================================
print("\n" + "=" * 50)
print("2. FETCHING A REAL WEBPAGE")
print("=" * 50)

url = "http://quotes.toscrape.com/"
print(f"Fetching: {url}")

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    print(f"Status: {response.status_code}")
    print(f"Content length: {len(response.text):,} characters")

    # Parse the HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # The page title
    print(f"Page title: {soup.title.text}")

except requests.exceptions.ConnectionError:
    print("Can't connect. Check your internet!")
    print("(The rest of this script will use sample data)")
    soup = None
except Exception as e:
    print(f"Error: {e}")
    soup = None


# ============================================================
# 3. Finding Elements — find() and find_all()
# ============================================================
print("\n" + "=" * 50)
print("3. find() and find_all()")
print("=" * 50)

if soup:
    # find() returns the FIRST match
    first_quote = soup.find("div", class_="quote")
    if first_quote:
        text = first_quote.find("span", class_="text").text
        author = first_quote.find("small", class_="author").text
        print(f"First quote:")
        print(f"  {text}")
        print(f"  — {author}")

    # find_all() returns ALL matches
    all_quotes = soup.find_all("div", class_="quote")
    print(f"\nAll quotes on page 1 ({len(all_quotes)} total):")
    for i, quote in enumerate(all_quotes, 1):
        text = quote.find("span", class_="text").text
        author = quote.find("small", class_="author").text
        tags = [tag.text for tag in quote.find_all("a", class_="tag")]
        print(f"\n  {i}. {text[:80]}...")
        print(f"     — {author}")
        print(f"     Tags: {', '.join(tags)}")
else:
    print("(Skipping — couldn't fetch the page)")


# ============================================================
# 4. CSS Selectors — A More Powerful Way to Find Elements
# ============================================================
print("\n" + "=" * 50)
print("4. CSS SELECTORS")
print("=" * 50)
print("""
CSS selectors are like GPS coordinates for HTML elements:

  soup.select("tag")          → find all <tag> elements
  soup.select(".class")       → find elements with class="class"
  soup.select("#id")          → find element with id="id"
  soup.select("div.quote")    → <div class="quote">
  soup.select("div > span")   → <span> directly inside <div>
  soup.select("a[href]")      → <a> tags that have an href attribute
""")

if soup:
    # Select using CSS selectors
    quotes = soup.select("div.quote")
    print(f"Found {len(quotes)} quotes using CSS selector 'div.quote'")

    # Get all authors using CSS selector
    authors = soup.select("small.author")
    unique_authors = set(a.text for a in authors)
    print(f"\nUnique authors: {', '.join(sorted(unique_authors))}")

    # Get all tags from the page
    all_tags = soup.select("a.tag")
    unique_tags = set(t.text for t in all_tags)
    print(f"\nAll tags: {', '.join(sorted(unique_tags))}")
else:
    print("(Skipping — couldn't fetch the page)")


# ============================================================
# 5. Extracting Text and Attributes
# ============================================================
print("\n" + "=" * 50)
print("5. EXTRACTING TEXT AND ATTRIBUTES")
print("=" * 50)

if soup:
    # .text or .get_text() — get the text content
    title = soup.find("h1")
    if title:
        print(f"Title text: {title.text}")

    # .get("attribute") — get an attribute value
    links = soup.find_all("a")
    print(f"\nLinks found: {len(links)}")
    for link in links[:5]:
        href = link.get("href", "no href")
        text = link.text.strip()
        print(f"  '{text}' → {href}")

    # ['attribute'] also works but raises KeyError if missing
    # .get() is safer — returns None if the attribute doesn't exist
else:
    print("(Skipping — couldn't fetch the page)")


# ============================================================
# 6. Handling Pagination — Multiple Pages
# ============================================================
print("\n" + "=" * 50)
print("6. PAGINATION — SCRAPING MULTIPLE PAGES")
print("=" * 50)


def scrape_quotes_page(url):
    """Scrape a single page of quotes. Returns (quotes_list, next_url)."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except Exception as e:
        print(f"  Error fetching {url}: {e}")
        return [], None

    soup = BeautifulSoup(response.text, "html.parser")

    quotes = []
    for quote_div in soup.find_all("div", class_="quote"):
        text = quote_div.find("span", class_="text").text
        author = quote_div.find("small", class_="author").text
        tags = [tag.text for tag in quote_div.find_all("a", class_="tag")]
        quotes.append({
            "text": text,
            "author": author,
            "tags": tags,
        })

    # Find the "Next" button
    next_btn = soup.find("li", class_="next")
    next_url = None
    if next_btn:
        next_link = next_btn.find("a")
        if next_link:
            next_url = "http://quotes.toscrape.com" + next_link.get("href")

    return quotes, next_url


# Scrape first 3 pages (being respectful with a delay!)
all_quotes = []
current_url = "http://quotes.toscrape.com/"
max_pages = 3

print(f"Scraping up to {max_pages} pages...")
try:
    for page_num in range(1, max_pages + 1):
        if current_url is None:
            break

        print(f"  Page {page_num}: {current_url}")
        quotes, next_url = scrape_quotes_page(current_url)
        all_quotes.extend(quotes)
        current_url = next_url

        # Be polite! Don't hammer the server.
        if current_url:
            time.sleep(1)  # wait 1 second between requests

    print(f"\nTotal quotes scraped: {len(all_quotes)}")

    # Analyze the data
    if all_quotes:
        authors = {}
        for q in all_quotes:
            authors[q["author"]] = authors.get(q["author"], 0) + 1

        print("\nMost quoted authors:")
        for author, count in sorted(authors.items(), key=lambda x: -x[1])[:5]:
            print(f"  {author}: {count} quotes")

        # Collect all tags
        all_tags = {}
        for q in all_quotes:
            for tag in q["tags"]:
                all_tags[tag] = all_tags.get(tag, 0) + 1

        print("\nMost common tags:")
        for tag, count in sorted(all_tags.items(), key=lambda x: -x[1])[:5]:
            print(f"  #{tag}: {count}")

except Exception as e:
    print(f"Scraping stopped: {e}")


# ============================================================
# 7. Ethics and Best Practices
# ============================================================
print("\n" + "=" * 50)
print("7. SCRAPING ETHICS")
print("=" * 50)
print("""
The Scraper's Code of Honor:
-----------------------------------------------------------------
1. CHECK robots.txt   → example.com/robots.txt tells you what's allowed
2. ADD DELAYS         → time.sleep(1) between requests (be polite!)
3. IDENTIFY YOURSELF  → Set a User-Agent header
4. RESPECT ToS        → Read the Terms of Service
5. DON'T OVERLOAD     → Limit concurrent requests
6. CACHE RESULTS      → Don't re-scrape what you already have
7. USE APIs FIRST     → If an API exists, use it instead!
8. NO PERSONAL DATA   → Don't scrape emails, phone numbers, etc.

Example of being a good citizen:
  headers = {"User-Agent": "MyBot/1.0 (learning; myemail@example.com)"}
  response = requests.get(url, headers=headers, timeout=10)
  time.sleep(1)  # breathe between requests
-----------------------------------------------------------------
""")


# ============================================================
# Recap
# ============================================================
print("=" * 50)
print("CHAPTER 23 RECAP")
print("=" * 50)
print("""
Web Scraping Cheat Sheet:
-----------------------------------------------------------------
INSTALL:     pip install requests beautifulsoup4

FETCH PAGE:  response = requests.get(url, timeout=10)
PARSE HTML:  soup = BeautifulSoup(response.text, "html.parser")

FIND ELEMENTS:
  soup.find("tag")                  → first match
  soup.find("tag", class_="name")   → first with class
  soup.find("tag", id="name")       → first with id
  soup.find_all("tag")              → all matches

CSS SELECTORS:
  soup.select("div.class")          → all matching divs
  soup.select("#id")                → element with id
  soup.select("div > span")         → direct children

EXTRACT DATA:
  element.text                      → text content
  element.get("href")               → attribute value
  element["class"]                  → attribute (KeyError if missing)

PAGINATION:
  Find the "next" link, follow it, repeat!

ALWAYS:
  - Use time.sleep() between requests
  - Handle errors gracefully
  - Check robots.txt and ToS
  - Use an API if one exists
-----------------------------------------------------------------
""")
