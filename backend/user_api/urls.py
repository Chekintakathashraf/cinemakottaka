
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

    path('alldistrict/',views.GetDistrictsView.as_view(),name='alldistrict'),
    path('allcitybydistrict/<int:id>/',views.GetCityByDistrictView.as_view(),name='allcitybydistrict'),
    path('selectlocation/',views.SelectlocationView.as_view(),name='selectlocation'),
    path('getallmoviebycity/',views.AllMovieDetails.as_view(),name='getallmoviebycity'),
    path('getallmoviebycitybylanguage/<int:id>/',views.AllMovieDetailsByLanguage.as_view(),name='getallmoviebycity'),
    path('tmdbmoviedetails/<int:id>/',views.TMDBMovieDetails.as_view(),name='tmdbmoviedetailsbymovieid'),
    path('theater/<int:id>/',views.Theaterofthatmovie.as_view(),name='theater'),
    path('showdate/',views.GetAllShowsDate.as_view(),name='showdate'),
    path('showtime/',views.GetAllTimeDate.as_view(),name='showtime'),

]