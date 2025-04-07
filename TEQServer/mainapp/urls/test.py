from django.urls import path

from mainapp.views import test

urlpatterns = [
    path("tests/", test.TestListAPIView.as_view()),
    path("test/", test.TestCreateAPIView.as_view()),
    path("test/<str:pk>/", test.TestRetrieveUpdateDestroyAPIView.as_view()),
    path("item/", test.ItemCreateAPIView.as_view()),
    path("item/<int:index>/<str:pk>", test.ItemUpdateDestroyAPIView.as_view()),
]
