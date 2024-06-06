from django.urls import path
from . import views
from .views import CashExport,Export_data,export_data_as_excel,CustomerFormView,FileListView,FileUploadView,CustomerListView,external_api_view






urlpatterns = [
    path('cash-register/api/customers', CustomerListView.as_view(), name='customer'),
    path('cash-register/api/customer/new', CustomerFormView.as_view(), name='customer-new'),
    path('cash-register/cash', views.TameiakiFilterView.as_view(), name='tameiaki'),
    path('cash-register/cash/new', views.CreatePostView.as_view(), name='new-cash'),
    path('cash-register/files', views.FileListView.as_view(), name='files'),
    path('cash-register/upload-fille/', FileUploadView.as_view(), name='file_upload'),
    # update
    path('cash-register/cash/update/<uuid:pk>', views.CashUpdateView.as_view(), name='edit-cash'),
    # export
    path('cash-register/cash/export', views.Export_data, name='export_data'),
    path('cash-register/api-customers/export', views.export_data_as_excel, name='export_data_client'),
    # api search
    path('external-api/', external_api_view, name='external-api'),
]