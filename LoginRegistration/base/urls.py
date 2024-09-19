from django.urls import path, include
from .views import authView, home, registration_success

urlpatterns = [
    path("", home, name="home"),
    path("signup/", authView, name="authView"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("registration-success/", registration_success, name="registration_success"),
]