# cinemakottaka

# Getting started

## To get started you can simply clone this cinemakottaka project repository and install the dependencies.



git clone https://github.com/Chekintakathashraf/cinemakottaka/
cd cd cinemakottaka

## Create a virtual environment to install dependencies in and activate it:

python3 -m venv venv
source venv/bin/activate

## Then install the dependencies:

(venv)$ pip install -r requirement.txt

Note the (venv) in front of the prompt. This indicates that this terminal session operates in a virtual environment set up by virtualenv2.

Once pip has finished downloading the dependencies:

(venv)$ cd backend
(venv)$ python3 manage.py runserver

And navigate to http://127.0.0.1:8000/

# Documentation
## Admin api


- To add language

### POST
/admin_api/addcategory/

required field : category_name - string


- To add city
### POST
/admin_api/addcity/

required field : district-id, city-string

- To add district
### POST
/admin_api/adddistrict/

required field : district-string

### POST
/admin_api/addmovie/

required field : movie_name - string, category_name - id, tmdb_id - string

### PATCH
/admin_api/approvecityenquery/{id}/

required field : cityenquery id

### PATCH
/admin_api/blockmovie/{id}/

required field : movie id

### PATCH
/admin_api/blockuser/{id}/

required field : user id

### PATCH
/admin_api/blockvendor/{id}/

required field : vendor id

### GET
/admin_api/getallmoviebylanguage/{id}/

required field : category id

### GET
/admin_api/getallpaidticket/

### GET
/admin_api/getallpendingticket/

### GET
/admin_api/getbookingdetails/

### GET
/admin_api/getbrokerchargedetails/

### GET
/admin_api/getcities/

### GET
/admin_api/getcityenquery/

### GET
/admin_api/getdistricts/

### GET
/admin_api/getunapprovedcityenquery/

### GET
/admin_api/getuserdetails/{id}/

required field : user id

### GET
/admin_api/getusers/

### GET
/admin_api/getvendordetails/{id}/

required field : vendor id

### GET
/admin_api/getvendors/

### GET
/admin_api/getvendorsbycity/{id}/

required field : city id

### GET
/admin_api/getvendorsbydistrict/{id}/

required field : district id

### GET
/admin_api/moviedetails/

### GET
/admin_api/tmdbmoviedetails/{id}/

required field : movie id

### GET
/admin_api/tmdbnowplayingmovies/

### GET
/admin_api/updatecity/{id}/

required field : city id

### PUT
/admin_api/updatecity/{id}/

required field : city id

### PATCH
/admin_api/updatecity/{id}/

required field : city id

### DELETE
/admin_api/updatecity/{id}/

required field : city id

### GET
/admin_api/updatedistrict/{id}/

required field : district id

### PUT
/admin_api/updatedistrict/{id}/

required field : district id

### PATCH
/admin_api/updatedistrict/{id}/

required field : district id

### DELETE
/admin_api/updatedistrict/{id}/

required field : district id

### PUT
/admin_api/updatemovie/{id}/

required field : movie id

### PATCH
/admin_api/updatemovie/{id}/

required field : movie id

### DELETE
/admin_api/updatemovie/{id}/

required field : movie id

### PATCH
/admin_api/verifyvendor/{id}/

required field : vendor id
