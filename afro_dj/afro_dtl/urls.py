
from django.urls import path
from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
   
    
]
