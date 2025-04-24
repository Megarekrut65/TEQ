from rest_framework.permissions import IsAuthenticated

from mainapp.models.answer import Answer
from mainapp.models.test import Test, TestMember


class IsTestOwner(IsAuthenticated):
    def has_permission(self, request, view):
        if not super().has_permission(request, view):
            return False

        test_id = view.kwargs.get("pk")
        if not test_id and request.method in ("POST", "PUT", "PATCH"):
            test_id = request.data.get("testId")

        if not test_id:
            test_id = view.kwargs.get("test_id")

        if not test_id:
            return False

        test = Test.objects.filter(id=test_id, owner=request.user).first()
        
        return test is not None

class IsAnswerTestOwner(IsAuthenticated):
    def has_permission(self, request, view):
        if not super().has_permission(request, view):
            return False

        answer_id = view.kwargs.get("pk")
        if not answer_id and request.method in ("POST", "PUT", "PATCH"):
            answer_id = request.data.get("answerId")

        if not answer_id:
            answer_id = view.kwargs.get("answer_id")

        if not answer_id:
            return False

        answer = Answer.objects.filter(id=answer_id, test__owner=request.user).first()

        return answer is not None

class IsTestOwnerMember(IsAuthenticated):
    def has_permission(self, request, view):
        if not super().has_permission(request, view):
            return False

        member_id = view.kwargs.get("pk")
        if not member_id:
            return False

        member = TestMember.objects.filter(id=member_id).first()
        if not member:
            return False

        return member.test.owner == request.user

class CanAccessTest(IsAuthenticated):
    def has_permission(self, request, view):
        if not super().has_permission(request, view):
            return False

        test_id = view.kwargs.get("pk")
        if not test_id and request.method in ("POST", "PUT", "PATCH"):
            test_id = request.data.get("testId")

        if not test_id:
            test_id = view.kwargs.get("test_id")

        if not test_id:
            return False

        test = Test.objects.filter(id=test_id).first()
        if not test:
            return False

        if test.is_public:
            return True

        if test.owner == request.user:
            return True

        test = TestMember.objects.filter(test__id=test_id, user=request.user).first()
        return test is not None

class CanAccessAnswer(IsAuthenticated):
    def has_permission(self, request, view):
        if not super().has_permission(request, view):
            return False

        answer_id = view.kwargs.get("pk")
        if not answer_id and request.method in ("POST", "PUT", "PATCH"):
            answer_id = request.data.get("answerId")

        if not answer_id:
            answer_id = view.kwargs.get("answer_id")

        if not answer_id:
            return False

        answer = Answer.objects.filter(id=answer_id).first()
        if not answer:
            return False

        return answer.owner == request.user or answer.test.owner == request.user
