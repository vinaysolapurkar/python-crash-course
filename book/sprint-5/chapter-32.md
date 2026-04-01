# Chapter 32: Automation with Python: Let the Computer Do the Work

> **Sprint 5, Chapter 32** | **12 min read** | **Code: [github link](https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/sprint-5-ai/chapter-32-automation/)**

Why spend 10 minutes doing something manually when you can spend 2 hours automating it? ...Wait, actually that math checks out over time. If you automate a 10-minute daily task, you save 40+ hours a year. Automate five tasks and you've saved an entire work week. This is the chapter where Python starts doing your job while you get coffee.

## What You'll Learn
- File operations with os, shutil, pathlib
- Bulk file renaming
- Email automation with smtplib
- Scheduling tasks with the schedule library
- Selenium - browser automation basics
- Three practical recipes you can use immediately

## Why Should I Care?

Automate reports. Organize a messy Downloads folder. Send emails at 9 AM without being awake at 9 AM. Scrape data on a schedule. Fill out web forms. Rename 500 files in 2 seconds. Every office worker has repetitive computer tasks that eat hours every week. Python can do all of them. While you sleep.

The irony of automation: you feel guilty the first time your script does in 3 seconds what used to take you 20 minutes. Then you feel like a genius. Then you automate everything.

## File Operations: os, shutil, pathlib

### pathlib: The Modern Way

`pathlib` is the best way to work with files and folders in Python. It's clean, readable, and cross-platform.

```python
from pathlib import Path

# Current directory
here = Path(".")
print(here.resolve())  # Full path: C:\Users\you\projects

# Home directory
home = Path.home()
print(home)  # C:\Users\you (Windows) or /home/you (Linux)

# Build paths (no more string concatenation!)
downloads = Path.home() / "Downloads"
print(downloads)  # C:\Users\you\Downloads

# Check if a path exists
print(downloads.exists())  # True
print(downloads.is_dir())  # True

# List all files in a directory
for item in downloads.iterdir():
    print(item.name)

# Find specific files (glob patterns)
for pdf in downloads.glob("*.pdf"):
    print(f"Found PDF: {pdf.name}")

# Recursive search (all subdirectories too)
for py_file in Path(".").rglob("*.py"):
    print(f"Python file: {py_file}")
```

### File Information

```python
from pathlib import Path
import os

file = Path("example.txt")

# Create a test file
file.write_text("Hello, automation!")

# File info
print(f"Name: {file.name}")           # example.txt
print(f"Extension: {file.suffix}")     # .txt
print(f"Stem (no ext): {file.stem}")   # example
print(f"Size: {file.stat().st_size} bytes")
print(f"Exists: {file.exists()}")

# Read content
content = file.read_text()
print(content)  # Hello, automation!
```

### Creating, Moving, Copying, Deleting

```python
from pathlib import Path
import shutil

# Create directories
Path("organized/reports").mkdir(parents=True, exist_ok=True)
Path("organized/images").mkdir(parents=True, exist_ok=True)
Path("organized/data").mkdir(parents=True, exist_ok=True)

# Move a file
source = Path("report.pdf")
destination = Path("organized/reports/report.pdf")
if source.exists():
    shutil.move(str(source), str(destination))

# Copy a file
shutil.copy2("original.txt", "backup.txt")  # copy2 preserves metadata

# Copy entire directory
shutil.copytree("my_project", "my_project_backup")

# Delete a file
Path("temp_file.txt").unlink(missing_ok=True)

# Delete an empty directory
Path("empty_folder").rmdir()

# Delete a directory with contents (careful!)
shutil.rmtree("old_project")  # Gone forever. No recycle bin. Be careful.
```

> **Warning:** `shutil.rmtree()` permanently deletes a folder and everything in it. No undo. No recycle bin. Triple-check your path before running this. Seriously.

## Practical Recipe 1: File Organizer

Your Downloads folder is chaos. Let's fix that:

