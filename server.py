import http.server
import socketserver
import os

PORT = 5555
DIRECTORY = "./templates/"
os.chdir(DIRECTORY)
Handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Server is started on {PORT} from directory {DIRECTORY}")
    httpd.serve_forever()