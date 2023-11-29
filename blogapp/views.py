from django.shortcuts import render
from django.http import HttpResponse
from .models import Autor

    # name=models.CharField(max_length=100)
    # secondname=models.CharField(max_length=100)
    # email=models.EmailField()
    # bio=models.TextField()
    # bday=models.DateField()



def index(requests):
    return HttpResponse('Hello')

def view_autor(requests):
    #фейковые данные
    for i in range(101):
        autor=Autor(name=f'aaa{i}', secondname=f'bbb{i}',email=f'aaa@{i}.ru',bio=f'cccc{i}', bday=f'2023-11-23')
        autor.save()
    return HttpResponse('autor')