from django.urls import path
from . import views
from .views import CashExport,Export_data,export_data_as_excel,CustomerFormView,FileListView






urlpatterns = [
    path('cash-register/customer-api', views.customers, name='customer'),
    path('cash/customer-new', CustomerFormView.as_view(), name='customer-new'),
    path('cash-register/cash', views.TameiakiFilterView.as_view(), name='tameiaki'),
    path('cash-register/new-cash', views.CreatePostView.as_view(), name='new-cash'),
    path('cash-files', views.FileListView.as_view(), name='files'),
    # update
    path('update/<uuid:pk>', views.CashUpdateView.as_view(), name='edit-cash'),
    # export
    path('export-xls-tameiakes/', views.Export_data, name='export_data'),
    path('export-data/', views.export_data_as_excel, name='export_data_client'),
]