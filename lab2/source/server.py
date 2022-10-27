#!/usr/bin/env python3
import http.server
import socketserver
import os
import time


#print('source code for "http.server":', http.server.__file__)

class web_server(http.server.SimpleHTTPRequestHandler):
    
    def do_GET(self):

        print(self.path)
        
        if self.path == '/':
            self.protocol_version = 'HTTP/1.1'
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=UTF-8")
            self.end_headers()   
            now = time.localtime()         
            time1 = time.strftime("%HH:%MM:%SS",now)
            self.wfile.write(b"Hello World!\n" + time1.encode('utf-8') + b"\n") 

        else:
            super().do_GET() 
    
# --- main ---

PORT = 4080

print(f'Starting: http://localhost:{PORT}')

tcp_server = socketserver.TCPServer(("",PORT), web_server)
tcp_server.serve_forever()
