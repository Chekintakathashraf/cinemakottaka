
from django.urls import path
from . import views
urlpatterns = [
    path('verifyvendor/<int:id>/',views.VerifyVendor.as_view(),name='verifyvendor'),
    path('blockvendor/<int:id>/',views.BlockVendor.as_view(),name='blockvendor'),
    path('getvendordetails/<int:id>/',views.GetVendorDetailsView.as_view(),name='getvendordetails'),
    path('getvendors/',views.GetVendorsView.as_view(),name='getvendorss'),

    
    path('blockuser/<int:id>/',views.BlockUser.as_view(),name='blockuser'),
    path('getuserdetails/<int:id>/',views.GetUserDetailsView.as_view(),name='getuserdetails'),
    path('getusers/',views.GetUsersView.as_view(),name='getusers'),

    path('adddistrict/',views.AddDistrictView.as_view(),name='adddistrict'),
    path('updatedistrict/<int:id>/',views.UpdateDistrictView.as_view(),name='updatedistrict'),
    path('getdistricts/',views.GetDistrictsView.as_view(),name='getdistricts'),

    path('addcity/',views.AddCityView.as_view(),name='addcity'),
    path('updatecity/<int:id>/',views.UpdateCityView.as_view(),name='updatecity'),
    path('getcities/',views.GetCitiesView.as_view(),name='getcities'),
]