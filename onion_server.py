# onion_server.py

import http.server
import socketserver

PORT = 8080

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"<html><body><h1>Welcome to your .onion site!</h1></body></html>")

if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Serving .onion site at port {PORT}")
        httpd.serve_forever()



        # To make this server accessible via Tor as a .onion service,
        # you need to run Tor and configure a hidden service that points to this server's port.
        # This cannot be done purely in Python; you must edit your Tor configuration file (torrc).

        # Example steps:
        # 1. Install Tor (https://www.torproject.org/download/)
        # 2. Edit your torrc file (location varies by OS, e.g., C:\Users\<user>\AppData\Roaming\tor\torrc on Windows)
        # 3. Add these lines to torrc:
        #    HiddenServiceDir C:\Users\Dominykas\Desktop\CODE\onion server\hidden_service
        #    HiddenServicePort 80 127.0.0.1:8080
        # 4. Start Tor. Tor will create a hostname file in the HiddenServiceDir folder containing your .onion address.
        # 5. Access your server via Tor Browser using the .onion address.

        # The Python code does not need to change, but you must run Tor and configure the hidden service as described above.