from django.contrib import admin
from . models import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class CustomUserAdmin(UserAdmin):
    list_display = ('id','username','phone_number','district','city','last_login','date_joined','is_active')
    readonly_fields = ('last_login', 'date_joined')
    ordering = ('id',)
    

admin.site.register(User,CustomUserAdmin)