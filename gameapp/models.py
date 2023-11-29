from django.db import models
from django.utils import timezone

# # Create your models here.
# Создайте модель для запоминания бросков монеты: орёл или
# решка. Также запоминайте время броска
class Coin(models.Model):
    time=models.DateTimeField(default=timezone.now)
    site=models.CharField(max_length=10)

# Доработаем задачу 1.
# Добавьте статический метод для статистики по n последним
# броскам монеты.
# Метод должен возвращать словарь с парой ключей значений, для орла и для решки.
    @staticmethod #без экземпляра класса (принадлежит к классу а не к экземпляру)
    def values():
        value=Coin.objects.order_by('-time')[:5] #отсортировали по полю тайм в обратном порядке
        return value
     #  print(value)
    
    def __str__(self):
        return f'{self.time}:{self.site}'
