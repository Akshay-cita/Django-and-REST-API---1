# Django-and-REST-API---1
DRF Practice (Songs and Artist)



## Models
### Song
Fields are: Album,Artist,Description

### Artist

Fields are: First Name,Last Name,Email Id

## Requirements

* [Django Rest Framework](https://www.django-rest-framework.org/tutorial/quickstart/)
* [Postgresql](https://www.postgresql.org/)



## URL

1. `http://127.0.0.1:8000/api/<Song id>/` Song in particular id 

2. `http://127.0.0.1:8000/api/songlist/` List out all the songs registered 

## Database
Here `postgresql` is used as database.It is free and Secure database. `pgadmin4`providing a powerful graphical interface that simplifies the creation, maintenance and use of database objects.

### Connecting PostgreSQL in project

In `settings.py` file make as per the following structure


    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'database name',
            'USER':'postgres username(defaultname is 'postgres')',
            'PASSWORD':'XXXXXX',
            'HOST':'127.0.0.1',
            'PORT':'5432',
            }
        }

`Psycopg2` is a DB API 2.0 compliant PostgreSQL driver that is actively developed. It is designed for multi-threaded applications and manages its own connection pool.

Installing in ubuntu `sudo apt-get install python-psycopg2`


