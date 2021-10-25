from config import settings, routes
from utils.routes import match_route
from utils.controllers import handle_route
from http import HTTPStatus, server
import socketserver
import io
import sys


class RequestHandlerClass(server.SimpleHTTPRequestHandler):

    def _not_found_response(self) -> None:
        self.send_error(HTTPStatus.NOT_FOUND, "Not found")

    def do_GET(self) -> None:
        matched_path = match_route('GET', self.path)
        if matched_path:
            route_response = handle_route(matched_path, self)
            body = route_response.content
            enc = sys.getfilesystemencoding()
            encoded = body.encode(enc, 'surrogateescape')
            f = io.BytesIO()
            f.write(encoded)
            f.seek(0)
            self.send_response(HTTPStatus.OK)
            # self.send_header("Content-type", "text/html; charset=%s" % enc)
            self.send_header("Content-type", "application/json")
            self.send_header("Content-Length", str(len(encoded)))
            self.end_headers()
            try:
                self.copyfile(f, self.wfile)
            finally:
                f.close()
            return None
        return self._not_found_response()


def run_server():
    socketserver.TCPServer.allow_reuse_address = True
    http_server = socketserver.TCPServer(
        ("", settings.PORT),
        RequestHandlerClass)
    print(f'Starting http server at {settings.SERVER_NAME}:{settings.PORT} ')
    try:
        http_server.serve_forever()
    except KeyboardInterrupt:
        http_server.shutdown()
