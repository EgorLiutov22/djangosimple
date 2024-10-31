from datetime import date

from django.http import HttpResponse


def index(request):
    return HttpResponse('Hello, world!')

def dayofweek(request):
    days = ('Понедельник','Вторник', 'Среда',
            'Четверг', 'Пятница', 'Суббота', 'Воскресенье')
    d = date.today().weekday()
    return HttpResponse(days[d])