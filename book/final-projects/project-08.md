# Project 8: Blog REST API

> **Difficulty:** 4/5 | **Time:** ~3 hours | **Skills:** Flask, SQLite, CRUD, authentication
> **Code:** https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/final-projects/project-08-blog-api/

## What You'll Build

A fully functional REST API for a blog application using Flask and SQLite. It includes user registration and login with token-based authentication, full CRUD operations for blog posts, and proper HTTP status codes. You can test it with `curl` or any API testing tool.

Here's what interacting with it looks like:

```bash
# Register a user
$ curl -X POST http://localhost:5000/api/register \
    -H "Content-Type: application/json" \
    -d '{"username": "alice", "password": "secret123"}'

{"message": "User created successfully", "user_id": 1}

# Login and get a token
$ curl -X POST http://localhost:5000/api/login \
    -H "Content-Type: application/json" \
    -d '{"username": "alice", "password": "secret123"}'

{"token": "abc123xyz...", "username": "alice"}

# Create a blog post
$ curl -X POST http://localhost:5000/api/posts \
    -H "Authorization: Bearer abc123xyz..." \
    -H "Content-Type: application/json" \
    -d '{"title": "My First Post", "content": "Hello, world!"}'

{"id": 1, "title": "My First Post", "author": "alice", "created_at": "..."}
```

## Skills You'll Use

- Flask web framework (learned in Chapter 15)
- SQLite database (learned in Chapter 11)
- REST API design (learned in Chapter 15)
- Password hashing (learned in Chapter 15)
- Error handling (learned in Chapter 8)
- JSON (learned in Chapter 7)

## Step-by-Step Build Guide

### Step 1: Install Dependencies and Set Up

```bash
pip install flask
```

Create the project structure:

```python
# blog_api.py

import sqlite3
import hashlib
import secrets
import os
from datetime import datetime
from functools import wraps
from flask import Flask, request, jsonify, g

app = Flask(__name__)
app.config["DATABASE"] = "blog.db"
```

### Step 2: Set Up the Database Layer

We'll use SQLite with a helper pattern that gives each request its own database connection.

```python
def get_db():
    """Get a database connection for the current request."""
    if "db" not in g:
        g.db = sqlite3.connect(app.config["DATABASE"])
        g.db.row_factory = sqlite3.Row  # Return rows as dictionaries
        g.db.execute("PRAGMA foreign_keys = ON")
    return g.db


@app.teardown_appcontext
def close_db(exception):
    """Close database connection when request ends."""
    db = g.pop("db", None)
    if db is not None:
        db.close()


def init_db():
    """Create database tables if they don't exist."""
    db = sqlite3.connect(app.config["DATABASE"])
    db.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            token TEXT UNIQUE,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """)
    db.execute("""
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            author_id INTEGER NOT NULL,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            updated_at TEXT DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (author_id) REFERENCES users (id)
        )
    """)
    db.commit()
    db.close()
```

### Step 3: Build Authentication

We need three pieces: password hashing, token generation, and a decorator to protect routes.

```python
def hash_password(password):
    """Hash a password with a salt using SHA-256."""
    salt = secrets.token_hex(16)
    hash_value = hashlib.sha256((salt + password).encode()).hexdigest()
    return f"{salt}:{hash_value}"


def verify_password(stored_hash, password):
    """Verify a password against a stored hash."""
    salt, hash_value = stored_hash.split(":")
    check = hashlib.sha256((salt + password).encode()).hexdigest()
    return check == hash_value


def generate_token():
    """Generate a secure random token."""
    return secrets.token_hex(32)


def login_required(f):
    """Decorator to require authentication on a route."""
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get("Authorization")

        if not auth_header or not auth_header.startswith("Bearer "):
            return jsonify({"error": "Missing or invalid token"}), 401

        token = auth_header.split(" ")[1]

        db = get_db()
        user = db.execute(
            "SELECT * FROM users WHERE token = ?", (token,)
        ).fetchone()

        if not user:
            return jsonify({"error": "Invalid or expired token"}), 401

        # Attach user info to the request context
        g.current_user = dict(user)
        return f(*args, **kwargs)

    return decorated
```

### Step 4: Create Auth Endpoints

