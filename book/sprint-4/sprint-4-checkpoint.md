# Sprint 4 Checkpoint: Job Listing Scraper & Dashboard

> **Estimated Time: 2-3 hours** | **Difficulty: Advanced** | **This is your masterpiece for Sprint 4**

Sprint 4 complete. Take a second and think about what you just learned: decorators, generators, APIs, databases, web scraping, testing, and clean code practices. Those aren't beginner topics. Those are the tools that professional Python developers use every single day.

**You now have the toolkit of a working developer.** Not a student. Not a hobbyist. A developer.

Let's prove it by building something real.

## The Project: Job Listing Scraper & Dashboard

You're going to build a complete application that scrapes job listings from the web, stores them in a database, provides a search interface, and includes a full test suite. Every chapter in this sprint feeds directly into this project.

Here's what you'll build:

1. **Scraper** - Collect job listings from a practice website (Chapter 23)
2. **Database** - Store listings in SQLite with proper schema (Chapter 22)
3. **Search Engine** - Query and filter listings (Chapter 22)
4. **API Client** - Fetch additional data from a public API (Chapter 21)
5. **Data Pipeline** - Process listings efficiently with generators (Chapter 20)
6. **Utilities** - Decorated helper functions for timing and logging (Chapter 19)
7. **Test Suite** - Prove it all works with pytest (Chapter 24)
8. **Clean Code** - Type hints, formatting, and linting throughout (Chapter 25)

## Skills Map

| Project Component | Chapter |
|--|--|
| `@timer` and `@logger` decorators | Chapter 19: Decorators |
| Generator-based data pipeline | Chapter 20: Generators |
| Fetching salary data from an API | Chapter 21: APIs |
| SQLite database for job listings | Chapter 22: Databases |
| Scraping job listings from HTML | Chapter 23: Web Scraping |
| pytest test suite with fixtures | Chapter 24: Testing |
| Type hints and black formatting | Chapter 25: Clean Code |

## Project Structure

```
job_scraper/
    scraper.py          # Web scraping logic
    database.py         # SQLite database operations
    api_client.py       # External API integration
    pipeline.py         # Generator-based data processing
    utils.py            # Decorators and helper functions
    dashboard.py        # Search and display interface
    main.py             # Entry point - ties everything together
    tests/
        test_scraper.py
        test_database.py
        test_pipeline.py
        test_utils.py
```

## Step-by-Step Build Guide

### Step 1: Set Up the Project (5 minutes)

Create the project structure and install dependencies:

```bash
mkdir job_scraper
cd job_scraper
mkdir tests

pip install requests beautifulsoup4 pytest black flake8 mypy
```

### Step 2: Build the Decorators (utils.py) - Chapter 19

Start with your utility decorators. You'll use these throughout the project:

```python
# utils.py
import functools
import time
from typing import Any, Callable


def timer(func: Callable) -> Callable:
    """Log how long a function takes to execute."""
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"[TIMER] {func.__name__} took {elapsed:.2f}s")
        return result
    return wrapper


def logger(func: Callable) -> Callable:
    """Log function calls with arguments and return values."""
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        args_str = ", ".join([repr(a) for a in args])
        kwargs_str = ", ".join([f"{k}={repr(v)}" for k, v in kwargs.items()])
        all_args = ", ".join(filter(None, [args_str, kwargs_str]))
        print(f"[LOG] Calling {func.__name__}({all_args})")
        result = func(*args, **kwargs)
        print(f"[LOG] {func.__name__} returned {type(result).__name__}")
        return result
    return wrapper


def retry(max_attempts: int = 3, delay: float = 1.0) -> Callable:
    """Retry a function if it raises an exception."""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts:
                        raise
                    print(f"[RETRY] Attempt {attempt} failed: {e}")
                    time.sleep(delay)
        return wrapper
    return decorator
```

### Step 3: Build the Database Layer (database.py) - Chapter 22

