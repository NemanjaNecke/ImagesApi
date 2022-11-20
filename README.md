# imagesAPI
 RESTful API for Images App
 API is currently hosted on pythonanywhere and can be accessed thorugh Angular Front end App https://images-rest-app.web.app/
Getting Started
First clone the repository from Github and switch to the new directory:

$ git clone git@github.com/USERNAME/{{ project_name }}.git
$ cd {{ project_name }}
Activate the virtualenv for your project.
python3 -m venv /path/to/new/virtual/environment or if in the same folder python3 -m venv venv
venv/Scripts/activate
Install project dependencies:

$ pip install -r requirements-dev/local.txt
Then simply apply the migrations:

$ python manage.py migrate
You can now run the development server:

$ python manage.py runserver
