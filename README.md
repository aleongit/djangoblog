# djangoblog

A Django App example with MySQL.
Use of Migrations, Forms, Views, Models, Templates and Bootstrap 5.


## For new project
- **new project**
```
django-admin startproject djangoblog
```

- **initial migration**
```
python manage.py makemigrations
python manage.py migrate
```

- **configure settings**
```
TIME_ZONE = 'Europe/Paris'
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
```

- **create app**
```
python manage.py startapp blog
```

- **add app to settings**
```
INSTALLED_APPS = [
    'blog.apps.BlogConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

- **create models in app**
- blog\models.py

- **migrate models**
```
python manage.py makemigrations blog
python manage.py migrate blog
```

- **admin access**
- **blog\admin.py**
```
from django.contrib import admin
from .models import Post, Valoracio

admin.site.register([
    Post,
    Valoracio
])
```

- **create superuser**
```
python manage.py createsuperuser

Username (leave blank to use 'aleon'):
Email address:
Password:
Password (again):
Superuser created successfully.
```

- **admin access**
- http://127.0.0.1:8000/admin/


## Getting Started

To run the demo locally, clone the repository and move into it:
- git clone git@github.com:aleongit/djangoblog.git
- cd djangoblog

## Requeriments
- python >= 3.8
- MySQL >= 8

## Install dependencies:
- pip install Django (v4)
- pip install mysqlclient

## DB
- create db and user djangoblog (schema.sql)
- configure db parameters in djangoblog\settings.py
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'djangoblog',
        'USER': 'djangoblog',
        'PASSWORD': '1234',
        'HOST': 'localhost',
        'PORT': '3307',
    }
}
```

## Run
- cd djangoblog
- python manage.py runserver
- Open your browser and go to http://127.0.0.1:8000/


![Screenshot](screenshots/1.png)

![Screenshot](screenshots/2.png)

![Screenshot](screenshots/3.png)

![Screenshot](screenshots/4.png)

![Screenshot](screenshots/5.png)

![Screenshot](screenshots/6.png)

![Screenshot](screenshots/7.png)