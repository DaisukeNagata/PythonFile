import sys
import requests
from http.server import BaseHTTPRequestHandler, HTTPServer

from urllib.parse import urlparse

def start(callback):
    
    def handler(*args):
        call(callback, *args)
    server = HTTPServer(('', int(8000)), handler)
    server.serve_forever()

class call(BaseHTTPRequestHandler):
    
    def __init__(self, callback, *args):
        self.callback = callback
        BaseHTTPRequestHandler.__init__(self, *args)

    def do_POST(self):
      
        parsed_path = urlparse(self.path)
        query = parsed_path.query
        self.send_response(200)
        self.end_headers()
        self.wfile.write(query.encode())
        
        return
        
