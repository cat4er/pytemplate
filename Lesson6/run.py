from wsgiref.simple_server import make_server
from urls import fronts
from views import routes
from my_framework.main import Framework


application = Framework(routes, fronts)

with make_server('', 8080, application) as httpd:
    print("Serving on port 8080...")
    httpd.serve_forever()
