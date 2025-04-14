from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView

from mainapp.models.test import TestMember, Test
from mainapp.permitions import IsTestOwner, IsTestOwnerMember
from mainapp.serializers.member import MemberSerializer, MemberListSerializer


class MemberCreateAPIView(CreateAPIView):
    model = TestMember
    permission_classes = [IsTestOwner]
    serializer_class = MemberListSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        test_id =self.kwargs.get("test_id")
        test = Test.objects.get(pk=test_id)

        emails = serializer.validated_data.get("emails")
        not_found = []
        members = []

        for email in emails:
            user = User.objects.filter(username=email).first()
            if user is None:
                not_found.append(email)
                continue

            member = TestMember.objects.filter(user=user, test=test).first()
            if member is None:
                member = TestMember.objects.create(user=user, test=test)
                members.append(member)

        serializer = MemberSerializer(members, many=True)
        data = {
            "members":serializer.data,
            "notFound":not_found
        }

        return JsonResponse(data, status=status.HTTP_201_CREATED)

class MemberListAPIView(ListAPIView):
    permission_classes = [IsTestOwner]
    serializer_class = MemberSerializer
    model = TestMember
    pagination_class = None

    def get_queryset(self):
        test_id =self.kwargs.get("test_id")
        test = Test.objects.get(pk=test_id)

        return TestMember.objects.filter(test=test)

class MemberDestroyAPIView(DestroyAPIView):
    permission_classes = [IsTestOwnerMember]
    model = TestMember
    queryset = TestMember.objects.all()