import signal
import unittest

from testutils.mockserver import (
    MockRequest, MockRequestHandlerClass,
    parse_response)
from utils.http_server import run_server


class Timeout:
    '''
    Set a timeout for the given action
    '''

    def __init__(self, seconds=1, error_message='Timeout'):
        self.seconds = seconds
        self.error_message = error_message

    def handle_timeout(self, signum, frame):
        raise TimeoutError(self.error_message)

    def __enter__(self):
        signal.signal(signal.SIGALRM, self.handle_timeout)
        signal.alarm(self.seconds)

    def __exit__(self, type, value, traceback):
        signal.alarm(0)


class HTTPServerTestCase(unittest.TestCase):

    def _test(self, request):
        handler = MockRequestHandlerClass(request, (0, 0), None)
        return parse_response(handler.wfile.getvalue())

    def test_not_found_route(self):
        '''
        GIVEN A HTTP request non-existent route in the config/routes file
        WHEN the http request is executed
        THEN the server must return: 404 Not found as a message
        '''
        request_response = self._test(MockRequest(b'/not_found/'))
        self.assertTrue('404 Not found' in request_response['HTTP_VERSION'])

    def test_run_server(self):
        '''
        GIVEN A request to start the http server
        WHEN the python src/main.py is executed
        THEN the run_server method must be started without raising Exceptions
        '''
        try:
            with Timeout(seconds=2):
                run_server()
        except TimeoutError:
            self.assertTrue(True)
        except Exception as e:
            print(e)
            self.assertTrue(False)
        else:
            self.assertTrue(True)


def main():
    unittest.main()


if __name__ == "__main__":
    main()
