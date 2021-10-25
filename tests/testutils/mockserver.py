
from io import BytesIO
from utils.http_server import RequestHandlerClass


class MockRequestHandlerClass(RequestHandlerClass):
    # On Python3, in socketserver.StreamRequestHandler, if this is
    # set it will use makefile() to produce the output stream. Otherwise,
    # it will use socketserver._SocketWriter, and we won't be able to get
    # to the data
    wbufsize = 1

    def finish(self):
        # Do not close self.wfile, so we can read its value
        self.wfile.flush()
        self.rfile.close()

    def date_time_string(self, timestamp=None):
        """ Mocked date time string """
        return 'DATETIME'

    def version_string(self):
        """ mock the server id """
        return 'BaseHTTP/x.x Python/x.x.x'


class MockSocket(object):
    def getsockname(self):
        return ('sockname',)


class MockRequest:
    _sock = MockSocket()

    def __init__(self, path):
        self._path = path

    def makefile(self, *args, **kwargs):
        if args[0] == 'rb':
            return BytesIO(b"GET %s HTTP/1.0" % self._path)
        elif args[0] == 'wb':
            return BytesIO(b'')
        else:
            raise ValueError("Unknown file type to make", args, kwargs)


def parse_response(response):
    '''
    Parses the HTTP plain text response to a
    key valued dict to facilitate the testing cases execution
    '''
    response = response.decode('UTF-8')
    splitted_response = response.split('\r\n')
    return {
        'HTTP_VERSION': splitted_response[0],
        'HTTP_STATUS_CODE': splitted_response[0],
        'SERVER_INFO': splitted_response[1],
        'DATE': splitted_response[2],
        'HEADERS': splitted_response[3:-2],
        'RESPONSE': splitted_response[-1]
    }
