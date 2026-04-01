"""
=============================================================
  PROJECT 8: BLOG REST API - SOLUTION
=============================================================
  A RESTful blog API built with Flask and SQLite.
  Features CRUD operations and simple token authentication.

  Dependencies:
    pip install flask

  Run:  python solution.py

  The API will be available at http://localhost:5000

  ── TESTING WITH CURL ──────────────────────────────────────

  # List all posts
  curl http://localhost:5000/posts

  # Get a single post
  curl http://localhost:5000/posts/1

  # Create a post (requires auth token)
  curl -X POST http://localhost:5000/posts \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer my-secret-token" \
    -d '{"title":"My First Post","content":"Hello world!","author":"Alice"}'

  # Update a post
  curl -X PUT http://localhost:5000/posts/1 \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer my-secret-token" \
    -d '{"title":"Updated Title","content":"New content"}'

  # Delete a post
  curl -X DELETE http://localhost:5000/posts/1 \
    -H "Authorization: Bearer my-secret-token"

  # Try without auth (should get 401)
  curl -X POST http://localhost:5000/posts \
    -H "Content-Type: application/json" \
    -d '{"title":"Sneaky Post"}'

=============================================================
"""

try:
    from flask import Flask, request, jsonify
except ImportError:
    print("Flask not installed. Run: pip install flask")
    exit(1)

import sqlite3
from datetime import datetime
from functools import wraps

# ── App Configuration ──────────────────────────────────────
app = Flask(__name__)

# In a real app, this would be in an environment variable!
API_TOKEN = "my-secret-token"
DATABASE = "blog.db"


# ── Database Helpers ───────────────────────────────────────

def get_db():
    """Get a SQLite database connection."""
    conn = sqlite3.connect(DATABASE)
    # Return rows as dict-like objects instead of tuples
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """Create the posts table if it doesn't exist."""
    conn = get_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            author TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()
    print("[DB] Database initialized.")


def row_to_dict(row):
    """Convert a sqlite3.Row to a regular dictionary."""
    if row is None:
        return None
    return dict(row)


# ── Authentication ─────────────────────────────────────────

def require_auth(f):
    """
    Decorator that checks for a valid Bearer token.
    Returns 401 Unauthorized if the token is missing or wrong.
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get("Authorization", "")

        # Expected format: "Bearer my-secret-token"
        if not auth_header.startswith("Bearer "):
            return jsonify({"error": "Missing Authorization header"}), 401

        token = auth_header.split("Bearer ", 1)[1].strip()
        if token != API_TOKEN:
            return jsonify({"error": "Invalid token"}), 401

        return f(*args, **kwargs)

    return decorated


# ── API Endpoints ──────────────────────────────────────────

@app.route("/")
def index():
    """Welcome page with API documentation."""
    return jsonify({
        "message": "Welcome to the Blog API!",
        "endpoints": {
            "GET /posts": "List all posts",
            "GET /posts/<id>": "Get a single post",
            "POST /posts": "Create a post (auth required)",
            "PUT /posts/<id>": "Update a post (auth required)",
            "DELETE /posts/<id>": "Delete a post (auth required)",
        },
        "auth": "Include header: Authorization: Bearer my-secret-token",
    })


@app.route("/posts", methods=["GET"])
def get_posts():
    """List all blog posts, newest first."""
    conn = get_db()
    rows = conn.execute(
        "SELECT * FROM posts ORDER BY created_at DESC"
    ).fetchall()
    conn.close()

    posts = [row_to_dict(row) for row in rows]
    return jsonify({"posts": posts, "count": len(posts)})


@app.route("/posts/<int:post_id>", methods=["GET"])
def get_post(post_id):
    """Get a single post by its ID."""
    conn = get_db()
    row = conn.execute(
        "SELECT * FROM posts WHERE id = ?", (post_id,)
    ).fetchone()
    conn.close()

    if row is None:
        return jsonify({"error": f"Post {post_id} not found"}), 404

    return jsonify({"post": row_to_dict(row)})


@app.route("/posts", methods=["POST"])
@require_auth
def create_post():
    """Create a new blog post. Requires authentication."""
    data = request.get_json()

    if not data:
        return jsonify({"error": "Request body must be JSON"}), 400

    # Validate required fields
    title = data.get("title", "").strip()
    content = data.get("content", "").strip()
    author = data.get("author", "").strip()

    if not title:
        return jsonify({"error": "Title is required"}), 400
    if not content:
        return jsonify({"error": "Content is required"}), 400
    if not author:
        return jsonify({"error": "Author is required"}), 400

    created_at = datetime.now().isoformat()

    conn = get_db()
    cursor = conn.execute(
        "INSERT INTO posts (title, content, author, created_at) VALUES (?, ?, ?, ?)",
        (title, content, author, created_at),
    )
    post_id = cursor.lastrowid
    conn.commit()

    # Fetch the created post to return it
    row = conn.execute("SELECT * FROM posts WHERE id = ?", (post_id,)).fetchone()
    conn.close()

    return jsonify({"message": "Post created!", "post": row_to_dict(row)}), 201


@app.route("/posts/<int:post_id>", methods=["PUT"])
@require_auth
def update_post(post_id):
    """Update an existing post. Requires authentication."""
    conn = get_db()

    # Check if post exists
    existing = conn.execute(
        "SELECT * FROM posts WHERE id = ?", (post_id,)
    ).fetchone()

    if existing is None:
        conn.close()
        return jsonify({"error": f"Post {post_id} not found"}), 404

    data = request.get_json()
    if not data:
        conn.close()
        return jsonify({"error": "Request body must be JSON"}), 400

    # Update only the fields that were provided
    title = data.get("title", existing["title"])
    content = data.get("content", existing["content"])
    author = data.get("author", existing["author"])

    conn.execute(
        "UPDATE posts SET title = ?, content = ?, author = ? WHERE id = ?",
        (title, content, author, post_id),
    )
    conn.commit()

    # Fetch and return the updated post
    row = conn.execute("SELECT * FROM posts WHERE id = ?", (post_id,)).fetchone()
    conn.close()

    return jsonify({"message": "Post updated!", "post": row_to_dict(row)})


@app.route("/posts/<int:post_id>", methods=["DELETE"])
@require_auth
def delete_post(post_id):
    """Delete a post. Requires authentication."""
    conn = get_db()

    # Check if post exists
    existing = conn.execute(
        "SELECT * FROM posts WHERE id = ?", (post_id,)
    ).fetchone()

    if existing is None:
        conn.close()
        return jsonify({"error": f"Post {post_id} not found"}), 404

    conn.execute("DELETE FROM posts WHERE id = ?", (post_id,))
    conn.commit()
    conn.close()

    return jsonify({"message": f"Post {post_id} deleted."}), 200


# ── Error Handlers ─────────────────────────────────────────

@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Endpoint not found"}), 404


@app.errorhandler(405)
def method_not_allowed(e):
    return jsonify({"error": "Method not allowed"}), 405


@app.errorhandler(500)
def server_error(e):
    return jsonify({"error": "Internal server error"}), 500


# ── Main ───────────────────────────────────────────────────

if __name__ == "__main__":
    init_db()

    print()
    print("=" * 50)
    print("  BLOG REST API")
    print("=" * 50)
    print(f"  Auth token: {API_TOKEN}")
    print("  Try: curl http://localhost:5000/posts")
    print("=" * 50)
    print()

    app.run(debug=True, port=5000)
