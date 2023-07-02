from django.urls import path
from . import views
from .views import CashExport,Export_data,export_data_as_excel






urlpatterns = [
    path('cash-register/customer-api', views.customers, name='customer'),
    path('cash-register/cash', views.TameiakiFilterView.as_view(), name='tameiaki'),
    path('cash-register/new-cash', views.CreatePostView.as_view(), name='new-cash'),
    # update
    path('update/<uuid:pk>', views.CashUpdateView.as_view(), name='edit-cash'),
    # export
    path('export-xls-tameiakes/', views.Export_data, name='export_data'),
    path('export-data/', views.export_data_as_excel, name='export_data_client'),
]