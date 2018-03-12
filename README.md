[![Build Status](https://travis-ci.org/RafRaf/sanic-router.svg?branch=master)](https://travis-ci.org/RafRaf/sanic-router)
# Sanic-router

Powerful Django-like router for Sanic. The process of using it is very simple and intuitive. Just run `autodiscovery`.


## Installation

* pip install sanic-router

## Example

Let's pretend we have a project structure like this:

#### tests/example/routes.py
```python
from .views import IndexView
from sanic_router import Include, Url

routes = (
    Url('', IndexView.as_view(), name='index'),
    Url('schema/', Include('tests.example.schema.routes', namespace='schema')),
)

```

#### tests/example/schema/routes.py
```python
from .views import SchemaList, SchemaDetail
from sanic_router import Url

routes = (
    Url('', SchemaList.as_view(), name='list'),
    Url('<id>/', SchemaDetail.as_view(), name='detail'),
)

```

At least, all you need to do is just run `autodiscovery` and after that, you can use Sanic's `url_for` as always you do:

```python
from sanic_router import autodiscovery

app = Sanic()

autodiscovery(app, 'tests.example.routes')
app.url_for('schema:detail', id=9000)
```
