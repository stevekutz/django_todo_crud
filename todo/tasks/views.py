from django.shortcuts import render
from django.http import HttpResponse

from .models import *

# Create your views here.
def index(request):
    tasks = Task.objects.all()  # returns everything, e.g.  returns a new QuerySet that is a copy of the current one

    context = {'tasks': tasks}  # create a context dictionary
    return render(request, 'tasks/list.html', context)