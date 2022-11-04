from urllib import response
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny,IsAuthenticated,IsAdminUser
from user_api.models import User
from user_api.authentication import JWTUserAuthentication
from vendor_api.models import Vendor
from user_api.serializers import UserSerializer
from vendor_api.serializers import VendorSerializer
from . serializers import UpdateVendorSerializer,UpdateUserSerializer,DistrictSerializer,CitySerializer,CityenquerySerializer,CategorySerializer,MovieSerializer
from . models import District,City,Cityenquery,Movie,Category
from rest_framework.response import Response

from django.core.mail import send_mail
from django.template.defaultfilters import slugify

import requests
from django.conf import settings


from user_api . models import BokkingTicket,BrokerCharge
from user_api . serializers import BookingTicketSerializer,BrokerChargeSerializer
# Create your views here.



class VerifyVendor(APIView):
    permission_classes=[IsAdminUser]
    authentication_classes = [JWTUserAuthentication]
    def patch(self, request,id):
        
        details = Vendor.objects.get(id=id)
        details.is_active=True
        print(details.is_active)
        serializer = UpdateVendorSerializer(details,data=request.data,partial = True)
        if serializer.is_valid():
            serializer.save()

            print('-------------------')
            print(details.email)
            print('---------------')

            mailingemail= details.email
            print(mailingemail)
            
            send_mail('Hello  ',
            'Congratulations, your Vender application is approved.',
            'ashrafchekintakath@gmail.com'
            ,[mailingemail]   
            ,fail_silently=False)


            print("Vendor verified Successfully")
            return Response(serializer.data)
        else:
            print("Vendor verification failed")
            print(serializer.errors)
            return Response(serializer.errors)

class BlockVendor(APIView):
    permission_classes=[IsAdminUser]
    authentication_classes = [JWTUserAuthentication]
    def patch(self, request,id):
        details = Vendor.objects.get(id=id)
        print('-------111111111-------------')
        if details.is_Vendor==True:
            print('-------222222-------------')
            details.is_active=False
            details.is_Vendor=False
        else:
            print('-------333333-------------')
            details.is_Vendor=True
        print(details.is_active)
        print('-------4444444444-------------')
        serializer = UpdateVendorSerializer(details,data=request.data,partial = True)
        if serializer.is_valid():
            print('-------5555555-------------')
            serializer.save()
            print("Vendor action Successfully")
            return Response(serializer.data)
        else:
            print("Vendor action failed")
            print(serializer.errors)
            return Response(serializer.errors)

class BlockUser(APIView):
    permission_classes=[IsAdminUser]
    authentication_classes = [JWTUserAuthentication]
    def patch(self, request,id):
        details = User.objects.get(id=id)
        if details.is_active==True:
            details.is_active=False
        else:
            details.is_active=True
        print(details.is_active)
        serializer = UpdateUserSerializer(details,data=request.data,partial = True)
        if serializer.is_valid():
            serializer.save()
            print("vender action Successfully")
            return Response(serializer.data)
        else:
            print("Vendor action failed")
            print(serializer.errors)
            return Response(serializer.errors)

class GetUserDetailsView(APIView):
    permission_classes=[IsAdminUser]
    authentication_classes = [JWTUserAuthentication]
    serializer_classes = UserSerializer
    def get(self, request,id):
        try:
            user = User.objects.get(id=id)
            serializer = UserSerializer(user,many=False)   
            return Response(serializer.data)
        except:
            message = {'message':'No User with this id already exist'}
            return Response(message)

class GetUsersView(APIView):
    permission_classes=[IsAdminUser]
    authentication_classes = [JWTUserAuthentication]
    serializer_classes = UserSerializer
    def get(self, request):
    
        users = User.objects.all()
        serializer = UserSerializer(users,many=True)   
        return Response(serializer.data)

class GetVendorDetailsView(APIView):
    permission_classes=[IsAdminUser]
    authentication_classes = [JWTUserAuthentication]
    serializer_classes = UserSerializer
    def get(self, request,id):
        try:
            vendor = Vendor.objects.get(id=id)
            serializer = VendorSerializer(vendor,many=False)   
            return Response(serializer.data)
        except:
            message = {'message':'No User with this id already exist'}
            return Response(message)

class GetVendorsView(APIView):
    permission_classes=[IsAdminUser]
    authentication_classes = [JWTUserAuthentication]
    serializer_classes = VendorSerializer
    def get(self, request):
    
        vendors = Vendor.objects.all()
        serializer = VendorSerializer(vendors,many=True)   
        return Response(serializer.data)

class AddDistrictView(APIView):
    permission_classes=[IsAdminUser]
    authentication_classes = [JWTUserAuthentication]
    serializer_classes = DistrictSerializer
    def post(self,request):
        data = request.data
        serializer = self.serializer_classes(data=data)
        if serializer.is_valid():
            serializer.save()
            
            print(serializer.data)
            
            response={
                "data" : serializer.data
            }
            return Response(response)
        else:
            print(serializer.errors)
            return Response(serializer.errors)

