#!/usr/bin/env python3
import http.server
from importlib.resources import path
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
            self.wfile.write(b"Hello World!\n")  
        elif self.path.startswith("/cmd="):
            self.protocol_version = 'HTTP/1.1'
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=UTF-8")
            self.end_headers()

            path1 = self.path[5:]
            if path1=="time":
                now = time.localtime()         
                time1 = time.strftime("%HH:%MM:%SS",now)
                self.wfile.write(time1.encode(encoding='UTF-8'))
            elif path1.startswith("rev"):
                splited = path1.split("str=")
                self.wfile.write(((splited[1])[::-1]).encode(encoding='UTF-8')) 


        else:
            super().do_GET()

# --- main ---


PORT = 4080

print(f'Starting: http://localhost:{PORT}')

tcp_server = socketserver.TCPServer(("", PORT), web_server)
tcp_server.serve_forever()
