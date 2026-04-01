"""
Chapter 21 Exercise: Weather Checker
======================================

Build a weather checker using the free wttr.in API!
No API key needed — it's completely free and open.

Requirements:

1. Ask the user for a city name
2. Fetch weather data from wttr.in
3. Display:
   - Current temperature
   - Weather description (sunny, cloudy, etc.)
   - Humidity
   - Wind speed
4. Handle errors gracefully (bad city, no internet, etc.)

API endpoint:
    https://wttr.in/{city}?format=j1

    This returns JSON with weather data. Key fields:
    - data["current_condition"][0]["temp_C"]      → temperature in Celsius
    - data["current_condition"][0]["temp_F"]      → temperature in Fahrenheit
    - data["current_condition"][0]["humidity"]     → humidity percentage
    - data["current_condition"][0]["weatherDesc"][0]["value"] → description
    - data["current_condition"][0]["windspeedKmph"] → wind speed

Bonus:
    - Show a 3-day forecast (data["weather"] is a list of days)
    - Add temperature unit conversion
    - Let the user check multiple cities in a loop

Starter code below:
"""

import requests


def get_weather(city):
    """
    Fetch weather data for a given city from wttr.in.

    Args:
        city: Name of the city (e.g., "London", "New York")

    Returns:
        dict with weather data, or None if the request failed.
    """
    url = f"https://wttr.in/{city}?format=j1"

    # TODO: Make a GET request to the URL
    # TODO: Handle errors (ConnectionError, Timeout, etc.)
    # TODO: Parse and return the JSON response
    # Hint: Use timeout=10 for the request
    pass


def display_weather(data, city):
    """
    Display weather data in a nice format.

    Args:
        data: The JSON response from wttr.in
        city: The city name for display
    """
    # TODO: Extract current conditions from data
    # Hint: current = data["current_condition"][0]

    # TODO: Display temperature, description, humidity, wind
    pass


def display_forecast(data, city):
    """
    Bonus: Display 3-day forecast.

    Args:
        data: The JSON response from wttr.in
        city: The city name for display
    """
    # TODO: Loop through data["weather"] (list of days)
    # Each day has: date, maxtempC, mintempC, hourly forecasts
    pass


def main():
    """Main function — run the weather checker."""
    print("=" * 40)
    print("  WEATHER CHECKER")
    print("  Powered by wttr.in")
    print("=" * 40)

    # TODO: Ask for a city
    # TODO: Call get_weather()
    # TODO: If successful, call display_weather()
    # TODO: Bonus: Ask if they want the forecast

    # For a loop version:
    # while True:
    #     city = input("\nEnter a city (or 'quit'): ").strip()
    #     if city.lower() == 'quit':
    #         break
    #     ...
    pass


if __name__ == "__main__":
    main()
