from wsgiref.simple_server import make_server

from my_framework.main import application

with make_server('', 8080, application) as httpd:
    print("Serving on port 8080...")
    httpd.serve_forever()