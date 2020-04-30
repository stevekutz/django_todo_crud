from django.urls import path
from . import views  # from root import views

# define paths list
urlpatterns = [
    path ('', views.index, name = "list"), 
    path('update_task/<str:prim_key>/', views.updateTask, name = "update_task"),
    
]   