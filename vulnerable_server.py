#!/bin/python

import socket

HOST = "0.0.0.0"
PORT = 8080

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind((HOST, PORT))
server.listen(5)

print(f"Lab test server is running on port {PORT}")

while True:
    client, address = server.accept()

    print("Connection from:", address)

    message = """Welcome to the Cybersecurity Lab Test Server.

This server is used for testing the network port scanner.
"""

    client.send(message.encode())
    client.close()
#!/bin/python

import socket
# Lab Test Server Configuration

HOST = "0.0.0.0"
PORT = 8080

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind((HOST, PORT))

server.listen(5)


while True:

    # Wait for a client/scanner to connect
    client, address = server.accept()

    print("Connection from:", address)

    # Message sent to connected clients
    message = """Welcome to the Cybersecurity Lab Test Server.

This server is used for testing the network port scanner.
"""

    # Send the message
    client.send(message.encode())

    # Close the client connection
    client.close()
