import django_filters
from .models import Cash

class CashFilter(django_filters.FilterSet):
    customer = django_filters.CharFilter(lookup_expr='icontains', label='Πελάτης')
    cash_model = django_filters.CharFilter(lookup_expr='icontains', label='Ταμειακή')
    class Meta:
        model = Cash
        fields = ['customer','cash_model']