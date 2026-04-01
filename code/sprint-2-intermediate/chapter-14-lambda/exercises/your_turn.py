"""
Chapter 14 Exercise: Student Grade Processor
=============================================
Use map, filter, and reduce to process student data!

Given a list of student dicts (below), you should:
  1. Use map() to calculate each student's average score
  2. Use filter() to find students who are passing (avg >= 60)
  3. Use reduce() to find the student with the highest average
  4. Use map() to assign letter grades to each student

Letter grade scale:
  A: 90-100
  B: 80-89
  C: 70-79
  D: 60-69
  F: below 60

HINTS:
  - map() returns a map object -- wrap in list() to see results
  - For reduce(), compare averages: lambda a, b: a if a['avg'] > b['avg'] else b
  - You can chain operations: pass the output of one to the input of another
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
    # TODO: Return "A", "B", "C", "D", or "F" based on the average
    # HINT: Use if/elif/else
    pass


def process_students(students):
    """Process the student data using map, filter, and reduce."""

    # STEP 1: Calculate averages using map()
    # Add an "avg" key to each student dict
    # HINT: lambda s: {**s, "avg": sum(s["scores"]) / len(s["scores"])}
    # TODO: students_with_avg = list(map(...))

    # STEP 2: Filter passing students (avg >= 60)
    # TODO: passing = list(filter(...))

    # STEP 3: Find the top student using reduce()
    # TODO: top_student = reduce(...)

    # STEP 4: Assign letter grades using map()
    # Add a "grade" key to each student dict
    # TODO: students_with_grades = list(map(...))

    # STEP 5: Print a formatted report card
    # TODO: Loop through and print each student's info
    pass


# Run the processor!
if __name__ == "__main__":
    print("=== STUDENT GRADE PROCESSOR ===\n")
    process_students(students)
