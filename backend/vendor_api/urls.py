
from django.urls import path
from . import views
urlpatterns = [
    path('register/',views.VendorRegister.as_view(),name='register'),
    path('loginvendor/',views.LoginVendorAPIView.as_view(),name='loginvendor'),
    path('refreshvendor/',views.RefreshVendorAPIView.as_view(), name="refreshvendor"),
    path('vendor/',views.VendorAPIView.as_view(),name='vendor'),
    path('logoutvendor/',views.LogoutVendorAPIView.as_view(),name='logoutvendor'),


    path('addshowtime/',views.AddShowTime.as_view(),name='addshowtime'),
    path('addshowdate/',views.AddShowDate.as_view(),name='addshowdate'),
    
    path('addscreen/',views.AddScreen.as_view(),name='addscreen'),
    path('updatescreen/<int:id>/',views.UpdateScreen.as_view(),name='updatescreen'),
]