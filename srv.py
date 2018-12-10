import http.server
import socketserver
import os

# define port here
PORT = 8000

# define webroot here
web_dir = os.path.join(os.path.dirname(__file__), 'web')
os.chdir(web_dir)

Handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("", PORT), Handler)
print("serving at port", PORT)
try: 
    httpd.serve_forever()
except KeyboardInterrupt: 
    pass 
httpd.server_close()