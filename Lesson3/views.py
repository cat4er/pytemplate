from my_framework.templator import render


class Index:
    def __call__(self, request):
        return '200 OK', render('index.html', year=request.get('year'))


class About:
    def __call__(self, request):
        return '200 OK', render('about.html', year=request.get('year'), time=request.get('time'))


class Riddles:
    def __call__(self, request):
        return '200 OK', render('riddles.html', year=request.get('year'))


class NotFound404:
    def __call__(self, request):
        return '404 WHAT', '404 PAGE NOT FOUND'
