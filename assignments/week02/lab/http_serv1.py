#!/usr/bin/env python

import socket 

host = '' # listen on all connections (WiFi, etc) 
port = 50000 
backlog = 5 # how many connections can we stack up
size = 1024 # number of bytes to receive at once

## create the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
# set an option to tell the OS to re-use the socket
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# the bind makes it a server
s.bind( (host,port) ) 
s.listen(backlog) 

html = open('tiny_html.html', 'r')
html_data = html.read()

while True: # keep looking for new connections forever
    client, address = s.accept() # look for a connection
#    data = client.recv(size)
    if html_data: # if the connection was closed there would be no data
        print "received: %s, sending it back"%html_data
        client.send(html_data) 
        client.close()
