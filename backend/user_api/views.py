from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny,IsAuthenticated,IsAdminUser
from .models import User
from .serializers import UserSerializer,VerifyOtpSerializer
from rest_framework.response import Response
from rest_framework import status
from . import verify
from .verify import send,check


import datetime
from django.contrib import auth
from . authentication import JWTUserAuthentication,create_access_token,create_refresh_token,decode_refresh_token
from . models import UserToken
from rest_framework import exceptions

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

class LoginUserAPIView(APIView):
    def post(self, request):
        phone_number = request.data['phone_number']
        password = request.data['password']

        user = User.objects.filter(phone_number=phone_number).first()
        print(user)
        if user is None:
            response = Response()
           
            response.data={
                'message':'Invalid phone_number'
            }
            return response

        if not user.check_password(password):
            response = Response()
           
            response.data={
                'message':'invalid password'
            }
            return response

        # user = auth.authenticate(phone_number=phone_number, password=password)
        # print(user)
        if user:
            access_token = create_access_token(user.id)
            refresh_token = create_refresh_token(user.id)

            UserToken.objects.create(
                user_id=user.id,
                token=refresh_token,
                expired_at=datetime.datetime.utcnow() + datetime.timedelta(days=7)
            )

            response = Response()
            
            response.set_cookie(key='refresh_token',value=refresh_token,httponly=True)
            response.data = {
                'token': access_token,
                'admin': user.is_admin,
                
            }
            return response
        else:
            response = Response()
            response.data={
                'message':'Not verifiede'
            }
            return response  


class RefreshUserAPIView(APIView):
    def post(self, request):
        refresh_token = request.COOKIES.get('refresh_token')
        id = decode_refresh_token(refresh_token)
        print(refresh_token)
        if not  UserToken.objects.filter(
            user_id=id,
            token=refresh_token,
            expired_at__gt=datetime.datetime.now(tz=datetime.timezone.utc)
        ).exists():
            raise exceptions.AuthenticationFailed('You are unauthenticated')

        access_token = create_access_token(id)
        print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
        print(access_token)
        print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
        return Response({
            'token':access_token
        })


class UserAPIView(APIView):
    authentication_classes = [JWTUserAuthentication]
    def get(self,request):
        return Response(UserSerializer(request.user).data)


class LogoutUserAPIView(APIView):
    def post(self, request):
        refresh_token=request.COOKIES.get('refresh_token')
        print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')
        print(refresh_token)
        print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')
        UserToken.objects.filter(token=refresh_token).delete()
        
        response = Response()
        response.delete_cookie(key='refresh_token')
        response.data={
            'message':'Now you are logout'
        }
        return response

    