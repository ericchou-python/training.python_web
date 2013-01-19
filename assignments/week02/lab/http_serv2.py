#!/usr/bin/env python

import socket, datetime, time, email

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

# GMT time
nowdt = datetime.datetime.now()
nowTuple = nowdt.timetuple()
nowTimeStamp = time.mktime(nowTuple)
returnTime = email.Utils.formatdate(nowTimeStamp)

def ok_response(body):
    return "HTTP/1.1 200 OK\r\nDate: " + returnTime + "\r\n\r\n" + body
    
while True: # keep looking for new connections forever
    client, address = s.accept() # look for a connection
#    data = client.recv(size)
    if html_data: # if the connection was closed there would be no data
        new_html_data = ok_response(html_data)
        print "received: %s, sending it back"%new_html_data
        client.send(new_html_data) 
        client.close()
