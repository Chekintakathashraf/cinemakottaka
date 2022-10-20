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

from django.core.mail import send_mail

from admin_api.models import City,Cityenquery
from admin_api.serializers import CityenquerySerializer

# Create your views here.

# class VendorRegister(APIView):
#     permission_classes=[AllowAny]
#     serializer_classes =VendorSerializer
    
#     def post(self, request):
#         data = request.data
        
#         serializer = self.serializer_classes(data=data)

#         if serializer.is_valid():
#             serializer.save()

#             print(serializer.data)

#             mailingemail=data['email']
#             print(mailingemail)
            
#             send_mail('Hello  ',
#             'Thank You For Registering on CINEMA KOTTAKA ,Your Vendor Application is underprocess ',
#             'ashrafchekintakath@gmail.com'
#             ,[mailingemail]   
#             ,fail_silently=False)

            
#             response={
#                 "data" : serializer.data
#             }
            

#             return Response(data= response, status = status.HTTP_201_CREATED)
        
#         return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class VendorRegister(APIView):
    permission_classes=[AllowAny]
    
    
    def post(self, request):
        data = request.data
        

        print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
        enq=data['city']
        cityvalue = City.objects.get(id=enq)
        print(cityvalue.city)

        print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')

        if cityvalue.city == 'other':
            print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
            print('--------------------------------')
            print(data['cityenqueryname'])
            print(data['email'])
            print('--------------------------------')
            # newcityenquery = Cityenquery.objects.create(
            #     cityenqueryname = data['othercityname'],
            #     email = data['email']

            # )
            # newcityenquery.save()
            # print(newcityenquery)

            serializer = CityenquerySerializer(data=data)
            if serializer.is_valid():
                serializer.save()

                print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')


                response={
                    "data" : "your reuest for new cities has been sent to Admin. We will inform you soon"
                    }
                

                return Response(data= response, status = status.HTTP_201_CREATED)
            return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = VendorSerializer(data=data)

            if serializer.is_valid():
                serializer.save()

                print(serializer.data)

                mailingemail=data['email']
                print(mailingemail)
                
                send_mail('Hello  ',
                'Thank You For Registering on CINEMA KOTTAKA ,Your Vendor Application is underprocess ',
                'ashrafchekintakath@gmail.com'
                ,[mailingemail]   
                ,fail_silently=False)

                
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