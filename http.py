import socket
import sys

def http_request(host, port):
    http_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    http_client.connect((host,port))
    http_client.send(b"GET / HTTP/1.1\r\nHost: " + host.encode() + b"\r\n\r\n")\
    
    response = http_client.recv(4096)

    print(response.decode("utf-8"))

    http_client.close()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 http.py <host> <port>")
    else:
        host = sys.argv[1]
        port = int(sys.argv[2])
        http_request(host,port)
