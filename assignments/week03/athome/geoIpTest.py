#!/usr/bin/env python

import urllib2, json, sys

#ip = raw_input("Enter an IP: ")
ip = sys.argv[1]

def geoInfo(ip):
    url = "http://api.hostip.info/get_json.php?ip=" + ip + "&position=true"
    response = urllib2.urlopen(url)
    answer = json.loads(response.read())
    ip, lat, lng = answer['ip'], answer['lat'], answer['lng']
    return ip, lat, lng

if __name__ == "__main__":
    ip, lat, lng = geoInfo(ip)
    url = "http://maps.googleapis.com/maps/api/staticmap?&zoom=07&size=512x512&maptype=roadmap\&markers=size:mid%7Ccolor:red|label:G|" + str(lat) + "," + str(lng) + "&sensor=false"
    print url
    
