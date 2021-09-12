from datetime import datetime

# Front controllers
def time_front(request):
    request['time'] = datetime.now().time().strftime("%H:%M")


def date_front(request):
    request['year'] = datetime.now().today().year


def other_front(request):
    request['key'] = 'key'


fronts = [time_front, date_front, other_front]

