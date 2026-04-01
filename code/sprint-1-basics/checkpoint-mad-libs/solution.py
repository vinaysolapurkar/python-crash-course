# ============================================================
# SOLUTION: Mad Libs Generator
# ============================================================
# The ultimate test of Chapters 1-8. Also, the ultimate test
# of your sense of humor. Results may vary.
# ============================================================

import random

# ----------------------------------------------------------
# STORY TEMPLATES
# ----------------------------------------------------------
# Each template uses {placeholders} that match our word types.
# We use .format(**words) to fill them in.

stories = {
    "The Adventurous Day": """
    ╔══════════════════════════════════════════════╗
    ║         THE ADVENTUROUS DAY                  ║
    ╚══════════════════════════════════════════════╝

    One {adjective1} morning, {name} woke up in {place} feeling
    extremely {adjective2}. "Today," they said {adverb},
    "I shall ride my {noun1} to the {adjective3} mountains!"

    Along the way, they encountered a {color} {animal} who was
    {verb_ing} a {food}. "That's the most {adjective1} thing
    I've ever seen!" {name} exclaimed.

    The {animal} looked up and said, "You should try the
    {food} — it tastes like {noun2} mixed with {noun3}."

    {name} tried it and immediately felt {number} times more
    {adjective2}. They {verb_past} all the way home, where
    their {plural_noun} were waiting with a {adjective3} surprise.

    THE END. (Or is it? Spoiler: it is.)
""",

    "The Job Interview": """
    ╔══════════════════════════════════════════════╗
    ║         THE JOB INTERVIEW                    ║
    ╚══════════════════════════════════════════════╝

    {name} walked into the interview at {place}, wearing a
    {color} suit and carrying a briefcase full of {plural_noun}.

    "So," the interviewer said {adverb}, "tell me about your
    experience with {noun1}."

    "Well," {name} replied, "I once {verb_past} a {adjective1}
    {animal} using nothing but a {noun2} and {number} gallons
    of {food}. It was quite {adjective2}."

    The interviewer leaned forward. "Impressive. And what's
    your greatest weakness?"

    "I'm too {adjective3}. Also, I can't stop {verb_ing}
    during meetings. And I once accidentally turned my boss's
    {noun3} into a {adjective1} {noun1}."

    "You're hired," the interviewer said. "You start {adverb}."

    THE END. ({name} got a corner office. The {animal} got one too.)
""",

    "The Superhero Origin": """
    ╔══════════════════════════════════════════════╗
    ║         THE SUPERHERO ORIGIN                 ║
    ╚══════════════════════════════════════════════╝

    In the {adjective1} city of {place}, a mild-mannered
    {noun1} salesperson named {name} was having a {adjective2} day.

    Suddenly, a {color} {animal} fell from the sky and landed
    on their {noun2}! There was a {adjective3} flash, and
    {name} felt a strange tingling in their {plural_noun}.

    "Great {food}!" they shouted {adverb}. "I can {verb_ing}
    at {number} miles per hour! I can {verb_past} through walls!
    I can even turn {noun3} into solid gold!"

    From that day forward, {name} became the hero known as
    "The {adjective1} {animal}" — defender of {place},
    protector of {plural_noun}, and world champion of {verb_ing}.

    Their arch-nemesis? A {adjective3} villain named
    "Doctor {noun1}" who {adverb} plotted to steal all
    the {food} in the world.

    To be continued... (in a {adjective2} sequel nobody asked for)
"""
}

# ----------------------------------------------------------
# WORD TYPES WE NEED (union of all templates)
# ----------------------------------------------------------
# Using a tuple of (key, prompt) so we have nice display names
word_prompts = (
    ("name",        "A person's name"),
    ("place",       "A place (city, country, or made-up land)"),
    ("adjective1",  "An adjective (descriptive word)"),
    ("adjective2",  "Another adjective"),
    ("adjective3",  "One more adjective (go wild)"),
    ("noun1",       "A noun (thing)"),
    ("noun2",       "Another noun"),
    ("noun3",       "One more noun"),
    ("plural_noun", "A plural noun (multiple things)"),
    ("verb_past",   "A verb in past tense (e.g., 'danced')"),
    ("verb_ing",    "A verb ending in -ing (e.g., 'dancing')"),
    ("adverb",      "An adverb (e.g., 'quickly', 'angrily')"),
    ("animal",      "An animal"),
    ("food",        "A food or drink"),
    ("color",       "A color"),
    ("number",      "A number"),
)