```python
from pathlib import Path
import shutil

def organize_downloads():
    """Sort files in Downloads folder by type."""

    downloads = Path.home() / "Downloads"

    # Map extensions to folder names
    categories = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".svg", ".webp", ".ico"],
        "Documents": [".pdf", ".doc", ".docx", ".txt", ".xlsx", ".csv", ".pptx"],
        "Videos": [".mp4", ".avi", ".mkv", ".mov", ".wmv"],
        "Audio": [".mp3", ".wav", ".flac", ".aac"],
        "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
        "Code": [".py", ".js", ".html", ".css", ".json", ".xml"],
        "Installers": [".exe", ".msi", ".dmg"],
    }

    moved_count = 0

    for file in downloads.iterdir():
        if file.is_dir():
            continue  # Skip folders

        # Find which category this file belongs to
        ext = file.suffix.lower()
        target_folder = "Other"  # Default

        for category, extensions in categories.items():
            if ext in extensions:
                target_folder = category
                break

        # Create target folder if it doesn't exist
        target_path = downloads / target_folder
        target_path.mkdir(exist_ok=True)

        # Move the file
        destination = target_path / file.name

        # Handle duplicates
        if destination.exists():
            destination = target_path / f"{file.stem}_copy{file.suffix}"

        shutil.move(str(file), str(destination))
        moved_count += 1
        print(f"  {file.name} -> {target_folder}/")

    print(f"\nDone! Organized {moved_count} files.")

# Run it!
organize_downloads()
```

Run this once and your Downloads folder goes from chaos to organized folders. Run it weekly (or schedule it - we'll get there) and it stays clean forever.

## Bulk File Renaming

Got 200 photos named `IMG_20240315_001.jpg`? Let's fix that:

```python
from pathlib import Path

def rename_photos(folder, prefix="vacation"):
    """Rename all images in a folder with a clean pattern."""

    folder = Path(folder)
    image_extensions = {".jpg", ".jpeg", ".png"}

    # Get all images, sorted by name
    images = sorted(
        f for f in folder.iterdir()
        if f.suffix.lower() in image_extensions
    )

    print(f"Found {len(images)} images")

    for i, image in enumerate(images, 1):
        new_name = f"{prefix}_{i:03d}{image.suffix.lower()}"
        new_path = folder / new_name

        image.rename(new_path)
        print(f"  {image.name} -> {new_name}")

    print(f"\nRenamed {len(images)} files!")

# Example usage:
# rename_photos("C:/Users/you/Photos/Beach Trip", prefix="beach_2024")
# Result: beach_2024_001.jpg, beach_2024_002.jpg, beach_2024_003.jpg...
```

Another common pattern - removing spaces from filenames:

```python
from pathlib import Path

def clean_filenames(folder):
    """Replace spaces and special chars in filenames."""
    folder = Path(folder)

    for file in folder.iterdir():
        if file.is_file():
            clean_name = file.name.replace(" ", "_").replace("(", "").replace(")", "")
            clean_name = clean_name.lower()

            if clean_name != file.name:
                file.rename(folder / clean_name)
                print(f"  '{file.name}' -> '{clean_name}'")
```

## Email Automation

Send emails from Python. Perfect for automated reports, alerts, or notifications.

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(to_email, subject, body):
    """Send an email using Gmail."""

    # Your email credentials
    sender_email = "your_email@gmail.com"
    app_password = "your-app-password"  # NOT your regular password!

    # Create the email
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "html"))

    # Send it
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()  # Encrypt the connection
        server.login(sender_email, app_password)
        server.send_message(msg)

    print(f"Email sent to {to_email}!")

# Usage:
send_email(
    to_email="colleague@example.com",
    subject="Weekly Report - Auto-generated",
    body="""
    <h2>Weekly Sales Report</h2>
    <p>Total sales: <b>$45,230</b></p>
    <p>Growth: <b>+12%</b> vs last week</p>
    <p><i>This report was generated automatically by Python.</i></p>
    """
)
```

> **Important - App Passwords:** Gmail doesn't let you use your regular password with smtplib. You need an **App Password**:
> 1. Go to your Google Account settings
> 2. Security -> 2-Step Verification (enable it if you haven't)
> 3. Search for "App passwords"
> 4. Generate a new app password for "Mail"
> 5. Use that 16-character password in your code
>
> Never hardcode the password. Use environment variables or a `.env` file, just like with API keys.

### Sending Emails with Attachments

```python
from email.mime.base import MIMEBase
from email import encoders
from pathlib import Path