```python
@app.route("/api/register", methods=["POST"])
def register():
    """Register a new user."""
    data = request.get_json()

    if not data or not data.get("username") or not data.get("password"):
        return jsonify({"error": "Username and password are required"}), 400

    username = data["username"].strip()
    password = data["password"]

    if len(username) < 3:
        return jsonify({"error": "Username must be at least 3 characters"}), 400
    if len(password) < 6:
        return jsonify({"error": "Password must be at least 6 characters"}), 400

    db = get_db()

    # Check if username exists
    existing = db.execute(
        "SELECT id FROM users WHERE username = ?", (username,)
    ).fetchone()

    if existing:
        return jsonify({"error": "Username already taken"}), 409

    password_hash = hash_password(password)

    cursor = db.execute(
        "INSERT INTO users (username, password_hash) VALUES (?, ?)",
        (username, password_hash)
    )
    db.commit()

    return jsonify({
        "message": "User created successfully",
        "user_id": cursor.lastrowid
    }), 201


@app.route("/api/login", methods=["POST"])
def login():
    """Login and receive an auth token."""
    data = request.get_json()

    if not data or not data.get("username") or not data.get("password"):
        return jsonify({"error": "Username and password are required"}), 400

    db = get_db()
    user = db.execute(
        "SELECT * FROM users WHERE username = ?", (data["username"],)
    ).fetchone()

    if not user or not verify_password(user["password_hash"], data["password"]):
        return jsonify({"error": "Invalid username or password"}), 401

    # Generate and store a new token
    token = generate_token()
    db.execute(
        "UPDATE users SET token = ? WHERE id = ?", (token, user["id"])
    )
    db.commit()

    return jsonify({
        "token": token,
        "username": user["username"],
        "message": "Login successful"
    })
```

### Step 5: Build the Blog Post CRUD Endpoints

These are the core of the API -- creating, reading, updating, and deleting blog posts.

```python
@app.route("/api/posts", methods=["GET"])
def get_posts():
    """Get all posts (public, no auth required)."""
    db = get_db()

    # Support optional query parameters
    author = request.args.get("author")
    limit = request.args.get("limit", 20, type=int)
    offset = request.args.get("offset", 0, type=int)

    if author:
        rows = db.execute("""
            SELECT p.*, u.username as author_name
            FROM posts p JOIN users u ON p.author_id = u.id
            WHERE u.username = ?
            ORDER BY p.created_at DESC
            LIMIT ? OFFSET ?
        """, (author, limit, offset)).fetchall()
    else:
        rows = db.execute("""
            SELECT p.*, u.username as author_name
            FROM posts p JOIN users u ON p.author_id = u.id
            ORDER BY p.created_at DESC
            LIMIT ? OFFSET ?
        """, (limit, offset)).fetchall()

    posts = []
    for row in rows:
        posts.append({
            "id": row["id"],
            "title": row["title"],
            "content": row["content"],
            "author": row["author_name"],
            "created_at": row["created_at"],
            "updated_at": row["updated_at"]
        })

    return jsonify({"posts": posts, "count": len(posts)})


@app.route("/api/posts/<int:post_id>", methods=["GET"])
def get_post(post_id):
    """Get a single post by ID."""
    db = get_db()
    row = db.execute("""
        SELECT p.*, u.username as author_name
        FROM posts p JOIN users u ON p.author_id = u.id
        WHERE p.id = ?
    """, (post_id,)).fetchone()

    if not row:
        return jsonify({"error": "Post not found"}), 404

    return jsonify({
        "id": row["id"],
        "title": row["title"],
        "content": row["content"],
        "author": row["author_name"],
        "created_at": row["created_at"],
        "updated_at": row["updated_at"]
    })


@app.route("/api/posts", methods=["POST"])
@login_required
def create_post():
    """Create a new blog post (auth required)."""
    data = request.get_json()

    if not data or not data.get("title") or not data.get("content"):
        return jsonify({"error": "Title and content are required"}), 400

    title = data["title"].strip()
    content = data["content"].strip()

    if len(title) > 200:
        return jsonify({"error": "Title must be under 200 characters"}), 400

    db = get_db()
    now = datetime.now().isoformat()

    cursor = db.execute(
        """INSERT INTO posts (title, content, author_id, created_at, updated_at)
           VALUES (?, ?, ?, ?, ?)""",
        (title, content, g.current_user["id"], now, now)
    )
    db.commit()

    return jsonify({
        "id": cursor.lastrowid,
        "title": title,
        "content": content,
        "author": g.current_user["username"],
        "created_at": now
    }), 201


@app.route("/api/posts/<int:post_id>", methods=["PUT"])
@login_required
def update_post(post_id):
    """Update a blog post (only the author can update)."""
    db = get_db()
    post = db.execute("SELECT * FROM posts WHERE id = ?", (post_id,)).fetchone()

    if not post:
        return jsonify({"error": "Post not found"}), 404
    if post["author_id"] != g.current_user["id"]:
        return jsonify({"error": "You can only edit your own posts"}), 403

    data = request.get_json()
    title = data.get("title", post["title"]).strip()
    content = data.get("content", post["content"]).strip()
    now = datetime.now().isoformat()

    db.execute(
        "UPDATE posts SET title = ?, content = ?, updated_at = ? WHERE id = ?",
        (title, content, now, post_id)
    )
    db.commit()

    return jsonify({
        "id": post_id,
        "title": title,
        "content": content,
        "updated_at": now,
        "message": "Post updated"
    })


@app.route("/api/posts/<int:post_id>", methods=["DELETE"])
@login_required
def delete_post(post_id):
    """Delete a blog post (only the author can delete)."""
    db = get_db()
    post = db.execute("SELECT * FROM posts WHERE id = ?", (post_id,)).fetchone()

    if not post:
        return jsonify({"error": "Post not found"}), 404
    if post["author_id"] != g.current_user["id"]:
        return jsonify({"error": "You can only delete your own posts"}), 403

    db.execute("DELETE FROM posts WHERE id = ?", (post_id,))
    db.commit()

    return jsonify({"message": "Post deleted", "id": post_id})
```

