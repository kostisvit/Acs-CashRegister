from django import forms
import django_filters
from .models import Cash

class CashFilter(django_filters.FilterSet):
    
    CHOICES = ((True, 'Online'), (False, 'Offline'))
    
    customer = django_filters.CharFilter(lookup_expr='icontains', label='Πελάτης')
    cash_model = django_filters.CharFilter(lookup_expr='icontains', label='Ταμειακή')
    status = django_filters.ChoiceFilter(choices=CHOICES, label='Κατάσταση')
    class Meta:
        model = Cash
        fields = ['customer','cash_model','status']