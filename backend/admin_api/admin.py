from django.contrib import admin
from . models import District,City,Cityenquery
# Register your models here.

class DistrictAdmin(admin.ModelAdmin):
    list_display = ('id','district')

class CityAdmin(admin.ModelAdmin):
    list_display = ('id','city','district')

class CityenqueryAdmin(admin.ModelAdmin):
    list_display = ('id','cityenqueryname','district','email')

admin.site.register(District,DistrictAdmin)
admin.site.register(City,CityAdmin)

admin.site.register(Cityenquery,CityenqueryAdmin)