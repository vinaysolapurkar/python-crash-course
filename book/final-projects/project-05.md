# Project 5: Weather Dashboard

> **Difficulty:** 3/5 | **Time:** ~2 hours | **Skills:** APIs, JSON parsing, formatted output, file I/O
> **Code:** https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/final-projects/project-05-weather-dashboard/

## What You'll Build

A command-line weather dashboard that fetches real weather data from the wttr.in API, displays current conditions and a multi-day forecast with formatted output, and lets you save favorite cities for quick access. No API key required.

Here's what it looks like:

```
=== WEATHER DASHBOARD ===

1. Check Weather     4. Remove Favorite
2. 3-Day Forecast    5. View Favorites
3. Add Favorite      6. Exit

Choice: 1
City: London

--- Current Weather: London ---
  Condition:   Partly cloudy
  Temperature: 15C (59F)
  Feels Like:  13C (55F)
  Humidity:    72%
  Wind:        14 km/h SW
  UV Index:    3

  Last updated: 2026-04-01 14:00
```

## Skills You'll Use

- HTTP requests with `urllib` (learned in Chapter 12)
- JSON parsing (learned in Chapter 7)
- String formatting and f-strings (learned in Chapter 2)
- File I/O for favorites (learned in Chapter 7)
- Error handling (learned in Chapter 8)
- Functions and modular design (learned in Chapter 5)

## Step-by-Step Build Guide

### Step 1: Set Up and Fetch Weather Data

The wttr.in API is a free weather service that requires no API key. We'll use Python's built-in `urllib` module so there's nothing to install.

```python
# weather_dashboard.py

import json
import os
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError

FAVORITES_FILE = "favorite_cities.json"


def fetch_weather(city):
    """Fetch weather data from wttr.in API.
    Returns parsed JSON or None on failure."""
    # wttr.in returns JSON when you add ?format=j1
    url = f"https://wttr.in/{city}?format=j1"

    try:
        request = Request(url, headers={"User-Agent": "Python-Weather-App"})
        with urlopen(request, timeout=10) as response:
            data = json.loads(response.read().decode())
            return data
    except HTTPError as e:
        print(f"  HTTP Error: {e.code} - Could not find city '{city}'.")
    except URLError as e:
        print(f"  Connection Error: {e.reason}")
        print("  Check your internet connection.")
    except json.JSONDecodeError:
        print("  Error: Could not parse weather data.")

    return None
```

### Step 2: Parse and Display Current Conditions

The wttr.in JSON response has a specific structure. We'll extract the key fields and display them in a clean, readable format.

```python
def display_current_weather(data, city):
    """Parse and display current weather conditions."""
    try:
        current = data["current_condition"][0]

        temp_c = current["temp_C"]
        temp_f = current["temp_F"]
        feels_c = current["FeelsLikeC"]
        feels_f = current["FeelsLikeF"]
        humidity = current["humidity"]
        description = current["weatherDesc"][0]["value"]
        wind_speed = current["windspeedKmph"]
        wind_dir = current["winddir16Point"]
        uv_index = current["uvIndex"]
        observation_time = current.get("observation_time", "N/A")

        # Area name from the API
        area = data.get("nearest_area", [{}])[0]
        area_name = area.get("areaName", [{}])[0].get("value", city)
        country = area.get("country", [{}])[0].get("value", "")

        print(f"\n--- Current Weather: {area_name}, {country} ---")
        print(f"  Condition:   {description}")
        print(f"  Temperature: {temp_c}C ({temp_f}F)")
        print(f"  Feels Like:  {feels_c}C ({feels_f}F)")
        print(f"  Humidity:    {humidity}%")
        print(f"  Wind:        {wind_speed} km/h {wind_dir}")
        print(f"  UV Index:    {uv_index}")
        print(f"\n  Observation time: {observation_time}")

    except (KeyError, IndexError) as e:
        print(f"  Error parsing weather data: {e}")
```

### Step 3: Build the Forecast Display

The API provides multi-day forecast data. We'll parse it and show a clean 3-day outlook with high/low temperatures and conditions.

```python
def display_forecast(data, city):
    """Display a 3-day weather forecast."""
    try:
        forecasts = data.get("weather", [])

        if not forecasts:
            print("  No forecast data available.")
            return

        area = data.get("nearest_area", [{}])[0]
        area_name = area.get("areaName", [{}])[0].get("value", city)

        print(f"\n--- 3-Day Forecast: {area_name} ---")
        print(f"  {'Date':<14}{'Condition':<22}{'High':<10}{'Low':<10}{'Rain %'}")
        print("  " + "-" * 60)

        for day in forecasts[:3]:
            date = day["date"]
            max_c = day["maxtempC"]
            min_c = day["mintempC"]
            max_f = day["maxtempF"]
            min_f = day["mintempF"]

            # Get midday weather for the description
            hourly = day.get("hourly", [])
            # Use the noon entry (index 4 out of 8 three-hour blocks)
            midday = hourly[4] if len(hourly) > 4 else hourly[0]
            desc = midday["weatherDesc"][0]["value"]
            chance_rain = midday.get("chanceofrain", "?")

            print(f"  {date:<14}{desc:<22}"
                  f"{max_c}C({max_f}F)  {min_c}C({min_f}F)  {chance_rain}%")

        # Simple visual bar for temperature trend
        print(f"\n  Temperature trend:")
        for day in forecasts[:3]:
            max_c = int(day["maxtempC"])
            bar = "#" * max(1, max_c // 2)
            print(f"    {day['date']}: {bar} {max_c}C")

    except (KeyError, IndexError) as e:
        print(f"  Error parsing forecast data: {e}")
```

