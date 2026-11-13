import functools, http.server
d = r"C:\Users\pietr\Downloads\Vanderlucia Cliente Cartao\site"
h = functools.partial(http.server.SimpleHTTPRequestHandler, directory=d)
http.server.ThreadingHTTPServer(("", 5511), h).serve_forever()
