from django.shortcuts import render
from django.http import HttpResponse
from random import *
from .models import Coin


# � Создайте представление “Привет, мир!” внутри вашего
# первого приложения
def index(request):
    return HttpResponse('Привет, мир!')

# � Создайте новое приложение. Подключите его к проекту. В
# приложении должно быть три простых представления,
# возвращающих HTTP ответ:
# � Орёл или решка
# � Значение одной из шести граней игрального кубика
# � Случайное число от 0 до 100
def coin(request):
    site=choice(['Орел','Решка'])
    arg=Coin(site=site)
    arg.save()             #http://127.0.0.1:8088/game/coin/
    return HttpResponse(str(site))

def cub(request):
    return HttpResponse(str(randint(1,7)))

def numbers(request):
    return HttpResponse(str(randint(1,101)))

def coin_values(request):
    value=Coin.values()
    print(value)
    lst=[]
    for i in value:
        print(i)
        lst.append(i)
    return HttpResponse(lst)