### Step 4: Implement Favorite Cities

Let users save their frequently checked cities to a JSON file for quick access.

```python
def load_favorites():
    """Load favorite cities from JSON file."""
    if not os.path.exists(FAVORITES_FILE):
        return []
    try:
        with open(FAVORITES_FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []


def save_favorites(favorites):
    """Save favorite cities to JSON file."""
    with open(FAVORITES_FILE, "w") as f:
        json.dump(favorites, f, indent=2)


def add_favorite(favorites):
    """Add a city to favorites."""
    city = input("\nCity to add: ").strip()
    if not city:
        print("  No city entered.")
        return favorites

    # Verify the city exists by fetching weather
    print(f"  Verifying '{city}'...")
    data = fetch_weather(city)
    if data:
        # Use the canonical name from the API
        area = data.get("nearest_area", [{}])[0]
        canonical = area.get("areaName", [{}])[0].get("value", city)

        if canonical.lower() not in [f.lower() for f in favorites]:
            favorites.append(canonical)
            save_favorites(favorites)
            print(f"  Added '{canonical}' to favorites!")
        else:
            print(f"  '{canonical}' is already in your favorites.")
    else:
        print("  Could not verify city. Not added.")

    return favorites


def remove_favorite(favorites):
    """Remove a city from favorites."""
    if not favorites:
        print("\n  No favorites saved yet.")
        return favorites

    print("\nYour favorites:")
    for i, city in enumerate(favorites, 1):
        print(f"  {i}. {city}")

    try:
        choice = int(input("Number to remove: "))
        if 1 <= choice <= len(favorites):
            removed = favorites.pop(choice - 1)
            save_favorites(favorites)
            print(f"  Removed '{removed}'.")
        else:
            print("  Invalid number.")
    except ValueError:
        print("  Please enter a number.")

    return favorites


def view_favorites(favorites):
    """Display favorites with a quick weather summary."""
    if not favorites:
        print("\n  No favorites saved yet. Add some with option 3!")
        return

    print("\n--- Favorite Cities ---")
    for city in favorites:
        data = fetch_weather(city)
        if data:
            current = data["current_condition"][0]
            temp = current["temp_C"]
            desc = current["weatherDesc"][0]["value"]
            print(f"  {city:<20} {temp}C  {desc}")
        else:
            print(f"  {city:<20} (could not fetch)")
```

### Step 5: Build the Main Application

```python
def check_weather():
    """Prompt for a city and show current weather."""
    city = input("\nCity: ").strip()
    if not city:
        print("  No city entered.")
        return

    print(f"  Fetching weather for '{city}'...")
    data = fetch_weather(city)
    if data:
        display_current_weather(data, city)


def check_forecast():
    """Prompt for a city and show 3-day forecast."""
    city = input("\nCity: ").strip()
    if not city:
        print("  No city entered.")
        return

    print(f"  Fetching forecast for '{city}'...")
    data = fetch_weather(city)
    if data:
        display_forecast(data, city)


def main():
    """Main application loop."""
    print("=" * 35)
    print("    WEATHER DASHBOARD")
    print("=" * 35)

    favorites = load_favorites()
    if favorites:
        print(f"Loaded {len(favorites)} favorite city/cities.")

    while True:
        print("\n1. Check Weather     4. Remove Favorite")
        print("2. 3-Day Forecast    5. View Favorites")
        print("3. Add Favorite      6. Exit")

        choice = input("\nChoice: ").strip()

        if choice == "1":
            check_weather()
        elif choice == "2":
            check_forecast()
        elif choice == "3":
            favorites = add_favorite(favorites)
        elif choice == "4":
            favorites = remove_favorite(favorites)
        elif choice == "5":
            view_favorites(favorites)
        elif choice == "6":
            print("\nStay dry out there!")
            break
        else:
            print("Invalid choice. Please enter 1-6.")


if __name__ == "__main__":
    main()
```

## Challenges (Level Up!)

1. **Weather alerts:** Compare the forecast against configurable thresholds (e.g., temperature below 0, rain chance above 80%) and display alerts. Store thresholds in a config JSON file.

2. **Historical comparison:** Cache each day's weather to a CSV file. After a week of data, show trends like "Today is 5 degrees warmer than the weekly average."

3. **Multiple API support:** Add a fallback API (like Open-Meteo, also free and keyless) so if wttr.in is down, the app still works. Abstract the API call behind a common interface.

## Portfolio Tips

This project shows you can work with real external APIs, handle network errors gracefully, and build data-rich displays. When presenting it:

- **GitHub:** Include screenshots showing both current weather and forecast output. Mention that it requires no API key (lowers the barrier for anyone trying your code).
- **Resume:** "Built a CLI weather dashboard consuming the wttr.in REST API with JSON parsing, multi-day forecasting, and persistent favorite cities."
- **Interview talking point:** Discuss how you handled network failures (timeouts, bad city names, no internet). Talk about your choice to use `urllib` over `requests` for zero dependencies, and how you'd refactor to use `requests` in a production setting.
