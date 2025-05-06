from django.urls import path

from mainapp.views import test

urlpatterns = [
    path("tests/", test.TestListAPIView.as_view()),
    path("public/tests/", test.PublicTestListAPIView.as_view()),
    path("test/", test.TestCreateAPIView.as_view()),
    path("test/<str:pk>/", test.TestRetrieveUpdateDestroyAPIView.as_view()),
    path("test/item/<str:pk>/", test.ItemCreateAPIView.as_view()),
    path("test/item/<int:index>/<str:pk>/", test.ItemUpdateDestroyAPIView.as_view()),
]
