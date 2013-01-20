#!/usr/bin/env python

# Failed IP: http://localhost:50000/ip/208.85.148.52
# Wroking IP: http://localhost:50000/ip/216.9.0.16

import socket, os, time, urllib2, json, subprocess

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
    pathList = path.split("/")
    print pathList
    if pathList[1] == "ip":
        ip = pathList[2] #/ip/<ip> to get the actual requested IP
        # Url that reuturns IP information in JSon format
        url = "http://api.hostip.info/get_json.php?ip=" + ip + "&position=true"
        response = urllib2.urlopen(url)
        answer = json.loads(response.read())
        if answer['lat'] == None: #Failed to return lat inforamtion from API
            return "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n<html><body>This IP does not have enough data</body></html"
        else:
            ip, city, country = answer['ip'], answer['city'], answer['country_name']
            print answer['lat'], ip, city, country
            mapUrl = subprocess.check_output(['python', 'geoIpTest.py', ip]) #a separate script that returns Google Map URL for full size image with marker
            embedUrl = "http://maps.googleapis.com/maps/api/staticmap?center=" + answer['lat'] + "," + answer["lng"] + "&zoom=11&size=200x200&sensor=false"
            return "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n<html><body><center><b>IP: </b>" + ip + "<br><b>Country: </b>" + country + "<br><b>City: </b>" + city + "<br><br><a href=\"" + mapUrl + "\">Full Google Map</a><br><br><img src=\"" + embedUrl + "\"></center></body></html>" 
    elif pathList[1] == "favicon.ico": #This to avoide error when the path does not match
        return "HTTP/1.1 200 OK\r\nContent-Type: image/png\r\n\r\n"

while True: # keep looking for new connections forever
    client, address = s.accept() # look for a connection
    data = client.recv(size)
    if data: # if the connection was closed there would be no data
#        print "received: %s, sending it back" % data #useful to see full request header
        request = data.split("\r")[0].split()
        print request
        if request[0] == 'GET' and request[2] == 'HTTP/1.1': 
            uri, path = parse_request(data)
            message = resolve_uri(uri, path)
        else: 
            raise ValueError("ValueError")

        client.send(message) 
        client.close()

