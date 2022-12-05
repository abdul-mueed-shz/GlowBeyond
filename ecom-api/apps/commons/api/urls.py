from django.urls import path
from .views import AuthDetails

urlpatterns = [
    path('set_auth_details', AuthDetails.as_view()),
]
