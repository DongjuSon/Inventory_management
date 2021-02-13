from django.db import models


# Create your models here.


class Product(models.Model):
    product_model = models.CharField(max_length=30, verbose_name='모델명(대분류)')
    procudt_name = models.CharField(max_length=30, verbose_name='품목명(상세분류)')
    quantity = models.IntegerField(verbose_name='수량')
    etc = models.TextField(verbose_name='비고')

