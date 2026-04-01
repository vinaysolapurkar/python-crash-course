# Project 7: Chat Application (CLI)

> **Difficulty:** 4/5 | **Time:** ~3 hours | **Skills:** sockets, threading, networking
> **Code:** https://github.com/vinaysolapurkar/python-crash-course/tree/main/code/final-projects/project-07-chat-app/

## What You'll Build

A real-time multi-user chat application with a server and client, built using Python's `socket` and `threading` modules. The server handles multiple connected clients simultaneously, broadcasting messages to all participants. Each client gets a username and can send messages that appear instantly on every other client's screen.

Here's what it looks like:

```
=== CHAT CLIENT ===
Connected to server at localhost:5555
Enter your username: alice

[Server] alice has joined the chat!
[bob] Hey alice, welcome!
[alice] Thanks! What are we talking about?
[charlie] Python sockets. This is pretty cool.
[alice] Agreed!
```

## Skills You'll Use

- Socket programming (learned in Chapter 14)
- Threading for concurrency (learned in Chapter 14)
- Error handling (learned in Chapter 8)
- String encoding/decoding (learned in Chapter 2)
- Object-oriented design (learned in Chapter 9)

## Step-by-Step Build Guide

### Step 1: Build the Chat Server

The server listens for incoming connections, assigns each client to a separate thread, and broadcasts messages to all connected clients. This is the backbone of the application.

```python
# chat_server.py

import socket
import threading
from datetime import datetime

HOST = "127.0.0.1"  # localhost
PORT = 5555
BUFFER_SIZE = 1024
ENCODING = "utf-8"


class ChatServer:
    """Multi-client chat server using TCP sockets."""

    def __init__(self, host=HOST, port=PORT):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET,
                                       socket.SO_REUSEADDR, 1)
        self.clients = {}  # {client_socket: username}
        self.lock = threading.Lock()  # Thread-safe client management

    def start(self):
        """Start the server and listen for connections."""
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print(f"[SERVER] Running on {self.host}:{self.port}")
        print("[SERVER] Waiting for connections...")

        try:
            while True:
                client_socket, address = self.server_socket.accept()
                print(f"[SERVER] Connection from {address}")

                # Start a new thread for each client
                thread = threading.Thread(
                    target=self.handle_client,
                    args=(client_socket, address),
                    daemon=True
                )
                thread.start()

                with self.lock:
                    active = len(self.clients)
                print(f"[SERVER] Active connections: {active + 1}")

        except KeyboardInterrupt:
            print("\n[SERVER] Shutting down...")
        finally:
            self.shutdown()

    def handle_client(self, client_socket, address):
        """Handle communication with a single client."""
        username = None

        try:
            # First message from client is their username
            client_socket.send("USERNAME".encode(ENCODING))
            username = client_socket.recv(BUFFER_SIZE).decode(ENCODING).strip()

            if not username:
                username = f"User-{address[1]}"

            with self.lock:
                self.clients[client_socket] = username

            # Announce the new user
            join_msg = f"[Server] {username} has joined the chat!"
            print(f"[SERVER] {username} connected from {address}")
            self.broadcast(join_msg, exclude=client_socket)
            client_socket.send(f"[Server] Welcome, {username}!".encode(ENCODING))

            # Listen for messages
            while True:
                message = client_socket.recv(BUFFER_SIZE).decode(ENCODING)
                if not message:
                    break

                # Handle special commands
                if message.startswith("/"):
                    self.handle_command(message, client_socket, username)
                else:
                    timestamp = datetime.now().strftime("%H:%M")
                    formatted = f"[{username} {timestamp}] {message}"
                    print(formatted)
                    self.broadcast(formatted, exclude=client_socket)

        except (ConnectionResetError, ConnectionAbortedError, OSError):
            pass
        finally:
            self.disconnect_client(client_socket, username)

    def handle_command(self, message, client_socket, username):
        """Handle chat commands like /users, /quit, /help."""
        command = message.strip().lower()

        if command == "/users":
            with self.lock:
                user_list = ", ".join(self.clients.values())
            client_socket.send(
                f"[Server] Online users: {user_list}".encode(ENCODING)
            )
        elif command == "/help":
            help_text = (
                "[Server] Commands: /users (list online), "
                "/quit (disconnect), /help (this message)"
            )
            client_socket.send(help_text.encode(ENCODING))
        elif command == "/quit":
            client_socket.send("[Server] Goodbye!".encode(ENCODING))
            raise ConnectionResetError("User quit")

    def broadcast(self, message, exclude=None):
        """Send a message to all connected clients."""
        with self.lock:
            disconnected = []
            for client_socket in self.clients:
                if client_socket != exclude:
                    try:
                        client_socket.send(message.encode(ENCODING))
                    except (BrokenPipeError, OSError):
                        disconnected.append(client_socket)

            # Clean up any broken connections
            for sock in disconnected:
                self.disconnect_client(sock, self.clients.get(sock))

    def disconnect_client(self, client_socket, username):
        """Remove a client and notify others."""
        with self.lock:
            if client_socket in self.clients:
                del self.clients[client_socket]

        try:
            client_socket.close()
        except OSError:
            pass

        if username:
            leave_msg = f"[Server] {username} has left the chat."
            print(f"[SERVER] {username} disconnected")
            self.broadcast(leave_msg)

    def shutdown(self):
        """Shut down the server gracefully."""
        print("[SERVER] Closing all connections...")
        with self.lock:
            for client_socket in list(self.clients.keys()):
                try:
                    client_socket.send(
                        "[Server] Server is shutting down.".encode(ENCODING)
                    )
                    client_socket.close()
                except OSError:
                    pass
            self.clients.clear()
        self.server_socket.close()
        print("[SERVER] Server stopped.")


if __name__ == "__main__":
    server = ChatServer()
    server.start()
```

