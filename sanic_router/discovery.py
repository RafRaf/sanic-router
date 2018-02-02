from sanic_router.utils import Url, Include


def autodiscovery(app, root_url: [Url, str]):
    """
    Make auto discovery for routes
    :param app: an Sanic's application
    :param root_url: an dot.notation.path.to.first.route file or Include object
    """
    def discovery(url: [Url, str], prefix: str=None, namespaces: tuple=None):
        for url_object in url.handler.routes:
            new_uri = ''.join((prefix or '', url_object.uri))

            if isinstance(url_object.handler, Include):
                new_namespaces = (namespaces or tuple()) + (url_object.handler.namespace or '',)
                discovery(url_object, new_uri, new_namespaces)
            else:
                new_name = ':'.join(namespaces + (url_object.name,)) if namespaces else url_object.name
                app.add_route(url_object.handler, new_uri, name=new_name)

    top_level_url = Url('', Include(root_url, '')) if isinstance(root_url, str) else root_url

    # Run the discovery procedure
    #
    discovery(top_level_url)
