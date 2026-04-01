# Chapter 23: Web Scraping - Extracting Data from the Web

> **Sprint 4, Chapter 23** | **Estimated Time: 20-25 minutes** | **Difficulty: Advanced**

## Why Should I Care?

Not everything has a nice, clean API. Sometimes the data you want is on a website but there's no API to access it. Price comparisons, news headlines, research data, job listings, product reviews, sports statistics - the data is right there on the page. You just need a way to grab it.

That's web scraping. And Python is ridiculously good at it.

Price monitoring tools that alert you when something goes on sale? Scrapers. Those "best flights" comparison sites? Scrapers. Academic researchers collecting data from hundreds of sources? Scrapers. Your future job listing dashboard project at the end of this sprint? Scraper.

## The Newspaper Analogy

APIs are like **politely asking for data**. You call the restaurant, place your order, and they deliver. Web scraping is like **reading the newspaper yourself and taking notes**. The information is published and public - you're just reading it programmatically instead of with your eyes.

Your Python script visits a web page (just like your browser does), reads the HTML (just like your browser does), and extracts the specific pieces you care about (which your browser shows visually, but you grab as data).

## HTML Basics: Just Enough to Scrape

You don't need to learn HTML deeply. You just need to understand enough to tell Python what to look for. Here's the crash course:

```html
<html>
  <head>
    <title>My Page</title>
  </head>
  <body>
    <h1>Welcome</h1>
    <p class="intro">This is a paragraph.</p>
    <div id="content">
      <a href="https://example.com">Click here</a>
      <ul>
        <li>Item 1</li>
        <li>Item 2</li>
        <li>Item 3</li>
      </ul>
    </div>
  </body>
</html>
```

The key concepts:
- **Tags** come in pairs: `<p>text</p>` (opening and closing)
- **Attributes** add info to tags: `<p class="intro">` has a `class` attribute
- **Nesting**: Tags contain other tags, forming a tree
- **id**: A unique identifier (one per page) - `id="content"`
- **class**: A group label (many elements can share one) - `class="intro"`

Common tags you'll encounter:
| Tag | Purpose |
|--|--|
| `<h1>` to `<h6>` | Headings |
| `<p>` | Paragraphs |
| `<a href="...">` | Links |
| `<div>` | Generic container |
| `<span>` | Inline container |
| `<ul>`, `<li>` | Unordered list and items |
| `<table>`, `<tr>`, `<td>` | Tables, rows, cells |
| `<img src="...">` | Images |

> **Don't Panic:** You don't need to learn HTML deeply. Just enough to tell Python what to look for. If you can read the five-line example above, you know enough to start scraping.

## The Workflow: requests + BeautifulSoup

Web scraping in Python uses two libraries:
1. **requests** - downloads the web page (you learned this in Chapter 21)
2. **BeautifulSoup** - parses the HTML and lets you search through it

Install BeautifulSoup:

```bash
pip install beautifulsoup4
```

Here's the basic pattern - you'll use this every single time:

```python
import requests
from bs4 import BeautifulSoup

# Step 1: Download the page
url = "https://quotes.toscrape.com/"
response = requests.get(url)

# Step 2: Parse the HTML
soup = BeautifulSoup(response.text, "html.parser")

# Step 3: Find what you want
title = soup.find("title")
print(title.text)  # Quotes to Scrape
```

Three steps. Download, parse, find. That's the entire workflow.

## Finding Elements: find() and find_all()

`find()` returns the **first** matching element. `find_all()` returns **all** matching elements as a list.

```python
import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Find the first quote
first_quote = soup.find("span", class_="text")
print(first_quote.text)
# "The world as we have created it is a process of our thinking..."

# Find ALL quotes
all_quotes = soup.find_all("span", class_="text")
for quote in all_quotes:
    print(quote.text)

# Find by id
# element = soup.find(id="specific-id")

# Find by multiple attributes
# element = soup.find("div", {"class": "content", "id": "main"})
```

Notice `class_` with an underscore - that's because `class` is a reserved word in Python. BeautifulSoup uses `class_` instead.

## Extracting Text and Attributes

Once you've found an element, you can extract its text content or its attributes:

```python
import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Get the text inside a tag
quote = soup.find("span", class_="text")
print(quote.text)       # The quote text
print(quote.string)     # Same thing for simple elements

# Get an attribute
link = soup.find("a")
print(link["href"])     # The URL the link points to
print(link.get("href")) # Same thing (safer - returns None if missing)

# Get all attributes as a dictionary
print(link.attrs)       # {'href': '/login', 'class': ['...'], ...}
```

