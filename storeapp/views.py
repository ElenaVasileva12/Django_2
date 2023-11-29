from django.shortcuts import render
from django.http import HttpResponse
from .models import Client,Product,Order
from django.db import models

def index(requests):
    return HttpResponse('Hello')

def view_client(requests):
    #фейковые данные
    for i in range(11):
        client=Client(name=f'client_{i}', 
                      email=f'client{i}@mail.ru', 
                      phone=f'1234567{i}',
                      address=f'Академика Каралева, {i}',
                      day_reg=f'2027-11-23 11:00')
        client.save()
    for i in range(11):
        product=Product(name=f'product_{i}', 
                        description=f'product_desc{i}',
                        prise=i**2,
                        count_product=i,
                        date_create=f'2027-11-23 11:00')
        product.save()

    order=Order.objects.create(customer=client,
                               date_ordered=f'2027-11-23 11:00', 
                               total_price=product.prise*product.count_product)



    return HttpResponse('Данные загружены')