### Django Todo CRUD 

#### Project Setup
1) Start virtual environment 
    ~~~ bash 
    pipenv shell
    ~~~
2) Install Django  
    ~~~ bash
    pipenv install django
    ~~~    
3) Create new project called `todo`
    ~~~ bash
    django-admin startproject todo
    ~~~    
4) Change directory into `todo` and launch server
    - default rocket ship start page should be displayed
    ~~~ bash
    python manage.py runserver
    ~~~    
5) Close server and run first migration
    ~~~ bash
    python manage.py migrate
    ~~~    
6) Create `superuser`
    - uses currently logged in user as default
    - email is optional
    ~~~ bash
    python manage.py createsuperuser
    ~~~ 
 7) Start server and log into the admin panel `8000/admin` 
    - Start server `python manage.py runserver`  
    - login into to admin panel with superuser credentials
    - once verified, quit server
8) Create a new app called `tasks`
    ~~~ bash
    python manage.py startapp
    ~~~        