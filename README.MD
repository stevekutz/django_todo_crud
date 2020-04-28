### Django Todo CRUD 

#### Project Setup
1) Start virtual environment using `pipenv`
    - another way to set up a virtual environment is with Python's `venv` <a href = "https://docs.python.org/3/tutorial/venv.html" > Python Virtual Environment documentation </a>
    - 
    ~~~ bash 
    pipenv shell
    ~~~
    - NOTES 
        - to exit the pip virtual environment, type `exit` in the terminal window where it was launch
        - `pip list` will show installed packages
        - `pipenv graph` will show a dependency graph showing sub-dependencies for installed packages
2) Install Django  
    ~~~ bash
    pipenv install django
    ~~~    
3) Create new `project` called `todo`
    ~~~ bash
    django-admin startproject todo
    ~~~    
4) Change directory into `todo` and launch server
    - default rocket ship start page should be displayed
    ~~~ bash
    cd todo
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
8) Create a new `app` called `tasks`
    - the `tasks` folder will show up inside the `todo` folder
    ~~~ bash
    python manage.py startapp
    ~~~   
    - the directory of tasks will look like:
    ~~~ text
    tasks/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    urls.py
    views.py
    ~~~
9) Add `tasks` to the `INSTALED_APPS` within `todo/settings.py`
    ~~~ py
    ...
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',

        # added tasks app
        'tasks',
    ]
    ...
    ~~~

### Setup a Simple Default View
1) Inside `tasks/views.py` import `HttpResponse`
    ~~~ py
    from django shortcuts import render
    from django.http import HttpResponse
    ~~~
2) Create a simple default view
    ~~~ py
    # Create your views here.
    def index(request):
        return HttpResponse("Test Index view")
    ~~~
### Create a `URLconf` (e.g. URL configuration) inside of the tasks `app`
- this will map the view to a URL
1) Create a `urls.py` file inside the `tasks` folder
2) Import path at top of `urls.py`
    ~~~ py
    from django.urls import path
    ~~~
3) Add a URL pattern
- `path` receives a `route` and a `view`
    - `route` is a string that receives a `URL pattern`
    - IF a route is found, the `view` function is called
    - the `views.py` module contains the `index` function
    ~~~ py
    from django.urls import path
    from . import views

    # define paths
    urlpatterns = [
        path ('', views.index) 
    ] 
    ~~~
###  Update the root `URLconf` for the todo `project`
1) Add the import `django.urls.include` to `/todo/todo/urls.py`
- It originally looks like `from django.urls import path`
~~~ py
    from django.urls import path, include
~~~
2) Append `path('', include('tasks.urls')),` to the `urlpatterns` list
- the imported function `include` will allow other `URLconfs` to be referenced   
- `/todo/todo/urls.py` should now look like  
    ~~~ py
    from django.contrib import admin
    from django.urls import path, include # added include 7:47

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('tasks.urls')), 
    ]
    ~~~
3) After launching virtual environment and relaunching the server, the browser will show the simple default view
<img src = "Simple_Default_View.png"/>

### Define template
1) Create folders `templates/tasks` within the `tasks` app
2) Create the file `list.html` inside `templates/tasks`
3) Add the following to `list.html`
    ~~~ html
    <h3> Todos </h3>
    ~~~
4) Modify the `tasks/views.py` file to return the template file `list.html`
- replace `return HttpResponse("Test Index view works")` with
`~~~ py
# Create your views here.
def index(request):
    return render(request, 'tasks/list.html')
5) Refreshing the browser should display the template
<img src = "Simple_Todos_View.png"/>

### Setup Database
1) Create the following model inside `tasks/models`
    ~~~ py
    class Task(models.Model):
        title = models.CharField(max_length = 200)
        complete = models.BooleanField(default=False)
        created = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return self.title 
    ~~~
2) Create tables for migration
- Quit server
- In terminal, run `python manage.py makemigrations`
3) Migrate the database
- In terminal, run `python manage.py migrate`
4) Register the database in `admin.py`
5) Launch the admin panel to verify `Tasks` table created
<img src = "Task_AdminPanel.png"/>
