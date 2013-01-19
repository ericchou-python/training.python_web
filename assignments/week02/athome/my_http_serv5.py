#!/usr/bin/env python

import socket, os, time, subprocess

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

def format_directory(location):
    fileList = os.listdir(location)
    resultFile = open('result.html', 'w')
    resultFile.write("<html><body>")
    resultFile.write("<h2>Directory Links</h2>")
    for i in fileList:
        if i == "images":
            imageList = os.listdir("web/images/")
            for image in imageList:
                resultFile.write("\r\n<a href=\"images/" + image + "\">" + image + "</a><br>")
        elif i == "make_time_result.html":
            next
        else:
            resultFile.write("\r\n<a href=\"" + i + "\">" + i + "</a><br>")
    resultFile.write("\r\n</body></html>\r\n")
    resultFile.close()
    f = open("result.html", "r")
    result = f.read()
    print result
    return "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n" + result
    f.close()

# parse out the request
def resolve_uri(uri, path):
    if path == "/web/directory":
        result = format_directory("web/")
        return result
    elif path == "/web/a_web_page.html":
        f = open("web/a_web_page.html", "r")
        result = f.read()
        return "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n" + result
        f.close()
    elif path == "/web/sample.txt":
        f = open("web/sample.txt", "r")
        result = f.read()
        return "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n" + result
        f.close()
    elif path == "/web/make_time.py":
        f = open("web/make_time_result.html", "w")
        subprocess.Popen(["python", "web/make_time.py"], stdout=f)
        f.close()
        time.sleep(2) #give some time to create the file
        f1 = open("web/make_time_result.html", "r")
        result = f1.read()
        print result
        return "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n" + result
        f1.close()
    elif path == "/web/images/JPEG_example.jpg":
        f = open("web/images/JPEG_example.jpg", "rb")
        result = f.read()
        return "HTTP/1.1 200 OK\r\nContent-Type: image/jpeg\r\n\r\n" + result
        f.close()
    elif path == "/web/images/Sample_Scene_Balls.jpg":
        f = open("web/images/Sample_Scene_Balls.jpg", "rb")
        result = f.read()
        return "HTTP/1.1 200 OK\r\nContent-Type: image/jpeg\r\n\r\n" + result
        f.close()
    elif path == "/web/images/sample_1.png":
        f = open("web/images/sample_1.png", "rb")
        result = f.read()
        return "HTTP/1.1 200 OK\r\nContent-Type: image/png\r\n\r\n" + result
        f.close()
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