```python
# database.py
import sqlite3
from typing import Optional

DB_NAME: str = "jobs.db"


def get_connection() -> sqlite3.Connection:
    """Get a database connection with row factory enabled."""
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def create_tables() -> None:
    """Create the jobs table if it doesn't exist."""
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS jobs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                company TEXT NOT NULL,
                location TEXT,
                description TEXT,
                url TEXT UNIQUE,
                scraped_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
        """)


def insert_job(
    title: str,
    company: str,
    location: str = "",
    description: str = "",
    url: str = ""
) -> Optional[int]:
    """Insert a job listing. Returns the job ID or None if duplicate."""
    try:
        with get_connection() as conn:
            cursor = conn.execute(
                """INSERT INTO jobs (title, company, location, description, url)
                   VALUES (?, ?, ?, ?, ?)""",
                (title, company, location, description, url),
            )
            return cursor.lastrowid
    except sqlite3.IntegrityError:
        return None  # Duplicate URL


def search_jobs(
    keyword: str = "",
    location: str = "",
    limit: int = 20
) -> list[dict]:
    """Search jobs by keyword and/or location."""
    with get_connection() as conn:
        query = "SELECT * FROM jobs WHERE 1=1"
        params: list = []

        if keyword:
            query += " AND (title LIKE ? OR description LIKE ?)"
            params.extend([f"%{keyword}%", f"%{keyword}%"])

        if location:
            query += " AND location LIKE ?"
            params.append(f"%{location}%")

        query += " ORDER BY scraped_at DESC LIMIT ?"
        params.append(limit)

        rows = conn.execute(query, params).fetchall()
        return [dict(row) for row in rows]


def get_job_count() -> int:
    """Get the total number of jobs in the database."""
    with get_connection() as conn:
        result = conn.execute("SELECT COUNT(*) FROM jobs").fetchone()
        return result[0]


def get_companies() -> list[dict]:
    """Get all companies with their job counts."""
    with get_connection() as conn:
        rows = conn.execute("""
            SELECT company, COUNT(*) as job_count
            FROM jobs
            GROUP BY company
            ORDER BY job_count DESC
        """).fetchall()
        return [dict(row) for row in rows]
```

### Step 4: Build the Scraper (scraper.py) - Chapter 23

For this project, we'll scrape from a practice site. You can adapt this to any job board:

```python
# scraper.py
import requests
from bs4 import BeautifulSoup
import time
from typing import Optional
from utils import timer, retry


@retry(max_attempts=3, delay=2.0)
def fetch_page(url: str) -> Optional[str]:
    """Fetch a web page and return its HTML content."""
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.text


def parse_job_listings(html: str) -> list[dict[str, str]]:
    """Parse job listings from HTML content."""
    soup = BeautifulSoup(html, "html.parser")
    jobs: list[dict[str, str]] = []

    # Adapt these selectors to your target site
    for listing in soup.find_all("div", class_="quote"):
        title_tag = listing.find("span", class_="text")
        company_tag = listing.find("small", class_="author")
        tags = listing.find_all("a", class_="tag")

        if title_tag and company_tag:
            jobs.append({
                "title": title_tag.text.strip(),
                "company": company_tag.text.strip(),
                "location": "Remote",
                "description": ", ".join(tag.text for tag in tags),
                "url": "",
            })

    return jobs


def get_next_page_url(html: str, base_url: str) -> Optional[str]:
    """Find the URL of the next page, or None if this is the last page."""
    soup = BeautifulSoup(html, "html.parser")
    next_btn = soup.find("li", class_="next")

    if next_btn:
        link = next_btn.find("a")
        if link:
            return base_url + link["href"]

    return None


@timer
def scrape_all_jobs(base_url: str = "https://quotes.toscrape.com") -> list[dict[str, str]]:
    """Scrape all job listings from all pages."""
    all_jobs: list[dict[str, str]] = []
    url: Optional[str] = base_url + "/"

    while url:
        print(f"Scraping: {url}")
        html = fetch_page(url)

        if html is None:
            break

        jobs = parse_job_listings(html)
        all_jobs.extend(jobs)

        url = get_next_page_url(html, base_url)
        if url:
            time.sleep(1)  # Be polite

    return all_jobs
```

### Step 5: Build the Data Pipeline (pipeline.py) - Chapter 20

Use generators to process the scraped data efficiently:

