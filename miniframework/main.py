# from http.server import HTTPServer, SimpleHTTPRequestHandler
# import logging

# logging.basicConfig(level=logging.INFO)


# class RequestHandler(SimpleHTTPRequestHandler):
#     def do_GET(self):
#         self.send_response(200)
#         self.send_header("Content-type", "application-json")
#         self.end_headers()
#         self.wfile.write(bytes('{"asd": "qweqwe"}', "utf-8"))


# logging.log(msg="Server started successfully!", level=logging.INFO)
# server = HTTPServer(("127.0.0.1", 8000), RequestHandler)
# server.serve_forever()
# server.close_request()

# router = Router()


def say_hello(request):
    request.send_response(200)
    request.send_header("Content-type", "text/html")
    request.end_headers()
    request.wfile.write(bytes('<html><body><a href="/get">Sating Goodbye!</a></body></html>', "utf-8"))

def get(request):
    request.send_response(200)
    request.send_header("Content-type", "text/html")
    request.end_headers()
    request.wfile.write(bytes('<html><body><a href="/hello">Saying Hello</a></body></html>', "utf-8"))
