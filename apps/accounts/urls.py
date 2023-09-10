from django.urls import path
from .views import CaptchaLoginView,SignUpView


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'), 
]