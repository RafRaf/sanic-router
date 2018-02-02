from .views import IndexView
from sanic_router import Include, Url


routes = (
    Url('', IndexView.as_view(), name='index'),
    Url('schema/', Include('tests.example.schema.routes', namespace='schema')),
)
