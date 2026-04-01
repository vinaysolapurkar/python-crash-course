"""
=============================================================
  PROJECT 7: CHAT APP - CLIENT
=============================================================
  The chat client that connects to the server.
  Run multiple instances in separate terminals to chat!

  Make sure server.py is running first.

  Run:  python client.py
  Quit: type /quit and press Enter

  No external dependencies needed!
=============================================================
"""

import socket
import threading
import sys

# ── Server Connection Details ──────────────────────────────
# These must match what server.py is using!
HOST = "127.0.0.1"
PORT = 5555
BUFFER_SIZE = 1024


def receive_messages(sock):
    """
    Continuously receive and display messages from the server.
    Runs in a separate thread so it doesn't block input.
    """
    while True:
        try:
            data = sock.recv(BUFFER_SIZE)
            if not data:
                print("\n[Disconnected from server]")
                break

            message = data.decode("utf-8")
            # Print the message (overwrite the input prompt for cleanliness)
            print(f"\r{message}")
            print("> ", end="", flush=True)

        except (ConnectionResetError, ConnectionAbortedError, OSError):
            print("\n[Connection lost]")
            break


def send_messages(sock, name):
    """
    Read user input and send messages to the server.
    Runs in the main thread.
    """
    print("> ", end="", flush=True)

    while True:
        try:
            message = input()

            if not message.strip():
                print("> ", end="", flush=True)
                continue

            # Check for quit command
            if message.strip().lower() == "/quit":
                print("Leaving the chat...")
                sock.send("/quit".encode("utf-8"))
                break

            # Send the message to the server
            sock.send(message.encode("utf-8"))
            print("> ", end="", flush=True)

        except (EOFError, KeyboardInterrupt):
            print("\nLeaving the chat...")
            try:
                sock.send("/quit".encode("utf-8"))
            except OSError:
                pass
            break


def main():
    """Connect to the chat server and start chatting!"""
    print()
    print("=" * 40)
    print("    CHAT CLIENT")
    print("=" * 40)

    # Get the user's name
    name = input("  Enter your name: ").strip()
    if not name:
        name = "Anonymous"

    # Create a socket and connect to the server
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        print(f"  Connecting to {HOST}:{PORT}...")
        sock.connect((HOST, PORT))
    except ConnectionRefusedError:
        print("  Could not connect to the server!")
        print("  Make sure server.py is running first.")
        return
    except OSError as e:
        print(f"  Connection error: {e}")
        return

    # Send our name to the server (first message = name)
    sock.send(name.encode("utf-8"))

    print(f"  Connected as '{name}'!")
    print("  Type messages and press Enter to send.")
    print("  Type /quit to leave.")
    print("=" * 40)
    print()

    # Start the receive thread (runs in background)
    receive_thread = threading.Thread(
        target=receive_messages,
        args=(sock,),
        daemon=True,  # Dies when main thread exits
    )
    receive_thread.start()

    # Send messages in the main thread
    # (This blocks until user types /quit or Ctrl+C)
    send_messages(sock, name)

    # Clean up
    sock.close()
    print("Disconnected. Goodbye!")


if __name__ == "__main__":
    main()
