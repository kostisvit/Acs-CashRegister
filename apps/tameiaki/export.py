from django.http import HttpResponse
from django.views import View
import xlwt

from .models import Cash

class CashExport(View):
    def get(self, request, *args, **kwargs):
        # Query the data you want to export
        cash = Cash.objects.all()

        # Create the HttpResponse object with XLS mime type
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="cash.xls"'

        # Create a workbook and add a worksheet
        workbook = xlwt.Workbook(encoding='utf-8')
        worksheet = workbook.add_sheet('Cash')

        # Write headers
        headers = ['Πελάτης', 'Μοντέλο Ταμ.', 'Αρ. Μητρώου','Ημ. Δήλωσης','OS Version','New OS Version','Κατάσταση','AES_Key','Σημειώσεις']
        for col, header in enumerate(headers):
            worksheet.write(0, col, header)

        # Write data
        row = 1
        for cash in cash:
            worksheet.write(row, 0, cash.customer)
            worksheet.write(row, 1, cash.cash_model)
            worksheet.write(row, 2, cash.cash_number)
            worksheet.write(row, 3, cash.register_date)
            worksheet.write(row, 4, cash.old_os)
            worksheet.write(row, 5, cash.new_os)
            worksheet.write(row, 6, cash.status)
            worksheet.write(row, 7, cash.aes_key)
            worksheet.write(row, 8, cash.info)
            
            row += 1

        # Save the workbook to the response
        workbook.save(response)
        return response