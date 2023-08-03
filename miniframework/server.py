from http.server import HTTPServer
from request import HTTPRequestHandler


class Server:
    def run(self):
        host = '127.0.0.1'
        port = 8000

        server_address = (host, port)
        httpd = HTTPServer(server_address, HTTPRequestHandler)

        print(f"Serving at http://{host}:{port}")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            httpd.server_close()
            print("Server shutting down...")


if __name__ == "__main__":
    server = Server()
    server.run()
