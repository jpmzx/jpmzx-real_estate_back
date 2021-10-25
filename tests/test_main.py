import unittest
import importlib


class MainTestCase(unittest.TestCase):

    def test_main(self):
        '''
        GIVEN A request to initialize main.py module
        WHEN the src/main.py module is executed
        THEN the module must execute its code without raise an exception
        '''
        try:
            importlib.import_module('main')
        except ImportError:
            run_server_imported = False
        else:
            run_server_imported = True
        self.assertTrue(run_server_imported)


def main():
    unittest.main()


if __name__ == "__main__":
    main()