def send_report_with_attachment(to_email, subject, body, attachment_path):
    """Send an email with a file attachment."""

    sender_email = "your_email@gmail.com"
    app_password = "your-app-password"

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "html"))

    # Attach the file
    file_path = Path(attachment_path)
    with open(file_path, "rb") as f:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(f.read())
        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition",
            f"attachment; filename={file_path.name}"
        )
        msg.attach(part)

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, app_password)
        server.send_message(msg)

    print(f"Email with attachment sent to {to_email}!")

# send_report_with_attachment(
#     "boss@company.com",
#     "Monthly Report",
#     "<p>Please find the report attached.</p>",
#     "reports/monthly_report.pdf"
# )
```

## Scheduling Tasks

The `schedule` library makes it easy to run Python functions at specific times:

```bash
pip install schedule
```

```python
import schedule
import time

def morning_report():
    print("Generating morning report...")
    # Your report logic here

def organize_files():
    print("Organizing downloads folder...")
    # Your file organizer logic here

def backup_data():
    print("Backing up data...")
    # Your backup logic here

# Schedule tasks
schedule.every().day.at("09:00").do(morning_report)
schedule.every().friday.at("17:00").do(organize_files)
schedule.every().hour.do(backup_data)

# More scheduling options:
schedule.every(10).minutes.do(lambda: print("Still running!"))
schedule.every().monday.do(lambda: print("Happy Monday!"))
schedule.every().day.at("23:59").do(lambda: print("End of day"))

print("Scheduler running. Press Ctrl+C to stop.")

while True:
    schedule.run_pending()
    time.sleep(60)  # Check every minute
```

The `while True` loop keeps the script running. It checks every 60 seconds if any scheduled task is due. Run this script in the background and your tasks execute automatically.

> **Pro Tip:** For production scheduling on a server, use `cron` (Linux/Mac) or Task Scheduler (Windows) to run your Python scripts. The `schedule` library is great for development and simple automation, but OS-level schedulers are more reliable for 24/7 operation.

## Selenium: Browser Automation

Selenium controls a web browser programmatically. It can click buttons, fill forms, navigate pages, and scrape dynamic content.

```bash
pip install selenium webdriver-manager
```

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up Chrome browser
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Navigate to a website
driver.get("https://www.python.org")

# Find elements and interact
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("list comprehension")
search_box.send_keys(Keys.RETURN)

time.sleep(2)  # Wait for results to load

# Get results
results = driver.find_elements(By.CSS_SELECTOR, ".list-recent-events li")
for result in results[:5]:
    print(result.text)

# Take a screenshot
driver.save_screenshot("python_search.png")

# Close the browser
driver.quit()
```

### Practical Example: Automated Form Filler

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

def fill_form(data):
    """Fill out a web form automatically."""

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        driver.get("https://example.com/form")

        # Wait for the form to load
        wait = WebDriverWait(driver, 10)

        # Fill in fields
        name_field = wait.until(EC.presence_of_element_located((By.ID, "name")))
        name_field.send_keys(data["name"])

        email_field = driver.find_element(By.ID, "email")
        email_field.send_keys(data["email"])

        message_field = driver.find_element(By.ID, "message")
        message_field.send_keys(data["message"])

        # Click submit
        submit_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        submit_btn.click()

        time.sleep(2)
        print("Form submitted successfully!")

    finally:
        driver.quit()

# fill_form({
#     "name": "Alex Smith",
#     "email": "alex@example.com",
#     "message": "This was submitted by a Python script!"
# })
```

> **Pro Tip:** Selenium is powerful but slow compared to `requests`. Use `requests` for APIs and simple page scraping (Chapter 21). Use Selenium only when you need to interact with JavaScript-heavy pages, click buttons, or fill forms.

## Practical Recipe 2: Automated Report Generator

Combine pandas, matplotlib, and email into one automated workflow:

```python
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from datetime import datetime

