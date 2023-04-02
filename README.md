# RESTful API for Image Gallery App
This API is currently hosted on PythonAnywhere and can be accessed through the Angular Front end App https://images-rest-app.web.app/.

Getting Started
First clone the repository from GitHub and switch to the new directory:
```
$ git clone git@github.com/USERNAME/{{ project_name }}.git 
$ cd {{ project_name }}
```
Activate the virtualenv for your project.
```
python3 -m venv /path/to/new/virtual/environment or if in the same folder python3 -m venv venv
venv/Scripts/activate
```
Install project dependencies:
```
$ pip install -r requirements-dev/local.txt
```

Then simply apply the migrations:
```
$ python manage.py migrate
```
You can now run the development server:
```
$ python manage.py runserver
```
