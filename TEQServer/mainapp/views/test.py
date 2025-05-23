from django.db.models import Count
from django.http import JsonResponse
from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated

from mainapp.models.test import Test, TestDocument
from mainapp.permitions import IsTestOwner, CanAccessTest
from mainapp.serializers.safe_test import PassTestSerializer
from mainapp.serializers.test import TestSerializer, ItemSerializer


class TestListAPIView(ListAPIView):
    serializer_class = TestSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Test.objects.filter(owner=self.request.user).order_by("-id")

class TestCreateAPIView(CreateAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        test = serializer.save(owner=self.request.user)
        TestDocument(id=test.id).save()

class TestRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    permission_classes = [IsTestOwner]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        item = TestDocument.objects.filter(id=instance.id).first()
        if item is None:
            return JsonResponse({"detail": "Test not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(instance)
        data = serializer.data

        return JsonResponse(data, status=status.HTTP_200_OK)


class ItemCreateAPIView(CreateAPIView):
    serializer_class = ItemSerializer
    permission_classes = [IsTestOwner]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["test_id"] = self.kwargs["pk"]

        return context

class ItemUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ItemSerializer
    permission_classes = [IsTestOwner]
    queryset = TestDocument.objects.all()

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["index"] = self.kwargs["index"]
        return context

    def get_object(self):
        return TestDocument.objects.get(pk=self.kwargs["pk"])

    def destroy(self, request, *args, **kwargs):
        test_id = self.kwargs["pk"]
        test = TestDocument.objects.get(id=test_id)

        index = self.kwargs["index"]

        if index >= len(test.items):
            return JsonResponse({"detail": "Index out of range"}, status=status.HTTP_400_BAD_REQUEST)

        test.items.remove(test.items[index])
        test.save()

        return JsonResponse({"detail": "Item removed"}, status=status.HTTP_200_OK)


class PublicTestListAPIView(ListAPIView):
    model = Test
    serializer_class = PassTestSerializer

    def get_queryset(self):
        queryset = Test.objects.filter(is_public=True)
        category = self.request.GET.get("category")
        if category:
            queryset = queryset.filter(category=category)

        return queryset.order_by("-answer_count", "-id")