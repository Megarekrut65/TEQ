from django.urls import path, include

urlpatterns = [
    path("", include("mainapp.urls.test")),
    path("", include("mainapp.urls.answer")),
    path("", include("mainapp.urls.member")),
    path("", include("mainapp.urls.pool")),
]
