"""
Chapter 14 Exercise SOLUTION: Student Grade Processor
======================================================
A complete student grade processor using map, filter, and reduce.
Functional programming at its finest -- report cards have never
looked this good!
"""

from functools import reduce

# Student data -- each student has a name and list of scores
students = [
    {"name": "Alice", "scores": [92, 88, 95, 90]},
    {"name": "Bob", "scores": [55, 62, 48, 70]},
    {"name": "Charlie", "scores": [78, 82, 75, 80]},
    {"name": "Diana", "scores": [98, 95, 100, 97]},
    {"name": "Eve", "scores": [45, 52, 38, 41]},
    {"name": "Frank", "scores": [88, 72, 65, 81]},
    {"name": "Grace", "scores": [60, 65, 58, 63]},
]


def get_letter_grade(avg):
    """Convert a numeric average to a letter grade."""
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"


def process_students(students):
    """Process student data using map, filter, and reduce. The functional way!"""

    # -------------------------------------------------------------------------
    # STEP 1: Calculate averages using map()
    # {**s} unpacks the existing dict, then we add the "avg" key
    # -------------------------------------------------------------------------
    students_with_avg = list(map(
        lambda s: {**s, "avg": sum(s["scores"]) / len(s["scores"])},
        students
    ))

    print("STEP 1: Calculated Averages")
    print("-" * 45)
    for s in students_with_avg:
        print(f"  {s['name']:<10} Scores: {s['scores']}  Avg: {s['avg']:.1f}")

    # -------------------------------------------------------------------------
    # STEP 2: Filter passing students (avg >= 60)
    # -------------------------------------------------------------------------
    passing = list(filter(
        lambda s: s["avg"] >= 60,
        students_with_avg
    ))

    failing = list(filter(
        lambda s: s["avg"] < 60,
        students_with_avg
    ))

    print(f"\nSTEP 2: Passing Students ({len(passing)}/{len(students_with_avg)})")
    print("-" * 45)
    for s in passing:
        print(f"  {s['name']:<10} Avg: {s['avg']:.1f}  -- PASS")
    for s in failing:
        print(f"  {s['name']:<10} Avg: {s['avg']:.1f}  -- FAIL")

    # -------------------------------------------------------------------------
    # STEP 3: Find the top student using reduce()
    # -------------------------------------------------------------------------
    top_student = reduce(
        lambda a, b: a if a["avg"] > b["avg"] else b,
        students_with_avg
    )

    # Also find the student who needs the most help
    bottom_student = reduce(
        lambda a, b: a if a["avg"] < b["avg"] else b,
        students_with_avg
    )

    print(f"\nSTEP 3: Top & Bottom Students")
    print("-" * 45)
    print(f"  Top student:    {top_student['name']} ({top_student['avg']:.1f})")
    print(f"  Needs help:     {bottom_student['name']} ({bottom_student['avg']:.1f})")

    # Class average using reduce
    class_total = reduce(lambda acc, s: acc + s["avg"], students_with_avg, 0)
    class_avg = class_total / len(students_with_avg)
    print(f"  Class average:  {class_avg:.1f}")

    # -------------------------------------------------------------------------
    # STEP 4: Assign letter grades using map()
    # -------------------------------------------------------------------------
    students_with_grades = list(map(
        lambda s: {**s, "grade": get_letter_grade(s["avg"])},
        students_with_avg
    ))

    # -------------------------------------------------------------------------
    # STEP 5: Print the beautiful report card!
    # -------------------------------------------------------------------------
    print(f"\nSTEP 4 & 5: Final Report Card")
    print("=" * 55)
    print(f"  {'Name':<10} {'Average':>8} {'Grade':>6} {'Status':>10}")
    print("  " + "-" * 50)

    # Sort by average (highest first) using sorted + lambda
    sorted_students = sorted(students_with_grades, key=lambda s: s["avg"], reverse=True)

    for s in sorted_students:
        status = "PASS" if s["avg"] >= 60 else "FAIL"
        # Add some flair based on grade
        emoji_map = {"A": "(!!)", "B": "(!)", "C": "(.)", "D": "(...)", "F": "(x)"}
        flair = emoji_map.get(s["grade"], "")

        print(f"  {s['name']:<10} {s['avg']:>7.1f} {s['grade']:>6} {status:>10} {flair}")

    print("  " + "-" * 50)
    print(f"  Class Average: {class_avg:.1f} ({get_letter_grade(class_avg)})")
    print("=" * 55)

    # Grade distribution using reduce
    print("\n  Grade Distribution:")
    for grade in ["A", "B", "C", "D", "F"]:
        count = len(list(filter(lambda s: s["grade"] == grade, students_with_grades)))
        bar = "#" * (count * 4)
        print(f"    {grade}: {bar} ({count})")

    # Summary stats
    all_scores = reduce(lambda acc, s: acc + s["scores"], students, [])
    print(f"\n  Summary:")
    print(f"    Total students: {len(students)}")
    print(f"    Total scores graded: {len(all_scores)}")
    print(f"    Highest single score: {max(all_scores)}")
    print(f"    Lowest single score: {min(all_scores)}")
    print(f"    Pass rate: {len(passing)/len(students)*100:.0f}%")


# Run the processor!
if __name__ == "__main__":
    print()
    print("  STUDENT GRADE PROCESSOR")
    print("  'Where functional programming meets report cards'")
    print()
    process_students(students)
    print("\n  Remember: grades don't define you, but clean code does!")