class AddCityView(APIView):
    permission_classes=[IsAdminUser]
    authentication_classes = [JWTUserAuthentication]
    serializer_classes = CitySerializer
    def post(self,request):
        data = request.data
        serializer = self.serializer_classes(data=data)
        if serializer.is_valid():
            serializer.save()
            
            print(serializer.data)
            
            response={
                "data" : serializer.data
            }
            return Response(response)
        else:
            print(serializer.errors)
            return Response(serializer.errors)

class UpdateDistrictView(APIView):
    permission_classes=[IsAdminUser]
    authentication_classes = [JWTUserAuthentication]
    def get(self, request,id):
        details = District.objects.get(id=id)
        serializer = DistrictSerializer(details,context={'request': request})
        return Response(serializer.data)
    def put(self, request,id):
        print(request.body)
        details = District.objects.get(id=id)
        serializer = DistrictSerializer(details,data=request.data,)
        if serializer.is_valid():
            print(serializer.validated_data)
            serializer.save()
            print("Update district successfully updated")
            return Response(serializer.data)
        else:
            print("Update district failed")
            return Response(serializer.errors)    
    def delete(self, request,id):
        details = District.objects.get(id=id)
        details.delete()
        return Response({'message':'District deleted'})
    def patch(self, request,id):
        details = District.objects.get(id=id)
        serializer = DistrictSerializer(details,data=request.data,partial = True)
        if serializer.is_valid():
            print(serializer.validated_data)
            serializer.save()
            print("Update district successfully updated")
            return Response(serializer.data)
        else:
            print("Update district failed")
            print(serializer.errors)
            return Response(serializer.errors)

class UpdateCityView(APIView):
    permission_classes=[IsAdminUser]
    authentication_classes = [JWTUserAuthentication]
    def get(self, request,id):
        details = City.objects.get(id=id)
        serializer = CitySerializer(details,context={'request': request})
        return Response(serializer.data)
    def put(self, request,id):
        print(request.body)
        details = City.objects.get(id=id)
        serializer = CitySerializer(details,data=request.data,)
        if serializer.is_valid():
            print(serializer.validated_data)
            serializer.save()
            print("Update city successfully updated")
            return Response(serializer.data)
        else:
            print("Update city failed")
            return Response(serializer.errors)    
    def delete(self, request,id):
        details = City.objects.get(id=id)
        details.delete()
        return Response({'message':'City deleted'})
    def patch(self, request,id):
        details = City.objects.get(id=id)
        serializer = CitySerializer(details,data=request.data,partial = True)
        if serializer.is_valid():
            print(serializer.validated_data)
            serializer.save()
            print("Update city successfully updated")
            return Response(serializer.data)
        else:
            print("Update city failed")
            print(serializer.errors)
            return Response(serializer.errors)

class GetDistrictsView(APIView):
    permission_classes=[IsAdminUser]
    authentication_classes = [JWTUserAuthentication]
    def get(self, request):
    
        districts = District.objects.all()
        serializer = DistrictSerializer(districts,many=True)   
        return Response(serializer.data)

class GetCitiesView(APIView):
    permission_classes=[IsAdminUser]
    authentication_classes = [JWTUserAuthentication]
    def get(self, request):
    
        cities = City.objects.all()
        serializer = CitySerializer(cities,many=True)   
        return Response(serializer.data)

class GetCityenqueryView(APIView):
    permission_classes=[IsAdminUser]
    authentication_classes = [JWTUserAuthentication]
    def get(self, request):
    
        cities = Cityenquery.objects.all()
        serializer = CityenquerySerializer(cities,many=True)   
        return Response(serializer.data)

class GetUnapprovedCityenqueryView(APIView):
    permission_classes=[IsAdminUser]
    authentication_classes = [JWTUserAuthentication]
    def get(self, request):
    
        cities = Cityenquery.objects.all().exclude(is_approved=True) 
        serializer = CityenquerySerializer(cities,many=True)  
        return Response(serializer.data)

class ApproveCityenqueryView(APIView):
    permission_classes=[IsAdminUser]
    authentication_classes = [JWTUserAuthentication]
    def patch(self, request,id):
        
        cities = Cityenquery.objects.get(id=id)
        cities.is_approved=True
        print(cities.is_approved)
        serializer = CityenquerySerializer(cities,data=request.data,partial = True)
        if serializer.is_valid():
            serializer.save()

            print('-------------------')
            print(cities.email)
            print('---------------')

            mailingemail= cities.email
            print(mailingemail)
            
            send_mail('Hello  ',
            'You have requested for The city on your registration.We are sorry for not verified that City.Now can register . Please register again.',
            'ashrafchekintakath@gmail.com'
            ,[mailingemail]   
            ,fail_silently=False)


            print("Vendor verified Successfully")
            return Response(serializer.data)
        else:
            print("Vendor verification failed")
            print(serializer.errors)
            return Response(serializer.errors)
    

