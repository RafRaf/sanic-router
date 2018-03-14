from sanic_router.exceptions import RouterException
from sanic_router.utils import Url, Include


def autodiscovery(app, root_url: [Url, str], sep: str=None):
    """
    Make auto discovery for routes
    :param app: Sanic's application
    :param root_url: dot.notation.path.to.first.route file or Include object
    :param sep: a character used as a separator on concatenation
    """
    all_route_names = set()
    separator = sep or ':'

    def discovery(url: [Url, str], prefix: str=None, namespaces: tuple=None):
        for url_object in url.handler.routes:
            new_uri = ''.join((prefix or '', url_object.uri))

            if isinstance(url_object.handler, Include):
                new_namespaces = (namespaces or tuple()) + (url_object.handler.namespace or '',)
                discovery(url_object, new_uri, new_namespaces)
            else:
                new_name = separator.join(namespaces + (url_object.name,)) if namespaces else url_object.name

                # Check for duplication
                #
                if new_name in all_route_names:
                    raise RouterException('Route `%s` is already registered' % new_name)

                app.add_route(url_object.handler, new_uri, name=new_name)
                all_route_names.add(new_name)

    top_level_url = Url('', Include(root_url, '')) if isinstance(root_url, str) else root_url

    # Run the discovery procedure
    #
    discovery(top_level_url)
