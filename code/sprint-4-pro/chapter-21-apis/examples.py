"""
Chapter 21: Working with APIs — Talking to the Internet
========================================================

APIs (Application Programming Interfaces) let your code talk to other services.

The Restaurant Analogy:
  - YOU are the customer (your Python code)
  - The MENU is the API documentation (tells you what you can order)
  - The WAITER is the HTTP request (carries your order to the kitchen)
  - The KITCHEN is the server (does the actual work)
  - The FOOD is the response (what you get back — usually JSON data)

You don't need to know HOW the kitchen works.
You just need to know what's on the menu and how to order.

We'll use the 'requests' library — install it with: pip install requests
"""

# ============================================================
# 0. Setup Check
# ============================================================
try:
    import requests
except ImportError:
    print("Please install requests: pip install requests")
    print("Then run this file again!")
    exit(1)

import json

# ============================================================
# 1. HTTP Methods — The Verbs of the Internet
# ============================================================
print("=" * 50)
print("1. HTTP METHODS EXPLAINED")
print("=" * 50)
print("""
HTTP methods are like verbs — they describe WHAT you want to do:

  GET    → "Give me data"        (reading a webpage, fetching info)
  POST   → "Here's new data"     (submitting a form, creating something)
  PUT    → "Update this data"    (replacing an entire record)
  PATCH  → "Change part of this" (updating just one field)
  DELETE → "Remove this"         (deleting a record)

90% of the time, you'll use GET and POST. Let's start there!
""")


# ============================================================
# 2. Your First API Call — GET Request
# ============================================================
print("=" * 50)
print("2. FIRST API CALL — GET")
print("=" * 50)

# JSONPlaceholder is a free fake API for testing. No API key needed!
# It's like a practice dummy for API calls.

url = "https://jsonplaceholder.typicode.com/posts/1"
print(f"Requesting: {url}")

try:
    response = requests.get(url, timeout=10)

    # The response object has lots of useful info:
    print(f"\nStatus Code: {response.status_code}")  # 200 = success!
    print(f"Content-Type: {response.headers.get('Content-Type', 'N/A')}")

    # Parse the JSON response
    data = response.json()  # converts JSON string to Python dict
    print(f"\nResponse Data:")
    print(f"  ID:     {data['id']}")
    print(f"  Title:  {data['title'][:50]}...")
    print(f"  Body:   {data['body'][:80]}...")
    print(f"  UserID: {data['userId']}")

except requests.exceptions.ConnectionError:
    print("Could not connect. Check your internet connection!")
except requests.exceptions.Timeout:
    print("Request timed out. The server is taking too long.")
except Exception as e:
    print(f"Something went wrong: {e}")


# ============================================================
# 3. Status Codes — What the Server Is Telling You
# ============================================================
print("\n" + "=" * 50)
print("3. HTTP STATUS CODES")
print("=" * 50)
print("""
Status codes are the server's way of saying how things went:

  2xx — SUCCESS (yay!)
    200  OK                  → Everything worked
    201  Created             → New resource was created
    204  No Content          → Success, but nothing to show

  3xx — REDIRECT
    301  Moved Permanently   → Use this other URL from now on
    304  Not Modified        → Nothing changed since last time

  4xx — CLIENT ERROR (your fault)
    400  Bad Request         → Your request doesn't make sense
    401  Unauthorized        → Login first!
    403  Forbidden           → You're logged in but not allowed
    404  Not Found           → That thing doesn't exist
    429  Too Many Requests   → Slow down! Rate limited.

  5xx — SERVER ERROR (their fault)
    500  Internal Server Error → Something broke on their end
    503  Service Unavailable   → Server is down for maintenance

Pro tip: 200 is your best friend. 404 is the internet's inside joke.
""")


# Demonstrate different status codes
print("--- Testing Status Codes ---")
test_urls = [
    ("https://jsonplaceholder.typicode.com/posts/1", "Valid post"),
    ("https://jsonplaceholder.typicode.com/posts/999999", "Non-existent post"),
]

for url, description in test_urls:
    try:
        resp = requests.get(url, timeout=10)
        print(f"  {description}: {resp.status_code}")
    except Exception as e:
        print(f"  {description}: Error - {e}")


# ============================================================
# 4. Query Parameters — Filtering Your Request
# ============================================================
print("\n" + "=" * 50)
print("4. QUERY PARAMETERS")
print("=" * 50)

# Query params are like adding filters to your search
# URL: /posts?userId=1&_limit=3
# Same as: "Give me posts by user 1, but only 3 of them"

try:
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts",
        params={
            "userId": 1,     # filter by user
            "_limit": 3,     # limit results
        },
        timeout=10,
    )

    print(f"URL sent: {response.url}")  # shows the full URL with params
    posts = response.json()
    print(f"Got {len(posts)} posts by User 1:\n")
    for post in posts:
        print(f"  [{post['id']}] {post['title'][:50]}")

except Exception as e:
    print(f"Error: {e}")


# ============================================================
# 5. POST Request — Sending Data
# ============================================================
print("\n" + "=" * 50)
print("5. POST REQUEST — SENDING DATA")
print("=" * 50)

