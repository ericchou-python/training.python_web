#!/usr/bin/env python

import socket, os

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

# Return the URI requested by the client
def parse_request(request): 
    uri = request.split("\r")[1].split()[1]
    path = request.split("\r")[0].split()[1]
    return uri, path

# parse out the request
def resolve_uri(uri, path):
    if path == "/web/directory":
        result = str(os.listdir("web/"))
        return "The directory contents are: " + result
    elif path == "/web/file":
        raise NotImplementedError("Coming Soon")
    else:
        return ValueError("URI does not Exist")

while True: # keep looking for new connections forever
    client, address = s.accept() # look for a connection
    data = client.recv(size)
    if data: # if the connection was closed there would be no data
#        print "received: %s, sending it back" % data #useful to see full request header
        request = data.split("\r")[0].split()
        if request[0] == 'GET' and request[2] == 'HTTP/1.1': 
            uri, path = parse_request(data)
            message = resolve_uri(uri, path)
        else: 
            raise ValueError("ValueError")

        client.send(message) 
        client.close()