def generate_weekly_report():
    """Generate a sales report with chart and summary."""

    # Step 1: Load/generate data
    data = pd.DataFrame({
        "day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
        "sales": [1200, 1450, 1380, 1560, 1890, 2100, 1750],
        "visitors": [450, 520, 490, 580, 620, 710, 590]
    })

    # Step 2: Calculate stats
    total_sales = data["sales"].sum()
    avg_sales = data["sales"].mean()
    best_day = data.loc[data["sales"].idxmax(), "day"]
    conversion_rate = (data["sales"].sum() / data["visitors"].sum() * 100)

    # Step 3: Create chart
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    ax1.bar(data["day"], data["sales"], color="steelblue", edgecolor="black")
    ax1.set_title("Daily Sales", fontweight="bold")
    ax1.set_ylabel("Sales ($)")

    ax2.plot(data["day"], data["visitors"], marker="o", color="coral", linewidth=2)
    ax2.set_title("Daily Visitors", fontweight="bold")
    ax2.set_ylabel("Visitors")
    ax2.grid(True, alpha=0.3)

    fig.suptitle(f"Weekly Report - {datetime.now().strftime('%B %d, %Y')}",
                 fontsize=14, fontweight="bold")
    plt.tight_layout()

    chart_path = Path("weekly_report.png")
    plt.savefig(chart_path, dpi=150, bbox_inches="tight")
    plt.close()

    # Step 4: Create email body
    report_html = f"""
    <h2>Weekly Sales Report</h2>
    <p>Generated: {datetime.now().strftime('%B %d, %Y at %I:%M %p')}</p>
    <table border="1" cellpadding="8" style="border-collapse: collapse;">
        <tr><td><b>Total Sales</b></td><td>${total_sales:,}</td></tr>
        <tr><td><b>Daily Average</b></td><td>${avg_sales:,.0f}</td></tr>
        <tr><td><b>Best Day</b></td><td>{best_day}</td></tr>
        <tr><td><b>Conversion Rate</b></td><td>{conversion_rate:.1f}%</td></tr>
    </table>
    <p><i>Chart attached. This report was auto-generated with Python.</i></p>
    """

    print(f"Report generated!")
    print(f"Total Sales: ${total_sales:,}")
    print(f"Best Day: {best_day}")
    print(f"Chart saved: {chart_path}")

    # Step 5: Send email (uncomment when ready)
    # send_report_with_attachment(
    #     "boss@company.com",
    #     f"Weekly Sales Report - {datetime.now().strftime('%B %d')}",
    #     report_html,
    #     str(chart_path)
    # )

    return report_html

generate_weekly_report()
```

## Practical Recipe 3: Watchdog - Monitor a Folder for Changes

```python
# pip install watchdog
from pathlib import Path
import time
import shutil

def watch_folder(watch_path, process_func, check_interval=5):
    """Watch a folder and process new files."""

    watch_path = Path(watch_path)
    seen_files = set(f.name for f in watch_path.iterdir() if f.is_file())

    print(f"Watching {watch_path} for new files...")
    print(f"Currently {len(seen_files)} files. Waiting for new ones...")

    try:
        while True:
            current_files = set(f.name for f in watch_path.iterdir() if f.is_file())
            new_files = current_files - seen_files

            for filename in new_files:
                filepath = watch_path / filename
                print(f"\nNew file detected: {filename}")
                process_func(filepath)

            seen_files = current_files
            time.sleep(check_interval)

    except KeyboardInterrupt:
        print("\nStopped watching.")

def process_new_file(filepath):
    """What to do when a new file appears."""
    print(f"  Processing: {filepath.name}")
    print(f"  Size: {filepath.stat().st_size} bytes")
    print(f"  Type: {filepath.suffix}")

    # Example: move PDFs to a reports folder
    if filepath.suffix.lower() == ".pdf":
        dest = Path.home() / "Documents" / "AutoReports" / filepath.name
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(str(filepath), str(dest))
        print(f"  Copied to: {dest}")

