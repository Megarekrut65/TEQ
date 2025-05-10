from django.urls import path

from mainapp.views.answer import TestRetrieveApiView, AnswerCreateApiView, AnswerRetrieveApiView, AnswerListApiView, \
    TestAnswerListApiView, LastAnswerRetrieveApiView, AnswerItemUpdateAPIView, AnswerCheckUpdateAPIView, \
    AnswerAgreeUpdateAPIView

urlpatterns = [
    path("test/<str:pk>/view", TestRetrieveApiView.as_view()),
    path("test/<str:test_id>/pass", AnswerCreateApiView.as_view()),
    path("answer/<str:pk>", AnswerRetrieveApiView.as_view()),
    path("answer/<str:pk>/last", LastAnswerRetrieveApiView.as_view()),
    path("answers/", AnswerListApiView.as_view()),
    path("answers/test/<str:test_id>/", TestAnswerListApiView.as_view()),
    path("answer/item/<int:index>/<str:pk>/", AnswerItemUpdateAPIView.as_view()),
    path("answer/check/<str:pk>/", AnswerCheckUpdateAPIView.as_view()),
    path("answer/agree/<str:pk>/", AnswerAgreeUpdateAPIView.as_view()),
]
