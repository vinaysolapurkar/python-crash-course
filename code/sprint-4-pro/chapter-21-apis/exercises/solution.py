"""
Chapter 21 Exercise SOLUTION: Weather Checker
==============================================
Check the weather for any city — no API key needed!
Powered by the awesome wttr.in service.

Run it: python solution.py
"""

import requests


def get_weather(city):
    """
    Fetch weather data for a given city from wttr.in.
    Returns parsed JSON data or None on failure.
    """
    # Replace spaces with + for URL encoding
    city_encoded = city.replace(" ", "+")
    url = f"https://wttr.in/{city_encoded}?format=j1"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()

        # wttr.in returns data even for invalid cities sometimes,
        # but current_condition will be empty or missing
        if not data.get("current_condition"):
            print(f"  No weather data found for '{city}'.")
            return None

        return data

    except requests.exceptions.ConnectionError:
        print("  No internet connection! Check your network.")
        return None
    except requests.exceptions.Timeout:
        print("  Request timed out. Try again later.")
        return None
    except requests.exceptions.HTTPError as e:
        print(f"  HTTP Error: {e}")
        return None
    except requests.exceptions.JSONDecodeError:
        print(f"  Invalid response for '{city}'. Is that a real city?")
        return None
    except Exception as e:
        print(f"  Unexpected error: {e}")
        return None


def display_weather(data, city):
    """Display current weather conditions in a nice format."""
    current = data["current_condition"][0]

    temp_c = current.get("temp_C", "N/A")
    temp_f = current.get("temp_F", "N/A")
    feels_c = current.get("FeelsLikeC", "N/A")
    feels_f = current.get("FeelsLikeF", "N/A")
    humidity = current.get("humidity", "N/A")
    description = current.get("weatherDesc", [{}])[0].get("value", "N/A")
    wind_kmph = current.get("windspeedKmph", "N/A")
    wind_mph = current.get("windspeedMiles", "N/A")
    wind_dir = current.get("winddir16Point", "N/A")
    visibility = current.get("visibility", "N/A")
    pressure = current.get("pressure", "N/A")
    uv_index = current.get("uvIndex", "N/A")

    # Pick a weather emoji
    desc_lower = description.lower()
    if "sun" in desc_lower or "clear" in desc_lower:
        emoji = "sunny"
    elif "cloud" in desc_lower or "overcast" in desc_lower:
        emoji = "cloudy"
    elif "rain" in desc_lower or "drizzle" in desc_lower:
        emoji = "rainy"
    elif "snow" in desc_lower:
        emoji = "snowy"
    elif "thunder" in desc_lower or "storm" in desc_lower:
        emoji = "stormy"
    elif "fog" in desc_lower or "mist" in desc_lower:
        emoji = "foggy"
    else:
        emoji = ""

    print(f"\n  {'=' * 45}")
    print(f"  Weather in {city.title()} ({emoji})")
    print(f"  {'=' * 45}")
    print(f"  Condition:    {description}")
    print(f"  Temperature:  {temp_c}C / {temp_f}F")
    print(f"  Feels like:   {feels_c}C / {feels_f}F")
    print(f"  Humidity:     {humidity}%")
    print(f"  Wind:         {wind_kmph} km/h ({wind_mph} mph) {wind_dir}")
    print(f"  Visibility:   {visibility} km")
    print(f"  Pressure:     {pressure} mb")
    print(f"  UV Index:     {uv_index}")
    print(f"  {'=' * 45}")

    # Fun commentary based on conditions
    temp_c_num = int(temp_c) if temp_c != "N/A" else 20
    if temp_c_num > 35:
        print(f"  Verdict: It's SCORCHING. Stay hydrated!")
    elif temp_c_num > 25:
        print(f"  Verdict: Nice and warm. Perfect for a walk!")
    elif temp_c_num > 15:
        print(f"  Verdict: Pleasant temperature. Enjoy it!")
    elif temp_c_num > 5:
        print(f"  Verdict: A bit chilly. Grab a jacket!")
    elif temp_c_num > 0:
        print(f"  Verdict: Cold! Bundle up!")
    else:
        print(f"  Verdict: FREEZING. Stay inside with hot cocoa!")


def display_forecast(data, city):
    """Display 3-day weather forecast."""
    weather = data.get("weather", [])

    if not weather:
        print("  No forecast data available.")
        return

    print(f"\n  {'=' * 55}")
    print(f"  3-Day Forecast for {city.title()}")
    print(f"  {'=' * 55}")
    print(f"  {'Date':<12} {'High':<10} {'Low':<10} {'Description':<25}")
    print(f"  {'-'*12} {'-'*10} {'-'*10} {'-'*25}")

    for day in weather[:3]:
        date = day.get("date", "N/A")
        max_c = day.get("maxtempC", "N/A")
        min_c = day.get("mintempC", "N/A")
        max_f = day.get("maxtempF", "N/A")
        min_f = day.get("mintempF", "N/A")

        # Get the general description from the hourly data (noon)
        hourly = day.get("hourly", [])
        if len(hourly) >= 4:
            desc = hourly[4].get("weatherDesc", [{}])[0].get("value", "N/A")
        elif hourly:
            desc = hourly[0].get("weatherDesc", [{}])[0].get("value", "N/A")
        else:
            desc = "N/A"

        print(f"  {date:<12} {max_c + 'C/' + max_f + 'F':<10} "
              f"{min_c + 'C/' + min_f + 'F':<10} {desc:<25}")

    print(f"  {'=' * 55}")


def main():
    """Main function — weather checker with a loop."""
    print("=" * 45)
    print("  WEATHER CHECKER")
    print("  Powered by wttr.in (free, no API key!)")
    print("=" * 45)
    print("  Type a city name to check the weather.")
    print("  Type 'quit' to exit.\n")

    while True:
        city = input("  Enter a city (or 'quit'): ").strip()

        if not city:
            print("  Please enter a city name!\n")
            continue

        if city.lower() in ("quit", "exit", "q"):
            print("\n  Stay dry out there! Goodbye!")
            break

        print(f"\n  Fetching weather for '{city}'...")
        data = get_weather(city)

        if data:
            display_weather(data, city)

            # Ask about forecast
            show_forecast = input("\n  Show 3-day forecast? (y/n): ").strip().lower()
            if show_forecast == "y":
                display_forecast(data, city)

        print()  # blank line before next prompt


if __name__ == "__main__":
    main()
