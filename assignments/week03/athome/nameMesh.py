#!/usr/bin/env python

# 1. Use Facebook API to get name of friends
# 2. Use names.whitepages.com to get name ranking in 2011
# 3. Genarate GraphViz file to visualize data

import json, urllib2
from bs4 import BeautifulSoup

def get_rank(url):
    """Get the rank of the name from names.whitepages.com"""
    page = urllib2.urlopen(url)
    html = page.read()
    parsed = BeautifulSoup(html)
    entry = parsed.find('table', class_='rank inline_block')
    rank = entry.attrs['title'].split()[3][:-2]
    return rank

f = open('echouFacebookFriends.txt', 'r')
friendList = json.loads(f.read())
f.close()

names = []

for i in friendList['data']:
    firstName =  i['name'].split()[0]
    names.append(firstName)

namesDict = {}
for name in names:
    url = 'http://names.whitepages.com/first/'+name
    rank = get_rank(url)
    print name, rank
    namesDict[name] = 5+(float(rank)/1000)
    print namesDict[name]

print namesDict

#write out .gv file
f = open('2011NameRank.gv', 'w')
f.write('graph g {\n')
f.write('node [fontsize=14];\n')
f.write('2011 [shape=diamond];\n')
for name in namesDict.keys():
    f.write('2011 -- %s [len= %s ];\n' % (name, namesDict[name]))
f.write('}\n')

f.close()
