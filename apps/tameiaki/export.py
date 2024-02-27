import xlwt, requests
from django.http import HttpResponse
from django.views import View
from .models import Cash
from django.http import HttpResponse
from django.shortcuts import render
from .resources import CashResource
from openpyxl import Workbook

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
        headers = ['Πελάτης', 'Μοντέλο Ταμ.', 'Αρ. Μητρώου','Ημ. Δήλωσης','OS Version','New OS Version','Κατάσταση','AES_Key','Voucher','POS Status','Σημειώσεις']
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
            worksheet.write(row, 8, cash.voucher)
            worksheet.write(row, 9, cash.pos_connect)
            worksheet.write(row, 10, cash.info)
            
            row += 1

        # Save the workbook to the response
        workbook.save(response)
        return response
    
    

def Export_data(request):
    if request.method == 'POST':
        # Get selected option from form
        file_format = request.POST['file-format']
        employee_resource = CashResource()
        dataset = employee_resource.export()
        if file_format == 'CSV':
            response = HttpResponse(dataset.csv, content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="exported_data.csv"'
            return response        
        elif file_format == 'JSON':
            response = HttpResponse(dataset.json, content_type='application/json')
            response['Content-Disposition'] = 'attachment; filename="exported_data.json"'
            return response
        elif file_format == 'XLS (Excel)':
            response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
            response['Content-Disposition'] = 'attachment; filename="exported_data.xls"'
            return response   

    return render(request, 'app/tameiaki/export.html')



# Export pelates, retrieve data from external api
def export_data_as_excel(request):
    # Make a request to the external API and retrieve the data
    response = requests.get('http://host.docker.internal:8280/customer-api')
    data = response.json()

    # Create an Excel workbook and select the active sheet
    workbook = Workbook()
    sheet = workbook.active
    
    # Write headers to the first row
    headers = ['Όνομα','Επώνυμο','Επιχείριση','Έίδος Επιχ.','Διεύθυνση','Email','ΑΦΜ','Τηλέφωνο Επικ.']
    sheet.append(headers)

    # Write data to subsequent rows
    for item in data:
        row = [item['first_name'],item['last_name'],item['company_name'],item['company_type'],item['company_address'],item['company_email'],item['company_afm'],item['phone_number']]
        sheet.append(row)

    # Set the appropriate response headers for Excel file download
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=data.xlsx'

    # Save the workbook to the response
    workbook.save(response)

    return response