### Step 6: Add Error Handlers and Run

```python
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Endpoint not found"}), 404


@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify({"error": "Method not allowed"}), 405


@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500


if __name__ == "__main__":
    init_db()
    print("Blog API running at http://localhost:5000")
    print("\nEndpoints:")
    print("  POST   /api/register     - Register a new user")
    print("  POST   /api/login        - Login and get token")
    print("  GET    /api/posts        - List all posts")
    print("  GET    /api/posts/<id>   - Get a single post")
    print("  POST   /api/posts        - Create a post (auth)")
    print("  PUT    /api/posts/<id>   - Update a post (auth)")
    print("  DELETE /api/posts/<id>   - Delete a post (auth)")
    app.run(debug=True)
```

### Step 7: Test Your API

Start the server and test with `curl` commands:

```bash
# Start the server
python blog_api.py

# In another terminal:

# Register
curl -X POST http://localhost:5000/api/register \
  -H "Content-Type: application/json" \
  -d '{"username": "alice", "password": "secret123"}'

# Login (copy the token from the response)
curl -X POST http://localhost:5000/api/login \
  -H "Content-Type: application/json" \
  -d '{"username": "alice", "password": "secret123"}'

# Create a post (replace YOUR_TOKEN)
curl -X POST http://localhost:5000/api/posts \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"title": "Hello World", "content": "My first blog post!"}'

# Get all posts
curl http://localhost:5000/api/posts

# Update a post
curl -X PUT http://localhost:5000/api/posts/1 \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"title": "Hello World (Updated)"}'

# Delete a post
curl -X DELETE http://localhost:5000/api/posts/1 \
  -H "Authorization: Bearer YOUR_TOKEN"
```

## Challenges (Level Up!)

1. **Comments system:** Add a comments table linked to posts. Create endpoints for adding, listing, and deleting comments. Comments should require authentication, and only the comment author or the post author can delete a comment.

2. **Pagination and search:** Add proper pagination with `page` and `per_page` query parameters, returning total count and page info. Add a `/api/posts/search?q=keyword` endpoint that searches titles and content.

3. **Rate limiting:** Implement simple rate limiting that allows only 30 requests per minute per token. Track request timestamps in memory and return a 429 status when the limit is exceeded.

## Portfolio Tips

A REST API is one of the most valuable portfolio pieces you can have -- it's the backbone of modern web applications. When presenting this:

- **GitHub:** Include a comprehensive README with all endpoints documented, example `curl` commands, and setup instructions. Consider adding a Postman collection file.
- **Resume:** "Built a RESTful blog API with Flask featuring token-based authentication, SQLite persistence, full CRUD operations, and authorization controls."
- **Interview talking point:** Discuss your authentication approach (token-based vs. session-based), why you check authorization on update/delete (only the author can modify their own posts), and how you'd improve security for production (HTTPS, JWT with expiration, password complexity rules, input sanitization).
