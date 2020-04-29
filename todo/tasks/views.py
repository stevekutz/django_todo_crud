from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import *

# Create your views here.
def index(request):
    tasks = Task.objects.all()  # returns everything, e.g.  returns a new QuerySet that is a copy of the current one

    form = TaskForm() 

    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid:
            form.save()
        return  redirect('/')   
    
    context = {'tasks': tasks, 'form': form}  # create a context dictionary
    return render(request, 'tasks/list.html', context)