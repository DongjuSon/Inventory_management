from django.db import models
from datetime import datetime
# Create your models here.

# 현업부서 리스트업
class TS_user(models.Model):
    depart_nm = models.CharField(max_length=20, verbose_name='부서')
    ts_nm = models.CharField(max_length=20, verbose_name='사용자명')

    def __str__(self):
        return self.depart_nm

    class Meta:
        db_table = 'TS_User'
        verbose_name = '현업 사용자 리스트'
        verbose_name_plural = '현업 사용자 리스트'



# 입출고 여부 선택
in_output_choice = (
    (0, 'input'),
    (1, 'output')
)

class Stock_mn(models.Model):
    depart = models.ForeignKey('stock_mn.TS_user', on_delete=models.CASCADE,verbose_name='부서')


    def __str__(self):
        return self.depart.depart_nm 

    class Meta:
        db_table = "Stock management"
        verbose_name = '입출고 관리'
        verbose_name_plural = '입출고 관리'


class Stock_printer(models.Model):
    stock_id = models.ForeignKey('stock_mn.Stock_mn', on_delete=models.CASCADE, verbose_name='입출고 부서')
    printer_id = models.ForeignKey('printer.Printer', on_delete=models.CASCADE, verbose_name='프린터 코드')
    reg_index = models.SmallIntegerField(choices=in_output_choice, verbose_name='입출고여부 정하기',default=0)
    reg_desc = models.TextField(verbose_name='입출고현황',default="")
    reg_qty = models.IntegerField(verbose_name='입출고수량',default=0)
    reg_date = models.DateTimeField(auto_now_add=True, verbose_name='입출고일자')


