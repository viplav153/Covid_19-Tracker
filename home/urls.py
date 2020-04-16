from django.contrib import admin
from django.urls import path, include

#to change the text at admin page
from home import views

urlpatterns = [ 
    path('', views.home, name='home'),
]