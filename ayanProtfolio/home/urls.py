from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [

     path('', views.home, name='home'),
     path('fullProject/<str:slug>', views.fullProject, name='fullProject'),
     path('skill/', views.skill, name='skill'),
     path('contact/', views.contact, name='contact'),
     path('certificate/', views.certificate, name='certificate'),
     path('education/', views.education, name='education'),
     path('testimonial/', views.testimonial, name='testimonial'),
     path('research_paper/', views.research_paper, name='research_paper'),
     path('exprience/', views.exprience, name='exprience'),
     path('achievement/', views.achievement, name='achievement'),

]