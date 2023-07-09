from django.contrib import admin
from .models import Cash
from import_export.admin import ImportExportModelAdmin


class CashAdmin(ImportExportModelAdmin):
    list_display = ('customer', 'cash_model', 'cash_number','register_date', 'old_os', 'new_os', 'update_date','status','info','document','created_at','updated_at')
    
admin.site.register(Cash,CashAdmin)
