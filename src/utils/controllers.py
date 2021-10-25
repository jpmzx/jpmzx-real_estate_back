import json
from urllib import parse


class ControllerBase:

    def __init__(self, request):
        self.request = request
        setattr(self.request, 'GET', self.process_params())

    def process_params(self):
        '''
        Extracts, Parses and returns the GET parameters provided
        in the path of the request
        '''
        # Extracts and transforms the GET params to key,valued dict
        parsed_params = parse.parse_qs(
            parse.urlparse(self.request.path).query)
        # Removes the unnecesary lists of the unique parameters
        parsed_params = {
            x: y if len(y) > 1 else y[0] for x, y in parsed_params.items()}
        return parsed_params


class Response:

    def __init__(self, content, status_code) -> None:
        self.status_code = status_code
        self.content = json.dumps(content)


def handle_route(route, request):
    viewset_instance = route[2](request)
    return getattr(
        viewset_instance, route[3])()
