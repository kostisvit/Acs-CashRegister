from django.urls import path
from . import views


urlpatterns = [
    path('email/', views.compose_email, name='send_mail')
]