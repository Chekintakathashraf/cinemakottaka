from django.contrib import admin
from .  models import Vendor
# Register your models here.

class VendorAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','email','is_active')

admin.site.register(Vendor,VendorAdmin)