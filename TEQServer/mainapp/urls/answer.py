from django.urls import path

from mainapp.views.answer import TestRetrieveApiView, AnswerCreateApiView, AnswerRetrieveApiView, AnswerListApiView

urlpatterns = [
    path("test/<str:pk>/view", TestRetrieveApiView.as_view()),
    path("test/<str:test_id>/pass", AnswerCreateApiView.as_view()),
    path("answer/<str:pk>", AnswerRetrieveApiView.as_view()),
    path("answers", AnswerListApiView.as_view()),
]
