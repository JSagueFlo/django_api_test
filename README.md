# About this project
This is a basic API example with Django  
Note that only GET requests are programmed in order to keep it simple  

There will be 3 endpoints for this API:  
* http://localhost:8000/frame/test/
* http://localhost:8000/raw/test/
* http://localhost:8000/raw/test2/

### GET frame/test/
This endpoint uses rest_framework package utilities in order to parse data from the database

### GET raw/test/
This endpoint just serializes raw model data from database  
This is a simple function returning an HttpResponse, please note that this can be done using Class-based views aswell

### GET raw/test2/
This endpoint parses model data values from database and returns it as a list of objects  
This is a simple function returning a JsonResponse, please note that this can be done using Class-based views aswell

## Setting up the enviroment
**Note:** The enviroment setup must be done **outside** the project directory
```
>python --version
Python 3.7.4

>python -m venv venv

>venv\Scripts\activate

>pip --version
pip 19.0.3
>python -m pip install --upgrade pip
...
Successfully installed pip-20.0.2
```

*Now you are ready to start developing*
```
>cd api_test
```

## Easy install
**Note:** You can install all the required packages with the following command
```
pip install -r requirements.txt
```

**Setup django:**
```
>python manage.py makemigrations
>python manage.py migrate
>python manage.py createsuperuser
```

## Packages installed
```
>pip install django
>django-admin --version
3.0.5

>pip install djangorestframework

>pip freeze > requirements.txt
```

## Project setup step-by-step
```
>django-admin startproject api_test
>cd api_test
>django-admin startapp api_raw
>django-admin startapp api_framework
```

## settings.py modifications
**Note:** api_test/settings.py
```
INSTALLED_APPS = [
    ...
    'rest_framework', #The package
    'api_framework',  #Our app using rest_framework
    'api_raw',        #Our raw app not using rest_framework
]
```