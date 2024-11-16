from django.urls import path

from mainapp.views import test

urlpatterns = [
    path("test/", test.TestCreateAPIView.as_view(), name="create-test"),
]
