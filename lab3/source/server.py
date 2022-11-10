#!/usr/bin/env python3
import http.server
from importlib.resources import path
import socketserver
import os
import json


#print('source code for "http.server":', http.server.__file__)



class web_server(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):

        print(self.path)

        if self.path == '/':
            self.protocol_version = 'HTTP/1.1'
            self.send_response(404)
            self.end_headers()
        elif self.path.startswith("/str="):
            self.protocol_version = 'HTTP/1.1'
            self.send_response(200)
            self.send_header("Content-type","application/json")
            self.end_headers()

            text_to_check = self.path[5:]
            
            # text_to_check = path1.split('&')[0]
            
            lowercase = 0
            uppercase = 0
            digits = 0
            special = 0
            
            for i in text_to_check:
                if(i.islower()):
                    lowercase+=1
                elif(i.isupper()):
                    uppercase+=1
                elif(i.isdigit()):
                    digits+=1
                else:
                    special+=1
                    
            self.wfile.write(json.dumps({'lowercase': lowercase, 'uppercase': uppercase, 'digits': digits, 'special': special}).encode())
            
            

        else:
            super().do_GET()

# --- main ---


PORT = 4080

print(f'Starting: http://localhost:{PORT}')

tcp_server = socketserver.TCPServer(("", PORT), web_server)
tcp_server.serve_forever()
