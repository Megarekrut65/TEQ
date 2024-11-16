from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from mainapp.models.test import Test, TestItem
from mainapp.serializers.test import TestSerializer, ItemSerializer


class TestCreateAPIView(CreateAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        test = serializer.save(owner=self.request.user.userprofile)
        TestItem(id=test.id).save()


class ItemView(CreateAPIView):
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]
