from http.server import BaseHTTPRequestHandler
from router import Router
from urls import url_patterns


class HTTPRequestHandler(BaseHTTPRequestHandler):
    """Base Http Request handler class"""

    def do_GET(self):
        print("Class HTTP Request initiated")
        router = Router()
        router.add(**url_patterns)
        router.route(self)
