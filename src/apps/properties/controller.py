from utils.db_client import DBManager
from utils.controllers import ControllerBase, Response
from apps.properties import queries


class PropertyViewSet(ControllerBase):

    def list(self):
        '''
        Returns a list of properties filtered using the given parameters
        '''
        db_client = DBManager()
        results = db_client.execute(
            queries.select_properties
        )
        return Response({
            'count': len(results),
            'results': results
        }, 200)

    def list_public(self):
        '''
        Returns a list of properties filtered using the given parameters
        '''
        # self.request.GET is handled on the ControllerBase class
        year = self.request.GET.get('year')
        city = self.request.GET.get('city')
        status = self.request.GET.get('status')

        query = f"""
            {queries.select_properties_public}
            where s.name in ('pre_venta', 'en_venta', 'vendido')"""

        # Adding custom where statements
        if year:
            query += f" and p.year = '{year}'"
        if city:
            query += f" and p.city = '{city}'"
        if status:
            query += f" and s.name = '{status}'"

        db_client = DBManager()
        results = db_client.execute(query)

        return Response({
            'count': len(results),
            'results': results
        }, 200)
