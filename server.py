import socket

# Define the host and port
HOST = socket.getfqdn()  # Localhost
PORT = 8000  # Port to bind to

# Create a socket object
server_socket = socket.socket()

# Bind the socket to the host and port
server_socket.bind((HOST, PORT))

# Start listening for incoming connections (max 1 connection in the backlog)
server_socket.listen(1)

print(f"Server running on http://{HOST}:{PORT}...")

# Wait for a connection
while True:
    # Accept an incoming connection
    client_socket, client_address = server_socket.accept()

    print(f"Connection from {client_address} has been established.")

    # Receive the request data (max 1024 bytes)
    request_data = client_socket.recv(1024).decode('utf-8')

    # Print the request (just for debugging)
    print("Request received:")
    print(request_data)

    # Simple HTTP response (an HTTP 200 OK response)
    response = """HTTP/1.1 200 OK
Content-Type: text/plain

Hello, World! You have connected to the Python socket server.
"""

    # Send the HTTP response to the client
    client_socket.sendall(response.encode('utf-8'))

    # Close the client connection
    client_socket.close()