# POST sends data TO the server (like submitting a form)
new_post = {
    "title": "Learning Python APIs",
    "body": "APIs are like restaurant waiters for your code!",
    "userId": 42,
}

try:
    response = requests.post(
        "https://jsonplaceholder.typicode.com/posts",
        json=new_post,  # 'json=' automatically sets Content-Type header
        timeout=10,
    )

    print(f"Status: {response.status_code}")  # 201 Created!
    created = response.json()
    print(f"Created post with ID: {created.get('id')}")
    print(f"Title: {created.get('title')}")
    # Note: JSONPlaceholder fakes the creation — it doesn't actually save it.

except Exception as e:
    print(f"Error: {e}")


# ============================================================
# 6. Headers — Extra Info with Your Request
# ============================================================
print("\n" + "=" * 50)
print("6. HEADERS")
print("=" * 50)

# Headers carry metadata about your request
# Think of them as notes on the outside of an envelope

try:
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts/1",
        headers={
            "Accept": "application/json",      # "I want JSON back"
            "User-Agent": "PythonCrashCourse/1.0",  # identify yourself
        },
        timeout=10,
    )

    # Response headers tell you about the server's response
    print("Response headers (selected):")
    for header in ["Content-Type", "Content-Length", "Cache-Control"]:
        value = response.headers.get(header, "N/A")
        print(f"  {header}: {value}")

except Exception as e:
    print(f"Error: {e}")


# ============================================================
# 7. Error Handling — Being a Responsible API Consumer
# ============================================================
print("\n" + "=" * 50)
print("7. PROPER ERROR HANDLING")
print("=" * 50)


def safe_api_call(url, params=None):
    """
    A well-behaved API call with proper error handling.
    Always wrap API calls in try/except — the internet is unpredictable!
    """
    try:
        response = requests.get(url, params=params, timeout=10)

        # raise_for_status() throws an exception for 4xx/5xx status codes
        response.raise_for_status()

        return response.json()

    except requests.exceptions.ConnectionError:
        print("  Network error: Can't reach the server.")
        print("  Check your internet connection!")
    except requests.exceptions.Timeout:
        print("  Timeout: The server took too long to respond.")
        print("  Try again later!")
    except requests.exceptions.HTTPError as e:
        print(f"  HTTP Error: {e}")
        if response.status_code == 404:
            print("  That resource doesn't exist!")
        elif response.status_code == 429:
            print("  Slow down! You're making too many requests.")
    except requests.exceptions.JSONDecodeError:
        print("  The response isn't valid JSON.")
    except Exception as e:
        print(f"  Unexpected error: {e}")

    return None  # return None if anything went wrong


# Test our safe function
print("--- Safe API calls ---")
result = safe_api_call("https://jsonplaceholder.typicode.com/users/1")
if result:
    print(f"  Got user: {result['name']} ({result['email']})")

print()
result = safe_api_call("https://jsonplaceholder.typicode.com/posts/999999")
if result:
    print(f"  Got: {result}")
else:
    print("  (Result was empty — that's expected for a non-existent post)")


# ============================================================
# 8. Working with Multiple Results
# ============================================================
print("\n" + "=" * 50)
print("8. WORKING WITH API DATA")
print("=" * 50)

try:
    # Get all users
    users = requests.get(
        "https://jsonplaceholder.typicode.com/users",
        timeout=10,
    ).json()

    print(f"Got {len(users)} users:\n")

    # Process and display the data
    print(f"  {'Name':<25} {'Email':<30} {'City':<15}")
    print(f"  {'-'*25} {'-'*30} {'-'*15}")
    for user in users:
        name = user['name']
        email = user['email']
        city = user['address']['city']
        print(f"  {name:<25} {email:<30} {city:<15}")

    # Some analysis
    print(f"\n  Most common email domain: "
          f"{max(set(u['email'].split('@')[1] for u in users), key=lambda d: sum(1 for u in users if d in u['email']))}")

except Exception as e:
    print(f"Error: {e}")


# ============================================================
# Recap
# ============================================================
print("\n" + "=" * 50)
print("CHAPTER 21 RECAP")
print("=" * 50)
print("""
API Cheat Sheet:
-----------------------------------------------------------------
INSTALL:         pip install requests

GET DATA:        response = requests.get(url, params={...}, timeout=10)
SEND DATA:       response = requests.post(url, json={...}, timeout=10)

RESPONSE:
  response.status_code   → 200, 404, etc.
  response.json()        → parse JSON to Python dict/list
  response.text          → raw text response
  response.headers       → response headers
  response.url           → actual URL that was requested

PARAMS:          requests.get(url, params={"key": "value"})
HEADERS:         requests.get(url, headers={"Accept": "application/json"})
TIMEOUT:         Always set a timeout!

ERROR HANDLING:
  response.raise_for_status()   → raise exception for 4xx/5xx
  try/except with specific exception types

GOLDEN RULES:
  1. Always use timeout (don't wait forever!)
  2. Always handle errors (the internet is unpredictable)
  3. Check status codes (200 = good, 4xx = your fault, 5xx = their fault)
  4. Respect rate limits (don't spam the server)
  5. Read the API docs (it's the menu — know what you can order!)
-----------------------------------------------------------------
""")
