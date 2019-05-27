from http.server import BaseHTTPRequestHandler
import http.server
from urllib.parse import urlparse
from urllib.parse import parse_qs
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import os


PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler
index = open("index.html", 'rb').read()


class Serv(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.end_headers()
            self.wfile.write(index)
        elif ".jpg" in self.path:
            self.path = self.path[1:]
            file = open(self.path, 'rb')
            file_to_open = file.read()
            self.send_response(200)
            self.end_headers()
            self.wfile.write(file_to_open)
        elif ".css" in self.path:
            self.path = self.path[1:]
            file = open(self.path, 'rb')
            file_to_open = file.read()
            self.send_response(200)
            self.end_headers()
            self.wfile.write(file_to_open)
        elif ".js" in self.path:
            self.path = self.path[1:]
            file = open(self.path, 'rb')
            file_to_open = file.read()
            self.send_response(200)
            self.end_headers()
            self.wfile.write(file_to_open)
        elif ".png" in self.path:
            self.path = self.path[1:]
            file = open(self.path, 'rb')
            file_to_open = file.read()
            self.send_response(200)
            self.end_headers()
            self.wfile.write(file_to_open)

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_body = self.rfile.read(content_length)
        post_data_dict = json.loads(str(post_body, encoding='utf-8'))
        print(post_body)

        if "/check" in self.path:
            check_text = post_data_dict['text']
            print(check_text)
            result = {"message": "OK", "session_id": 1}
            result_json = json.dumps(result)
            self.send_response(200, "OK")
            self.send_header("Content-Type", 'text/plain')
            self.end_headers()
            self.wfile.write(bytes(result_json, 'utf-8'))
        if "/update" in self.path:
            update_text = post_data_dict['text']
            print(update_text)
            result = {"message": "OK", "session_id": 1}
            result_json = json.dumps(result)
            self.send_response(200, "OK")
            self.send_header("Content-Type", 'text/plain')
            self.end_headers()
            self.wfile.write(bytes(result_json, 'utf-8'))


httpd = HTTPServer(('localhost', 8000), Serv)
httpd.serve_forever()
