**Documentation:** https://docs.apistar.com 📘

---

# Features

Why might you consider using API Star for your next Web API project?

* **Schema generation** - Support for automatically generating OpenAPI schemas.
* **Expressive** - Type annotated views, that make for expressive, testable code.
* **Performance** - Dynamic behaviour for determining how to run each view makes API Star incredibly efficient.
* **Throughput** - Support for asyncio allows for building high-throughput non-blocking applications.

---

# Quickstart

Install API Star:

```bash
$ pip3 install apistar
```

Create a new project in `app.py`:

```python
from apistar import App, Route


def welcome(name=None):
    if name is None:
        return {'message': 'Welcome to API Star!'}
    return {'message': 'Welcome to API Star, %s!' % name}


routes = [
    Route('/', method='GET', handler=welcome),
]

app = App(routes=routes)


if __name__ == '__main__':
    app.serve('127.0.0.1', 5000, debug=True)
```

Open `http://127.0.0.1:5000/docs/` in your browser:

![API documentation](https://raw.githubusercontent.com/encode/apistar/master/docs/img/api-docs.png)
