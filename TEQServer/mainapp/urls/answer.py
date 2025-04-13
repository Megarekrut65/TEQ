from django.urls import path

from mainapp.views.answer import TestRetrieveApiView, AnswerCreateApiView, AnswerRetrieveApiView

urlpatterns = [
    path("test/<str:pk>/view", TestRetrieveApiView.as_view()),
    path("test/<str:test_id>/pass", AnswerCreateApiView.as_view()),
    path("answer/<str:pk>", AnswerRetrieveApiView.as_view()),
]
