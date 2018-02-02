from unittest import TestCase
from unittest.mock import patch

from sanic import Sanic

from sanic_router import autodiscovery


class SimpleTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = Sanic()

    def _get_routes(self):
        """
        Get a list of all discovered routes
        :return: list of routes
        """
        routes = list()

        with patch('tests.tests.SimpleTestCase.app') as app_mock:
            app_mock.add_route = lambda handle, uri, name: routes.append(name)
            autodiscovery(self.app, 'tests.example.routes')
        return routes

    def test_autodiscovery_names(self):
        routes = self._get_routes()

        # Are all routes have expected names?
        #
        self.assertListEqual(routes, ['index', 'schema:list', 'schema:detail'])

    def test_url_for(self):
        schema_id = 9000

        # Real routes auto discovery
        #
        autodiscovery(self.app, 'tests.example.routes')

        # Check for a needed URL
        #
        self.assertEqual(self.app.url_for('schema:detail', id=schema_id), '/schema/%d' % schema_id)
