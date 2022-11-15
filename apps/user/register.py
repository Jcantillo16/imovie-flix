from .serializer import UserSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User


class UserRegister(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLogin(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        try:
            user = User.objects.get(email=email, password=password)
            user.is_login = True
            user.save()
            return Response({'message': 'Login Successful'}, status=status.HTTP_200_OK)
        except:
            return Response({'message': 'Login Failed'}, status=status.HTTP_400_BAD_REQUEST)


class UserLogout(APIView):
    def post(self, request):
        email = request.data.get('email')
        try:
            user = User.objects.get(email=email)
            if user.is_login:
                user.is_login = False
                user.save()
                return Response({'message': 'Logout Successful'}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'User is already logged out'}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'message': 'Logout Failed, user not exist'}, status=status.HTTP_400_BAD_REQUEST)
