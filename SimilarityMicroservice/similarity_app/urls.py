from django.urls import path

from similarity_app.views import CalculateSimilarityAPIView

urlpatterns = [
    path('similarity/', CalculateSimilarityAPIView.as_view()),
]