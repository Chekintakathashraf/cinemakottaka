
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

    path('getcityenquery/',views.GetCityenqueryView.as_view(),name='getcityenquery'),
    path('approvecityenquery/<int:id>/',views.ApproveCityenqueryView.as_view(),name='approvecityenquery'),


    path('addcategory/',views.AddCategoryView.as_view(),name='addcategory'),

    path('tmdbnowplayingmovies/',views.TMDBNowplayingMovies.as_view(),name='tmdbnowplayingmovies'),
    
    path('addmovie/',views.AddMoviesView.as_view(),name='addmovie'),
    path('blockmovie/<int:id>/',views.BlockMovie.as_view(),name='blockmovie'),
    path('updatemovie/<int:id>/',views.UpdateMovie.as_view(),name='updatemovie'),
]