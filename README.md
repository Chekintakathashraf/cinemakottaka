# cinemakottaka

# Getting started

To get started you can simply clone this cinemakottaka project repository and install the dependencies.



git clone https://github.com/Chekintakathashraf/cinemakottaka/
cd cd cinemakottaka

Create a virtual environment to install dependencies in and activate it:

python3 -m venv venv
source venv/bin/activate

Then install the dependencies:

(venv)$ pip install -r requirement.txt

Note the (venv) in front of the prompt. This indicates that this terminal session operates in a virtual environment set up by virtualenv2.

Once pip has finished downloading the dependencies:

(venv)$ cd backend
(venv)$ python3 manage.py runserver

And navigate to http://127.0.0.1:8000/

