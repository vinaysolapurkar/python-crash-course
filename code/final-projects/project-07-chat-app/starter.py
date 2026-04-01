"""
=============================================================
  PROJECT 7: CLI CHAT APPLICATION
=============================================================

Build a real-time chat app using Python sockets! You'll
create both a server and a client. Multiple clients can
connect and chat with each other.

WHAT YOU'LL PRACTICE:
  - Socket programming (TCP)
  - Threading (concurrent connections)
  - Client-server architecture
  - Network communication
  - Error handling for connections

DEPENDENCIES:
  None! Uses only Python standard library.

FILE STRUCTURE:
  You need to create THREE files:
  - server.py   (the chat server)
  - client.py   (the chat client)
  - solution.py (explains how to run everything)

REQUIREMENTS:
  Server (server.py):
  1. Listen for incoming connections on a port
  2. Accept multiple clients using threading
  3. Broadcast messages to all connected clients
  4. Handle client disconnections gracefully
  5. Show connection/disconnection events

  Client (client.py):
  1. Connect to the server
  2. Send messages in one thread
  3. Receive messages in another thread
  4. Handle server disconnection
  5. Support a /quit command

HOW TO RUN:
  Terminal 1:  python server.py
  Terminal 2:  python client.py
  Terminal 3:  python client.py  (another user)

EXAMPLE OUTPUT (Server):
  [SERVER] Starting on 127.0.0.1:5555
  [SERVER] Waiting for connections...
  [SERVER] Alice connected from ('127.0.0.1', 54321)
  [SERVER] Bob connected from ('127.0.0.1', 54322)
  [Alice] Hey everyone!
  [Bob] Hi Alice!
  [SERVER] Bob disconnected.

EXAMPLE OUTPUT (Client):
  Enter your name: Alice
  Connected to chat server!
  Type messages and press Enter. /quit to leave.

  [Bob] Hi Alice!
  > Hey everyone!
  [Bob] How's it going?
  > Pretty good!

HINTS:
  - socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  - server: socket.bind(), socket.listen(), socket.accept()
  - client: socket.connect()
  - Use threading.Thread for concurrent operations
  - Encode messages: msg.encode('utf-8')
  - Decode messages: data.decode('utf-8')

Good luck!
=============================================================
"""

# This is the starter template. You need to create:
#
# 1. server.py - The chat server
# 2. client.py - The chat client
#
# See the instructions above and the hints below for each file.


# ─── SERVER SKELETON (put this in server.py) ───────────────
"""
import socket
import threading

HOST = '127.0.0.1'
PORT = 5555

# TODO: Create a socket
# TODO: Bind to HOST:PORT
# TODO: Listen for connections
# TODO: Keep a list of connected clients

def broadcast(message, sender_socket=None):
    # TODO: Send message to all clients except sender
    pass

def handle_client(client_socket, address):
    # TODO: Receive client's name
    # TODO: Loop: receive messages and broadcast them
    # TODO: Handle disconnection
    pass

def main():
    # TODO: Accept connections in a loop
    # TODO: Start a new thread for each client
    pass
"""


# ─── CLIENT SKELETON (put this in client.py) ───────────────
"""
import socket
import threading

HOST = '127.0.0.1'
PORT = 5555

def receive_messages(sock):
    # TODO: Loop forever receiving messages
    # TODO: Print received messages
    # TODO: Handle disconnection
    pass

def send_messages(sock, name):
    # TODO: Loop forever getting input
    # TODO: Send messages to server
    # TODO: Handle /quit command
    pass

def main():
    # TODO: Get user's name
    # TODO: Connect to server
    # TODO: Send name to server
    # TODO: Start receive thread
    # TODO: Start send loop (in main thread)
    pass
"""
