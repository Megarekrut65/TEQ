from django.urls import path, include

urlpatterns = [
    path("", include("mainapp.urls.user")),
    path("", include("mainapp.urls.test")),
]
