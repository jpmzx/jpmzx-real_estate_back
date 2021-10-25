from apps.properties.controller import PropertyViewSet
routes = (
    ('GET', '/property/', PropertyViewSet, 'list'),
    ('GET', '/property/public/', PropertyViewSet, 'list_public'),
)
