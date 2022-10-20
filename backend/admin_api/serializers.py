from rest_framework import serializers
from vendor_api.models import Vendor
from user_api.models import User
from . models import District,City,Cityenquery

class UpdateVendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'
        extra_kwargs = {
            'password' : {'write_only' : True}
        }

class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'password' : {'write_only' : True}
        }

class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = '__all__'

        
class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'
        

class CityenquerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Cityenquery
        fields = '__all__'