from django.urls import path
from . import views




urlpatterns = [
    path('cash-register/customer-api', views.customers, name='customer'),
    path('cash-register/tameiaki', views.tameiaki, name='tameiaki'),
    path('cash-register/new-cash', views.CreatePostView.as_view(), name='new-cash'),
]