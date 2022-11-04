from django.contrib import admin
from . models import User,BokkingTicket
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class CustomUserAdmin(UserAdmin):
    list_display = ('id','username','phone_number','district','city','last_login','date_joined','is_active')
    readonly_fields = ('last_login', 'date_joined')
    ordering = ('id',)

class BokkingTicketAdmin(admin.ModelAdmin):
    list_display = ('id','user','price','show','screen')  

admin.site.register(User,CustomUserAdmin)
admin.site.register(BokkingTicket,BokkingTicketAdmin)