from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny,IsAuthenticated,IsAdminUser
from user_api.models import User
from user_api.authentication import JWTUserAuthentication
from vendor_api.models import Vendor
from user_api.serializers import UserSerializer
from vendor_api.serializers import VendorSerializer
from . serializers import UpdateVendorSerializer,UpdateUserSerializer,DistrictSerializer,CitySerializer
from . models import District,City
from rest_framework.response import Response

from django.core.mail import send_mail

# Create your views here.

class VerifyVendor(APIView):
    permission_classes=[IsAdminUser]
    authentication_classes = [JWTUserAuthentication]
    def patch(self, request,id):
        
        details = Vendor.objects.get(id=id)
        details.is_active=True
        print(details.is_active)
        serializer = UpdateVendorSerializer(details,data=request.data,partial = True)
        if serializer.is_valid():
            serializer.save()

            print('-------------------')
            print(details.email)
            print('---------------')

            mailingemail= details.email
            print(mailingemail)
            
            send_mail('Hello  ',
            'Congratulations, your Vender application is approved.',
            'ashrafchekintakath@gmail.com'
            ,[mailingemail]   
            ,fail_silently=False)


            print("Vendor verified Successfully")
            return Response(serializer.data)
        else:
            print("Vendor verification failed")
            print(serializer.errors)
            return Response(serializer.errors)

class BlockVendor(APIView):
    permission_classes=[IsAdminUser]
    authentication_classes = [JWTUserAuthentication]
    def patch(self, request,id):
        details = Vendor.objects.get(id=id)
        if details.is_Vendor==True:
            details.is_active=False
            details.is_Vendor=False
        else:
            details.is_Vendor=True
        print(details.is_active)
        serializer = UpdateUserSerializer(details,data=request.data,partial = True)
        if serializer.is_valid():
            serializer.save()
            print("Vendor action Successfully")
            return Response(serializer.data)
        else:
            print("Vendor action failed")
            print(serializer.errors)
            return Response(serializer.errors)

class BlockUser(APIView):
    permission_classes=[IsAdminUser]
    authentication_classes = [JWTUserAuthentication]
    def patch(self, request,id):
        details = User.objects.get(id=id)
        if details.is_active==True:
            details.is_active=False
        else:
            details.is_active=True
        print(details.is_active)
        serializer = UpdateUserSerializer(details,data=request.data,partial = True)
        if serializer.is_valid():
            serializer.save()
            print("vender action Successfully")
            return Response(serializer.data)
        else:
            print("Vendor action failed")
            print(serializer.errors)
            return Response(serializer.errors)

class GetUserDetailsView(APIView):
    permission_classes=[IsAdminUser]
    authentication_classes = [JWTUserAuthentication]
    serializer_classes = UserSerializer
    def get(self, request,id):
        try:
            user = User.objects.get(id=id)
            serializer = UserSerializer(user,many=False)   
            return Response(serializer.data)
        except:
            message = {'message':'No User with this id already exist'}
            return Response(message)

class GetUsersView(APIView):
    permission_classes=[IsAdminUser]
    authentication_classes = [JWTUserAuthentication]
    serializer_classes = UserSerializer
    def get(self, request):
    
        users = User.objects.all()
        serializer = UserSerializer(users,many=True)   
        return Response(serializer.data)

class GetVendorDetailsView(APIView):
    permission_classes=[IsAdminUser]
    authentication_classes = [JWTUserAuthentication]
    serializer_classes = UserSerializer
    def get(self, request,id):
        try:
            vendor = Vendor.objects.get(id=id)
            serializer = VendorSerializer(vendor,many=False)   
            return Response(serializer.data)
        except:
            message = {'message':'No User with this id already exist'}
            return Response(message)

class GetVendorsView(APIView):
    permission_classes=[IsAdminUser]
    authentication_classes = [JWTUserAuthentication]
    serializer_classes = VendorSerializer
    def get(self, request):
    
        vendors = Vendor.objects.all()
        serializer = VendorSerializer(vendors,many=True)   
        return Response(serializer.data)

