from wsgiref.util import setup_testing_defaults
from wsgiref.simple_server import make_server
from Lesson1.urls import *


class Application:

    def __init__(self, routes, fronts):
        self.routes = routes
        self.fronts = fronts

    def __call__(self, environ, start_response):
        setup_testing_defaults(environ)
        print('work')
        path = environ['PATH_INFO']
        # проверка на слэш
        if not path.endswith('/'):
            path = f'{path}/'
        if path in self.routes:
            view = self.routes[path]
        else:
            view = NotFound404()
        request = {}

        # общий обработчик
        for front in self.fronts:
            front(request)
        code, body = view(request)
        start_response(code, [('Content-Type', 'text/html')])
        return [body.encode('utf-8')]


application = Application(routes, fronts)

with make_server('', 8080, application) as httpd:
    print("Serving on port 8080...")
    httpd.serve_forever()
