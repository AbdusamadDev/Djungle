from http.server import BaseHTTPRequestHandler


class Router(BaseHTTPRequestHandler):
    def __init__(self):
        self.routes = {}

    def add(self, **kwargs):
        print("Asdasd")
        self.routes.update(**kwargs)
        print(self.routes)

    def route(self, request):
        path = request.path
        print("Request path: ", request.path)
        handler = self.routes.get(path, None)
        print("Routes: ", self.routes)
        if handler:
            handler(request)
        else:
            print("Url is not found")
