# ============================================================
# YOUR TURN: Duplicate Finder for a Playlist
# ============================================================
# You've got a playlist with duplicate songs. Your mission:
# find the duplicates, count them, and create a clean playlist
# that keeps the original order.
#
# YOUR PROGRAM SHOULD:
# 1. Start with a pre-loaded playlist (a list of song strings)
# 2. Find which songs appear more than once
# 3. Show how many times each duplicate appears
# 4. Create a clean playlist with duplicates removed
#    BUT keep the original order (first occurrence stays)
# 5. Display the results
#
# STARTER PLAYLIST:
#   playlist = [
#       "Bohemian Rhapsody", "Stairway to Heaven",
#       "Hotel California", "Bohemian Rhapsody",
#       "Imagine", "Stairway to Heaven",
#       "Smells Like Teen Spirit", "Bohemian Rhapsody",
#       "Hotel California", "Yesterday",
#       "Imagine", "Bohemian Rhapsody"
#   ]
#
# EXPECTED OUTPUT (something like):
#    === PLAYLIST DUPLICATE FINDER ===
#
#    Original playlist (12 songs):
#      1. Bohemian Rhapsody
#      2. Stairway to Heaven
#      ... etc ...
#
#    Duplicates found:
#      "Bohemian Rhapsody" appears 4 times (3 extras)
#      "Stairway to Heaven" appears 2 times (1 extra)
#      "Hotel California" appears 2 times (1 extra)
#      "Imagine" appears 2 times (1 extra)
#
#    Cleaned playlist (7 unique songs):
#      1. Bohemian Rhapsody
#      2. Stairway to Heaven
#      ... etc (original order preserved) ...
#
#    Removed 5 duplicate entries!
#
# HINTS:
# - Use a set to track songs you've already seen
# - Use the "seen set + ordered list" pattern from the chapter
# - Use list.count(item) to count how many times a song appears
# - A song is a duplicate if playlist.count(song) > 1
#
# BONUS:
# - Let the user add a new song and check if it's a dupe
# - Show which positions (indices) the duplicates are at
#
# Type your code below!
# ============================================================

