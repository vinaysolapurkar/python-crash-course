"""
=============================================================
  PROJECT 8: BLOG REST API
=============================================================

Build a REST API for a blog using Flask! You'll create
endpoints to create, read, update, and delete blog posts,
with a SQLite database and simple token authentication.

WHAT YOU'LL PRACTICE:
  - Flask web framework
  - REST API design (GET, POST, PUT, DELETE)
  - SQLite database
  - JSON request/response handling
  - Simple authentication
  - Error handling and status codes

DEPENDENCIES:
  pip install flask

REQUIREMENTS:
  1. Endpoints:
     GET    /posts         - List all posts
     GET    /posts/<id>    - Get a single post
     POST   /posts         - Create a post (auth required)
     PUT    /posts/<id>    - Update a post (auth required)
     DELETE /posts/<id>    - Delete a post (auth required)

  2. Post model:
     - id (auto-increment)
     - title (string)
     - content (text)
     - author (string)
     - created_at (datetime)

  3. Simple token auth:
     - Check for "Authorization: Bearer <token>" header
     - Use a hardcoded token for simplicity

  4. Proper HTTP status codes:
     - 200 OK, 201 Created, 204 No Content
     - 400 Bad Request, 401 Unauthorized, 404 Not Found

TESTING WITH CURL:
  # List posts
  curl http://localhost:5000/posts

  # Get one post
  curl http://localhost:5000/posts/1

  # Create a post
  curl -X POST http://localhost:5000/posts \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer my-secret-token" \
    -d '{"title":"Hello","content":"World","author":"Me"}'

  # Update a post
  curl -X PUT http://localhost:5000/posts/1 \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer my-secret-token" \
    -d '{"title":"Updated Title"}'

  # Delete a post
  curl -X DELETE http://localhost:5000/posts/1 \
    -H "Authorization: Bearer my-secret-token"

HINTS:
  - Use flask.request.json to get POST/PUT body data
  - Use flask.jsonify() to return JSON responses
  - sqlite3 is in the standard library
  - Use a decorator for the auth check

Good luck!
=============================================================
"""

# pip install flask
try:
    from flask import Flask, request, jsonify
except ImportError:
    print("Flask not installed. Run: pip install flask")
    exit(1)

import sqlite3
from datetime import datetime


app = Flask(__name__)

# Simple auth token (in production, use proper auth!)
API_TOKEN = "my-secret-token"
DATABASE = "blog.db"


def get_db():
    """Get a database connection."""
    # TODO: Connect to SQLite database
    # TODO: Return connection
    pass


def init_db():
    """Create the posts table if it doesn't exist."""
    # TODO: Create table with columns:
    # id, title, content, author, created_at
    pass


def require_auth(f):
    """Decorator to require authentication."""
    # TODO: Check Authorization header
    # TODO: Return 401 if invalid
    # TODO: Call the wrapped function if valid
    pass


# ── API Endpoints ──────────────────────────────────────────

@app.route("/posts", methods=["GET"])
def get_posts():
    """List all blog posts."""
    # TODO: Query all posts from database
    # TODO: Return as JSON
    pass


@app.route("/posts/<int:post_id>", methods=["GET"])
def get_post(post_id):
    """Get a single post by ID."""
    # TODO: Query post by ID
    # TODO: Return 404 if not found
    pass


@app.route("/posts", methods=["POST"])
def create_post():
    """Create a new blog post (auth required)."""
    # TODO: Check auth
    # TODO: Validate request data
    # TODO: Insert into database
    # TODO: Return 201 Created
    pass


@app.route("/posts/<int:post_id>", methods=["PUT"])
def update_post(post_id):
    """Update an existing post (auth required)."""
    # TODO: Check auth
    # TODO: Find post
    # TODO: Update fields
    # TODO: Return updated post
    pass


@app.route("/posts/<int:post_id>", methods=["DELETE"])
def delete_post(post_id):
    """Delete a post (auth required)."""
    # TODO: Check auth
    # TODO: Delete from database
    # TODO: Return 204 No Content
    pass


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
