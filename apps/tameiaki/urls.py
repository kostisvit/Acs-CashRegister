from django.urls import path
from . import views




urlpatterns = [
    path('cash-register/customer', views.customers, name='customer'),
    path('cash-register/tameiaki', views.tameiaki, name='tameiaki'),
    #path('cash-register/new-cash', views.CashNew, name='new-cash'),
]