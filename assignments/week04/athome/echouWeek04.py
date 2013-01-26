#!/usr/bin/env python

from cgi import parse_qs, escape
import re, bookdb

database = bookdb.database #This is a local file

def index(environ, start_response):
    """This function will be mounted on "/" and display a link 
    to the hello world page"""
    body = ""
    for i in database:
        url = "books?isbn=" + database[i]['isbn']
        title = database[i]['title']
        body += '<a href="%s"> %s </a><br>' % (url,title)
    start_response('200 OK', [('Content-Type', 'text/html')])
    return ["<h2>Python Books</h2>" + body]
          

def books(environ, start_response):
    parameters = parse_qs(environ.get('QUERY_STRING', ''))
    isbn = parameters['isbn'][0]
    print isbn
    for i in database:
        if isbn == database[i]['isbn']:
            title = database[i]['title']
            publisher = database[i]['publisher']
            author = database[i]['author']
    start_response('200 OK', [('Content-Type', 'text/html')])
    return ['''<b>Title   </b> %s <br>
            <b>Author </b> %s <br>
            <b>Publisher </b> %s <br>
            <b>ISBN </b> %s''' % (title, author, publisher, isbn)]

def hello(environ, start_response):
    """Like the example above, but it uses teh name spacified in
    URL."""
    # get teh name from teh URL if it was specified there
    args = environ['myapp.url_args']
    if args:
        subject = escape(args[0])
    else:
        subject = 'World'
    start_response('200 OK', [('Content-Type', 'text/html')])
    return ['''Hello %(subject)s
            Hello %(subject)s!
            ''' % {'subject': subject}]

def not_found(environ, start_response):
    """Called if no URL matches."""
    start_response('404 NOT FOUND', [('Content-Type', 'text/plain')])
    return ['NOT FOUND']

# map urls to functions
urls = [
    (r'^$', index),
    (r'hello/?$', hello),
    (r'hello/(.+)$', hello),
    (r'books/?$', books)
    ]

def application(environ, start_response):
    """
    The main WSGI application. Dispatch the current request to 
    the function from above and store teh regular expression
    captures in the WSGI environment as `myapp.url_args` so that 
    the functions from above can access the url placeholders.

    If nothing matches call the 'not_found' function.
    """
#    print environ
    path = environ.get('PATH_INFO', '').lstrip('/')
    for regex, callback in urls:
        match = re.search(regex, path)
        if match is not None:
            """
            print "*" * 10
            print environ
            print "*" * 10
            """
            environ['myapp.url_args'] = match.groups()
            return callback(environ, start_response)
    return not_found(environ, start_response)


if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    srv = make_server('localhost', 8080, application)
    srv.serve_forever()

