from django.contrib import admin
from stock_mn.models import *
# Register your models here.

class TS_userAdmin(admin.ModelAdmin):
    list_display = ('depart_nm','ts_nm')

class Stock_mnAdmin(admin.ModelAdmin):
    list_display = ('id',)

class Stock_printerAdmin(admin.ModelAdmin):
    list_display = ('printer_id',)


admin.site.register(TS_user,TS_userAdmin)
admin.site.register(Stock_mn,Stock_mnAdmin)
admin.site.register(Stock_printer,Stock_printerAdmin)

