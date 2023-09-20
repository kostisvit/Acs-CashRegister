from django import forms
from .models import Cash,UploadFile
from encrypted_model_fields.fields import EncryptedCharField
from django.core.validators import RegexValidator
import requests

class CashForm(forms.ModelForm):
    customer = forms.ChoiceField(choices=[],label='Πελάτης')
    cash_model = forms.CharField(max_length=100, label='Μοντέλο Ταμειακής')
    cash_number = forms.CharField(max_length=100, label='Αριθμός Μητρώου')
    register_date = forms.DateField(required=False,label='Ημ. Δήλωσης')
    old_os = forms.CharField(max_length=100, label='Old OS Version',required=False)
    new_os = forms.CharField(max_length=100, label='New OS Version')
    update_date = forms.DateField(required=False,label='Ημ. Αναβάθμισης')
    status = forms.BooleanField(label='Κατάσταση(Ενεργή)',initial=True,required=False)
    aes_key = forms.CharField(max_length=100, label='AES Key', required=False)
    info = forms.CharField(widget=forms.Textarea, label='Σημειώσεις', required=False)
    #file = forms.FileField(label='Μεταφόρτωση αρχείου',required=False,widget=forms.ClearableFileInput(attrs={'multiple': True}))


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        options = self.get_dropdown_options()
        self.fields['customer'].choices = options
        self.fields['register_date'].widget = forms.widgets.DateInput(
            attrs={
                'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)',
                'class': 'form-control'
                }
            )
        self.fields['update_date'].widget = forms.widgets.DateInput(
            attrs={
                'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)',
                'class': 'form-control'
                }
            )

    def get_dropdown_options(self):
        response = requests.get('http://host.docker.internal:8280/customer-api') # http://127.0.0.1:8280/customers-api(without container)
        if response.status_code == 200:
            options = response.json()
            return  [(option['company_name'], option['company_name']) for option in options]
        return []

    class Meta:
        model = Cash
        fields = ['customer','cash_model', 'cash_number','register_date','old_os','new_os','update_date','status','aes_key','info']


#Customer API Form
class ClientForm(forms.Form):
    first_name = forms.CharField(label='Ονομα',max_length=100)
    last_name = forms.CharField(label='Επώνυμο',max_length=150)
    company_name = forms.CharField(label='Επωνυμία',max_length=150)
    company_type = forms.CharField(label='Επιχείρηση',max_length=150)
    company_address = forms.CharField(label='Διεύθυνση',max_length=150)
    company_email = forms.EmailField(label='Email',required=False)
    company_afm = forms.CharField(label='ΑΦΜ',max_length=150,validators=[RegexValidator(regex=r'^\d{9}$',message='Please enter exactly 9 digits.',code='invalid_number')])
    phone_number = forms.CharField(label='Τηλ. Επικοινωνίας',max_length=150)




#Upload file form
class FileUploadForm(forms.ModelForm):
    customer = forms.ChoiceField(choices=[],label='Πελάτης')
    file = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = UploadFile
        fields = ['customer','file']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        options = self.get_dropdown_options()
        self.fields['customer'].choices = options

    def get_dropdown_options(self):
        response = requests.get('http://host.docker.internal:8280/customer-api') # http://127.0.0.1:8280/customers-api(without container)
        if response.status_code == 200:
            options = response.json()
            return  [(option['company_name'], option['company_name']) for option in options]
        return []
