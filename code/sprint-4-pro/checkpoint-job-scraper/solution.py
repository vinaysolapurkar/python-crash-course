"""
CHECKPOINT SOLUTION: Job Listing Scraper & Dashboard
=====================================================
The grand finale of Sprint 4! This project combines:
  - Decorators (Chapter 19) — @timer, @logger
  - Generators (Chapter 20) — sample data generation
  - APIs knowledge (Chapter 21) — data fetching patterns
  - Databases (Chapter 22) — SQLite storage
  - Scraping concepts (Chapter 23) — data extraction
  - Testing (Chapter 24) — pytest tests
  - Type hints & clean code (Chapter 25) — fully annotated

Run the app:    python solution.py
Run the tests:  pytest solution.py -v
"""

import sqlite3
import csv
import os
import time
import random
from functools import wraps
from typing import Optional, Union
from datetime import datetime, timedelta
from dataclasses import dataclass


# ============================================================
# Decorators
# ============================================================

def timer(func):
    """Decorator: measure and print execution time."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start: float = time.time()
        result = func(*args, **kwargs)
        elapsed: float = time.time() - start
        print(f"  [TIMER] {func.__name__} took {elapsed:.4f}s")
        return result
    return wrapper


def logger(func):
    """Decorator: log function calls with timestamp."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        timestamp: str = datetime.now().strftime("%H:%M:%S")
        print(f"  [{timestamp}] Calling {func.__name__}...")
        result = func(*args, **kwargs)
        return result
    return wrapper


# ============================================================
# Job Class
# ============================================================

@dataclass
class Job:
    """Represents a job listing with all relevant details."""
    title: str
    company: str
    location: str
    salary: float
    job_type: str        # "Full-time", "Part-time", "Contract", "Remote"
    description: str
    date_posted: str     # "YYYY-MM-DD"
    job_id: Optional[int] = None

    def __str__(self) -> str:
        salary_str: str = f"${self.salary:,.0f}"
        return (f"{self.title} at {self.company} | {self.location} | "
                f"{salary_str} | {self.job_type}")

    def to_dict(self) -> dict[str, Union[str, float, int, None]]:
        """Convert to dictionary for serialization."""
        return {
            "title": self.title,
            "company": self.company,
            "location": self.location,
            "salary": self.salary,
            "job_type": self.job_type,
            "description": self.description,
            "date_posted": self.date_posted,
            "job_id": self.job_id,
        }

    @classmethod
    def from_dict(cls, data: dict[str, Union[str, float, int, None]]) -> "Job":
        """Create a Job from a dictionary."""
        return cls(
            title=str(data["title"]),
            company=str(data["company"]),
            location=str(data["location"]),
            salary=float(data["salary"]),
            job_type=str(data["job_type"]),
            description=str(data["description"]),
            date_posted=str(data["date_posted"]),
            job_id=data.get("job_id"),
        )

    @classmethod
    def from_row(cls, row: sqlite3.Row) -> "Job":
        """Create a Job from a database row."""
        return cls(
            job_id=row["id"],
            title=row["title"],
            company=row["company"],
            location=row["location"],
            salary=row["salary"],
            job_type=row["job_type"],
            description=row["description"],
            date_posted=row["date_posted"],
        )


# ============================================================
# Database Layer
# ============================================================

DB_FILE: str = "jobs.db"


def get_connection() -> sqlite3.Connection:
    """Get a database connection with row factory."""
    conn: sqlite3.Connection = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn


def create_table() -> None:
    """Create the jobs table if it doesn't exist."""
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS jobs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                company TEXT NOT NULL,
                location TEXT NOT NULL,
                salary REAL NOT NULL,
                job_type TEXT NOT NULL,
                description TEXT,
                date_posted TEXT NOT NULL
            )
        """)


def insert_job(job: Job) -> int:
    """Insert a job into the database. Returns the new job ID."""
    with get_connection() as conn:
        cursor = conn.execute("""
            INSERT INTO jobs (title, company, location, salary, job_type,
                              description, date_posted)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (job.title, job.company, job.location, job.salary,
              job.job_type, job.description, job.date_posted))
        return cursor.lastrowid or 0