### Step 2: Build the Chat Client

The client connects to the server, sends a username, then runs two threads: one for receiving messages (so they appear in real time) and one for reading user input.

```python
# chat_client.py

import socket
import threading
import sys

HOST = "127.0.0.1"
PORT = 5555
BUFFER_SIZE = 1024
ENCODING = "utf-8"


class ChatClient:
    """Chat client that connects to the ChatServer."""

    def __init__(self, host=HOST, port=PORT):
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.running = True
        self.username = None

    def connect(self):
        """Connect to the server and start chatting."""
        try:
            self.client_socket.connect((self.host, self.port))
            print(f"Connected to server at {self.host}:{self.port}")
        except ConnectionRefusedError:
            print(f"Could not connect to {self.host}:{self.port}")
            print("Make sure the server is running first.")
            return

        # Wait for username request
        response = self.client_socket.recv(BUFFER_SIZE).decode(ENCODING)
        if response == "USERNAME":
            self.username = input("Enter your username: ").strip()
            if not self.username:
                self.username = "Anonymous"
            self.client_socket.send(self.username.encode(ENCODING))

        # Start the receive thread
        receive_thread = threading.Thread(
            target=self.receive_messages,
            daemon=True
        )
        receive_thread.start()

        # Main thread handles sending
        self.send_messages()

    def receive_messages(self):
        """Continuously receive and display messages from the server."""
        while self.running:
            try:
                message = self.client_socket.recv(BUFFER_SIZE).decode(ENCODING)
                if not message:
                    print("\nDisconnected from server.")
                    self.running = False
                    break
                print(f"\r{message}")
                # Re-show the input prompt
                print(f"[{self.username}] ", end="", flush=True)
            except (ConnectionResetError, OSError):
                if self.running:
                    print("\nLost connection to server.")
                    self.running = False
                break

    def send_messages(self):
        """Read user input and send messages to the server."""
        print("\nType your messages (or /help for commands, /quit to exit):\n")

        while self.running:
            try:
                message = input(f"[{self.username}] ")
                if not message:
                    continue

                if message.strip().lower() == "/quit":
                    self.client_socket.send(message.encode(ENCODING))
                    print("Disconnecting...")
                    self.running = False
                    break

                self.client_socket.send(message.encode(ENCODING))

            except (EOFError, KeyboardInterrupt):
                print("\nDisconnecting...")
                self.running = False
                break

        self.disconnect()

    def disconnect(self):
        """Close the connection."""
        self.running = False
        try:
            self.client_socket.close()
        except OSError:
            pass
        print("Disconnected.")


def main():
    print("=" * 30)
    print("     CHAT CLIENT")
    print("=" * 30)

    # Allow custom host/port from command line
    host = sys.argv[1] if len(sys.argv) > 1 else HOST
    port = int(sys.argv[2]) if len(sys.argv) > 2 else PORT

    client = ChatClient(host, port)
    client.connect()


if __name__ == "__main__":
    main()
```

### Step 3: Test the Application

Open three terminal windows. In the first, start the server:

```bash
python chat_server.py
```

In the second and third terminals, start clients:

```bash
python chat_client.py
```

Give each client a different username. Type messages in one client and watch them appear in the other. Try the `/users` and `/help` commands.

### Step 4: Understanding the Architecture

Take a moment to understand what's happening under the hood:

1. The **server** creates a TCP socket and listens on port 5555
2. When a client connects, the server spawns a **new thread** to handle that client
3. Each client thread listens for incoming messages in an infinite loop
4. When a message arrives, the server **broadcasts** it to all other clients
5. The **lock** (`threading.Lock`) prevents race conditions when multiple threads modify the client list simultaneously
6. The **client** uses two threads: one for receiving (background) and one for sending (foreground/input)

This is the same fundamental pattern used by real chat systems, just simplified.

## Challenges (Level Up!)

1. **Private messages:** Implement a `/dm username message` command that sends a message only to a specific user. The server needs to look up the recipient's socket by username.

2. **Chat rooms:** Add support for multiple rooms with `/join roomname` and `/leave` commands. Only broadcast messages to users in the same room. Track room membership in a dictionary.

3. **Message history:** Store the last 50 messages on the server. When a new client connects, send them the recent history so they can catch up on the conversation.

## Portfolio Tips

A networking project is a standout on any junior developer's portfolio. When presenting this:

- **GitHub:** Include clear instructions for running the server and client. Add a diagram showing the client-server architecture. Mention the threading model.
- **Resume:** "Built a multi-user CLI chat application using TCP sockets and threading with broadcast messaging, user commands, and graceful disconnection handling."
- **Interview talking point:** Explain the threading model and why you used a lock for the client dictionary. Discuss the difference between TCP and UDP and why TCP is appropriate for chat (reliable, ordered delivery). Mention how you'd scale this - an event loop with `asyncio` or a message broker like Redis Pub/Sub.
