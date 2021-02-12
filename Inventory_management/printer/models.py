from django.db import models

# Create your models here.

class Printer(models.Model):
    printer_model = models.CharField(max_length=30, verbose_name='적용 프린터')
    toner_name = models.CharField(max_length=30, verbose_name='토너명')
    quantity = models.IntegerField(verbose_name='현재수량')
    etc = models.TextField(verbose_name='비고')
    