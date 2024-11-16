from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView

from mainapp.models.user import UserProfile
from mainapp.serializers.user import UserLoginSerializer, UserRegistrationSerializer, UserProfileSerializer


def get_user_data(request, user):
    token, _ = Token.objects.get_or_create(user=user)
    profile = UserProfile.objects.get(user=user)
    if profile is None:
        return None

    user_serializer = UserProfileSerializer(instance=profile, context={"request": request})
    data = user_serializer.data
    data["token"] = token.key

    return data


class UserLoginView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data)
        if not serializer.is_valid():
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        username = serializer.validated_data["email"]
        password = serializer.validated_data["password"]

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)

            data = get_user_data(request, user)
            return JsonResponse(data, status=status.HTTP_200_OK)

        return JsonResponse({"detail": "Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED)

class UserRegistrationView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserRegistrationSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        data = get_user_data(request, user)

        return JsonResponse(data, status=status.HTTP_201_CREATED)