# ----------------------------------------------------------
# GAME FUNCTIONS
# ----------------------------------------------------------

def show_title():
    """Display the magnificent title screen."""
    print()
    print("=" * 50)
    print(r"""
     __  __           _   _     _ _
    |  \/  | __ _  __| | | |   (_) |__  ___
    | |\/| |/ _` |/ _` | | |   | | '_ \/ __|
    | |  | | (_| | (_| | | |___| | |_) \__ \
    |_|  |_|\__,_|\__,_| |_____|_|_.__/|___/
    """)
    print("    The Sprint 1 Checkpoint Project!")
    print("=" * 50)


def collect_words():
    """Ask the user for all the words we need. Returns a dict."""
    print("\n--- TIME TO FILL IN THE BLANKS! ---")
    print("(The weirder your answers, the funnier the story)\n")

    words = {}
    for key, prompt in word_prompts:
        answer = input(f"  Enter {prompt}: ").strip()
        # Default to something funny if they skip
        if not answer:
            answer = "banana"
            print(f"    (Nothing entered — using '{answer}' because why not)")
        words[key] = answer

    return words


def choose_story():
    """Let the user pick a story or go random."""
    story_names = list(stories.keys())

    print("\n--- CHOOSE YOUR STORY ---")
    print("  [R] Random (surprise me!)")
    for i, name in enumerate(story_names, 1):
        print(f"  [{i}] {name}")

    choice = input("\nYour pick: ").strip().lower()

    if choice == "r" or choice == "":
        selected = random.choice(story_names)
        print(f"  Randomly selected: '{selected}'!")
    elif choice.isdigit() and 1 <= int(choice) <= len(story_names):
        selected = story_names[int(choice) - 1]
    else:
        selected = random.choice(story_names)
        print(f"  Invalid choice — randomly going with: '{selected}'!")

    return selected


def play_round(round_number):
    """Play one round of Mad Libs."""
    print(f"\n{'=' * 50}")
    print(f"  ROUND {round_number}")
    print(f"{'=' * 50}")

    # Collect words from the user
    words = collect_words()

    # Let them choose (or randomize) the story
    story_name = choose_story()

    # Fill in the story!
    print("\n" + "=" * 50)
    print("  AND NOW... YOUR STORY!")
    print("=" * 50)

    story_template = stories[story_name]
    try:
        finished_story = story_template.format(**words)
        print(finished_story)
    except KeyError as e:
        print(f"\n  Oops! Missing word for: {e}")
        print("  (This shouldn't happen, but just in case...)")

    return words  # Return for potential reuse


# ----------------------------------------------------------
# MAIN GAME LOOP
# ----------------------------------------------------------

show_title()

rounds_played = 0
all_words_used = set()  # Track unique words used across all rounds

while True:
    rounds_played += 1
    words = play_round(rounds_played)

    # Track all unique words entered (using sets — Chapter 8!)
    all_words_used.update(words.values())

    # Ask to play again
    print("-" * 50)
    print(f"  Rounds played: {rounds_played}")
    print(f"  Unique words used: {len(all_words_used)}")
    print("-" * 50)

    again = input("\nPlay again? (yes/no): ").strip().lower()
    if again not in ("yes", "y", "sure", "absolutely", "yep"):
        break

# ----------------------------------------------------------
# GAME OVER STATS
# ----------------------------------------------------------
print("\n" + "=" * 50)
print("  GAME OVER — THANKS FOR PLAYING!")
print("=" * 50)
print(f"  Rounds played: {rounds_played}")
print(f"  Unique words used: {len(all_words_used)}")
print(f"  Stories available: {len(stories)}")

if rounds_played >= 3:
    print("\n  You played 3+ rounds! You're a Mad Libs champion!")
elif rounds_played == 1:
    print("\n  Just one round? The stories miss you already.")
else:
    print("\n  Nice run! Come back when you need more laughs.")

print("\n  All your unique words:")
for word in sorted(all_words_used):
    print(f"    - {word}")

print("\n  'The pen is mightier than the sword.'")
print("  '...especially when the pen writes Mad Libs.'")
print("     — Nobody, but it should be somebody")
print()
