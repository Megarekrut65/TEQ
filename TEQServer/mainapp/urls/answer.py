from django.urls import path

from mainapp.views.answer import TestRetrieveApiView

urlpatterns = [
    path("test/<str:pk>/view", TestRetrieveApiView.as_view()),
]
