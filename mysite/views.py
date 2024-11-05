from datetime import date

from django.http import HttpResponse


def index(request):
    return HttpResponse('Hello, world!')


def dayofweek(request):
    days = ('Понедельник', 'Вторник', 'Среда',
            'Четверг', 'Пятница', 'Суббота', 'Воскресенье')
    d = date.today().weekday()
    ans = days[d]
    return HttpResponse(ans)


def dayofweek_(request, wrong):
    return dayofweek(request)


def wrong(request):
    return HttpResponse('Неверный адрес')


def calc(request, a, operator, b):
    match operator:
        case '+':
            return HttpResponse(a + b)
        case '-':
            return HttpResponse(a - b)
        case '*':
            return HttpResponse(a * b)
        case 'del':
            return HttpResponse(a / b)
        case _:
            return HttpResponse('error')
