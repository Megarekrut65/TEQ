from rest_framework import serializers

from mainapp.models.test import TestMember
from userapp.serializers import UserProfileSerializer
from utility.case_serializers import CamelCaseModelSerializer, CamelCaseSerializer


class MemberSerializer(CamelCaseModelSerializer):
    user = UserProfileSerializer(read_only=True, source="user.userprofile")

    class Meta:
        model = TestMember
        fields = ["id","user"]

class MemberListSerializer(CamelCaseSerializer):
    emails = serializers.ListField(child=serializers.EmailField())