## CSS Selectors: The Power Tool

`find()` and `find_all()` are great for simple searches. For more complex searches, use **CSS selectors** with `select()`:

```python
import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Select by class (use a dot)
quotes = soup.select(".text")

# Select by id (use a hash)
# header = soup.select_one("#header")

# Select by tag
paragraphs = soup.select("p")

# Select nested elements (parent > child)
# Authors that are inside quote divs
authors = soup.select(".quote .author")

# Select by attribute
# links = soup.select('a[href^="https"]')  # Links starting with https
```

Common CSS selector patterns:
| Selector | Meaning |
|--|--|
| `tag` | All elements of that type |
| `.class` | All elements with that class |
| `#id` | Element with that id |
| `parent child` | child anywhere inside parent |
| `parent > child` | Direct child only |
| `tag.class` | Tag with that class |

`select()` returns a list (like `find_all`). `select_one()` returns the first match (like `find`).

## A Complete Scraping Example

Let's scrape all quotes from quotes.toscrape.com with their authors and tags:

```python
import requests
from bs4 import BeautifulSoup

def scrape_quotes(url):
    """Scrape quotes from a page."""
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    
    soup = BeautifulSoup(response.text, "html.parser")
    quotes = []
    
    for quote_div in soup.find_all("div", class_="quote"):
        text = quote_div.find("span", class_="text").text
        author = quote_div.find("small", class_="author").text
        tags = [tag.text for tag in quote_div.find_all("a", class_="tag")]
        
        quotes.append({
            "text": text,
            "author": author,
            "tags": tags
        })
    
    return quotes

# Scrape page 1
quotes = scrape_quotes("https://quotes.toscrape.com/")
for q in quotes:
    print(f'"{q["text"][:60]}..."')
    print(f'  - {q["author"]}')
    print(f'  Tags: {", ".join(q["tags"])}')
    print()
```

## Handling Pagination

Most websites spread content across multiple pages. Here's how to scrape all of them:

```python
import requests
from bs4 import BeautifulSoup
import time

def scrape_all_quotes():
    """Scrape quotes from ALL pages."""
    base_url = "https://quotes.toscrape.com"
    all_quotes = []
    page_url = base_url + "/"
    
    while page_url:
        print(f"Scraping: {page_url}")
        response = requests.get(page_url, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Scrape quotes on this page
        for quote_div in soup.find_all("div", class_="quote"):
            text = quote_div.find("span", class_="text").text
            author = quote_div.find("small", class_="author").text
            all_quotes.append({"text": text, "author": author})
        
        # Find the "next" button
        next_button = soup.find("li", class_="next")
        if next_button:
            next_link = next_button.find("a")["href"]
            page_url = base_url + next_link
        else:
            page_url = None  # No more pages
        
        time.sleep(1)  # Be polite - wait between requests
    
    return all_quotes

all_quotes = scrape_all_quotes()
print(f"\nTotal quotes scraped: {len(all_quotes)}")
```

Key points:
- Look for a "next" link on each page
- Build the full URL by combining the base URL with the relative link
- **Always add a delay** (`time.sleep(1)`) between requests - hammering a server with rapid requests is rude and might get you blocked

## Saving Scraped Data

Once you've scraped the data, save it. Here are two approaches:

```python
import json
import csv

# Save as JSON
def save_as_json(data, filename):
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Saved {len(data)} items to {filename}")

# Save as CSV
def save_as_csv(data, filename):
    if not data:
        return
    
    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
    print(f"Saved {len(data)} items to {filename}")

# Or save to SQLite (Chapter 22!)
import sqlite3

def save_to_database(quotes, db_name="quotes.db"):
    with sqlite3.connect(db_name) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS quotes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                text TEXT NOT NULL,
                author TEXT NOT NULL
            )
        """)
        conn.executemany(
            "INSERT INTO quotes (text, author) VALUES (?, ?)",
            [(q["text"], q["author"]) for q in quotes]
        )
    print(f"Saved {len(quotes)} quotes to {db_name}")
```

See how the chapters build on each other? APIs from Chapter 21, databases from Chapter 22, and now scraping to feed data into both.

## Error Handling for Scraping

Web pages change. Elements disappear. Servers go down. Your scraper needs to handle all of this:

