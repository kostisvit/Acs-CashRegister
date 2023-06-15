from import_export import resources, fields
from .models import Cash

class CashResource(resources.ModelResource):
    customer = fields.Field(
       attribute="customer",
       column_name="Pet Name",
       
   )

    class Meta:
        model = Cash
        fields = ('customer', 'cash_model', 'cash_number','register_date', 'old_os', 'new_os','aes_key', 'status','info')
        export_order = ('customer', 'cash_model', 'cash_number','register_date', 'old_os', 'new_os','aes_key', 'status','info')
        widgets = {
            'register_date': {'format': '%d/%m/%Y'},
        }