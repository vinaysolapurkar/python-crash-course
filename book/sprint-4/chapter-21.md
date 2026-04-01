# Chapter 21: Working with APIs -- Talking to the Internet

> **Sprint 4, Chapter 21** | **Estimated Time: 20-25 minutes** | **Difficulty: Advanced**

## Why Should I Care?

Every time you check the weather on your phone, that app doesn't have its own weather satellites. It asks someone else's server for the data. Every time you see stock prices update in real time, your app is calling an API. Social media bots, AI chatbots, payment processing, maps, translation services -- all APIs.

**APIs are how programs talk to each other over the internet.** If you want to build anything that connects to the outside world -- and you do -- you need this chapter.

## The Restaurant Analogy

Think of an API like **ordering at a restaurant**.

- **You** are the client (your Python program)
- **The menu** is the API documentation (what you can order)
- **Your order** is the request (what you're asking for)
- **The waiter** is the API (the intermediary)
- **The kitchen** is the server (where the work happens)
- **Your food** is the response (what you get back)

You don't walk into the kitchen and cook your own food. You don't need to know *how* the kitchen works. You just read the menu, place your order, and the waiter brings you what you asked for.

APIs work exactly the same way. You don't need to know how Google's weather service works internally. You just send a request and get data back.

## HTTP Methods: The Four Magic Words

When you talk to an API, you use **HTTP methods** -- think of them as different types of requests:

| Method | What It Does | Restaurant Analogy |
|---|---|---|
| `GET` | Read/retrieve data | "Can I see the menu?" |
| `POST` | Create new data | "I'd like to place an order." |
| `PUT` | Update existing data | "Actually, change my order to..." |
| `DELETE` | Remove data | "Cancel my order." |

90% of the time, you'll use `GET` (reading data) and `POST` (sending data). The others are important but less common for beginners.

## The requests Library

Python's built-in `urllib` library can make HTTP requests, but it's painful to use. The `requests` library is what everyone actually uses. It's not built-in, so install it first:

```bash
pip install requests
```

### Your First API Call

Let's start with the simplest possible API call -- getting a random joke:

```python
import requests

response = requests.get("https://official-joke-api.appspot.com/random_joke")

print(response.status_code)  # 200
print(response.json())
# {'type': 'general', 'setup': 'Why did the scarecrow win an award?',
#  'punchline': 'Because he was outstanding in his field.'}
```

That's it. Three lines of code and you're talking to the internet.

Let's break it down:

1. `requests.get(url)` -- sends a GET request to that URL
2. `response.status_code` -- the HTTP status code (200 means success)
3. `response.json()` -- parses the response body as JSON (a Python dictionary)

## Status Codes: What the Server Is Telling You

When the server responds, it includes a status code that tells you what happened:

| Code | Meaning | What to Do |
|---|---|---|
| `200` | OK -- success! | Parse the data |
| `201` | Created -- new resource made | Your POST worked |
| `400` | Bad Request -- you messed up | Check your request |
| `401` | Unauthorized -- need credentials | Add an API key |
| `403` | Forbidden -- not allowed | You don't have permission |
| `404` | Not Found -- doesn't exist | Check the URL |
| `429` | Too Many Requests -- slow down | Wait and retry |
| `500` | Server Error -- they messed up | Not your fault, try again later |

The easy rule: **2xx means success, 4xx means you did something wrong, 5xx means the server did something wrong.**

> **Pro Tip:** Always check the response status code before trying to parse the data. A `404` response doesn't have the data you expect, and trying to parse it will give you confusing errors.

## Parsing JSON Responses

Most APIs return data in **JSON** format (JavaScript Object Notation). Good news -- JSON maps directly to Python dictionaries and lists:

```python
import requests

response = requests.get("https://api.github.com/users/python")

if response.status_code == 200:
    data = response.json()
    
    print(f"Name: {data['name']}")
    print(f"Location: {data['location']}")
    print(f"Public repos: {data['public_repos']}")
    print(f"Followers: {data['followers']}")
else:
    print(f"Error: {response.status_code}")
```

JSON objects become Python dicts. JSON arrays become Python lists. JSON strings, numbers, booleans, and null become their Python equivalents. It's a seamless translation.

## Sending Data with POST Requests

GET retrieves data. POST sends data. Here's how:

```python
import requests

# POST with JSON data
data = {
    "title": "My Post",
    "body": "This is the content.",
    "userId": 1
}

response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json=data  # Automatically converts to JSON and sets headers
)

print(response.status_code)  # 201 (Created)
print(response.json())
# {'title': 'My Post', 'body': 'This is the content.', 'userId': 1, 'id': 101}
```

The `json=data` parameter is a shortcut that:
1. Converts your Python dict to a JSON string
2. Sets the `Content-Type` header to `application/json`

## Query Parameters

Many APIs let you customize your request with query parameters -- the stuff after the `?` in a URL:

```python
import requests

# Instead of building the URL manually...
# requests.get("https://api.github.com/search/repositories?q=python&sort=stars")

# ...use the params argument (cleaner)
params = {
    "q": "python",
    "sort": "stars",
    "per_page": 5
}

response = requests.get(
    "https://api.github.com/search/repositories",
    params=params
)

data = response.json()
for repo in data["items"]:
    print(f"{repo['name']}: {repo['stargazers_count']:,} stars")
```

Using `params=` is cleaner than building the URL string yourself, and it handles special characters automatically.

## API Keys and Authentication

Most serious APIs require authentication -- usually an **API key**. This is a unique string that identifies you and tracks your usage.

```python
import requests

# Method 1: API key as a query parameter
response = requests.get(
    "https://api.example.com/data",
    params={"api_key": "your_key_here"}
)

# Method 2: API key in headers (more common, more secure)
headers = {
    "Authorization": "Bearer your_api_key_here"
}
response = requests.get(
    "https://api.example.com/data",
    headers=headers
)

# Method 3: Basic authentication
response = requests.get(
    "https://api.example.com/data",
    auth=("username", "password")
)
```

> **Wait, What?** "Where do I get an API key?" Sign up on the API provider's website. Most have a free tier. OpenWeatherMap, GitHub, NewsAPI -- they all give you a key when you register.

**Important:** Never put API keys directly in your code, especially if you're pushing to GitHub. Use environment variables:

```python
import os
import requests

api_key = os.environ.get("WEATHER_API_KEY")

if not api_key:
    print("Error: Set the WEATHER_API_KEY environment variable")
else:
    response = requests.get(
        "https://api.openweathermap.org/data/2.5/weather",
        params={"q": "London", "appid": api_key}
    )
```

## Rate Limiting: Don't Be That Person

APIs limit how many requests you can make in a given time period. This is called **rate limiting**. Hit the limit and you'll get a `429 Too Many Requests` response.

```python
import requests
import time

def polite_request(url, max_retries=3, delay=1):
    """Make a request with retry logic for rate limiting."""
    for attempt in range(max_retries):
        response = requests.get(url)
        
        if response.status_code == 200:
            return response
        elif response.status_code == 429:
            wait_time = int(response.headers.get("Retry-After", delay))
            print(f"Rate limited. Waiting {wait_time} seconds...")
            time.sleep(wait_time)
        else:
            response.raise_for_status()  # Raise an exception for other errors
    
    print("Max retries exceeded")
    return None
```

General rules:
- Read the API docs for rate limits
- Add a small delay between requests (`time.sleep(1)`)
- Cache responses when possible (don't ask for the same data twice)
- Handle 429 responses gracefully

## Error Handling for API Calls

API calls can fail in many ways -- network errors, timeouts, bad responses. Always handle errors:

```python
import requests

def safe_api_call(url, timeout=10):
    """Make an API call with proper error handling."""
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()  # Raises exception for 4xx/5xx
        return response.json()
    
    except requests.exceptions.Timeout:
        print(f"Request timed out after {timeout} seconds")
        return None
    
    except requests.exceptions.ConnectionError:
        print("Could not connect. Check your internet connection.")
        return None
    
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error: {e}")
        return None
    
    except requests.exceptions.JSONDecodeError:
        print("Response was not valid JSON")
        return None

# Use it
data = safe_api_call("https://api.github.com/users/python")
if data:
    print(f"Name: {data['name']}")
```

The `timeout=10` parameter prevents your program from hanging forever if the server doesn't respond. Always set a timeout.

> **Don't Panic:** API error handling looks like a lot of code, but it's the same pattern every time. Write it once, reuse it forever. Professional developers copy-paste this pattern into every project.

## Putting It All Together: A Complete API Client

Let's build a simple GitHub user lookup tool:

```python
import requests

class GitHubClient:
    """Simple GitHub API client."""
    
    BASE_URL = "https://api.github.com"
    
    def __init__(self, token=None):
        self.session = requests.Session()
        if token:
            self.session.headers["Authorization"] = f"Bearer {token}"
    
    def get_user(self, username):
        """Get info about a GitHub user."""
        response = self.session.get(
            f"{self.BASE_URL}/users/{username}",
            timeout=10
        )
        
        if response.status_code == 404:
            print(f"User '{username}' not found.")
            return None
        
        response.raise_for_status()
        data = response.json()
        
        return {
            "name": data.get("name", "N/A"),
            "bio": data.get("bio", "N/A"),
            "public_repos": data["public_repos"],
            "followers": data["followers"],
            "url": data["html_url"]
        }
    
    def get_repos(self, username, sort="stars"):
        """Get a user's repositories."""
        response = self.session.get(
            f"{self.BASE_URL}/users/{username}/repos",
            params={"sort": sort, "per_page": 5},
            timeout=10
        )
        response.raise_for_status()
        
        return [
            {"name": repo["name"], "stars": repo["stargazers_count"]}
            for repo in response.json()
        ]

# Use it
client = GitHubClient()

user = client.get_user("python")
if user:
    print(f"Name: {user['name']}")
    print(f"Bio: {user['bio']}")
    print(f"Repos: {user['public_repos']}")
    print(f"Followers: {user['followers']:,}")

print("\nTop repos:")
for repo in client.get_repos("python"):
    print(f"  {repo['name']}: {repo['stars']:,} stars")
```

Notice we used `requests.Session()` -- this reuses the connection and headers across multiple requests. More efficient and cleaner.

## Your Turn: Weather Checker

**Challenge:** Build a weather checker using the free wttr.in API (no API key needed!):

```python
import requests

def get_weather(city):
    """Get weather for a city using wttr.in."""
    response = requests.get(
        f"https://wttr.in/{city}",
        params={"format": "j1"}  # JSON format
    )
    
    if response.status_code == 200:
        data = response.json()
        current = data["current_condition"][0]
        
        return {
            "city": city,
            "temp_c": current["temp_C"],
            "temp_f": current["temp_F"],
            "description": current["weatherDesc"][0]["value"],
            "humidity": current["humidity"],
            "wind_speed": current["windspeedKmph"]
        }
    return None

# Test it
weather = get_weather("London")
if weather:
    print(f"Weather in {weather['city']}:")
    print(f"  Temperature: {weather['temp_c']}C / {weather['temp_f']}F")
    print(f"  Conditions: {weather['description']}")
    print(f"  Humidity: {weather['humidity']}%")
```

Extend it to:
1. Accept city names from user input
2. Handle errors (bad city names, no internet)
3. Compare weather between two cities

**Starter code:** [https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/sprint-4-pro/chapter-21-apis/](https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/sprint-4-pro/chapter-21-apis/)

## TL;DR

| Concept | What It Does |
|---|---|
| API | A way for programs to talk to each other over the internet |
| `requests.get(url)` | Send a GET request (retrieve data) |
| `requests.post(url, json=data)` | Send a POST request (send data) |
| `response.status_code` | HTTP status code (200 = OK, 404 = not found) |
| `response.json()` | Parse the response as a Python dictionary |
| `params={}` | Add query parameters to the URL |
| `headers={}` | Add headers (like API keys) to the request |
| `timeout=10` | Don't wait forever for a response |
| `response.raise_for_status()` | Raise an exception if the status code is 4xx or 5xx |

**The one-sentence version:** Use the `requests` library to send HTTP requests to APIs, get back JSON data, and always handle errors and check status codes.

Next up: Databases -- where we learn to store data for real, not just in files.
