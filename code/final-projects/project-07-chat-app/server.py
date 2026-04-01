"""
=============================================================
  PROJECT 7: CHAT APP - SERVER
=============================================================
  The chat server that accepts multiple client connections
  and broadcasts messages to everyone.

  Run this first:  python server.py
  Then run client.py in separate terminal windows.

  No external dependencies needed!
=============================================================
"""

import socket
import threading
from datetime import datetime

# ── Server Configuration ───────────────────────────────────
HOST = "127.0.0.1"  # localhost - only accepts local connections
PORT = 5555          # Port to listen on (pick any unused port > 1024)
BUFFER_SIZE = 1024   # Max message size in bytes

# ── Connected Clients ──────────────────────────────────────
# We keep track of all connected clients and their names.
# A lock ensures thread-safe access to the shared list.
clients = {}  # {socket: name}
clients_lock = threading.Lock()


def broadcast(message, sender_socket=None):
    """
    Send a message to ALL connected clients.
    Optionally exclude the sender so they don't see their own message.
    """
    with clients_lock:
        disconnected = []
        for client_socket in clients:
            # Skip the sender if specified
            if client_socket == sender_socket:
                continue
            try:
                client_socket.send(message.encode("utf-8"))
            except (BrokenPipeError, ConnectionResetError, OSError):
                disconnected.append(client_socket)

        # Clean up any clients that failed
        for sock in disconnected:
            name = clients.pop(sock, "Unknown")
            log(f"{name} disconnected (broken pipe)")


def handle_client(client_socket, address):
    """
    Handle a single client connection.
    Runs in its own thread - one per client.
    """
    name = "Unknown"

    try:
        # Step 1: Receive the client's chosen name
        name = client_socket.recv(BUFFER_SIZE).decode("utf-8").strip()
        if not name:
            name = f"User-{address[1]}"

        # Register the client
        with clients_lock:
            clients[client_socket] = name

        log(f"{name} connected from {address}")
        broadcast(f"[SERVER] {name} has joined the chat!", sender_socket=None)

        # Step 2: Receive and broadcast messages
        while True:
            data = client_socket.recv(BUFFER_SIZE)
            if not data:
                break  # Client disconnected

            message = data.decode("utf-8").strip()
            if not message:
                continue

            # Check for quit command
            if message.lower() == "/quit":
                break

            # Broadcast the message with the sender's name
            formatted = f"[{name}] {message}"
            log(formatted)
            broadcast(formatted, sender_socket=client_socket)

    except (ConnectionResetError, ConnectionAbortedError, OSError):
        pass  # Client disconnected abruptly

    finally:
        # Clean up when client leaves
        with clients_lock:
            if client_socket in clients:
                del clients[client_socket]

        client_socket.close()
        log(f"{name} disconnected")
        broadcast(f"[SERVER] {name} has left the chat.")


def log(message):
    """Print a timestamped server log message."""
    timestamp = datetime.now().strftime("%H:%M:%S")
    print(f"[{timestamp}] {message}")


def main():
    """Start the chat server and accept connections."""
    # Create a TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Allow port reuse (avoids "Address already in use" errors)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Bind to the address and start listening
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)  # Allow up to 5 pending connections

    print("=" * 45)
    print("  CHAT SERVER")
    print("=" * 45)
    log(f"Server started on {HOST}:{PORT}")
    log("Waiting for connections...")
    print("  Press Ctrl+C to stop the server.")
    print("=" * 45)
    print()

    try:
        while True:
            # Accept a new client connection
            # This blocks until someone connects
            client_socket, address = server_socket.accept()

            # Start a new thread to handle this client
            # daemon=True means the thread dies when main thread exits
            thread = threading.Thread(
                target=handle_client,
                args=(client_socket, address),
                daemon=True,
            )
            thread.start()

            with clients_lock:
                active = len(clients) + 1  # +1 for the new one being set up
            log(f"Active connections: ~{active}")

    except KeyboardInterrupt:
        log("Server shutting down...")
        broadcast("[SERVER] Server is shutting down. Goodbye!")
    finally:
        server_socket.close()
        log("Server stopped.")


if __name__ == "__main__":
    main()
