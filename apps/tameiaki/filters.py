import django_filters
from .models import Cash

class CashFilter(django_filters.FilterSet):
    class Meta:
        model = Cash
        fields = ['customer','cash_model']