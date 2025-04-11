from django.urls import path, include

urlpatterns = [
    path("", include("mainapp.urls.test")),
    path("", include("mainapp.urls.answer")),
]
