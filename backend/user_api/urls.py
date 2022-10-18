
from django.urls import path
from . import views
urlpatterns = [
    path('register/',views.UserRegister.as_view(),name='register'),
    path('verifyuser/',views.VerifyUserOtp.as_view(),name='verifyuser'),
    path('loginuser/',views.LoginUserAPIView.as_view(),name='loginuser'),
    path('refreshuser/',views.RefreshUserAPIView.as_view(), name="refresh"),
    path('user/',views.UserAPIView.as_view(),name='user'),
    path('logoutuser/',views.LogoutUserAPIView.as_view(),name='logoutuser'),


    path('loginuserwithotp/',views.LoginUserWithOtpAPIView.as_view(),name='loginuserwithotp'),
    path('verifyloginuserotp/',views.VerifyLoginUserOtp.as_view(),name='verifyloginuserotp'),

]