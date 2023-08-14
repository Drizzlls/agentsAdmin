from django.urls import path
from .views import pageForm, index, checkForm, checkFormNew

urlpatterns = [
    path('<int:idAgent>/', pageForm),
    path('checkForm/', checkFormNew, name='checkForm'),
    path('', index),
]
