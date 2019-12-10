from server import start_server

if __name__ == "__main__":
    # Start HTTP Server
    try:
        start_server()
    except:
        print("Stopping Server.")
