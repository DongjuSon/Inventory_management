from django.db import models

# Create your models here.

class Printer(models.Model):
    printer_model = models.CharField(max_length=30, verbose_name='적용 프린터')
    toner_name = models.CharField(max_length=30, verbose_name='토너명')
    quantity = models.IntegerField(verbose_name='현재수량')
    etc = models.TextField(verbose_name='비고')

    def __str__(self):
        return self.printer_model + " - " + self.toner_name

    class Meta:
        db_table = "Ptinter management"
        verbose_name = '프린터 재고관리'
        verbose_name_plural = '프린터 재고관리'