from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny,IsAuthenticated,IsAdminUser
from user_api.models import User
from user_api.authentication import JWTUserAuthentication
from vendor_api.models import Vendor
from user_api.serializers import UserSerializer
from vendor_api.serializers import VendorSerializer
from . serializers import UpdateVendorSerializer,UpdateUserSerializer
from rest_framework.response import Response
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