from django.contrib import admin
from . models import District,City
# Register your models here.

class DistrictAdmin(admin.ModelAdmin):
    list_display = ('id','district')

class CityAdmin(admin.ModelAdmin):
    list_display = ('id','city','district')

admin.site.register(District,DistrictAdmin)
admin.site.register(City,CityAdmin)