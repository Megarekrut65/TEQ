from django.http import JsonResponse
from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated

from mainapp.models.test import Test, TestItem
from mainapp.permitions import IsTestOwner
from mainapp.serializers.test import TestSerializer, ItemSerializer


class TestListAPIView(ListAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    permission_classes = [IsAuthenticated]

class TestCreateAPIView(CreateAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        test = serializer.save(owner=self.request.user)
        TestItem(id=test.id).save()

class TestRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        item = TestItem.objects.filter(id=instance.id).first()
        if item is None:
            return JsonResponse({"detail": "Test not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(instance)
        data = serializer.data
        data["items"] = item.items

        return JsonResponse(data, status=status.HTTP_200_OK)


class ItemCreateAPIView(CreateAPIView):
    serializer_class = ItemSerializer
    permission_classes = [IsTestOwner]
