from http.server import HTTPServer, BaseHTTPRequestHandler


class SSimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        print(self.path)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'Hello, world!')
        


httpd = HTTPServer(('192.168.0.60', 12345), SSimpleHTTPRequestHandler)
httpd.serve_forever()