```python
# pipeline.py
from typing import Generator


def filter_by_keyword(
    jobs: list[dict], keyword: str
) -> Generator[dict, None, None]:
    """Yield only jobs whose title or description contains the keyword."""
    keyword_lower = keyword.lower()
    for job in jobs:
        if (keyword_lower in job.get("title", "").lower()
                or keyword_lower in job.get("description", "").lower()):
            yield job


def clean_job_data(
    jobs: list[dict],
) -> Generator[dict, None, None]:
    """Clean and normalize job data."""
    seen_titles: set[str] = set()

    for job in jobs:
        # Strip whitespace
        cleaned = {k: v.strip() if isinstance(v, str) else v for k, v in job.items()}

        # Skip duplicates
        title_key = cleaned.get("title", "").lower()
        if title_key in seen_titles:
            continue
        seen_titles.add(title_key)

        yield cleaned


def format_for_display(
    jobs: list[dict],
) -> Generator[str, None, None]:
    """Format jobs as readable strings."""
    for i, job in enumerate(jobs, 1):
        yield (
            f"\n-- Job {i} --\n"
            f"Title:    {job.get('title', 'N/A')}\n"
            f"Company:  {job.get('company', 'N/A')}\n"
            f"Location: {job.get('location', 'N/A')}\n"
            f"Tags:     {job.get('description', 'N/A')}"
        )
```

### Step 6: Build the Dashboard (dashboard.py)

```python
# dashboard.py
from database import search_jobs, get_job_count, get_companies


def display_dashboard() -> None:
    """Display the main dashboard."""
    total = get_job_count()
    companies = get_companies()

    print("=" * 50)
    print("       JOB LISTING DASHBOARD")
    print("=" * 50)
    print(f"\nTotal listings: {total}")
    print(f"Companies: {len(companies)}")

    print("\nTop Companies:")
    for company in companies[:10]:
        print(f"  {company['company']}: {company['job_count']} listing(s)")

    print("\n" + "-" * 50)


def search_interface() -> None:
    """Interactive search interface."""
    while True:
        print("\nSearch Jobs (or 'quit' to exit)")
        keyword = input("Keyword: ").strip()

        if keyword.lower() == "quit":
            break

        location = input("Location (optional): ").strip()
        results = search_jobs(keyword=keyword, location=location)

        if results:
            print(f"\nFound {len(results)} result(s):\n")
            for job in results:
                print(f"  [{job['id']}] {job['title']}")
                print(f"       {job['company']} | {job['location']}")
                print()
        else:
            print("No jobs found matching your criteria.")
```

### Step 7: Tie It Together (main.py)

```python
# main.py
from scraper import scrape_all_jobs
from database import create_tables, insert_job, get_job_count
from pipeline import clean_job_data
from dashboard import display_dashboard, search_interface
from utils import timer


@timer
def run_scraper() -> int:
    """Scrape jobs and save to database."""
    print("Starting scraper...")
    raw_jobs = scrape_all_jobs()
    print(f"Scraped {len(raw_jobs)} raw listings")

    # Process through pipeline
    clean_jobs = list(clean_job_data(raw_jobs))
    print(f"After cleaning: {len(clean_jobs)} unique listings")

    # Save to database
    saved = 0
    for job in clean_jobs:
        result = insert_job(
            title=job["title"],
            company=job["company"],
            location=job.get("location", ""),
            description=job.get("description", ""),
            url=job.get("url", ""),
        )
        if result:
            saved += 1

    return saved


def main() -> None:
    """Main entry point."""
    create_tables()

    print("Job Listing Scraper & Dashboard")
    print("=" * 40)
    print("1. Scrape new listings")
    print("2. View dashboard")
    print("3. Search jobs")
    print("4. Exit")

    while True:
        choice = input("\nChoice (1-4): ").strip()

        if choice == "1":
            saved = run_scraper()
            print(f"Saved {saved} new listings to database")
            print(f"Total in database: {get_job_count()}")

        elif choice == "2":
            display_dashboard()

        elif choice == "3":
            search_interface()

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try 1-4.")


if __name__ == "__main__":
    main()
```

### Step 8: Write Tests (tests/) - Chapter 24

