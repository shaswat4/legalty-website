from django.contrib import admin
from django.urls import path , include
from .views import trueHome

urlpatterns = [
    path ( 'home/' ,  trueHome , name= 'true-home' ) ,
]
