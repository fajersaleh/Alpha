#!/bin/python
import socket

HOST = "0.0.0.0"
PORT = 8080

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)

print(f"Lab server running on port {PORT}")

while True:
    client, address = server.accept()

    print("Connection from:", address)

    message = """
Welcome to the Cybersecurity Lab Server

This is a test server for network scanning projects.
"""

    client.send(message.encode())
    client.close()
