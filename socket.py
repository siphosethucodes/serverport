import socket

def start_server():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to a specific address and port
    host = ''  # Listen on all available interfaces
    port = 4545
    server_socket.bind((host, port))

    # Enable the server to accept connections, with a maximum of 5 queued connections
    server_socket.listen(5)

    print(f"Server listening on port {port}")

    try:
        while True:
            # Wait for a client to establish a connection
            client_socket, client_address = server_socket.accept()

            print(f"Connection established with {client_address}")

            # In a real server, you would handle client requests here

            # Close the client socket
            client_socket.close()

    except KeyboardInterrupt:
        print("Server stopped by user.")

    finally:
        # Close the server socket
        server_socket.close()

if __name__ == "__main__":
    start_server()
