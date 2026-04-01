# ============================================================
# CHECKPOINT PROJECT: Mad Libs Generator
# ============================================================
# Congratulations! You've completed Chapters 1-8!
# Time to put it all together with a classic: MAD LIBS.
#
# YOUR MISSION:
# Build a Mad Libs game that:
#   1. Asks the user for various words (nouns, verbs, adjectives, etc.)
#   2. Has at least 3 different story templates
#   3. Randomly selects a template (or lets the user choose)
#   4. Fills in the blanks with the user's words
#   5. Displays the hilarious result
#   6. Asks if they want to play again
#
# SKILLS YOU'LL USE:
#   - Variables & f-strings          (Chapter 2)
#   - Numbers for random selection   (Chapter 3)
#   - String methods for formatting  (Chapter 4)
#   - if/elif/else for menu choices  (Chapter 5)
#   - Lists for word storage         (Chapter 6)
#   - Loops for replay               (Chapter 7)
#   - Tuples/sets for word types     (Chapter 8)
#
# SUGGESTED WORD TYPES TO ASK FOR:
#   - noun, plural_noun, verb, verb_past, adjective,
#   - adverb, name, place, food, animal, number, color
#
# DESIGN TIPS:
#   - Use a dictionary to store the user's words:
#       words = {"noun": "bicycle", "adjective": "sparkly", ...}
#   - Use .format(**words) or f-strings to fill in templates
#   - Use random.choice() to pick a random template
#   - Use a while loop for the "play again?" feature
#   - Use a set to track which word types you need
#
# STORY TEMPLATE EXAMPLE:
#   "Today I went to {place} and saw a {adjective} {animal}.
#    It was {adverb} eating a {food} while singing about {noun}."
#
# CHALLENGE YOURSELF:
#   - Make each story template need different word types
#   - Collect all needed word types from ALL templates
#     (so the user enters words once, and any template works)
#   - Add ASCII art for extra flair
#   - Keep score of how many rounds they've played
#
# This is YOUR project. Be creative. Be weird. Be funny.
# The best Mad Libs are the ones that make you snort-laugh.
#
# Type your code below!
# ============================================================

