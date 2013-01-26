#!/usr/bin/env python

import cgi
form = cgi.FieldStorage()
print('Content-type: text/html')

html = """
<TITLE>CGI Form Response</TITLE>
<h1>Greetings</h1>
<HR>
<P>%s</P>
<HR>"""

if not 'user' in form:
    print(html % 'Who are you?')
else:
    print(html % ('Hello, %s,' % form['user'].value))
