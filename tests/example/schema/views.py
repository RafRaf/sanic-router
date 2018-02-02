from sanic.views import HTTPMethodView
from sanic.response import text


class SchemaList(HTTPMethodView):
    def get(self, request):
        return text('test')


class SchemaDetail(HTTPMethodView):
    def get(self, request):
        return text('test')
