from server import start_server
from threading import Thread

if __name__ == "__main__":
    # Start HTTP Server on a New Thread
    Thread(target = start_server, daemon = True).start()
