#!/usr/bin/env python

import socket
import sys

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 50000)
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(1)

while True:
    # Wait for a connection
    connection, client_address = server_socket.accept()

    try:
        print 'Connection from: ', client_address[0], ' port ', client_address[1]
        while True:
            # Receive the data and send it back
            data = connection.recv(80)
            if data:
                result = data.split()
                num1, num2 = result[0], result[1]
                print "first number is %s, second number is %s" % (num1, num2)
                sendBack = int(num1) + int(num2)
                print "sending result of %s back" % str(sendBack)
                connection.sendall(str(sendBack))
            else:
                break

    finally:
        # Clean up the connection
        connection.close()

server_socket.close()