```python
import requests
from bs4 import BeautifulSoup
import time

def robust_scrape(url, max_retries=3):
    """Scrape a page with proper error handling."""
    
    for attempt in range(max_retries):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, "html.parser")
            
            # Safely extract data (use .text only if element exists)
            title_tag = soup.find("h1")
            title = title_tag.text if title_tag else "No title found"
            
            return {"title": title, "url": url}
            
        except requests.exceptions.Timeout:
            print(f"Timeout on attempt {attempt + 1}")
            time.sleep(2)
            
        except requests.exceptions.HTTPError as e:
            print(f"HTTP error: {e}")
            return None
            
        except requests.exceptions.ConnectionError:
            print("Connection failed. Check your internet.")
            return None
    
    print(f"Failed after {max_retries} attempts")
    return None
```

The most common scraping bug: assuming an element exists. Always check before calling `.text`:

```python
# This crashes if the element doesn't exist
title = soup.find("h1").text  # AttributeError if no <h1>

# This is safe
title_tag = soup.find("h1")
title = title_tag.text if title_tag else "Not found"
```

## Ethics and Legality: Can I Scrape This?

Before you scrape anything, ask yourself these questions:

**The "Can I Scrape This?" Decision Guide:**

1. **Is there an API?** Use it instead. APIs are faster, more reliable, and the site owner prefers it.

2. **Check robots.txt.** Visit `example.com/robots.txt` - it tells you what bots are allowed to access. Respect it.

```python
import requests

# Check what's allowed
response = requests.get("https://quotes.toscrape.com/robots.txt")
print(response.text)
```

3. **Check the Terms of Service.** Some sites explicitly prohibit scraping. Read the ToS.

4. **Don't overload the server.** Add delays between requests. Don't make hundreds of requests per second.

5. **Don't scrape personal data.** Scraping public information is generally okay. Scraping personal data (emails, phone numbers) raises legal and ethical issues.

6. **Is the data copyrighted?** You can scrape it for personal analysis, but republishing someone else's content is a different story.

**General rules:**
- Public data for personal/research use: Usually fine
- Adding delays and respecting robots.txt: Always do this
- Scraping behind a login wall: Gray area - be careful
- Scraping and republishing content: Probably not okay
- Overwhelming a server with requests: Never okay

> **Pro Tip:** quotes.toscrape.com was literally built for practicing web scraping. It's a sandbox. For your learning projects, use sites like this that are designed for scraping practice.

## Your Turn: Scrape Quotes from quotes.toscrape.com

**Challenge:** Build a complete quote scraper that:

1. Scrapes all quotes from all pages of quotes.toscrape.com
2. Extracts the quote text, author, and tags
3. Saves results to both a JSON file and a SQLite database
4. Handles errors gracefully
5. Includes a 1-second delay between page requests

Here's a skeleton to get you started:

```python
import requests
from bs4 import BeautifulSoup
import json
import sqlite3
import time

def scrape_page(url):
    """Scrape quotes from a single page."""
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    
    quotes = []
    for div in soup.find_all("div", class_="quote"):
        # TODO: Extract text, author, and tags
        pass
    
    # TODO: Find the next page URL (or None if last page)
    next_url = None
    
    return quotes, next_url

def scrape_all():
    """Scrape all pages and return all quotes."""
    url = "https://quotes.toscrape.com/"
    all_quotes = []
    
    while url:
        print(f"Scraping: {url}")
        quotes, url = scrape_page(url)
        all_quotes.extend(quotes)
        if url:
            time.sleep(1)
    
    return all_quotes

if __name__ == "__main__":
    quotes = scrape_all()
    print(f"Scraped {len(quotes)} quotes!")
    
    # Save to JSON
    with open("quotes.json", "w") as f:
        json.dump(quotes, f, indent=2)
    
    # Save to SQLite (use what you learned in Chapter 22!)
```

**Starter code:** [https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/sprint-4-pro/chapter-23-scraping/](https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/sprint-4-pro/chapter-23-scraping/)

## TL;DR

| Concept | What It Does |
|--|--|
| `requests.get(url)` | Downloads a web page |
| `BeautifulSoup(html, "html.parser")` | Parses HTML into a searchable tree |
| `soup.find(tag, class_=...)` | Find the first matching element |
| `soup.find_all(tag, class_=...)` | Find all matching elements |
| `soup.select("css selector")` | Find elements using CSS selectors |
| `element.text` | Get the text inside an element |
| `element["attribute"]` | Get an attribute value |
| `time.sleep(1)` | Be polite - wait between requests |
| `robots.txt` | Check what the site allows you to scrape |

**The one-sentence version:** Use `requests` to download a web page and `BeautifulSoup` to search through its HTML and extract the data you need, always being respectful of the site's rules and server resources.

Next up: Testing - where we learn to prove our code actually works.
