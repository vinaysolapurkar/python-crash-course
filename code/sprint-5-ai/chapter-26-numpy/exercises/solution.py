"""
Chapter 26: NumPy — SOLUTION
==============================

Look at you, crunching student data like a pro!
NumPy makes this stuff feel almost too easy.
"""

import numpy as np

# Subject names for nice output
subjects = ["Math", "Science", "English", "History"]
student_names = ["Student 0", "Student 1", "Student 2", "Student 3", "Student 4"]

# TASK 1: Create the scores array (5 students x 4 subjects)
scores = np.array([
    [85, 92, 78, 90],   # Student 0
    [55, 68, 72, 61],   # Student 1
    [93, 87, 95, 89],   # Student 2
    [72, 58, 81, 76],   # Student 3
    [88, 91, 69, 85],   # Student 4
])
print(f"Scores array shape: {scores.shape}")
print(f"Scores:\n{scores}\n")

# TASK 2: Average score per student (axis=1 = across columns)
student_averages = np.mean(scores, axis=1)
print("Average per student:")
for name, avg in zip(student_names, student_averages):
    print(f"  {name}: {avg:.1f}")

# TASK 3: Average score per subject (axis=0 = across rows)
subject_averages = np.mean(scores, axis=0)
print("\nAverage per subject:")
for subj, avg in zip(subjects, subject_averages):
    print(f"  {subj}: {avg:.1f}")

# TASK 4: Top performer — who has the highest average?
top_student = np.argmax(student_averages)
print(f"\nTop performer: {student_names[top_student]} "
      f"(avg: {student_averages[top_student]:.1f})")

# TASK 5: Weakest subject — which has the lowest average?
weakest_subject = np.argmin(subject_averages)
print(f"Weakest subject: {subjects[weakest_subject]} "
      f"(avg: {subject_averages[weakest_subject]:.1f})")

# TASK 6: Normalize scores to 0-1 scale
# Formula: (score - min) / (max - min)
score_min = np.min(scores)
score_max = np.max(scores)
normalized = (scores - score_min) / (score_max - score_min)
print(f"\nNormalized scores (0-1 scale):")
print(f"{np.round(normalized, 2)}")

# TASK 7: Count scores above 80
above_80 = np.sum(scores > 80)
print(f"\nScores above 80: {above_80} out of {scores.size}")
print(f"That's {above_80 / scores.size * 100:.0f}% of all scores!")

# TASK 8 (BONUS): Replace failing scores with 60
curved_scores = scores.copy()  # Always copy before modifying!
print(f"\nOriginal min: {np.min(scores)}")
curved_scores[curved_scores < 60] = 60  # Boolean indexing magic!
print(f"After grade floor of 60: min is now {np.min(curved_scores)}")
print(f"Curved scores:\n{curved_scores}")

# EXTRA: Let's see some more stats just because we can
print(f"\n--- BONUS STATS ---")
print(f"Overall class average: {np.mean(scores):.1f}")
print(f"Standard deviation: {np.std(scores):.1f}")
print(f"Median score: {np.median(scores):.1f}")
print(f"Score range: {np.min(scores)} to {np.max(scores)}")
