"""
Chapter 32: Automation — Making Python Do Your Boring Stuff
=============================================================

Why do something manually when Python can do it for you?

Automation is the art of making your computer handle repetitive tasks:
  - Organizing files into folders
  - Sending emails automatically
  - Scraping websites
  - Running tasks on a schedule

This is the chapter where Python becomes your personal assistant.
You write the script once, and it works for you forever!
"""

import os
import shutil
import time
from pathlib import Path
from datetime import datetime

# ============================================================
# 1. FILE OPERATIONS WITH os, shutil, and pathlib
# ============================================================
# Three modules, three levels of sophistication:
#   os: The classic. Low-level file operations.
#   shutil: Shell utilities. Copy, move, and delete with ease.
#   pathlib: The modern way. Object-oriented paths. Beautiful!

print("=" * 60)
print("FILE OPERATIONS")
print("=" * 60)

# --- pathlib: The Modern Approach ---
# pathlib turns file paths into objects with methods.
# Instead of os.path.join("folder", "file.txt"),
# you write Path("folder") / "file.txt". Much cleaner!

# Get current directory
current_dir = Path(__file__).parent.resolve()
demo_dir = current_dir / "automation_demo"

# Create a directory (exist_ok=True means no error if it already exists)
demo_dir.mkdir(exist_ok=True)
print(f"Created demo directory: {demo_dir}")

# Create some files to play with
sample_files = {
    "report.txt": "Monthly sales report for Q4",
    "data.csv": "name,age,city\nAlice,25,NYC\nBob,30,LA",
    "notes.txt": "Remember to review the PR",
    "photo.txt": "(pretend this is a photo)",  # .txt for safety
    "script.py": "print('Hello, automation!')",
}

for filename, content in sample_files.items():
    filepath = demo_dir / filename
    filepath.write_text(content)
    print(f"  Created: {filepath.name}")
print()

# --- Listing files ---
print("Files in demo directory:")
for item in demo_dir.iterdir():
    size = item.stat().st_size
    print(f"  {item.name:20s} ({size} bytes)")
print()

# --- Path properties ---
example_path = demo_dir / "report.txt"
print(f"Full path:  {example_path}")
print(f"Name:       {example_path.name}")
print(f"Stem:       {example_path.stem}")         # Name without extension
print(f"Suffix:     {example_path.suffix}")        # Extension
print(f"Parent:     {example_path.parent}")
print(f"Exists?     {example_path.exists()}")
print()

# --- Glob: Find files matching a pattern ---
print("All .txt files:")
for txt_file in demo_dir.glob("*.txt"):
    print(f"  {txt_file.name}")
print()


# ============================================================
# 2. COPY, MOVE, RENAME
# ============================================================
print("=" * 60)
print("COPY, MOVE, RENAME")
print("=" * 60)

# Copy a file
backup_dir = demo_dir / "backup"
backup_dir.mkdir(exist_ok=True)

src = demo_dir / "report.txt"
dst = backup_dir / "report_backup.txt"
shutil.copy2(src, dst)  # copy2 preserves metadata
print(f"Copied: {src.name} -> {dst}")

# Rename a file
old_name = demo_dir / "notes.txt"
new_name = demo_dir / "meeting_notes.txt"
if old_name.exists():
    old_name.rename(new_name)
    print(f"Renamed: notes.txt -> meeting_notes.txt")

# Move a file
file_to_move = demo_dir / "data.csv"
moved_file = backup_dir / "data.csv"
if file_to_move.exists():
    shutil.move(str(file_to_move), str(moved_file))
    print(f"Moved: data.csv -> backup/data.csv")
print()


# ============================================================
# 3. BULK RENAME — A Real-World Use Case
# ============================================================
# Imagine you have 100 photos named IMG_001.jpg, IMG_002.jpg, etc.
# You want to rename them to vacation_001.jpg, vacation_002.jpg.

print("=" * 60)
print("BULK RENAME")
print("=" * 60)

