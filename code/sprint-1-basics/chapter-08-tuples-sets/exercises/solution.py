# ============================================================
# SOLUTION: Duplicate Finder for a Playlist
# ============================================================
# Because nobody wants to hear "Bohemian Rhapsody" four times
# in a row. (Okay, maybe some people do. But still.)
# ============================================================

# Our messy playlist
playlist = [
    "Bohemian Rhapsody", "Stairway to Heaven",
    "Hotel California", "Bohemian Rhapsody",
    "Imagine", "Stairway to Heaven",
    "Smells Like Teen Spirit", "Bohemian Rhapsody",
    "Hotel California", "Yesterday",
    "Imagine", "Bohemian Rhapsody"
]

print("=" * 45)
print("      PLAYLIST DUPLICATE FINDER")
print("  (Cleaning up your questionable taste)")
print("=" * 45)

# ----------------------------------------------------------
# Step 1: Show the original playlist
# ----------------------------------------------------------
print(f"\nOriginal playlist ({len(playlist)} songs):")
for i, song in enumerate(playlist, 1):
    print(f"  {i:>2}. {song}")

# ----------------------------------------------------------
# Step 2: Find duplicates and count them
# ----------------------------------------------------------
# Use a set to track which songs we've already counted
counted = set()
duplicates = []

for song in playlist:
    if song not in counted:
        count = playlist.count(song)
        if count > 1:
            duplicates.append((song, count))
        counted.add(song)

print(f"\n--- Duplicates Found ({len(duplicates)} songs with repeats) ---")
if duplicates:
    total_extras = 0
    for song, count in duplicates:
        extras = count - 1
        total_extras += extras
        print(f'  "{song}" appears {count} times ({extras} extra{"s" if extras > 1 else ""})')

    # Bonus: show positions of duplicates
    print("\n--- Duplicate Positions ---")
    for song, count in duplicates:
        positions = [i + 1 for i, s in enumerate(playlist) if s == song]
        print(f'  "{song}": positions {positions}')
else:
    total_extras = 0
    print("  No duplicates! Your playlist is pristine.")

# ----------------------------------------------------------
# Step 3: Create clean playlist (preserve order)
# ----------------------------------------------------------
seen = set()
clean_playlist = []
for song in playlist:
    if song not in seen:
        seen.add(song)
        clean_playlist.append(song)

print(f"\n--- Cleaned Playlist ({len(clean_playlist)} unique songs) ---")
for i, song in enumerate(clean_playlist, 1):
    print(f"  {i:>2}. {song}")

print(f"\nRemoved {total_extras} duplicate entr{'ies' if total_extras != 1 else 'y'}!")
print(f"Went from {len(playlist)} -> {len(clean_playlist)} songs. Marie Kondo approved.")

# ----------------------------------------------------------
# Bonus: Let user add a song and check for dupes
# ----------------------------------------------------------
print("\n--- Add a Song ---")
new_song = input("Add a song to the clean playlist (or press Enter to skip): ").strip()

if new_song:
    if new_song in seen:
        print(f'"{new_song}" is already in the playlist! No duplicates on our watch.')
    else:
        clean_playlist.append(new_song)
        seen.add(new_song)
        print(f'Added "{new_song}"! Playlist now has {len(clean_playlist)} songs.')

    print("\nFinal playlist:")
    for i, song in enumerate(clean_playlist, 1):
        print(f"  {i:>2}. {song}")
else:
    print("No song added. The playlist stands as is.")

print("\nRock on! (Or jazz on. Or pop on. We don't judge.)")
