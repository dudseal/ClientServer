import socket

def handle_client(client_socket):
    # Receive the HTTP request from the client
    #Start the server, then type http://IP:800
    
    request = client_socket.recv(1024).decode('utf-8')
    print(f"Request received:\n{request}")

    # Check if it's a GET request
    if request.startswith("GET / HTTP/1.1"):
        response = "HTTP/1.1 200 OK\r\n"
        response += "Content-Type: text/html; charset=UTF-8\r\n"
        response += "\r\n"
        response += "<html><body><h1>Welcome to the Python HTTP Server!</h1></body></html>"
    else:
        response = "HTTP/1.1 404 Not Found\r\n"
        response += "Content-Type: text/html; charset=UTF-8\r\n"
        response += "\r\n"
        response += "<html><body><h1>404 Not Found</h1></body></html>"

    # Send the HTTP response
    client_socket.sendall(response.encode('utf-8'))

    # Close the connection with the client
    client_socket.close()

def start_server(host, port):
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Listening on {host}:{port}...")

    while True:
        # Wait for a connection from a client
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")

        # Handle the client request
        handle_client(client_socket)

if __name__ == "__main__":
    host = '0.0.0.0'  # Listen on all available interfaces
    port = 8080        # You can choose any available port

    start_server(host, port)