from rest_framework.generics import RetrieveAPIView

from mainapp.models.test import Test
from mainapp.permitions import CanAccessTest
from mainapp.serializers.answer import TestSerializer


class TestRetrieveApiView(RetrieveAPIView):
    serializer_class = TestSerializer
    queryset = Test.objects.all()
    model = Test
    permission_classes = [CanAccessTest]