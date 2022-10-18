from rest_framework import serializers
from vendor_api.models import Vendor
from user_api.models import User

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