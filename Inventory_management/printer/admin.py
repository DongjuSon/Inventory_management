from django.contrib import admin
from printer.models import *

# Register your models here.

class PrinterAdmin(admin.ModelAdmin):
    list_display = ('printer_model','toner_name', 'quantity', 'etc')


admin.site.register(Printer, PrinterAdmin)