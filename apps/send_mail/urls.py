from django.urls import path
from .views import compose_email
from . import views


urlpatterns = [
    path('email/send/', views.compose_email, name='send_mail')
]