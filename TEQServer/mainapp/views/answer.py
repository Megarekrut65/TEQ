from rest_framework.generics import RetrieveAPIView, CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated

from mainapp.models.answer import Answer, AnswerDocument
from mainapp.models.test import Test
from mainapp.permitions import CanAccessTest, CanAccessAnswer
from mainapp.serializers.answer import PassTestSerializer, AnswerSerializer
from mainapp.test_checker import check_test


class TestRetrieveApiView(RetrieveAPIView):
    serializer_class = PassTestSerializer
    queryset = Test.objects.all()
    model = Test
    permission_classes = [CanAccessTest]

class AnswerCreateApiView(CreateAPIView):
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()
    model = Answer
    permission_classes = [CanAccessTest]

    def perform_create(self, serializer):
        test = Test.objects.get(pk=self.kwargs["test_id"])
        answer = serializer.save(owner=self.request.user, version=test.version, test=test)

        if test.auto_check:
            check_test(answer)


class AnswerRetrieveApiView(RetrieveAPIView):
    serializer_class = AnswerSerializer
    model = Answer
    permission_classes = [CanAccessTest]

    def get_object(self):
        test_id = self.kwargs["pk"]
        test = Test.objects.get(pk=test_id)
        return Answer.objects.filter(owner=self.request.user, test=test).order_by("pass_date").last()

class AnswerListApiView(ListAPIView):
    serializer_class = AnswerSerializer
    model = Answer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Answer.objects.filter(owner=self.request.user).order_by("-pass_date").all()