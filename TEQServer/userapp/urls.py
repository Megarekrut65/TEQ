from django.urls import path

from userapp import views

urlpatterns = [
    path("register/", views.UserRegistrationView.as_view(), name="register"),
    path("login/", views.UserLoginView.as_view(), name="login"),
]