# Create sample files to rename
bulk_dir = demo_dir / "photos"
bulk_dir.mkdir(exist_ok=True)

for i in range(1, 6):
    (bulk_dir / f"IMG_{i:03d}.txt").write_text(f"Photo {i}")

print("Before rename:")
for f in sorted(bulk_dir.iterdir()):
    print(f"  {f.name}")

# Bulk rename!
for filepath in sorted(bulk_dir.glob("IMG_*.txt")):
    new_name = filepath.name.replace("IMG_", "vacation_")
    filepath.rename(filepath.parent / new_name)

print("\nAfter rename:")
for f in sorted(bulk_dir.iterdir()):
    print(f"  {f.name}")
print()


# ============================================================
# 4. EMAIL WITH smtplib
# ============================================================
# Sending emails from Python! This is incredibly useful for
# automated reports, alerts, and notifications.
#
# NOTE: For Gmail, you need an "App Password" (not your regular password).
# Go to: Google Account > Security > 2-Step Verification > App Passwords

print("=" * 60)
print("EMAIL WITH smtplib")
print("=" * 60)

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(to_email, subject, body, sender_email=None, sender_password=None):
    """
    Send an email using Gmail's SMTP server.

    NOTE: This is the STRUCTURE of how email sending works.
    To actually send emails, you need:
    1. A Gmail account with 2FA enabled
    2. An App Password (not your regular password!)
    3. Set environment variables:
       GMAIL_ADDRESS=your-email@gmail.com
       GMAIL_APP_PASSWORD=your-app-password
    """
    sender_email = sender_email or os.getenv("GMAIL_ADDRESS")
    sender_password = sender_password or os.getenv("GMAIL_APP_PASSWORD")

    if not sender_email or not sender_password:
        print("  [DEMO] Email would be sent:")
        print(f"    To: {to_email}")
        print(f"    Subject: {subject}")
        print(f"    Body: {body[:100]}...")
        return False

    # Create the email
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        # Connect to Gmail's SMTP server
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()                          # Secure the connection
            server.login(sender_email, sender_password)  # Login
            server.send_message(msg)                     # Send!
        print(f"  Email sent to {to_email}!")
        return True
    except Exception as e:
        print(f"  Failed to send email: {e}")
        return False

# Demo (won't actually send without credentials)
send_email(
    to_email="colleague@example.com",
    subject="Weekly Report - Automated",
    body="Hi!\n\nHere's the automated weekly report.\n\nBest,\nPython Bot"
)
print()


# ============================================================
# 5. SCHEDULING WITH schedule
# ============================================================
# The 'schedule' library lets you run functions at specific times.
# Like cron jobs, but in Python and way more readable!

print("=" * 60)
print("SCHEDULING")
print("=" * 60)

try:
    import schedule
    HAS_SCHEDULE = True
except ImportError:
    HAS_SCHEDULE = False
    print("schedule not installed. Run: pip install schedule\n")

if HAS_SCHEDULE:
    # Define tasks
    def morning_report():
        print(f"  [TASK] Morning report generated at {datetime.now().strftime('%H:%M:%S')}")

    def backup_files():
        print(f"  [TASK] Files backed up at {datetime.now().strftime('%H:%M:%S')}")

    def send_reminder():
        print(f"  [TASK] Reminder sent at {datetime.now().strftime('%H:%M:%S')}")

    # Schedule tasks (these are examples — we won't run the loop long)
    schedule.every(10).seconds.do(morning_report)   # Every 10 seconds
    schedule.every().hour.do(backup_files)           # Every hour
    schedule.every().day.at("09:00").do(send_reminder)  # Every day at 9 AM

    print("Scheduled tasks:")
    for job in schedule.get_jobs():
        print(f"  {job}")
    print()

    # Run for a short demo (normally this would run forever)
    print("Running scheduler for 5 seconds...")
    end_time = time.time() + 5
    while time.time() < end_time:
        schedule.run_pending()
        time.sleep(1)

    # Clear all jobs (cleanup)
    schedule.clear()
    print("Scheduler stopped.\n")
