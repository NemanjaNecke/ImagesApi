# RESTful API for Image Gallery App
This API is currently hosted on PythonAnywhere and can be accessed through the Angular Front end App https://images-rest-app.web.app/.


Images App

`GET /api/images/` - Retrieves a list of all images.

`POST /api/images/` - Adds a new image.

`GET /api/images/{id}/`- Retrieves a specific image by ID.

`PUT /api/images/{id}/` - Updates a specific image by ID.

`DELETE /api/images/{id}/` - Deletes a specific image by ID.

`GET /api/categories/` - Retrieves a list of all categories.

`POST /api/categories/` - Adds a new category.

`GET /api/category-image/{id}/` - Retrieves a specific category by ID along with its associated images.


Users App

`GET /api/users/` - Retrieves a list of all users.

`POST /api/users/`- Adds a new user.

`GET /api/users/{id}/` - Retrieves a specific user by ID.

`PUT /api/users/{id}/` - Updates a specific user by ID.

`DELETE /api/users/{id}/` - Deletes a specific user by ID.

`GET /api/profiles/` - Retrieves a list of all profiles.

`POST /api/profiles/` - Adds a new profile.

`GET /api/profiles/{id}/` - Retrieves a specific profile by ID.

`PUT /api/profiles/{id}/` - Updates a specific profile by ID.

`DELETE /api/profiles/{id}/` - Deletes a specific profile by ID.

`GET /api/profile-pic/` - Retrieves a list of all profile pictures.

`POST /api/profile-pic/` - Adds a new profile picture.

`GET /api/profile-pic/{id}/` - Retrieves a specific profile picture by ID.

`PUT /api/profile-pic/{id}/` - Updates a specific profile picture by ID.

`DELETE /api/profile-pic/{id}/` - Deletes a specific profile picture by ID.

`GET /api/auth/` - Retrieves the authentication endpoints.

`POST /api/auth/login/` - Logs a user in and returns an authentication token.

`POST /api/auth/logout/` - Logs a user out.

`POST /api/auth/password/reset/` - Sends an email to reset a user's password.

`POST /api/auth/registration/`- Registers a new user.

`POST /api/api-key/` - Retrieves an API key for the current user.

`GET /api/profile-pic-profile/{id}/` - Retrieves a specific profile's associated profile picture by ID.

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
