#!/usr/bin/env python3

import socket

HOST = ""

PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_Stream) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()

# 3 - Data is exchanged

    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)