class AddCategoryView(APIView):
    permission_classes=[IsAdminUser]
    authentication_classes = [JWTUserAuthentication]

    def post(self, request):
        data = request.data
        request.data._mutable=True
        data['slug']=slugify(data['category_name'])
        data.update(request.data)
        serializer = CategorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            print(serializer.errors)
            return Response(serializer.errors)


class AddMoviesView(APIView):
    permission_classes=[IsAdminUser]
    authentication_classes = [JWTUserAuthentication]

    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            print(serializer.errors)
            return Response(serializer.errors)

class BlockMovie(APIView):
    permission_classes=[IsAdminUser]
    authentication_classes = [JWTUserAuthentication]
    def patch(self, request,id):
        movie = Movie.objects.get(id=id)
        if movie.is_active==True:
            movie.is_active=False
        else:
            movie.is_active=True
        print(movie.is_active)
        serializer = MovieSerializer(movie,data=request.data,partial = True)
        if serializer.is_valid():
            serializer.save()
            print("Movie action Successfully")
            return Response(serializer.data)
        else:
            print("Movie action failed")
            print(serializer.errors)
            return Response(serializer.errors)

class UpdateMovie(APIView):
    permission_classes=[IsAdminUser]
    authentication_classes = [JWTUserAuthentication]
    def patch(self, request,id):
        movie = Movie.objects.get(id=id)
        serializer = MovieSerializer(movie,data=request.data,partial = True)
        if serializer.is_valid():
            serializer.save()
            print("Movie update Successfully")
            return Response(serializer.data)
        else:
            print("Movie update failed")
            print(serializer.errors)
            return Response(serializer.errors)
    def delete(self, request,id):
        details = Movie.objects.get(id=id)
        details.delete()
        return Response({'message':'Movie deleted'})
    def put(self, request,id):
        movie = Movie.objects.get(id=id)
        serializer = MovieSerializer(movie,data=request.data)
        if serializer.is_valid():
            serializer.save()
            print("Movie update Successfully")
            return Response(serializer.data)
        else:
            print("Movie update failed")
            print(serializer.errors)
            return Response(serializer.errors)


class TMDBNowplayingMovies(APIView):
    permission_classes=[IsAdminUser]
    authentication_classes = [JWTUserAuthentication]

    def get(self,request):
        url='https://api.themoviedb.org/3/movie/now_playing?api_key='+settings.API_KEY
        response=requests.get(url)
        print(response)
        data=response.json()
        results=data['results']
        # final=results[0]
        # print(final['id'])
        # print(final['original_title'])
        
        answer={}

        for a in range(20):
            final=results[a]
            print(type(final))
            print(final['id'])
            print(final['original_title'])
            
            # answer[a]=final['id'],final['original_title']
            answer[final['id']]=final['original_title']
            
        print('********************')
        print(answer)
        # return Response(results)
        # return Response(data)
        return Response(answer)

# class TMDBMovieDetails(APIView):
#         permission_classes=[IsAdminUser]
#         authentication_classes = [JWTUserAuthentication]

#         def get(self,request,movie_id):
#             url='https://api.themoviedb.org/3/movie/'+str(movie_id)+'?api_key='+settings.API_KEY
#             response=requests.get(url)
#             print(response)
#             data=response.json()
#             return Response(data)

class TMDBMovieDetails(APIView):
        permission_classes=[IsAdminUser]
        authentication_classes = [JWTUserAuthentication]

        def get(self,request,id):
            print('************************************')
            movie=Movie.objects.get(id=id)
            print(movie)
            movie_id=movie.tmdb_id
            print('+++++++++++++++++++++++++')

            url='https://api.themoviedb.org/3/movie/'+str(movie_id)+'?api_key='+settings.API_KEY
            response=requests.get(url)
            print(response)
            data=response.json()
            return Response(data)

class MovieDetails(APIView):
    permission_classes=[IsAdminUser]
    authentication_classes = [JWTUserAuthentication]
    def get(self, request):
    
        movie = Movie.objects.all()
        serializer =MovieSerializer(movie,many=True)   
        return Response(serializer.data)

class GetAllMovieByLanguage(APIView):
    permission_classes=[IsAdminUser]
    authentication_classes = [JWTUserAuthentication]
    def get(self, request,id):

        
        movie = Movie.objects.filter(category_name=id)
        serializer =MovieSerializer(movie,many=True)
         
        return Response(serializer.data)

class GetAllBookedDetails(APIView):
    permission_classes=[IsAdminUser]
    authentication_classes = [JWTUserAuthentication]
    def get(self, request):

        
        ticket = BokkingTicket.objects.all()
        serializer =BookingTicketSerializer(ticket,many=True)
         
        return Response(serializer.data)

class GetAllBrokerCharge(APIView):
    permission_classes=[IsAdminUser]
    authentication_classes = [JWTUserAuthentication]
    def get(self, request):

        
        ticket = BrokerCharge.objects.all()
        serializer =BrokerChargeSerializer(ticket,many=True)
         
        return Response(serializer.data)