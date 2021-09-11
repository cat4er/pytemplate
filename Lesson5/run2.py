from wsgiref.simple_server import make_server
from urls import fronts
from views import routes
from my_framework.main import Framework, Framework1, Framework2


application2 = Framework2()


with make_server('', 8082, application2) as httpd:
    print("Serving on port 8082...")
    httpd.serve_forever()