from rest_framework import serializers
from django.contrib.auth.models import User

from userapp.models import UserProfile
from utility.case_serializers import CamelCaseSerializer


class UserRegistrationSerializer(CamelCaseSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    fullname = serializers.CharField(max_length=255)

    def validate_email(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("A user with this email already exists.")
        return value

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["email"],
            password=validated_data["password"],
        )

        UserProfile.objects.create(user=user, fullname=validated_data["fullname"])
        return user

class UserLoginSerializer(CamelCaseSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

class UserProfileSerializer(serializers.ModelSerializer):
    email = serializers.CharField(source="username", read_only=True)
    fullname = serializers.CharField(source="userprofile.fullname", read_only=True)

    class Meta:
        model = User
        fields = ["id", "fullname", "email"]
