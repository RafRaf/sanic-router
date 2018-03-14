from unittest import TestCase
from unittest.mock import patch, Mock

from sanic import Sanic

from sanic_router import autodiscovery, Url
from sanic_router.exceptions import RouterException


class SimpleTestCase(TestCase):
    EXPECTED_ROUTES = [
        'index',
        'schema:list',
        'schema:detail',
    ]

    @classmethod
    def setUpClass(cls):
        cls.app = Sanic()
        cls.routes_path = 'tests.example.routes'

    def _get_routes(self, sep: str=None):
        """
        Get a list of all discovered routes
        :return: list of routes
        """
        routes = list()

        with patch('tests.tests.SimpleTestCase.app') as app_mock:
            app_mock.add_route = lambda handle, uri, name: routes.append(name)
            autodiscovery(self.app, self.routes_path, sep)
        return routes

    def test_autodiscovery_names(self):
        routes = self._get_routes()

        # Check the expected names
        #
        self.assertListEqual(routes, self.EXPECTED_ROUTES)

    def test_url_for(self):
        schema_id = 9000

        # Routes discovery
        #
        autodiscovery(self.app, self.routes_path)

        # Check for a needed URL
        #
        self.assertEqual(self.app.url_for('schema:detail', id=schema_id), '/schema/%d' % schema_id)

    def test_url_names_duplication(self):
        module_mock = Mock(spec=('routes',))
        module_mock.routes = (
            Url('some_url', Mock(), name='list'),
            Url('some_url/<id>/', Mock(), name='list'),  # <- the name duplication is here
        )

        with self.assertRaises(RouterException):
            with patch('importlib.import_module') as import_module_mock:
                import_module_mock.return_value = module_mock

                # Autodiscovery mocked modules
                #
                autodiscovery(self.app, self.routes_path)

    def test_route_separator(self):
        sep = '.'
        routes = self._get_routes(sep)

        # Check the expected names
        #
        self.assertListEqual(
            routes,
            list(map(lambda x: x.replace(':', sep), self.EXPECTED_ROUTES)),
        )
