from django.urls import path

from mainapp.views import user

urlpatterns = [
    path("register/", user.UserRegistrationView.as_view(), name="register"),
    path("login/", user.UserLoginView.as_view(), name="login"),
]
