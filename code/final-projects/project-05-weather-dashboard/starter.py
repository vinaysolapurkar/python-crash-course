"""
=============================================================
  PROJECT 5: WEATHER DASHBOARD
=============================================================

Build a weather dashboard that fetches real weather data
from the internet! We'll use wttr.in, a free weather API
that doesn't require an API key.

WHAT YOU'LL PRACTICE:
  - HTTP requests (urllib or requests)
  - JSON parsing
  - Formatted terminal output
  - Error handling for network issues
  - File I/O (saving favorite cities)

DEPENDENCIES:
  pip install requests

  (Or use urllib from the standard library - no install needed!)

REQUIREMENTS:
  1. Fetch weather from wttr.in for any city
  2. Display current conditions (temp, humidity, wind, etc.)
  3. Show a 3-day forecast
  4. Display temperature in both Celsius and Fahrenheit
  5. Format output with box-drawing characters
  6. Save/load favorite cities to a JSON file
  7. Handle errors gracefully (bad city, no internet)

API INFO:
  wttr.in is free and needs no API key!
  URL format: https://wttr.in/CityName?format=j1
  This returns JSON weather data.

EXAMPLE OUTPUT:
  ┌──────────────────────────────────┐
  │   WEATHER: London, England       │
  │   2026-03-30 14:00               │
  ├──────────────────────────────────┤
  │   Temperature: 12C (54F)         │
  │   Feels Like:  10C (50F)         │
  │   Humidity:    72%               │
  │   Wind:        15 km/h SW        │
  │   Conditions:  Partly Cloudy     │
  ├──────────────────────────────────┤
  │   3-DAY FORECAST                 │
  │   Mon: 8-14C  Partly Cloudy     │
  │   Tue: 6-11C  Rain              │
  │   Wed: 9-15C  Sunny             │
  └──────────────────────────────────┘

HINTS:
  - requests.get(url).json() gives you a dict
  - wttr.in JSON has: current_condition, weather (forecast)
  - Use try/except around network calls
  - F = C * 9/5 + 32 for temperature conversion
  - Box chars: ┌ ┐ └ ┘ │ ─ ├ ┤

Good luck!
=============================================================
"""

import json
import os

# Try to import requests; fall back to urllib if not installed
try:
    import requests
    HAS_REQUESTS = True
except ImportError:
    import urllib.request
    import urllib.error
    HAS_REQUESTS = False


FAVORITES_FILE = "favorite_cities.json"


def fetch_weather(city):
    """Fetch weather data from wttr.in for the given city.
    Returns the parsed JSON dict, or None on error."""
    # TODO: Build the URL: https://wttr.in/{city}?format=j1
    # TODO: Make the request (try requests, or urllib)
    # TODO: Parse and return JSON
    # TODO: Handle errors (network, bad city)
    pass


def display_current_weather(data):
    """Display current weather conditions in a nice box."""
    # TODO: Extract current conditions from the data
    # TODO: Format temperature in C and F
    # TODO: Print with box-drawing characters
    pass


def display_forecast(data):
    """Display the 3-day forecast."""
    # TODO: Extract forecast data
    # TODO: Show date, temp range, and conditions for each day
    pass


def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    # TODO: Return the conversion
    pass


def load_favorites():
    """Load favorite cities from JSON file."""
    # TODO: Read and return the list of cities
    pass


def save_favorites(cities):
    """Save favorite cities to JSON file."""
    # TODO: Write the list to JSON
    pass


def add_favorite(city):
    """Add a city to favorites."""
    # TODO: Load, append, save
    pass


def show_favorites():
    """Display the list of favorite cities."""
    # TODO: Load and print favorites
    pass


def main():
    """Main menu loop."""
    # TODO: Show menu (check weather, favorites, exit)
    # TODO: Handle user input
    # TODO: Loop until exit
    pass


if __name__ == "__main__":
    main()
