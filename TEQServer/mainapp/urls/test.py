from django.urls import path

from mainapp.views import test

urlpatterns = [
    path("tests/", test.TestListAPIView.as_view(), name="get-tests"),
    path("test/", test.TestCreateAPIView.as_view(), name="create-test"),
    path("test/<str:pk>/", test.TestRetrieveUpdateDestroyAPIView.as_view(), name="update-retrieve-destroy-test"),
    path("test/item/", test.ItemCreateAPIView.as_view(), name="add-item"),
]
