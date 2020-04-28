from django.contrib import admin

# Register your models here.

from .models import *
#from tasks.models import Task  #will also work
# .models import Task      #will also work
admin.site.register(Task)