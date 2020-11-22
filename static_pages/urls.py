from django.contrib import admin
from django.urls import path , include
from .views import trueHome , about_us

urlpatterns = [
    path ( 'home/' ,  trueHome , name= 'true-home' ) ,
    path ( 'about/' ,  about_us , name= 'about' ) ,
]
