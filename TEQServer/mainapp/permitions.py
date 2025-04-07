from rest_framework.permissions import IsAuthenticated

from mainapp.models.test import Test, TestMember


class IsTestOwner(IsAuthenticated):
    def has_permission(self, request, view):
        if not super().has_permission(request, view):
            return False

        test_id = view.kwargs.get("pk")
        if not test_id and request.method in ("POST", "PUT", "PATCH"):
            test_id = request.data.get("testId")

        if not test_id:
            return False

        test = Test.objects.filter(id=test_id, owner=request.user).first()
        
        return test is not None

class IsTestMember(IsAuthenticated):
    def has_permission(self, request, view):
        if not super().has_permission(request, view):
            return False

        test_id = view.kwargs.get("test_id")
        if not test_id:
            return False

        test = TestMember.objects.filter(test__id=test_id, user=request.user).first()
        return test is not None
