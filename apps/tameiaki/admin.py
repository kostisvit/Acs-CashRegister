from django.contrib import admin
from .models import Cash,UploadFile
from import_export.admin import ImportExportModelAdmin


class CashAdmin(ImportExportModelAdmin):
    list_display = ('customer', 'cash_model', 'cash_number','register_date', 'old_os', 'new_os', 'update_date','status','voucher','info','created_at','updated_at')

class FileAdmin(ImportExportModelAdmin):
    list_display = ('id','customer','file','created_at')


admin.site.register(Cash,CashAdmin)
admin.site.register(UploadFile,FileAdmin)
