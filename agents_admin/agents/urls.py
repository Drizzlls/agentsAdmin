from django.urls import path, include
from .views import AddAgentForDirection, EducationAgentForDirection, AddAgentForClient, EducationAgentForClient


urlpatterns = [
    path('agent/registration/', AddAgentForDirection.as_view()),
    path('agent/education/', EducationAgentForDirection.as_view()),
    path('clients/registration/',  AddAgentForClient.as_view()),
    path('clients/education/', EducationAgentForClient.as_view()),
]