class AddDistrictView(APIView):
    permission_classes=[IsAdminUser]
    authentication_classes = [JWTUserAuthentication]
    serializer_classes = DistrictSerializer
    def post(self,request):
        data = request.data
        serializer = self.serializer_classes(data=data)
        if serializer.is_valid():
            serializer.save()
            
            print(serializer.data)
            
            response={
                "data" : serializer.data
            }
            return Response(response)
        else:
            print(serializer.errors)
            return Response(serializer.errors)

class AddCityView(APIView):
    permission_classes=[IsAdminUser]
    authentication_classes = [JWTUserAuthentication]
    serializer_classes = CitySerializer
    def post(self,request):
        data = request.data
        serializer = self.serializer_classes(data=data)
        if serializer.is_valid():
            serializer.save()
            
            print(serializer.data)
            
            response={
                "data" : serializer.data
            }
            return Response(response)
        else:
            print(serializer.errors)
            return Response(serializer.errors)

class UpdateDistrictView(APIView):
    permission_classes=[IsAdminUser]
    authentication_classes = [JWTUserAuthentication]
    def get(self, request,id):
        details = District.objects.get(id=id)
        serializer = DistrictSerializer(details,context={'request': request})
        return Response(serializer.data)
    def put(self, request,id):
        print(request.body)
        details = District.objects.get(id=id)
        serializer = DistrictSerializer(details,data=request.data,)
        if serializer.is_valid():
            print(serializer.validated_data)
            serializer.save()
            print("Update district successfully updated")
            return Response(serializer.data)
        else:
            print("Update district failed")
            return Response(serializer.errors)    
    def delete(self, request,id):
        details = District.objects.get(id=id)
        details.delete()
        return Response({'message':'District deleted'})
    def patch(self, request,id):
        details = District.objects.get(id=id)
        serializer = DistrictSerializer(details,data=request.data,partial = True)
        if serializer.is_valid():
            print(serializer.validated_data)
            serializer.save()
            print("Update district successfully updated")
            return Response(serializer.data)
        else:
            print("Update district failed")
            print(serializer.errors)
            return Response(serializer.errors)

class UpdateCityView(APIView):
    permission_classes=[IsAdminUser]
    authentication_classes = [JWTUserAuthentication]
    def get(self, request,id):
        details = City.objects.get(id=id)
        serializer = CitySerializer(details,context={'request': request})
        return Response(serializer.data)
    def put(self, request,id):
        print(request.body)
        details = City.objects.get(id=id)
        serializer = CitySerializer(details,data=request.data,)
        if serializer.is_valid():
            print(serializer.validated_data)
            serializer.save()
            print("Update city successfully updated")
            return Response(serializer.data)
        else:
            print("Update city failed")
            return Response(serializer.errors)    
    def delete(self, request,id):
        details = City.objects.get(id=id)
        details.delete()
        return Response({'message':'City deleted'})
    def patch(self, request,id):
        details = City.objects.get(id=id)
        serializer = CitySerializer(details,data=request.data,partial = True)
        if serializer.is_valid():
            print(serializer.validated_data)
            serializer.save()
            print("Update city successfully updated")
            return Response(serializer.data)
        else:
            print("Update city failed")
            print(serializer.errors)
            return Response(serializer.errors)

class GetDistrictsView(APIView):
    permission_classes=[IsAdminUser]
    authentication_classes = [JWTUserAuthentication]
    def get(self, request):
    
        districts = District.objects.all()
        serializer = DistrictSerializer(districts,many=True)   
        return Response(serializer.data)

class GetCitiesView(APIView):
    permission_classes=[IsAdminUser]
    authentication_classes = [JWTUserAuthentication]
    def get(self, request):
    
        cities = City.objects.all()
        serializer = CitySerializer(cities,many=True)   
        return Response(serializer.data)