"""
Chapter 32: Automation — SOLUTION
====================================

Your Downloads folder is now sparkling clean!
This is genuinely useful — you could run this on your actual
Downloads folder and finally achieve inbox zero... for files.

Just point it at any directory and let Python do the sorting!
"""

import os
import shutil
from pathlib import Path
from collections import defaultdict

# Category mapping: folder name -> list of extensions
CATEGORIES = {
    "documents": [".pdf", ".doc", ".docx", ".txt", ".pptx", ".ppt",
                   ".xlsx", ".xls", ".odt", ".rtf", ".tex"],
    "images":    [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg",
                   ".webp", ".ico", ".tiff", ".raw"],
    "code":      [".py", ".js", ".html", ".css", ".java", ".cpp",
                   ".c", ".h", ".rb", ".go", ".rs", ".ts", ".jsx",
                   ".tsx", ".php", ".sh", ".bat"],
    "data":      [".csv", ".json", ".xml", ".sql", ".db", ".sqlite",
                   ".yaml", ".yml", ".toml"],
    "audio":     [".mp3", ".wav", ".flac", ".aac", ".ogg", ".wma", ".m4a"],
    "video":     [".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv", ".webm"],
    "archives":  [".zip", ".tar", ".gz", ".rar", ".7z", ".bz2"],
}


def get_category(filename):
    """Return the category folder name for a given filename."""
    suffix = Path(filename).suffix.lower()
    for category, extensions in CATEGORIES.items():
        if suffix in extensions:
            return category
    return "other"


def create_messy_directory(base_path):
    """Create a directory with various file types for testing."""
    base_path = Path(base_path)

    # Clean up if exists
    if base_path.exists():
        shutil.rmtree(base_path)
    base_path.mkdir(parents=True)

    # Sample files (we create them with dummy content)
    sample_files = {
        "quarterly_report.pdf": "PDF content here",
        "vacation_photo.jpg": "JPEG data",
        "family_photo.png": "PNG data",
        "sunset.gif": "GIF data",
        "automation_script.py": "print('Hello!')",
        "website.html": "<html><body>Hello</body></html>",
        "styles.css": "body { color: red; }",
        "app.js": "console.log('Hello');",
        "sales_data.csv": "month,sales\nJan,1000\nFeb,1200",
        "config.json": '{"key": "value"}',
        "database.sql": "SELECT * FROM users;",
        "favorite_song.mp3": "MP3 audio data",
        "podcast.wav": "WAV audio data",
        "tutorial_video.mp4": "MP4 video data",
        "meeting_notes.txt": "Discussed the project timeline.",
        "presentation.pptx": "PowerPoint data",
        "spreadsheet.xlsx": "Excel data",
        "project.zip": "ZIP archive data",
        "mystery_file.xyz": "What even is this?",
        "readme.md": "# Project Readme",
    }

    for filename, content in sample_files.items():
        (base_path / filename).write_text(content)

    return list(sample_files.keys())


def organize_files(directory, dry_run=False):
    """
    Organize files in a directory into subfolders by type.

    Args:
        directory: Path to the directory to organize
        dry_run: If True, only show what would happen (don't move files)

    Returns:
        Dictionary of {category: [files_moved]}
    """
    directory = Path(directory)
    if not directory.exists():
        print(f"Directory not found: {directory}")
        return {}

    mode = "DRY RUN" if dry_run else "ORGANIZING"
    print(f"{'=' * 50}")
    print(f"  FILE ORGANIZER ({mode})")
    print(f"{'=' * 50}")
    print(f"  Directory: {directory}")
    print()

    # Track what we move
    moved = defaultdict(list)
    skipped = []

    # Loop through all items in the directory
    for item in sorted(directory.iterdir()):
        # Skip directories (we only organize files)
        if item.is_dir():
            skipped.append(item.name)
            continue

        # Determine the category
        category = get_category(item.name)
        category_dir = directory / category

        if dry_run:
            # Just show what would happen
            print(f"  {item.name:30s} -> {category}/")
            moved[category].append(item.name)
        else:
            # Create category folder if needed
            category_dir.mkdir(exist_ok=True)

            # Move the file
            destination = category_dir / item.name

            # Handle filename conflicts
            if destination.exists():
                stem = item.stem
                suffix = item.suffix
                counter = 1
                while destination.exists():
                    destination = category_dir / f"{stem}_{counter}{suffix}"
                    counter += 1

            shutil.move(str(item), str(destination))
            print(f"  Moved: {item.name:30s} -> {category}/{destination.name}")
            moved[category].append(destination.name)

    # Print summary
    print(f"\n{'=' * 50}")
    print("  SUMMARY")
    print(f"{'=' * 50}")

    total = 0
    for category, files in sorted(moved.items()):
        print(f"  {category:15s}: {len(files)} files")
        total += len(files)

    if skipped:
        print(f"  {'(skipped dirs)':15s}: {len(skipped)}")

    print(f"  {'TOTAL':15s}: {total} files organized")
    print()

    return dict(moved)


# ============================================================
# MAIN
# ============================================================
if __name__ == "__main__":
    base = Path(__file__).parent.resolve() / "messy_downloads"

    # Step 1: Create the messy directory
    print("Creating messy directory with sample files...\n")
    files = create_messy_directory(base)

    print(f"Files in messy directory ({len(files)} files):")
    for f in sorted(base.iterdir()):
        category = get_category(f.name)
        print(f"  {f.name:30s}  [{category}]")
    print()

    # Step 2: Dry run first (always a good idea!)
    organize_files(base, dry_run=True)

    # Step 3: Do it for real!
    organize_files(base, dry_run=False)

    # Step 4: Show the organized structure
    print("ORGANIZED STRUCTURE:")
    print(f"{'=' * 50}")
    for folder in sorted(base.iterdir()):
        if folder.is_dir():
            files_in_folder = list(folder.iterdir())
            print(f"\n  {folder.name}/ ({len(files_in_folder)} files)")
            for f in sorted(files_in_folder):
                print(f"    {f.name}")
    print()

    # Cleanup
    shutil.rmtree(base)
    print(f"Cleaned up demo directory: {base}")
    print("\nNow go point this at your real Downloads folder!")
    print("(Just change the 'base' path and remove the cleanup step)")
