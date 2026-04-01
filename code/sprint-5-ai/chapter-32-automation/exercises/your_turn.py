"""
Chapter 32: Automation — YOUR TURN!
=====================================

Build an Automated File Organizer!

You know that Downloads folder that's a complete disaster?
Let's fix that with Python! Your script will sort files into
subfolders based on their file extension.

Before:
  downloads/
    report.pdf
    vacation.jpg
    script.py
    data.csv
    song.mp3
    notes.txt
    presentation.pptx
    photo.png

After:
  downloads/
    documents/    -> .pdf, .doc, .docx, .txt, .pptx, .xlsx
    images/       -> .jpg, .jpeg, .png, .gif, .bmp, .svg
    code/         -> .py, .js, .html, .css, .java, .cpp
    data/         -> .csv, .json, .xml, .sql
    audio/        -> .mp3, .wav, .flac, .aac
    video/        -> .mp4, .avi, .mkv, .mov
    other/        -> everything else

TASKS:
1. Create a sample "messy" directory with fake files
2. Define the category mapping (extension -> folder)
3. Loop through all files in the directory
4. Create category folders as needed
5. Move each file to the correct folder
6. Print a summary of what was moved
7. BONUS: Add a "dry run" mode that shows what WOULD happen
"""

import os
import shutil
from pathlib import Path

# TODO 1: Define the category mapping
# Dictionary: category_name -> list of extensions
# Example: {"images": [".jpg", ".jpeg", ".png", ...], ...}
CATEGORIES = {
    # Fill these in!
}

# TODO 2: Create a function to determine the category for a file
def get_category(filename):
    """Return the category folder name for a given filename."""
    # Hint: Get the suffix with Path(filename).suffix.lower()
    # Loop through CATEGORIES to find a match
    # Return "other" if no match found
    pass

# TODO 3: Create a sample messy directory with fake files
def create_messy_directory(base_path):
    """Create a directory with various file types for testing."""
    # Create the directory
    # Create sample files (just empty files for testing):
    #   report.pdf, vacation.jpg, script.py, data.csv,
    #   song.mp3, notes.txt, presentation.pptx, photo.png,
    #   movie.mp4, styles.css, app.js, database.sql
    pass

# TODO 4: Build the file organizer function
def organize_files(directory, dry_run=False):
    """
    Organize files in a directory into subfolders by type.

    Args:
        directory: Path to the directory to organize
        dry_run: If True, only show what would happen (don't move files)
    """
    # Convert to Path object
    # Loop through files (not directories!) in the directory
    # For each file:
    #   1. Get its category
    #   2. Create the category folder if it doesn't exist
    #   3. Move the file (or print what would happen if dry_run)
    # Print a summary
    pass


# TODO 5: Run it!
if __name__ == "__main__":
    base = Path(__file__).parent.resolve() / "messy_downloads"

    # Create the messy directory
    create_messy_directory(base)
    print("Before organizing:")
    for f in sorted(base.iterdir()):
        print(f"  {f.name}")
    print()

    # Organize! (try dry_run=True first)
    organize_files(base, dry_run=True)

    # Then do it for real
    # organize_files(base, dry_run=False)

    # Cleanup (optional)
    # shutil.rmtree(base)
