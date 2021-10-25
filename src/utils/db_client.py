from config import settings
import pymysql
from datetime import datetime, date


class DBManager:

    HOST = settings.DATABASE['HOST']
    DATABASE = settings.DATABASE['DATABASE']
    USER = settings.DATABASE['USER']
    PASSWORD = settings.DATABASE['PASSWORD']
    PORT = settings.DATABASE['PORT']

    def _serialize_results(self):
        # Serializes the cursor results into one list o dicts
        # eatch dict is equivalent to one row and contains a
        # key, value pair with its col : row value definition.
        table_fields_name = [x[0] for x in self.cursor.description]
        results = []
        for row in self.cursor.fetchall():
            row_dict = {}
            for value_index, value in enumerate(row):
                # Converts date and datetime objects to ISO-8601 format string
                if isinstance(value, datetime) or isinstance(value, date):
                    value = value.isoformat()
                # Adds a column_name: row_value key value to row_dict
                row_dict[table_fields_name[value_index]] = value
            results.append(row_dict)
        return results

    def _open_connection(self) -> None:
        self.conn = pymysql.connect(
            host=self.HOST,
            port=int(self.PORT),
            user=self.USER,
            passwd=self.PASSWORD,
            db=self.DATABASE)
        self.cursor = self.conn.cursor()

    def execute(self, command):
        self._open_connection()
        self.cursor.execute(command)
        result = self._serialize_results()
        self._close_connection()
        return result

    def _close_connection(self) -> None:
        self.cursor.close()
        self.conn.close()
