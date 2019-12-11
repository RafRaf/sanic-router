import importlib


class Url:
    def __init__(self, uri: str, handler, name: str=None):
        self.uri = uri
        self.handler = handler
        self.name = name

    def __repr__(self):
        return '%s: %s' % (self.uri, self.name or '__no_name__') if self.name else self.uri


class Include:
    def __init__(self, module_name: str, namespace: str):
        self.module_name = module_name
        self.namespace = namespace

        try:
            module = importlib.import_module(module_name)

            self.routes = getattr(module, 'routes')
        except ImportError:
            raise NotImplementedError('Can\'t import route module: %s' % module_name)
        except AttributeError:
            raise NotImplementedError('Route module (%s) does not have routes definition' % module_name)

    def __repr__(self):
        return '%s: %s' % (self.module_name, ','.join(self.routes))
