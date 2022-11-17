# cinemakottaka

# Getting started

## To get started you can simply clone this cinemakottaka project repository and install the dependencies.



git clone https://github.com/Chekintakathashraf/cinemakottaka/ 

cd cinemakottaka

## Create a virtual environment to install dependencies in and activate it:

python3 -m venv venv

source venv/bin/activate

## Then install the dependencies:

(venv)$ pip install -r requirement.txt

Note the (venv) in front of the prompt. This indicates that this terminal session operates in a virtual environment set up by virtualenv2.

Once pip has finished downloading the dependencies:

(venv)$ cd backend.

## Create The following Api Accounts

- Twilio
- Email-smtp
- tmdb api
- razor pay
- celery
- rabbit mq
- redis

## create .env file in project directry and paste this
TWILIO_VERIFY_SERVICE_SID=

TWILIO_ACCOUNT_SID=

TWILIO_AUTH_TOKEN=


EMAIL_BACKEND = 

EMAIL_HOST = 

EMAIL_PORT = 

EMAIL_HOST_USER = 

EMAIL_HOST_PASSWORD = 

EMAIL_USE_TLS = True

API_KEY=

RAZORPAY_PUBLIC_KEY =

RAZORPAY__SECRET_KEY =



(venv)$ python3 manage.py runserver

And navigate to http://127.0.0.1:8000/

# Documentation
## Admin api


## To add language of movie
``` POST
/admin_api/addcategory/

required body field : category_name - string
```

### To add city
```POST
/admin_api/addcity/

required body field : district-id, city-string
```

### To add district
```POST
/admin_api/adddistrict/

required body field : district-string
```

### To add movies 
```POST
/admin_api/addmovie/

required body field : movie_name - string, category_name - id, tmdb_id - string
```

### To aprove city enquary 
```PATCH
/admin_api/approvecityenquery/{id}/

required param : cityenquery id
```

### To block mocie
```PATCH
/admin_api/blockmovie/{id}/

required param : movie id
```

### To block user
```PATCH
/admin_api/blockuser/{id}/

required param : user id
```

### To block vendor
```PATCH
/admin_api/blockvendor/{id}/

required param : vendor id
```

### To get all movie by language
```GET
/admin_api/getallmoviebylanguage/{id}/

required param : category id
```

### To get all paid ticket
```GET
/admin_api/getallpaidticket/
```

### To get all pending ticket
```GET
/admin_api/getallpendingticket/
```

### To get all booking details
```GET
/admin_api/getbookingdetails/
```

### To get all broker charge details
```GET
/admin_api/getbrokerchargedetails/
```

### To get all cities
```GET
/admin_api/getcities/
```

### To get all enquired cities
```GET
/admin_api/getcityenquery/
```

### To get all districts
```GET
/admin_api/getdistricts/
```

### To get all un approved city enquiery
```GET
/admin_api/getunapprovedcityenquery/
```

### To get a particular user details
```GET
/admin_api/getuserdetails/{id}/

required param : user id
```

### To get all users 
```GET
/admin_api/getusers/
```

### To get particular vendor details
```GET
/admin_api/getvendordetails/{id}/

required param : vendor id
```

### To get all vendors
```GET
/admin_api/getvendors/
```

### To get all vendor by city 
```GET
/admin_api/getvendorsbycity/{id}/

required param : city id
```

### To get all vendors by district
```GET
/admin_api/getvendorsbydistrict/{id}/

required parm : district id
```

### To get all movies
```GET
/admin_api/moviedetails/
```

### To get a details of particular movie
```GET
/admin_api/tmdbmoviedetails/{id}/

required param : movie id
```

### To get now playing movie by tmdb
```GET
/admin_api/tmdbnowplayingmovies/
```
### To get city
```GET
/admin_api/updatecity/{id}/

required param : city id
```
### To update city
```PUT
/admin_api/updatecity/{id}/

required param : city id
```
### To update district
```PATCH
/admin_api/updatecity/{id}/

required param : city id
```
### To delete city
```DELETE
/admin_api/updatecity/{id}/

required param : city id
```
### To get district details
```GET
/admin_api/updatedistrict/{id}/

required param : district id
```
### To update district
```PUT
/admin_api/updatedistrict/{id}/

required param : district id
```
### To update district
```PATCH
/admin_api/updatedistrict/{id}/

required param : district id
```
### To delete district
```DELETE
/admin_api/updatedistrict/{id}/

required param : district id
```

### To update movie 
```PATCH
/admin_api/updatemovie/{id}/

required param : movie id
```
### To delete movie 
```DELETE
/admin_api/updatemovie/{id}/

required param : movie id
```
### To verify vendor 
```PATCH
/admin_api/verifyvendor/{id}/

required param : vendor id
```

