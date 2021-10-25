import unittest
import json
from testutils.mockserver import (
    MockRequestHandlerClass, MockRequest, parse_response)


class PropertiesAPITestCase(unittest.TestCase):

    def _test(self, request):
        handler = MockRequestHandlerClass(request, (0, 0), None)
        return parse_response(handler.wfile.getvalue())

    def test_get_list_public(self):
        '''
        Tests the /property/public/ API capabilities.

        Note: the public properties are the properties that currently has
        a status like ('pre_venta', 'en_venta', 'vendido')

        The required fields to be returned by the API Endpoint are:
            - 'id'
            - 'address'
            - 'city'
            - 'status_name'
            - 'status_label',
            - 'price'
            - 'year'

        GIVEN a HTTP request to GET all the public properties
        WHEN the /property/public/ path is called
        THEN the JSON with the found properties must be returned
        '''
        request_response = self._test(MockRequest(b'/property/public/'))
        dict_response = json.loads(request_response['RESPONSE'])
        required_fields_per_property = [
            'id', 'address', 'city', 'status_name', 'status_label',
            'price', 'year'
        ]
        self.assertEqual(
            len(dict_response['results']),
            dict_response['count'])
        if dict_response['count']:
            self.assertEqual(
                required_fields_per_property,
                [x for x in dict_response['results'][0].keys()]
            )

    def test_get_list_public_with_year_param(self):
        '''
        Tests the /property/public/ path using GET params to test the API
        capabilities and filter the returned data propertly.

        Note: This filter can not exclude the public properties statuses

        GIVEN A HTTP request to GET all the public properties with year param
        WHEN the /property/public/?year=2011 path is called
        THEN the JSON with the found properties must be returned
        '''
        year_request_response = self._test(MockRequest(
            b'/property/public/?year=2011'))
        year_dict_response = json.loads(year_request_response['RESPONSE'])
        self.assertEqual(
            2011,
            year_dict_response['results'][0]['year'])

    def test_get_list_public_with_city_param(self):
        '''
        Tests the /property/public/ path using GET params to test the API
        capabilities and filter the returned data propertly.

        Note: This filter can not exclude the public properties statuses

        GIVEN A HTTP request to GET all the public properties with city param
        WHEN the /property/public/?city=bogota path is called
        THEN the JSON with the found properties must be returned
        '''
        city_request_response = self._test(MockRequest(
            b'/property/public/?city=bogota'))
        city_dict_response = json.loads(city_request_response['RESPONSE'])
        self.assertEqual(
            'bogota',
            city_dict_response['results'][0]['city'])

    def test_get_list_public_with_status_param(self):
        '''
        Tests the /property/public/ path using GET params to test the API
        capabilities and filter the returned data propertly.

        Note: This filter can not exclude the public properties statuses

        GIVEN A HTTP request to GET all the public properties with status param
        WHEN the /property/public/?status=en_venta path is called
        THEN the JSON with the found properties must be returned
        '''
        status_request_response = self._test(MockRequest(
            b'/property/public/?status=en_venta'))
        status_dict_response = json.loads(status_request_response['RESPONSE'])
        self.assertEqual(
            'en_venta',
            status_dict_response['results'][0]['status_name'])

    def test_get_list_public_with_year_and_city_params(self):
        '''
        Tests the /property/public/ path using GET params to test the API
        capabilities and filter the returned data propertly.

        Note: This filter can not exclude the public properties statuses

        GIVEN A HTTP request to GET all the public properties with year and
            city params
        WHEN the /property/public/?city=bogota&year=2011 path is called
        THEN the JSON with the found properties must be returned
        '''
        city_year_request_response = self._test(MockRequest(
            b'/property/public/?city=bogota&year=2011'))
        city_year_dict_response = json.loads(
            city_year_request_response['RESPONSE'])
        self.assertEqual(
            'bogota',
            city_year_dict_response['results'][0]['city'])
        self.assertEqual(
            2011,
            city_year_dict_response['results'][0]['year'])

    def test_get_list(self):
        '''
        Tests the /property/ path using GET params to test the API and its
        returned data.

        The required fields to be returned by the API Endpoint are:
            - 'id'
            - 'address'
            - 'city'
            - 'price'
            - 'year'
            - 'status_id'
            - 'status_update_date'
            - 'status_name'
            - 'status_label'

        Note: This API shows all the properties and their
            corresponding statuses

        GIVEN A HTTP request to GET all the existent properties
        WHEN the /property/ path is called
        THEN the JSON with the found properties must be returned
        '''
        request_response = self._test(MockRequest(b'/property/'))
        required_fields_per_property = [
            'id', 'address', 'city', 'price', 'year',
            'status_id', 'status_update_date', 'status_name',
            'status_label']
        dict_response = json.loads(request_response['RESPONSE'])
        self.assertEqual(
            len(dict_response['results']),
            dict_response['count'])

        if dict_response['count']:
            self.assertEqual(
                required_fields_per_property,
                [x for x in dict_response['results'][0].keys()]
            )


def main():
    unittest.main()


if __name__ == "__main__":
    main()
