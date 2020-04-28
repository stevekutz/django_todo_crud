from django.urls import path
from . import views  # from root import views

# define paths list
urlpatterns = [
    path ('', views.index) 

]   