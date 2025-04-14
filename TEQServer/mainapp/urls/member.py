from django.urls import path

from mainapp.views.member import MemberCreateAPIView, MemberListAPIView, MemberDestroyAPIView

urlpatterns = [
    path("member/<str:test_id>/add", MemberCreateAPIView.as_view()),
    path("members/<str:test_id>", MemberListAPIView.as_view()),
    path("member/<int:pk>", MemberDestroyAPIView.as_view()),
]
