# Generated by Django 4.2.7 on 2023-11-28 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0007_order_products'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='products',
        ),
    ]
