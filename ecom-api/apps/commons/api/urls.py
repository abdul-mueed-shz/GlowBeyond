from django.urls import path
from .views import AuthDetails, LogoutView

urlpatterns = [
    path('set_auth_details', AuthDetails.as_view()),
    path('logout', LogoutView.as_view()),
]
