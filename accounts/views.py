from django.shortcuts import render
from django.contrib.auth import get_user_model, authenticate
from django.shortcuts import render
from rest_framework import status, response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import UserSerializer, LoginSerializer
from .service import send_message


User = get_user_model()


class RegisterAPIView(APIView):
    permission_classes = []
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            send_message(user)
            return response.Response(serializer.data,
                                     status=status.HTTP_201_CREATED)
class ActivateUserAccount(APIView):
    def get(self, request, activation_code):
        user = User.objects.get(activation_code=activation_code)
        user.is_active = True
        user.activation_code = ''
        user.save()
        return render(request, 'index.html', locals())

# Create your views here.
class LoginAPIView(TokenObtainPairView):
    serializer_class = LoginSerializer