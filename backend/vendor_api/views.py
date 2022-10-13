import email
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .serializers import VendorSerializer
from .models import Vendor,VendorToken
from rest_framework.response import Response
from rest_framework import status

import datetime
from . authentication import JWTVendorAuthentication,create_access_token,create_refresh_token,decode_refresh_token

from rest_framework import exceptions
from django.contrib.auth.hashers import check_password



# Create your views here.

class VendorRegister(APIView):
    permission_classes=[AllowAny]
    serializer_classes =VendorSerializer
    
    def post(self, request):
        data = request.data
        
        serializer = self.serializer_classes(data=data)

        if serializer.is_valid():
            serializer.save()
            print('*****************************')
            print(serializer.data)
            print('*****************************')

            print('*****************************')
            response={
                "data" : serializer.data
            }
            

            return Response(data= response, status = status.HTTP_201_CREATED)
        
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class LoginVendorAPIView(APIView):
    def post(self, request):
        email = request.data['email']
        givenpassword = request.data['password']
        print('*****************************')
        print(email,'---------',givenpassword)
        print('*****************************')
        
        vendor = Vendor.objects.filter(email=email).first()
        print(vendor,"123")
        if vendor is None:
            response = Response()
           
            response.data={
                'message':'Invalid email'
            }
            return response


        storedpassword = str(vendor.password)

        print(givenpassword,'jjjj',storedpassword)

        ans = check_password(givenpassword, storedpassword)
        print(ans)


        if  not check_password(givenpassword, storedpassword) :
            response = Response()
            response.data={
               'message':'Password Inncorect'
            }
            return response  

        if vendor.is_active:
            access_token = create_access_token(vendor.id)
            refresh_token = create_refresh_token(vendor.id)

            VendorToken.objects.create(
                vendor_id = vendor.id,
                token= refresh_token,
                expired_at =  datetime.datetime.utcnow()+datetime.timedelta(seconds=7),
            )

            response = Response()
            
            response.set_cookie(key='refresh_token',value=refresh_token,httponly=True)
            response.data = {
                'token': access_token,
                
            }
            return response
        else:
            response = Response()
            response.data={
                'message':'Not verifiede vendor'
            }
            return response  

class RefreshVendorAPIView(APIView):
    def post(self, request):
        refresh_token = request.COOKIES.get('refresh_token')
        id = decode_refresh_token(refresh_token)
        print(refresh_token)
        print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')
        datas = VendorToken.objects.all()
        print(datas)
        print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')
        print(' ')
        print(' ')
        print(id)
        print(' ')
        print(refresh_token)
        print(' ')
        if not  VendorToken.objects.filter(
            vendor_id=id,
            token=refresh_token,
            # expired_at__gt=datetime.datetime.now(tz=datetime.timezone.utc)
        ).exists():
            print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
            
            raise exceptions.AuthenticationFailed('You are unauthenticated')

        access_token = create_access_token(id)
        print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
        print(access_token)
        print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
        return Response({
            'token':access_token
        })


class LogoutVendorAPIView(APIView):
    def post(self, request):
        refresh_token=request.COOKIES.get('refresh_token')
        VendorToken.objects.filter(token=refresh_token).delete()
        response = Response()
        response.delete_cookie(key='refresh_token')
        response.data={
            'message':'logout'
        }
        return response 



class VendorAPIView(APIView):
    authentication_classes = [JWTVendorAuthentication]
    def get(self, request):
        print(request)
        print('koooooooooooooooooooyyyyyyyyyyyyyyy')
        vendor=request.user
        print(vendor)
        print('koooooooooooooooooooyyyyyyyyyyyyyyy')
        vendors=Vendor.objects.get(email=vendor.email)
        serializer=VendorSerializer(vendors,many=False)
        return Response(serializer.data)