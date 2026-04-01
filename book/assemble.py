"""Assemble all chapter Markdown files into a single manuscript."""
import os
import glob

BOOK_ORDER = [
    # Front Matter
    "front-matter/title-page.md",
    "front-matter/copyright.md",
    "front-matter/dedication.md",
    "front-matter/how-to-use-this-book.md",
    "front-matter/what-you-need.md",

    # Sprint 1
    "sprint-1/sprint-1-intro.md",
    "sprint-1/chapter-01.md",
    "sprint-1/chapter-02.md",
    "sprint-1/chapter-03.md",
    "sprint-1/chapter-04.md",
    "sprint-1/chapter-05.md",
    "sprint-1/chapter-06.md",
    "sprint-1/chapter-07.md",
    "sprint-1/chapter-08.md",
    "sprint-1/sprint-1-checkpoint.md",

    # Sprint 2
    "sprint-2/sprint-2-intro.md",
    "sprint-2/chapter-09.md",
    "sprint-2/chapter-10.md",
    "sprint-2/chapter-11.md",
    "sprint-2/chapter-12.md",
    "sprint-2/chapter-13.md",
    "sprint-2/chapter-14.md",
    "sprint-2/sprint-2-checkpoint.md",

    # Sprint 3
    "sprint-3/sprint-3-intro.md",
    "sprint-3/chapter-15.md",
    "sprint-3/chapter-16.md",
    "sprint-3/chapter-17.md",
    "sprint-3/chapter-18.md",
    "sprint-3/sprint-3-checkpoint.md",

    # Sprint 4
    "sprint-4/sprint-4-intro.md",
    "sprint-4/chapter-19.md",
    "sprint-4/chapter-20.md",
    "sprint-4/chapter-21.md",
    "sprint-4/chapter-22.md",
    "sprint-4/chapter-23.md",
    "sprint-4/chapter-24.md",
    "sprint-4/chapter-25.md",
    "sprint-4/sprint-4-checkpoint.md",

    # Sprint 5
    "sprint-5/sprint-5-intro.md",
    "sprint-5/chapter-26.md",
    "sprint-5/chapter-27.md",
    "sprint-5/chapter-28.md",
    "sprint-5/chapter-29.md",
    "sprint-5/chapter-30.md",
    "sprint-5/chapter-31.md",
    "sprint-5/chapter-32.md",
    "sprint-5/sprint-5-checkpoint.md",

    # Final Projects
    "final-projects/final-zone-intro.md",
    "final-projects/project-01.md",
    "final-projects/project-02.md",
    "final-projects/project-03.md",
    "final-projects/project-04.md",
    "final-projects/project-05.md",
    "final-projects/project-06.md",
    "final-projects/project-07.md",
    "final-projects/project-08.md",
    "final-projects/project-09.md",
    "final-projects/project-10.md",

    # Back Matter
    "back-matter/appendix-a-cheat-sheet.md",
    "back-matter/appendix-b-common-errors.md",
    "back-matter/appendix-c-what-next.md",
    "back-matter/appendix-d-resources.md",
    "back-matter/about-author.md",
]

book_dir = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(book_dir, "manuscript.md")

missing = []
found = 0

with open(output_path, "w", encoding="utf-8") as out:
    for filename in BOOK_ORDER:
        filepath = os.path.join(book_dir, filename)
        if os.path.exists(filepath):
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            out.write(content)
            if not content.endswith("\n"):
                out.write("\n")
            out.write("\n---\n\n")
            found += 1
        else:
            missing.append(filename)
            print(f"  WARNING: Missing file: {filename}")

# Count words
with open(output_path, "r", encoding="utf-8") as f:
    word_count = len(f.read().split())

print(f"\nManuscript assembled: {output_path}")
print(f"Files included: {found}/{len(BOOK_ORDER)}")
if missing:
    print(f"Missing files: {len(missing)}")
print(f"Total words: {word_count:,}")
