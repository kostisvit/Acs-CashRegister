from django import forms
from .models import Cash

class CashForm(forms.Form):
    cash_model = forms.CharField(max_length=100, label='Μοντέλο Ταμειακής')
    cash_number = forms.EmailField(max_length=100, label='Αριθμός Μητρώου')
    register_date = forms.CharField(max_length=100)
    old_os = forms.CharField(max_length=100, label='Old OS Version')
    new_os = forms.CharField(max_length=100, label='New OS Version')
    status = forms.BooleanField(label='Κατάσταση')
    info = forms.CharField(widget=forms.Textarea, label='Σημειώσεις')

    class Meta:
      model = Cash