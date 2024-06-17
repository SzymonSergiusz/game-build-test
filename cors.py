import http.server
import socketserver

class CORSRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', '*')
        super().end_headers()

PORT = 8000

with socketserver.TCPServer(("", PORT), CORSRequestHandler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
