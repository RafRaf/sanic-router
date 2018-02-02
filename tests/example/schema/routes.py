from .views import SchemaList, SchemaDetail
from sanic_router import Url


routes = (
    Url('', SchemaList.as_view(), name='list'),
    Url('<id>/', SchemaDetail.as_view(), name='detail'),
)
