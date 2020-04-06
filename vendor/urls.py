from django.contrib import admin
from django.urls import path 
from  . import  views

urlpatterns = [

    path('',views.homepage),
    path('about',views.aboutpage),
    path('contact',views.contactpage),
    path('login',views.login_page),
    path('register',views.register_page),

]