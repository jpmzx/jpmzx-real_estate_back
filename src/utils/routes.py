from config.routes import routes
from urllib import parse


def match_route(method, path):
    route = None
    # Removes the GET parameters from the path
    path = parse.urlparse(path).path
    # Check if the path exists in the routes definition
    filtered_routes = filter(
        lambda route: (
            route[0] == method) and (
            route[1] == path), routes)
    # A matched list of routes
    filtered_routes = list(filtered_routes)
    if filtered_routes:
        # Select the first matched route
        route = filtered_routes[0]
    return route
