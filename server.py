import socket

# Create a socket object
server_socket = socket.socket()
# Define the host and port
HOST = socket.getfqdn()  # Localhost
PORT = 8000  # Port to bind to

server_socket.bind(('0.0.0.0', PORT)) # Bind the socket to the host and port

# Start listening for incoming connections (max 5 connection in the backlog)
server_socket.listen(5)

print(f"Server running on http://{HOST}:{PORT}...")

# Wait for a connection
while True:
    # Accept an incoming connection
    client_socket, client_address = server_socket.accept()

    print(f"Connection from {client_address} has been established.")

    # Receive the request data (max 1024 bytes)
    request_data = client_socket.recv(1024).decode('utf-8')

    #Print the request (just for debugging)
    #print("Request received:")
    #print(request_data)
    try:
        with open("project.html","r") as html_file:
            html_content = html_file.read()
    except FileNotFoundError:
        html_content = "<html><body><h1>Error 404</h1><p>File not found.</p></body></html>"
    
    # Simple HTTP response (an HTTP 200 OK response)
    response = f"""HTTP/1.1 200 OK
Content-Type: text/html

{html_content}
"""

    # Send the HTTP response to the client
    client_socket.sendall(response.encode('utf-8'))

    # Close the client connection
    client_socket.close()
