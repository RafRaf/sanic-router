from sanic.views import HTTPMethodView
from sanic.response import text


class IndexView(HTTPMethodView):
    def get(self, request):
        return text('test')