## User API

### To get all city by district
```GET
/user_api/allcitybydistrict/{id}/
required field : district id
```

### To get all districts
```GET
/user_api/alldistrict/
```

### To get available seat of that show
```GET
/user_api/availableseatofshow/{id}/
required field : show id
```

### To get booked seat of that show
```GET
/user_api/bookedseatofshow/{id}/
required field : show id
```

### To bookticket 
```POST
/user_api/bookticket/
required field : show - show id, screen - screen id, seat_no - list of seat id
```

### To get all movie
```GET
/user_api/getallmovie/
```

### To get all movie by languages
```GET
/user_api/getallmoviebylanguage/{id}/
required field : language category id
```
### To get all movie languages
```GET
/user_api/getallmoviecategory/
```

### To login user with password
```POST
/user_api/loginuser/
required field : phone_number-10 digit number, password - string
```

### To login user with otp
```POST
/user_api/loginuserwithotp/
required field : phone_number-10 digit number
```

### To logout
```POST
/user_api/logoutuser/
```

### To make dummy payment without razorpay
```PATCH
/user_api/payment/{id}/
required param : ticket id
```

### To refresh token
```POST
/user_api/refreshuser/
```

### To register user
```POST
/user_api/register/
required body : username-string, email-email, phone_number-10 digit number, password - string
```

### To get all seat details by show 
```GET
/user_api/seatofshow/{id}/
required param : show id
```

### To select user current location
```PATCH
/user_api/selectlocation/
required body field : district-district id, city - city id
```

### To get show by our choice
```GET
/user_api/showbychoice/{date}/{time}/{vendor}/{movie}/
required param : date id,time id,vendor id, movie id
```

### To get all showdate
```GET
/user_api/showdate/
```

### To get all showtime
```GET
/user_api/showtime/
```

### To get theater details
```GET
/user_api/theater/{id}/
required param : movie id
```

### To get therater by user city 
```GET
/user_api/theaterbycity/
```

### To get movie tmdb details
```GET
/user_api/tmdbmoviedetails/{id}/
required field : movie id
```

### To get own user details
```GET
/user_api/user/
```

### To verify the login user otp 
```POST
/user_api/verifyloginuserotp/
required body field : code - string
```

### To verify the User 
```POST
/user_api/verifyuser/
required body field : phone_number-10 digit number, code - string
```
## Vender API

### POST
/vendor_api/addscreen/
required field : screen_name - string, total_seet - number, price- number

### POST
/vendor_api/addseat/
required field : seet_no-1, show-show id, screen-screen id

### POST
/vendor_api/addshow/
required field : movie - movie id , screen - creen id, date- date id, time - time id

### POST
/vendor_api/addshowdate/
required field : time - hour:minute:second

### POST
/vendor_api/addshowtime/
required field : date - year-month-day

### PATCH
/vendor_api/blockshow/{id}/
required field : show id

### GET
/vendor_api/bookedseatbyshow/{id}/
required field : show id

### GET
/vendor_api/getallfinishedshow/

### GET
/vendor_api/getallscreen/

### GET
/vendor_api/getallscreenbymovieid/{id}/
required field : movie id

### GET
/vendor_api/getallscreenbyshow/{id}/
required field : show id

### GET
/vendor_api/getallshow/

### To get all show by date
```GET
/vendor_api/getallshowbydate/{id}/
required param : date id
```

### To get all show by language
```GET
/vendor_api/getallshowbylanguage/{id}/
required param : category id
```

### To get all show by movie
```GET
/vendor_api/getallshowbymovie/{id}/
required param : movie id
```

### To get all show by screen
```GET
/vendor_api/getallshowbyscreen/{id}/
required param : screen id
```

### To get all show by time
```GET
/vendor_api/getallshowbytime/{id}/
required param : time id
```

### To get all upcomingshow 
```GET
/vendor_api/getallupcomingshow/
```

### Too login vendor
```POST
/vendor_api/loginvendor/
required body field : email - email, password - string
```

### To logout vendor
```POST
/vendor_api/logoutvendor/
```

### To refresh token
```POST
/vendor_api/refreshvendor/
```

### To register vendor
```POST
/vendor_api/register/
required body field : first_name - string, last_name - string, email-email, phone_number - 10 digit number, password - string, district - district id, city - city id or else other & cityenqueryname - string
```

### To get unbooked seat of particular show
```GET
/vendor_api/unbookedseatbyshow/{id}/
required param : show id
```

### To update screen
```PUT
/vendor_api/updatescreen/{id}/
required param : screen id
```

### To update screen
```PATCH
/vendor_api/updatescreen/{id}/
required param : screen id
```

### To get our vendor details
```GET
/vendor_api/vendor/
```
