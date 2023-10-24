from django import forms
import django_filters
from .models import Cash,UploadFile

class CashFilter(django_filters.FilterSet):
    
    CHOICES = ((True, 'Online'), (False, 'Offline'))
    VOUCHER_CHOICES = ((True, 'Voucher'), (False, 'No Voucher'))
    
    customer = django_filters.CharFilter(lookup_expr='icontains', label='Πελάτης')
    cash_model = django_filters.CharFilter(lookup_expr='icontains', label='Ταμειακή')
    status = django_filters.ChoiceFilter(choices=CHOICES, label='Κατάσταση')
    voucher = django_filters.ChoiceFilter(choices=VOUCHER_CHOICES, label='Voucher')
    
    class Meta:
        model = Cash
        fields = ['customer','cash_model','status']

class CustomerFilter(django_filters.FilterSet):
    
    customer = django_filters.CharFilter(lookup_expr='icontains', label='Πελάτης')
    
    class Meta:
        model = Cash
        fields = ['customer']


class FileFilter(django_filters.FilterSet):

    customer = django_filters.CharFilter(lookup_expr='icontains', label='Πελάτης')

    class Meta:
        model = UploadFile
        fields = ['customer']