from wsgicors import CORS


class CORSMixin:
    def __call__(self, environ, start_response, **options):
        cors = CORS(super().__call__, **options)
        return cors(environ, start_response)
