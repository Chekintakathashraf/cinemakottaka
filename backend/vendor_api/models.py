from django.db import models
from admin_api.models import District,City
# Create your models here.

class Vendor(models.Model):
    first_name     = models.CharField(max_length=100)
    last_name      = models.CharField(max_length=100)
    email          = models.EmailField(max_length=100, unique=True)
    phone_number   = models.CharField(max_length=10,unique=True)
    password       = models.CharField(max_length=255)

    district       = models.ForeignKey(District,on_delete=models.CASCADE,null=True) 
    city           = models.ForeignKey(City,on_delete=models.CASCADE,null=True) 
    
    create_date    = models.DateTimeField(auto_now_add=True)
    last_login     = models.DateTimeField(auto_now=True)
    modified_date  = models.DateTimeField(auto_now=True)
    is_Vendor      = models.BooleanField(default=True)
    is_Paid        = models.BooleanField(default=False)
    is_active      = models.BooleanField(default=False,blank=True)
    
    def __str__(self):
        return self.email

class VendorToken(models.Model):
    vendor_id = models.IntegerField()
    token = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    expired_at = models.DateTimeField()

    def __str__(self):
        return str(self.vendor_id) +' '+ self.token