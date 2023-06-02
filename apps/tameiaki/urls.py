from django.urls import path
from . import views
from .views import CashExport






urlpatterns = [
    path('cash-register/customer-api', views.customers, name='customer'),
    path('cash-register/cash', views.TameiakiFilterView.as_view(), name='tameiaki'),
    path('cash-register/new-cash', views.CreatePostView.as_view(), name='new-cash'),
    # update
    path('update/<uuid:pk>', views.CashUpdateView.as_view(), name='edit-cash'),
    # export
    path('export-xls/', CashExport.as_view(), name='export-cash'),
]