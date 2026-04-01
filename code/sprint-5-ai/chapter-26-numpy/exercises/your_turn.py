"""
Chapter 26: NumPy — YOUR TURN!
================================

You're a teaching assistant and you've got a dataset of student scores.
Time to crunch some numbers with NumPy! No more slow Python loops —
we're doing this the fast way.

DATASET:
- 5 students, 4 subjects (Math, Science, English, History)
- Each row is a student, each column is a subject

TASKS:
1. Create the scores array from the data below
2. Calculate the average score for EACH student (across all subjects)
3. Calculate the average score for EACH subject (across all students)
4. Find which student has the highest overall average (print their index)
5. Find which subject has the lowest average
6. Normalize all scores to a 0-1 scale using: (score - min) / (max - min)
7. Count how many scores are above 80
8. BONUS: Replace all failing scores (below 60) with 60 (grade floor)

Student data:
    Student 0: Math=85, Science=92, English=78, History=90
    Student 1: Math=55, Science=68, English=72, History=61
    Student 2: Math=93, Science=87, English=95, History=89
    Student 3: Math=72, Science=58, English=81, History=76
    Student 4: Math=88, Science=91, English=69, History=85
"""

import numpy as np

# Subject names for nice output
subjects = ["Math", "Science", "English", "History"]
student_names = ["Student 0", "Student 1", "Student 2", "Student 3", "Student 4"]

# TODO 1: Create the scores array (5 students x 4 subjects)
# Hint: np.array([[...], [...], ...])
scores = None

# TODO 2: Average score per student
# Hint: np.mean() with axis parameter. axis=1 means "across columns"
student_averages = None
print("Average per student:")
# Print each student's average

# TODO 3: Average score per subject
# Hint: axis=0 means "across rows"
subject_averages = None
print("\nAverage per subject:")
# Print each subject's average

# TODO 4: Top performer
# Hint: np.argmax() on student_averages
top_student = None
print(f"\nTop performer: ???")

# TODO 5: Weakest subject
# Hint: np.argmin() on subject_averages
weakest_subject = None
print(f"Weakest subject: ???")

# TODO 6: Normalize scores to 0-1 scale
# Formula: (score - min) / (max - min)
# Hint: np.min() and np.max() on the entire array
normalized = None
print(f"\nNormalized scores:\n???")

# TODO 7: Count scores above 80
# Hint: Boolean indexing + np.sum() or len()
above_80 = None
print(f"\nScores above 80: ???")

# TODO 8 (BONUS): Replace failing scores with 60
# Hint: Boolean indexing on the left side of assignment
# Make a copy first so we don't modify the original!
curved_scores = None
print(f"\nOriginal min: ???")
print(f"After grade floor of 60: min is now ???")
