from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RouteSerializer,UserSignupDeatails
from rest_framework_simplejwt.tokens import RefreshToken
from .models import  UserSignup




class RegisterView(APIView):
    def post(self, request):
        serializer = RouteSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            
            # Generate a JWT token for the user
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)

            return Response(
                {
                    'msg': 'Registration successful',
                    'token': access_token
                },
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class UserSignupView(APIView):
    def get(self,request):
        users =  UserSignup.objects.all()
        serializer = UserSignupDeatails(users,many=True)
        return Response(
            {'users':serializer.data},
            status=status.HTTP_200_OK
        )


        

       
