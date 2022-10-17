from django.urls import path
from .views import pageForm, index, checkForm

urlpatterns = [
    path('<int:idAgent>/', pageForm),
    path('checkForm/', checkForm, name='checkForm'),
    path('', index),
]
