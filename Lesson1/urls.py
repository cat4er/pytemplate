from datetime import datetime

from views import *


# Front controllers
def time_front(request):
    request['time'] = datetime.now().time().strftime("%H:%M")


def date_front(request):
    request['year'] = datetime.now().today().year


def other_front(request):
    request['key'] = 'key'


routes = {
    '/': Index(),
    '/404': NotFound404(),
    '/about/': About(),
    '/riddles/': Riddles(),
}

fronts = [time_front, date_front, other_front]
