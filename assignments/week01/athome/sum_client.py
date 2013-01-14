#!/usr/bin/env python
#
# use system argument 1 and 2 to specificy the two numbers
#

import socket
import sys

# Create a TCP/IP socket
client_connect = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# Connect the socket to the port where the server is listening
server_address = ('localhost', 50000)
#server_address = ('208.85.148.52', 50000) #VM public IP
client_connect.connect(server_address)

try:
    # Send data
    num1 = sys.argv[1]
    num2 = sys.argv[2]
    msg = num1.strip() + " " + num2.strip()
    client_connect.sendall(msg)
    
    # print the response
    response = client_connect.recv(4096)
    print response

finally:
    # close the socket to clean up
    client_connect.close()