else:
    print("""
DEMO: The schedule library:

    import schedule

    def daily_report():
        print("Generating daily report...")

    schedule.every().day.at("09:00").do(daily_report)
    schedule.every(30).minutes.do(check_emails)
    schedule.every().monday.at("08:00").do(weekly_meeting_reminder)

    # Run the scheduler
    while True:
        schedule.run_pending()
        time.sleep(60)
""")


# ============================================================
# 6. SELENIUM — Browser Automation
# ============================================================
# Selenium controls a real web browser from Python.
# It can click buttons, fill forms, take screenshots — anything
# you can do in a browser, Selenium can do programmatically.
#
# Think of it as a robot that uses your computer for you!

print("=" * 60)
print("SELENIUM — Browser Automation")
print("=" * 60)

try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    HAS_SELENIUM = True
except ImportError:
    HAS_SELENIUM = False

if HAS_SELENIUM:
    print("""
Selenium is installed! Here's how to use it:

NOTE: You also need a browser driver (like ChromeDriver).
      Modern selenium can auto-download it.
""")
    # We'll show the code but not run it (needs a browser)
    print("Example: Searching Google with Selenium")
    print("""
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys

    # Open a browser
    driver = webdriver.Chrome()

    # Navigate to a website
    driver.get("https://www.google.com")

    # Find the search box and type something
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Python automation tutorial")
    search_box.send_keys(Keys.RETURN)

    # Wait for results
    import time
    time.sleep(2)

    # Take a screenshot!
    driver.save_screenshot("search_results.png")

    # Get all result titles
    results = driver.find_elements(By.CSS_SELECTOR, "h3")
    for result in results[:5]:
        print(result.text)

    # Close the browser
    driver.quit()
    """)
else:
    print("""
Selenium is not installed. Run: pip install selenium

Selenium example (open browser, search, screenshot):

    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys

    driver = webdriver.Chrome()             # Open Chrome
    driver.get("https://www.google.com")    # Go to Google

    # Find search box, type query, press Enter
    search = driver.find_element(By.NAME, "q")
    search.send_keys("Python automation")
    search.send_keys(Keys.RETURN)

    driver.save_screenshot("results.png")   # Screenshot!
    driver.quit()                           # Close browser

Common Selenium actions:
    driver.find_element(By.ID, "login-button").click()
    driver.find_element(By.NAME, "email").send_keys("user@email.com")
    driver.find_element(By.CSS_SELECTOR, ".submit-btn").click()
    driver.find_element(By.XPATH, "//a[@href='/about']").click()
""")
print()


# ============================================================
# CLEANUP
# ============================================================
print("=" * 60)
print("CLEANUP")
print("=" * 60)

# Remove the demo directory and all its contents
if demo_dir.exists():
    shutil.rmtree(demo_dir)
    print(f"Cleaned up: {demo_dir}")
print()


# ============================================================
# RECAP
# ============================================================
print("=" * 60)
print("CHAPTER 32 RECAP")
print("=" * 60)
print("""
You now have the tools to automate just about anything:

1. File Operations (pathlib, shutil, os):
   - Create, copy, move, rename, delete files
   - Bulk operations with glob patterns
   - Path objects for clean, readable code

2. Email (smtplib):
   - Send automated emails and notifications
   - Use App Passwords for Gmail security

3. Scheduling (schedule library):
   - Run functions at specific times/intervals
   - schedule.every().day.at("09:00").do(task)

4. Browser Automation (Selenium):
   - Control a browser programmatically
   - Fill forms, click buttons, take screenshots
   - Web scraping for dynamic JavaScript sites

Automation motto: "If you do it more than twice, automate it!"

Next up: The Checkpoint — putting it ALL together with an
AI-Powered Resume Analyzer!
""")
