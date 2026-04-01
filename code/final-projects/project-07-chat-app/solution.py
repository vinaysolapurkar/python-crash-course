"""
=============================================================
  PROJECT 7: CLI CHAT APPLICATION - SOLUTION
=============================================================

  This project has THREE files:
    - server.py  (the chat server - run first)
    - client.py  (the chat client - run in separate terminals)
    - solution.py (this file - instructions)

  HOW TO RUN:
  ───────────
  1. Open Terminal 1 and run:
       python server.py

     You should see:
       [SERVER] Server started on 127.0.0.1:5555
       [SERVER] Waiting for connections...

  2. Open Terminal 2 and run:
       python client.py

     Enter a name like "Alice" when prompted.

  3. Open Terminal 3 and run:
       python client.py

     Enter a name like "Bob" when prompted.

  4. Type messages in either client terminal!
     Messages from one client will appear in all other
     client terminals.

  5. Type /quit in a client to disconnect.
     Press Ctrl+C in the server to shut it down.

  ARCHITECTURE:
  ─────────────
  The server uses TCP sockets and threading:

    Client A ──┐
               ├── Server (broadcasts to all) ──┤
    Client B ──┘                                ├── Client A sees B's msgs
                                                └── Client B sees A's msgs

  Each client connection gets its own thread on the server.
  Each client has two threads:
    - Main thread: reads user input and sends to server
    - Background thread: receives messages from server

  WHAT YOU LEARNED:
  ─────────────────
  - socket.socket() for TCP connections
  - server.bind() and server.listen() for servers
  - client.connect() for clients
  - threading.Thread for concurrent operations
  - Thread safety with locks
  - Encode/decode for network byte strings
  - Graceful error handling for network failures

  No external dependencies needed - just Python!
=============================================================
"""

print(__doc__)

print("To run the chat app:")
print("  1. Open a terminal and run:  python server.py")
print("  2. Open another terminal:    python client.py")
print("  3. Open one more terminal:   python client.py")
print("  4. Start chatting between the clients!")
print()
print("All files are in this directory:")
print("  - server.py (run first)")
print("  - client.py (run in 2+ terminals)")