# watch_folder(Path.home() / "Downloads", process_new_file)
```

> **Fun Fact:** The original name for Python came from Monty Python's Flying Circus, not the snake. Guido van Rossum, Python's creator, was a fan of the show and wanted a name that was "short, unique, and slightly mysterious." The snake imagery came later, but the language was named after a bunch of British comedians doing silly sketches. Which honestly explains a lot about Python's personality.

## Putting It All Together

Here's the ultimate automation combo - a scheduled script that:
1. Organizes your Downloads folder
2. Generates a report
3. Emails it to you

```python
import schedule
import time

def daily_automation():
    """Run all daily automation tasks."""
    print("\n-- Running Daily Automation --")

    # 1. Organize downloads
    print("\n1. Organizing files...")
    # organize_downloads()  # From earlier in this chapter

    # 2. Generate report
    print("\n2. Generating report...")
    # generate_weekly_report()  # From earlier in this chapter

    # 3. Send email
    print("\n3. Sending report...")
    # send_email(...)  # From earlier in this chapter

    print("\n-- Daily Automation Complete --")

# Run every weekday at 9 AM
schedule.every().monday.at("09:00").do(daily_automation)
schedule.every().tuesday.at("09:00").do(daily_automation)
schedule.every().wednesday.at("09:00").do(daily_automation)
schedule.every().thursday.at("09:00").do(daily_automation)
schedule.every().friday.at("09:00").do(daily_automation)

print("Automation scheduler running...")
print("Tasks scheduled for weekdays at 9:00 AM")
print("Press Ctrl+C to stop\n")

while True:
    schedule.run_pending()
    time.sleep(60)
```

## Your Turn: Automated Report Emailer

Create `auto_report.py` that combines everything from this chapter:

```python
# 1. Create a function that scans a folder and counts files by type
#    (how many PDFs, images, CSVs, etc.)

# 2. Create a function that generates a bar chart of the file counts

# 3. Create a function that formats the results as an HTML email body

# 4. (Optional) Set up email sending with smtplib

# 5. (Optional) Schedule it to run every Friday at 5 PM

# Starter code:
from pathlib import Path
import matplotlib.pyplot as plt
from collections import Counter
from datetime import datetime

def scan_folder(folder_path):
    """Count files by extension in a folder."""
    folder = Path(folder_path)
    extensions = Counter()

    for file in folder.iterdir():
        if file.is_file():
            ext = file.suffix.lower() if file.suffix else "no extension"
            extensions[ext] += 1

    return dict(extensions.most_common(10))  # Top 10 types

def create_chart(file_counts, output_path="folder_report.png"):
    """Create a bar chart of file types."""
    # Your code here: plt.bar(), labels, title, save
    pass

def create_email_body(folder_path, file_counts):
    """Generate an HTML email with the report."""
    # Your code here: HTML table with file counts
    pass

# Test it
counts = scan_folder(Path.home() / "Downloads")
print(counts)
# {'.pdf': 23, '.jpg': 45, '.xlsx': 12, ...}
```

## TL;DR

- **pathlib** is the modern way to work with files: `Path.home() / "Downloads"`, `path.glob("*.pdf")`
- **shutil** handles moving, copying, and deleting files and folders
- Bulk rename files with loops: `path.rename(new_path)`
- **smtplib** sends emails from Python - use App Passwords for Gmail, never hardcode credentials
- **schedule** runs functions at specific times: `schedule.every().day.at("09:00").do(task)`
- **Selenium** automates web browsers: clicking, typing, filling forms, taking screenshots
- Combine pandas + matplotlib + email for automated reporting pipelines
- Automation gets better over time - start with one annoying task, automate it, then add more
- Be careful with `shutil.rmtree()` - it permanently deletes folders with no undo
- You just learned to make your computer work while you sleep. Welcome to the good life.
