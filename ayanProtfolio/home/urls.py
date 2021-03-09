from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [

     path('', views.home, name='home'),
     path('skill/', views.skill, name='skill'),
     path('contact/', views.contact, name='contact'),
     path('certificate/', views.certificate, name='certificate'),
]