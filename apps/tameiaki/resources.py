from import_export import resources, fields
from .models import Cash

class CashResource(resources.ModelResource):
    customer = fields.Field(
       attribute="customer",
       column_name="Customer",
       
   )

    class Meta:
        model = Cash
        fields = ('customer', 'cash_model', 'cash_number','register_date', 'old_os', 'new_os','update_date','aes_key','voucher','pos_connect', 'status','info')
        export_order = ('customer', 'cash_model', 'cash_number','register_date', 'old_os', 'new_os','update_date','aes_key','voucher','pos_connect', 'status','info')
        widgets = {
            'register_date': {'format': '%d/%m/%Y'},
            'update_date': {'format': '%d/%m/%Y'},
        }