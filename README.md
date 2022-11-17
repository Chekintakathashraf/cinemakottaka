# cinemakottaka

# Getting started

## To get started you can simply clone this cinemakottaka project repository and install the dependencies.



git clone https://github.com/Chekintakathashraf/cinemakottaka/ .

cd cinemakottaka

## Create a virtual environment to install dependencies in and activate it:

python3 -m venv venv.

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

###To block mocie
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
