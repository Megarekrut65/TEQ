from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView

from similarity_app.algorithms.fine_tuned_similarity_model import get_similarity
from similarity_app.serializers import SimilaritySerializer


class CalculateSimilarityAPIView(APIView):
    serializer_class = SimilaritySerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data

        similarity = get_similarity(data["text1"], data["text2"])

        return JsonResponse({"similarity": similarity}, status=status.HTTP_200_OK)