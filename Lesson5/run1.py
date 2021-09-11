from wsgiref.simple_server import make_server
from urls import fronts
from views import routes
from my_framework.main import Framework, Framework1, Framework2


application1 = Framework1(routes, fronts)


with make_server('', 8081, application1) as httpd:
    print("Serving on port 8081...")
    httpd.serve_forever()
