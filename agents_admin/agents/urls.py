from django.urls import path, include
from .views import agentRegistration,wasTrained


urlpatterns = [
    path('', agentRegistration),
    path('registration/', agentRegistration),
    path('education/', wasTrained),
]
