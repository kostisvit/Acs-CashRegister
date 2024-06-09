from django.urls import path
from . import views
from .views import CashExport,Export_data,export_data_as_excel,CustomerFormView,FileListView,FileUploadView,CustomerListView,external_api_view,download_json_api_customer






urlpatterns = [
    path('cash/api/customers', CustomerListView.as_view(), name='customer'),
    path('cash/api/customer/new', CustomerFormView.as_view(), name='customer-new'),
    path('cash/', views.TameiakiFilterView.as_view(), name='tameiaki'),
    path('cash/new', views.CreatePostView.as_view(), name='new-cash'),
    path('cash/files', views.FileListView.as_view(), name='files'),
    path('cash/upload-fille/', FileUploadView.as_view(), name='file_upload'),
    # update
    path('cash/cash/update/<uuid:pk>', views.CashUpdateView.as_view(), name='edit-cash'),
    # export
    path('cash/cash/export', views.Export_data, name='export_data'),
    path('cash/api/customers/export', views.export_data_as_excel, name='export_data_client'),
    path('cash/api/customers/export/json', views.download_json_api_customer, name='export_json'),
    # api search
    path('cash/external-api/', external_api_view, name='external-api'),
]