def insert_many_jobs(jobs: list[Job]) -> int:
    """Insert multiple jobs at once. Returns count inserted."""
    with get_connection() as conn:
        data = [
            (j.title, j.company, j.location, j.salary,
             j.job_type, j.description, j.date_posted)
            for j in jobs
        ]
        conn.executemany("""
            INSERT INTO jobs (title, company, location, salary, job_type,
                              description, date_posted)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, data)
    return len(data)


def get_all_jobs() -> list[Job]:
    """Get all jobs from the database."""
    with get_connection() as conn:
        rows = conn.execute(
            "SELECT * FROM jobs ORDER BY date_posted DESC"
        ).fetchall()
    return [Job.from_row(row) for row in rows]


def get_job_count() -> int:
    """Get total number of jobs in the database."""
    with get_connection() as conn:
        result = conn.execute("SELECT COUNT(*) FROM jobs").fetchone()
    return result[0] if result else 0


def search_jobs(query: str) -> list[Job]:
    """Search jobs by title, company, or description."""
    with get_connection() as conn:
        rows = conn.execute("""
            SELECT * FROM jobs
            WHERE title LIKE ? OR company LIKE ? OR description LIKE ?
            ORDER BY date_posted DESC
        """, (f"%{query}%", f"%{query}%", f"%{query}%")).fetchall()
    return [Job.from_row(row) for row in rows]


def filter_jobs(
    location: Optional[str] = None,
    job_type: Optional[str] = None,
    min_salary: Optional[float] = None,
    max_salary: Optional[float] = None,
) -> list[Job]:
    """Filter jobs by various criteria."""
    query: str = "SELECT * FROM jobs WHERE 1=1"
    params: list[Union[str, float]] = []

    if location:
        query += " AND location LIKE ?"
        params.append(f"%{location}%")
    if job_type:
        query += " AND job_type = ?"
        params.append(job_type)
    if min_salary is not None:
        query += " AND salary >= ?"
        params.append(min_salary)
    if max_salary is not None:
        query += " AND salary <= ?"
        params.append(max_salary)

    query += " ORDER BY salary DESC"

    with get_connection() as conn:
        rows = conn.execute(query, params).fetchall()
    return [Job.from_row(row) for row in rows]


def get_stats() -> dict[str, Union[dict, float, int]]:
    """Get comprehensive job statistics."""
    stats: dict = {}

    with get_connection() as conn:
        # Total count
        stats["total"] = conn.execute("SELECT COUNT(*) FROM jobs").fetchone()[0]

        # By location
        rows = conn.execute("""
            SELECT location, COUNT(*) as count
            FROM jobs GROUP BY location ORDER BY count DESC
        """).fetchall()
        stats["by_location"] = {r["location"]: r["count"] for r in rows}

        # By job type
        rows = conn.execute("""
            SELECT job_type, COUNT(*) as count
            FROM jobs GROUP BY job_type ORDER BY count DESC
        """).fetchall()
        stats["by_type"] = {r["job_type"]: r["count"] for r in rows}

        # Salary stats
        row = conn.execute("""
            SELECT MIN(salary) as min_sal, MAX(salary) as max_sal,
                   AVG(salary) as avg_sal
            FROM jobs
        """).fetchone()
        stats["salary"] = {
            "min": row["min_sal"] or 0,
            "max": row["max_sal"] or 0,
            "avg": round(row["avg_sal"] or 0, 2),
        }

        # By company (top 10)
        rows = conn.execute("""
            SELECT company, COUNT(*) as count, AVG(salary) as avg_salary
            FROM jobs GROUP BY company ORDER BY count DESC LIMIT 10
        """).fetchall()
        stats["top_companies"] = [
            {"company": r["company"], "count": r["count"],
             "avg_salary": round(r["avg_salary"], 2)}
            for r in rows
        ]

    return stats


def clear_all_jobs() -> None:
    """Delete all jobs from the database."""
    with get_connection() as conn:
        conn.execute("DELETE FROM jobs")


# ============================================================
# Sample Data Generator
# ============================================================

def generate_sample_jobs(count: int = 50) -> list[Job]:
    """Generate realistic sample job listings using generators."""

    titles: list[str] = [
        "Python Developer", "Senior Python Engineer", "Backend Developer",
        "Full-Stack Developer", "Data Scientist", "Data Analyst",
        "Machine Learning Engineer", "DevOps Engineer", "Cloud Engineer",
        "Software Engineer", "Junior Developer", "Technical Lead",
        "QA Engineer", "Frontend Developer", "API Developer",
        "Site Reliability Engineer", "Security Engineer",
        "Database Administrator", "Systems Architect", "Product Manager",
    ]

    companies: list[str] = [
        "TechCorp", "DataFlow Inc", "CloudNine Solutions", "PyWorks",
        "InnovateTech", "CodeCrafters", "Digital Dynamics", "AlgoRithm",
        "ByteForce", "NeuralNet Labs", "StackOverflow Co", "GitPush Inc",
        "Lambda Logic", "Quantum Computing Corp", "AI Solutions Ltd",
        "DevHub", "CodeBase Systems", "CyberSec Pro", "WebWave", "AppForge",
    ]

    locations: list[str] = [
        "San Francisco, CA", "New York, NY", "Austin, TX", "Seattle, WA",
        "Denver, CO", "Chicago, IL", "Boston, MA", "Portland, OR",
        "Los Angeles, CA", "Remote", "Miami, FL", "Atlanta, GA",
    ]

    job_types: list[str] = ["Full-time", "Part-time", "Contract", "Remote"]
    type_weights: list[int] = [50, 10, 15, 25]

    descriptions: list[str] = [
        "Join our team to build scalable applications using Python and modern frameworks.",
        "We're looking for a passionate developer to help us reshape the industry.",
        "Work on cutting-edge technology with a team of talented engineers.",
        "Help us build the next generation of data-driven products.",
        "Collaborate with cross-functional teams to deliver impactful solutions.",
        "Lead the development of APIs and microservices in a fast-paced environment.",
        "Design and implement robust systems that handle millions of requests.",
        "Be part of a startup culture with big-company resources.",
    ]

    jobs: list[Job] = []
    for _ in range(count):
        title: str = random.choice(titles)

        # Salary based on seniority
        if "Senior" in title or "Lead" in title or "Architect" in title:
            salary = random.randint(130000, 200000)
        elif "Junior" in title:
            salary = random.randint(55000, 85000)
        elif "Manager" in title:
            salary = random.randint(120000, 180000)
        else:
            salary = random.randint(80000, 150000)

        # Round salary to nearest 5000
        salary = round(salary / 5000) * 5000

        # Random date within last 30 days
        days_ago: int = random.randint(0, 30)
        date_posted: str = (
            datetime.now() - timedelta(days=days_ago)
        ).strftime("%Y-%m-%d")

        jobs.append(Job(
            title=title,
            company=random.choice(companies),
            location=random.choice(locations),
            salary=float(salary),
            job_type=random.choices(job_types, weights=type_weights, k=1)[0],
            description=random.choice(descriptions),
            date_posted=date_posted,
        ))

    return jobs


# ============================================================
# CLI Display Functions
# ============================================================

def display_jobs(jobs: list[Job], title: str = "Job Listings",
                 page_size: int = 10) -> None:
    """Display jobs with pagination."""
    if not jobs:
        print(f"\n  No {title.lower()} found.")
        return

    total_pages: int = (len(jobs) + page_size - 1) // page_size
    current_page: int = 0

    while True:
        start: int = current_page * page_size
        end: int = min(start + page_size, len(jobs))
        page_jobs: list[Job] = jobs[start:end]

        print(f"\n  {title} ({len(jobs)} total) — Page {current_page + 1}/{total_pages}")
        print(f"  {'─' * 70}")
        print(f"  {'#':<4} {'Title':<25} {'Company':<18} {'Location':<16} {'Salary':>10}")
        print(f"  {'─' * 70}")

        for i, job in enumerate(page_jobs, start + 1):
            salary_str: str = f"${job.salary:,.0f}"
            print(f"  {i:<4} {job.title[:24]:<25} {job.company[:17]:<18} "
                  f"{job.location[:15]:<16} {salary_str:>10}")

        print(f"  {'─' * 70}")

        if total_pages <= 1:
            break

        nav = input("  [n]ext, [p]rev, [q]uit viewing: ").strip().lower()
        if nav == "n" and current_page < total_pages - 1:
            current_page += 1
        elif nav == "p" and current_page > 0:
            current_page -= 1
        elif nav == "q":
            break


def display_stats(stats: dict) -> None:
    """Display job statistics in a dashboard format."""
    print(f"\n  {'=' * 55}")
    print(f"  JOB MARKET STATISTICS")
    print(f"  {'=' * 55}")

    print(f"\n  Total Jobs: {stats['total']}")

    # Salary
    sal = stats["salary"]
    print(f"\n  Salary Range:")
    print(f"    Min:     ${sal['min']:>10,.0f}")
    print(f"    Average: ${sal['avg']:>10,.0f}")
    print(f"    Max:     ${sal['max']:>10,.0f}")

    # By type
    print(f"\n  By Job Type:")
    for jtype, count in stats["by_type"].items():
        bar: str = "#" * (count * 2)
        print(f"    {jtype:<12} {count:>3} {bar}")

    # By location (top 8)
    print(f"\n  Top Locations:")
    for location, count in list(stats["by_location"].items())[:8]:
        bar = "#" * count
        print(f"    {location:<20} {count:>3} {bar}")

    # Top companies
    print(f"\n  Top Hiring Companies:")
    for comp in stats["top_companies"][:5]:
        print(f"    {comp['company']:<22} {comp['count']:>3} jobs | "
              f"Avg salary: ${comp['avg_salary']:,.0f}")

    print(f"  {'=' * 55}")


def export_to_csv(jobs: list[Job], filename: str = "jobs_export.csv") -> str:
    """Export jobs to a CSV file. Returns the filename."""
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            "Title", "Company", "Location", "Salary",
            "Type", "Description", "Date Posted",
        ])
        for job in jobs:
            writer.writerow([
                job.title, job.company, job.location, job.salary,
                job.job_type, job.description, job.date_posted,
            ])
    return filename


# ============================================================
# Main CLI Dashboard
# ============================================================

@timer
@logger
def load_sample_data(count: int = 50) -> int:
    """Generate and insert sample job data."""
    clear_all_jobs()
    jobs: list[Job] = generate_sample_jobs(count)
    inserted: int = insert_many_jobs(jobs)
    return inserted


def main() -> None:
    """Main CLI dashboard — the command center for job hunting."""
    create_table()

    # Check if DB needs sample data
    if get_job_count() == 0:
        print("\n  Database is empty. Generating sample job listings...")
        count = load_sample_data(50)
        print(f"  Loaded {count} sample jobs!")

    while True:
        job_count: int = get_job_count()
        print(f"\n{'=' * 50}")
        print(f"  JOB LISTING DASHBOARD ({job_count} jobs)")
        print(f"{'=' * 50}")
        print("  1. View all jobs")
        print("  2. Search jobs")
        print("  3. Filter by location")
        print("  4. Filter by job type")
        print("  5. Filter by salary range")
        print("  6. View statistics")
        print("  7. Export to CSV")
        print("  8. Refresh sample data")
        print("  0. Quit")
        print(f"{'=' * 50}")

        choice: str = input("\n  Choose: ").strip()

        if choice == "1":
            jobs = get_all_jobs()
            display_jobs(jobs, "All Jobs")

        elif choice == "2":
            query = input("  Search term: ").strip()
            if query:
                jobs = search_jobs(query)
                display_jobs(jobs, f"Search: '{query}'")

        elif choice == "3":
            print("  Common locations: San Francisco, New York, Austin, "
                  "Seattle, Denver, Remote")
            location = input("  Location: ").strip()
            if location:
                jobs = filter_jobs(location=location)
                display_jobs(jobs, f"Jobs in '{location}'")

        elif choice == "4":
            print("  Types: Full-time, Part-time, Contract, Remote")
            job_type = input("  Job type: ").strip()
            if job_type:
                jobs = filter_jobs(job_type=job_type)
                display_jobs(jobs, f"'{job_type}' Jobs")

        elif choice == "5":
            try:
                min_sal = input("  Min salary (e.g., 100000, or press Enter): ").strip()
                max_sal = input("  Max salary (or press Enter): ").strip()
                min_salary = float(min_sal) if min_sal else None
                max_salary = float(max_sal) if max_sal else None
                jobs = filter_jobs(min_salary=min_salary, max_salary=max_salary)
                label = f"Salary"
                if min_salary:
                    label += f" >= ${min_salary:,.0f}"
                if max_salary:
                    label += f" <= ${max_salary:,.0f}"
                display_jobs(jobs, label)
            except ValueError:
                print("  Invalid salary value!")

        elif choice == "6":
            stats = get_stats()
            display_stats(stats)

        elif choice == "7":
            jobs = get_all_jobs()
            filename = export_to_csv(jobs)
            print(f"  Exported {len(jobs)} jobs to '{filename}'!")

        elif choice == "8":
            count_input = input("  How many jobs to generate? (default 50): ").strip()
            count = int(count_input) if count_input.isdigit() else 50
            loaded = load_sample_data(count)
            print(f"  Refreshed with {loaded} new job listings!")

        elif choice == "0":
            print("\n  Happy job hunting! May your code compile and your "
                  "interviews go smoothly! 🎯")
            break

        else:
            print("  Invalid option. Choose 0-8.")


# ============================================================
# Tests — Run with: pytest solution.py -v
# ============================================================
import pytest


class TestJob:
    """Tests for the Job class."""

    def test_job_creation(self) -> None:
        job = Job("Python Dev", "TechCo", "NYC", 120000.0,
                  "Full-time", "Build stuff", "2024-01-15")
        assert job.title == "Python Dev"
        assert job.company == "TechCo"
        assert job.salary == 120000.0

    def test_job_str(self) -> None:
        job = Job("Dev", "Co", "NYC", 100000.0, "Full-time", "Desc", "2024-01-01")
        result = str(job)
        assert "Dev" in result
        assert "Co" in result
        assert "$100,000" in result

    def test_job_to_dict(self) -> None:
        job = Job("Dev", "Co", "NYC", 100000.0, "Full-time", "Desc", "2024-01-01")
        d = job.to_dict()
        assert d["title"] == "Dev"
        assert d["salary"] == 100000.0
        assert isinstance(d, dict)

    def test_job_from_dict(self) -> None:
        data = {
            "title": "Dev", "company": "Co", "location": "NYC",
            "salary": 100000.0, "job_type": "Full-time",
            "description": "Desc", "date_posted": "2024-01-01",
        }
        job = Job.from_dict(data)
        assert job.title == "Dev"
        assert job.salary == 100000.0

    def test_job_roundtrip(self) -> None:
        """Test to_dict -> from_dict preserves data."""
        original = Job("ML Engineer", "AI Corp", "SF", 180000.0,
                       "Remote", "AI stuff", "2024-06-15")
        rebuilt = Job.from_dict(original.to_dict())
        assert rebuilt.title == original.title
        assert rebuilt.salary == original.salary
        assert rebuilt.location == original.location


class TestDatabase:
    """Tests for database operations."""

    @pytest.fixture(autouse=True)
    def setup_test_db(self, tmp_path):
        """Use a temporary database for each test."""
        global DB_FILE
        DB_FILE = str(tmp_path / "test_jobs.db")
        create_table()

    def test_create_table(self) -> None:
        """Table creation shouldn't error."""
        create_table()  # should not raise

    def test_insert_and_retrieve(self) -> None:
        job = Job("Dev", "Co", "NYC", 100000.0, "Full-time", "Desc", "2024-01-01")
        insert_job(job)
        jobs = get_all_jobs()
        assert len(jobs) == 1
        assert jobs[0].title == "Dev"

    def test_search(self) -> None:
        insert_job(Job("Python Dev", "TechCo", "NYC", 120000.0,
                       "Full-time", "Python work", "2024-01-01"))
        insert_job(Job("Java Dev", "OtherCo", "LA", 110000.0,
                       "Full-time", "Java work", "2024-01-01"))

        results = search_jobs("Python")
        assert len(results) == 1
        assert results[0].title == "Python Dev"

    def test_search_case_insensitive(self) -> None:
        insert_job(Job("Python Dev", "TechCo", "NYC", 120000.0,
                       "Full-time", "Desc", "2024-01-01"))
        # SQLite LIKE is case-insensitive for ASCII
        results = search_jobs("python")
        assert len(results) == 1

    def test_filter_by_location(self) -> None:
        insert_job(Job("Dev1", "Co", "NYC", 100000.0, "Full-time", "", "2024-01-01"))
        insert_job(Job("Dev2", "Co", "LA", 100000.0, "Full-time", "", "2024-01-01"))

        results = filter_jobs(location="NYC")
        assert len(results) == 1
        assert results[0].location == "NYC"

    def test_filter_by_type(self) -> None:
        insert_job(Job("Dev1", "Co", "NYC", 100000.0, "Full-time", "", "2024-01-01"))
        insert_job(Job("Dev2", "Co", "NYC", 80000.0, "Part-time", "", "2024-01-01"))

        results = filter_jobs(job_type="Part-time")
        assert len(results) == 1

    def test_filter_by_salary(self) -> None:
        insert_job(Job("Jr", "Co", "NYC", 60000.0, "Full-time", "", "2024-01-01"))
        insert_job(Job("Sr", "Co", "NYC", 150000.0, "Full-time", "", "2024-01-01"))

        results = filter_jobs(min_salary=100000.0)
        assert len(results) == 1
        assert results[0].title == "Sr"

    def test_stats(self) -> None:
        insert_job(Job("Dev1", "Co1", "NYC", 100000.0, "Full-time", "", "2024-01-01"))
        insert_job(Job("Dev2", "Co2", "LA", 120000.0, "Remote", "", "2024-01-01"))

        stats = get_stats()
        assert stats["total"] == 2
        assert "NYC" in stats["by_location"]
        assert stats["salary"]["min"] == 100000.0
        assert stats["salary"]["max"] == 120000.0

    def test_insert_many(self) -> None:
        jobs = [
            Job(f"Dev{i}", "Co", "NYC", 100000.0, "Full-time", "", "2024-01-01")
            for i in range(10)
        ]
        count = insert_many_jobs(jobs)
        assert count == 10
        assert get_job_count() == 10


class TestSampleData:
    """Tests for sample data generation."""

    def test_generate_produces_correct_count(self) -> None:
        jobs = generate_sample_jobs(20)
        assert len(jobs) == 20

    def test_generated_jobs_have_required_fields(self) -> None:
        jobs = generate_sample_jobs(5)
        for job in jobs:
            assert job.title
            assert job.company
            assert job.location
            assert job.salary > 0
            assert job.job_type in ["Full-time", "Part-time", "Contract", "Remote"]
            assert job.date_posted

    def test_salary_ranges_reasonable(self) -> None:
        jobs = generate_sample_jobs(100)
        for job in jobs:
            assert 50000 <= job.salary <= 210000, f"Salary {job.salary} out of range"


class TestExport:
    """Tests for export functionality."""

    def test_export_csv(self, tmp_path) -> None:
        jobs = [
            Job("Dev", "Co", "NYC", 100000.0, "Full-time", "Desc", "2024-01-01")
        ]
        filepath = str(tmp_path / "test_export.csv")
        result = export_to_csv(jobs, filepath)
        assert os.path.exists(result)

        # Verify CSV content
        with open(result, "r") as f:
            reader = csv.reader(f)
            rows = list(reader)
        assert len(rows) == 2  # header + 1 data row
        assert rows[0][0] == "Title"
        assert rows[1][0] == "Dev"


# ============================================================
# Entry Point
# ============================================================
if __name__ == "__main__":
    main()
