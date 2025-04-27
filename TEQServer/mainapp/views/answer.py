from rest_framework.generics import RetrieveAPIView, CreateAPIView, ListAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated

from mainapp.models.answer import Answer, AnswerDocument
from mainapp.models.test import Test
from mainapp.permitions import CanAccessTest, CanAccessAnswer, IsTestOwner, IsAnswerTestOwner
from mainapp.serializers.answer import PassTestSerializer, AnswerSerializer, AnswerItemSerializer, \
    AnswerItemGradeSerializer, AnswerCheckSerializer
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


class LastAnswerRetrieveApiView(RetrieveAPIView):
    serializer_class = AnswerSerializer
    model = Answer
    permission_classes = [CanAccessTest]

    def get_object(self):
        test_id = self.kwargs["pk"]
        test = Test.objects.get(pk=test_id)
        return Answer.objects.filter(owner=self.request.user, test=test).order_by("pass_date").last()

class AnswerRetrieveApiView(RetrieveAPIView):
    serializer_class = AnswerSerializer
    model = Answer
    permission_classes = [CanAccessAnswer]

    def get_queryset(self):
        return Answer.objects.filter(owner=self.request.user)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        obj = self.get_object()
        context["is_owner"] = obj.owner == self.request.user

        return context

class AnswerListApiView(ListAPIView):
    serializer_class = AnswerSerializer
    model = Answer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Answer.objects.filter(owner=self.request.user).order_by("-pass_date")

class TestAnswerListApiView(ListAPIView):
    serializer_class = AnswerSerializer
    model = Answer
    permission_classes = [IsTestOwner]

    def get_queryset(self):
        test_id = self.kwargs["test_id"]
        return Answer.objects.filter(test_id=test_id).order_by("pass_date")

class AnswerItemUpdateAPIView(UpdateAPIView):
    serializer_class = AnswerItemGradeSerializer
    permission_classes = [IsAnswerTestOwner]
    queryset = AnswerDocument.objects.all()

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["index"] = self.kwargs["index"]
        context["answer_id"] = self.kwargs["pk"]
        return context

    def get_object(self):
        return AnswerDocument.objects.get(pk=self.kwargs["pk"])

class AnswerUpdateAPIView(UpdateAPIView):
    serializer_class = AnswerCheckSerializer
    permission_classes = [IsAnswerTestOwner]
    queryset = Answer.objects.all()
