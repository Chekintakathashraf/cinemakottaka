from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny,IsAuthenticated,IsAdminUser
from .models import User
from .serializers import UserSerializer,VerifyOtpSerializer
from rest_framework.response import Response
from rest_framework import status
from . import verify
from .verify import send,check
class UserRegister(APIView):
    permission_classes=[AllowAny]
    serializer_classes = UserSerializer
    
    def post(self, request):
        data = request.data
        serializer = self.serializer_classes(data=data)

        if serializer.is_valid():
            serializer.save()
            phone_number=data['phone_number']
            print(phone_number)
            send(phone_number)
            response={
                "data" : serializer.data
            }
            

            return Response(data= response, status = status.HTTP_201_CREATED)
        
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class VerifyUserOtp(APIView):
    def post(self,request):
        try:
            data=request.data
            phone_number=data['phone_number']
            code=data['code']
            if check(phone_number,code):
                print('hello')
                user = User.objects.get(phone_number=phone_number)   
                print(user)       
                user.is_active= True
                user.save()
                serializer = VerifyOtpSerializer(user, many=False)
                return Response(serializer.data)
            else:
                message = {'detail':'otp is not valid'}
                
                return Response(message, status=status.HTTP_400_BAD_REQUEST)
        except:
            message = {'detail':'somthin whent worng'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)