from django.shortcuts import render
from .models import Project
from django.core.paginator import Paginator

# Create your views here.

def home(request):
    project = Project.objects.all()
    paginator = Paginator(project, 4)
    page = request.GET.get('page')
    project = paginator.get_page(page)
    context = {
        'project':project,
    }
    return render(request, 'home.html', context)
def fullProject(request, slug):
    projects = Project.objects.filter(id=slug).first()  
    project = Project.objects.all()
    paginator = Paginator(project, 3)
    page = request.GET.get('page')
    project = paginator.get_page(page)
    context = {
        'projects':projects,
        'project':project,
    }
    return render(request, 'fullProject.html', context)

def skill(request):
    project = Project.objects.all()
    paginator = Paginator(project, 3)
    page = request.GET.get('page')
    project = paginator.get_page(page)
    context = {
        'project':project,
    }
    return render(request, 'skill.html', context)    
def contact(request):
    project = Project.objects.all()
    paginator = Paginator(project, 3)
    page = request.GET.get('page')
    project = paginator.get_page(page)
    context = {
        'project':project,
    }
    return render(request, 'contact.html', context)  
def certificate(request):
    return render(request, 'certificate.html')    
def education(request):
    project = Project.objects.all()
    paginator = Paginator(project, 3)
    page = request.GET.get('page')
    project = paginator.get_page(page)
    context = {
        'project':project,
    }
    return render(request, 'education.html', context)           
