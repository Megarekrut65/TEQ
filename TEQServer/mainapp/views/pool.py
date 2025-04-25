from django.http import JsonResponse
from rest_framework import status
from rest_framework.generics import RetrieveAPIView, CreateAPIView, UpdateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from mainapp.models.pool import TestPool, TestCategory
from mainapp.serializers.pool import PoolSerializer, CategorySerializer, ItemSerializer


class PoolRetrieveAPIView(RetrieveAPIView):
    serializer_class = PoolSerializer
    queryset = TestPool.objects.all()
    model = TestPool
    permission_classes = [IsAuthenticated]

    def get_object(self):
        pool = TestPool.objects.filter(owner=self.request.user).first()
        if pool is None:
            pool = TestPool.objects.create(owner=self.request.user)

        return pool

class CategoryCreateAPIView(CreateAPIView):
    serializer_class = CategorySerializer
    model = TestCategory
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        pool = TestPool.objects.filter(owner=self.request.user).first()
        context = super().get_serializer_context()
        context["pool"] = pool

        return context

class CategoryUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    model = TestCategory
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        pool = TestPool.objects.filter(owner=self.request.user).first()
        return TestCategory.objects.filter(pool_id=pool.id)


class ItemCreateAPIView(CreateAPIView):
    serializer_class = ItemSerializer
    model = TestCategory
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        category_id = self.kwargs["category_id"]
        pool = TestPool.objects.filter(owner=self.request.user).first()
        category = TestCategory.objects.filter(id=category_id, pool_id=pool.id).first()

        context = super().get_serializer_context()
        context["category"] = category

        return context

class ItemUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ItemSerializer
    model = TestCategory
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        pool = TestPool.objects.filter(owner=self.request.user).first()
        return TestCategory.objects.filter(pool_id=pool.id)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["index"] = self.kwargs["index"]

        return context

    def destroy(self, request, *args, **kwargs):
        category_id = self.kwargs["pk"]
        category = TestCategory.objects.get(id=category_id)

        index = self.kwargs["index"]

        if index >= len(category.items):
            return JsonResponse({"detail": "Index out of range"}, status=status.HTTP_400_BAD_REQUEST)

        category.items.remove(category.items[index])
        category.save()

        return JsonResponse({"detail": "Item removed"}, status=status.HTTP_200_OK)