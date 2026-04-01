"""
=============================================================
  PROJECT 5: WEATHER DASHBOARD - SOLUTION
=============================================================
  A CLI weather dashboard using the free wttr.in API.
  Shows current conditions, 3-day forecast, and saves
  favorite cities.

  Dependencies:
    pip install requests
    (Or it will fall back to urllib - no install needed!)

  Run:  python solution.py
=============================================================
"""

import json
import os

# Try requests first; fall back to urllib (standard library)
try:
    import requests
    HAS_REQUESTS = True
except ImportError:
    import urllib.request
    import urllib.error
    HAS_REQUESTS = False


FAVORITES_FILE = "favorite_cities.json"
WTTR_URL = "https://wttr.in/{}?format=j1"


# ── API Functions ──────────────────────────────────────────

def fetch_weather(city):
    """
    Fetch weather data from wttr.in.
    Returns parsed JSON dict or None on error.
    """
    url = WTTR_URL.format(city.replace(" ", "+"))

    try:
        if HAS_REQUESTS:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return response.json()
        else:
            req = urllib.request.Request(url)
            req.add_header("User-Agent", "python-weather-app")
            with urllib.request.urlopen(req, timeout=10) as resp:
                data = resp.read().decode("utf-8")
                return json.loads(data)

    except Exception as e:
        print(f"\n  Error fetching weather: {e}")
        print("  Check your internet connection or city name.")
        return None


def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return int(celsius) * 9 // 5 + 32


# ── Display Functions ──────────────────────────────────────

def draw_box_top(width):
    return "  ┌" + "─" * width + "┐"

def draw_box_mid(width):
    return "  ├" + "─" * width + "┤"

def draw_box_bot(width):
    return "  └" + "─" * width + "┘"

def draw_box_line(text, width):
    return f"  │ {text:<{width - 2}} │"


def display_weather(data):
    """Display current weather and forecast in a formatted box."""
    if not data:
        return

    # ── Extract current conditions ──
    try:
        current = data["current_condition"][0]
        # The nearest_area gives us the resolved city name
        area = data["nearest_area"][0]
        city_name = area["areaName"][0]["value"]
        region = area["region"][0]["value"]
        country = area["country"][0]["value"]

        temp_c = current["temp_C"]
        temp_f = current["temp_F"]
        feels_c = current["FeelsLikeC"]
        feels_f = current["FeelsLikeF"]
        humidity = current["humidity"]
        wind_speed = current["windspeedKmph"]
        wind_dir = current["winddir16Point"]
        description = current["weatherDesc"][0]["value"]
    except (KeyError, IndexError) as e:
        print(f"  Error parsing weather data: {e}")
        return

    # ── Build the display ──
    width = 42

    location = f"{city_name}, {region}" if region else f"{city_name}, {country}"

    print()
    print(draw_box_top(width))
    print(draw_box_line(f"WEATHER: {location}", width))
    print(draw_box_line(f"Conditions: {description}", width))
    print(draw_box_mid(width))
    print(draw_box_line(f"Temperature:  {temp_c}C ({temp_f}F)", width))
    print(draw_box_line(f"Feels Like:   {feels_c}C ({feels_f}F)", width))
    print(draw_box_line(f"Humidity:     {humidity}%", width))
    print(draw_box_line(f"Wind:         {wind_speed} km/h {wind_dir}", width))

    # ── 3-Day Forecast ──
    forecast = data.get("weather", [])
    if forecast:
        print(draw_box_mid(width))
        print(draw_box_line("3-DAY FORECAST", width))
        print(draw_box_line("─" * (width - 2), width))

        for day in forecast[:3]:
            try:
                date_str = day["date"]
                min_c = day["mintempC"]
                max_c = day["maxtempC"]
                min_f = day["mintempF"]
                max_f = day["maxtempF"]
                desc = day["hourly"][4]["weatherDesc"][0]["value"]  # midday

                line = f"{date_str}  {min_c}-{max_c}C ({min_f}-{max_f}F)"
                print(draw_box_line(line, width))
                print(draw_box_line(f"  {desc}", width))
            except (KeyError, IndexError):
                continue

    print(draw_box_bot(width))


# ── Favorites Management ───────────────────────────────────

def load_favorites():
    """Load favorite cities from JSON file."""
    if not os.path.exists(FAVORITES_FILE):
        return []
    try:
        with open(FAVORITES_FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []


def save_favorites(cities):
    """Save favorite cities to JSON file."""
    try:
        with open(FAVORITES_FILE, "w") as f:
            json.dump(cities, f, indent=2)
    except IOError as e:
        print(f"  Error saving favorites: {e}")


def add_favorite(city):
    """Add a city to the favorites list."""
    favorites = load_favorites()
    # Avoid duplicates (case-insensitive)
    if city.lower() not in [c.lower() for c in favorites]:
        favorites.append(city)
        save_favorites(favorites)
        print(f"  '{city}' added to favorites!")
    else:
        print(f"  '{city}' is already in your favorites.")


def remove_favorite(city):
    """Remove a city from favorites."""
    favorites = load_favorites()
    updated = [c for c in favorites if c.lower() != city.lower()]
    if len(updated) < len(favorites):
        save_favorites(updated)
        print(f"  '{city}' removed from favorites.")
    else:
        print(f"  '{city}' not found in favorites.")


def show_favorites():
    """Display the favorites list."""
    favorites = load_favorites()
    if not favorites:
        print("\n  No favorite cities saved yet.")
        return

    print("\n  Your Favorite Cities:")
    print("  " + "─" * 30)
    for i, city in enumerate(favorites, 1):
        print(f"  {i}. {city}")
    print("  " + "─" * 30)


def check_favorite_weather():
    """Fetch weather for all favorite cities."""
    favorites = load_favorites()
    if not favorites:
        print("\n  No favorites saved. Add some first!")
        return

    print(f"\n  Fetching weather for {len(favorites)} favorite cities...")
    for city in favorites:
        data = fetch_weather(city)
        if data:
            display_weather(data)


# ── Main Menu ──────────────────────────────────────────────

def show_menu():
    """Display the main menu."""
    print()
    print("=" * 36)
    print("    WEATHER DASHBOARD")
    print("=" * 36)
    print("  1. Check Weather (any city)")
    print("  2. Add to Favorites")
    print("  3. View Favorites")
    print("  4. Weather for All Favorites")
    print("  5. Remove a Favorite")
    print("  6. Exit")
    print()


def main():
    """Main program loop."""
    print()
    print("*" * 36)
    print("  Welcome to Weather Dashboard!")
    print("  Powered by wttr.in (free API)")
    print("*" * 36)

    while True:
        show_menu()
        choice = input("  Choose an option (1-6): ").strip()

        if choice == "1":
            city = input("\n  Enter city name: ").strip()
            if city:
                print(f"  Fetching weather for {city}...")
                data = fetch_weather(city)
                if data:
                    display_weather(data)

                    # Offer to save as favorite
                    save = input("\n  Save to favorites? (y/n): ").strip().lower()
                    if save == "y":
                        add_favorite(city)
            else:
                print("  Please enter a city name.")

        elif choice == "2":
            city = input("\n  City to add to favorites: ").strip()
            if city:
                add_favorite(city)

        elif choice == "3":
            show_favorites()

        elif choice == "4":
            check_favorite_weather()

        elif choice == "5":
            show_favorites()
            city = input("\n  City to remove: ").strip()
            if city:
                remove_favorite(city)

        elif choice == "6":
            print("\n  Stay dry out there! Goodbye!")
            break

        else:
            print("  Invalid choice. Please enter 1-6.")


if __name__ == "__main__":
    main()