```python
# tests/test_database.py
import pytest
import sqlite3
from database import create_tables, insert_job, search_jobs, get_job_count

DB_NAME = ":memory:"


@pytest.fixture
def test_db(monkeypatch):
    """Create a fresh in-memory database for each test."""
    import database
    monkeypatch.setattr(database, "DB_NAME", ":memory:")

    # We need a persistent connection for in-memory databases
    conn = sqlite3.connect(":memory:")
    conn.row_factory = sqlite3.Row
    conn.execute("""
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            company TEXT NOT NULL,
            location TEXT,
            description TEXT,
            url TEXT UNIQUE,
            scraped_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """)

    def mock_get_connection():
        return conn

    monkeypatch.setattr(database, "get_connection", mock_get_connection)
    return conn


def test_insert_job(test_db):
    """Test inserting a job listing."""
    import database
    job_id = database.insert_job(
        title="Python Developer",
        company="Acme Corp",
        location="Remote",
        url="https://example.com/job1",
    )
    assert job_id is not None
    assert job_id > 0


def test_search_jobs_by_keyword(test_db):
    """Test searching jobs by keyword."""
    import database
    database.insert_job(
        title="Python Developer",
        company="Acme Corp",
        url="https://example.com/1",
    )
    database.insert_job(
        title="Java Developer",
        company="Other Corp",
        url="https://example.com/2",
    )

    results = database.search_jobs(keyword="Python")
    assert len(results) == 1
    assert results[0]["title"] == "Python Developer"


# tests/test_utils.py
import pytest
from utils import timer, logger


def test_timer_returns_result():
    """Test that @timer preserves the return value."""
    @timer
    def add(a, b):
        return a + b

    assert add(2, 3) == 5


def test_timer_preserves_function_name():
    """Test that @timer preserves __name__."""
    @timer
    def my_function():
        pass

    assert my_function.__name__ == "my_function"


# tests/test_pipeline.py
from pipeline import filter_by_keyword, clean_job_data


def test_filter_by_keyword():
    """Test filtering jobs by keyword."""
    jobs = [
        {"title": "Python Developer", "description": ""},
        {"title": "Java Developer", "description": ""},
        {"title": "Data Scientist", "description": "Python required"},
    ]

    results = list(filter_by_keyword(jobs, "python"))
    assert len(results) == 2


def test_clean_removes_duplicates():
    """Test that cleaning removes duplicate titles."""
    jobs = [
        {"title": "Python Developer", "company": "A"},
        {"title": "Python Developer", "company": "B"},
        {"title": "Java Developer", "company": "C"},
    ]

    results = list(clean_job_data(jobs))
    assert len(results) == 2
```

### Step 9: Clean Up - Chapter 25

Run the full clean code suite:

```bash
# Format everything
black *.py tests/*.py

# Check for style issues
flake8 *.py tests/*.py

# Check types
mypy *.py

# Run tests
pytest tests/ -v
```

Fix any issues that come up. This is the professional workflow.

## Starter and Solution Code

**Starter code (skeleton with TODOs):**
[https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/sprint-4-pro/checkpoint-job-scraper/starter/](https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/sprint-4-pro/checkpoint-job-scraper/starter/)

**Solution code (complete working project):**
[https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/sprint-4-pro/checkpoint-job-scraper/solution/](https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/sprint-4-pro/checkpoint-job-scraper/solution/)

## Extension Ideas

If you want to go further:

- **Add email alerts** - Send yourself an email when new jobs matching your criteria are found
- **Schedule the scraper** - Run it automatically every day using `schedule` or cron
- **Build a web interface** - Use Flask (you'll learn this in Sprint 5!) to create a browser-based dashboard
- **Add salary estimation** - Use a public API to estimate salaries based on job title and location
- **Export to CSV/Excel** - Let users download search results

## What You've Accomplished

Let's take stock. In Sprint 4, you learned:

- How to write and use **decorators** to add behavior to functions
- How to use **generators** to process data memory-efficiently
- How to call **APIs** and work with JSON data from the internet
- How to store and query data in a real **database**
- How to **scrape** data from websites
- How to write **tests** that prove your code works
- How to write **clean, professional code** with type hints and linting

These aren't academic exercises. These are the exact skills listed on job postings for Python developers. You just built them all into a single project.

---

**You're one sprint away from building AI applications. ONE. Let that sink in.**

Sprint 5 covers AI, machine learning, and building intelligent applications with Python. Everything you've learned - from variables in Sprint 1 to databases and APIs in Sprint 4 - comes together. You have the foundation. You're ready.

See you in Sprint 5.
