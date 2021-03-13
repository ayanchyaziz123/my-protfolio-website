from django.shortcuts import redirect, render
from .models import Contact, Project
from django.core.paginator import Paginator
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

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
    paginator = Paginator(project, 4)
    page = request.GET.get('page')
    project = paginator.get_page(page)
    context = {
        'projects':projects,
        'project':project,
    }
    return render(request, 'fullProject.html', context)

def skill(request):
    project = Project.objects.all()
    paginator = Paginator(project, 4)
    page = request.GET.get('page')
    project = paginator.get_page(page)
    context = {
        'project':project,
    }
    return render(request, 'skill.html', context)    



def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        data  = Contact(name=name, email=email, subject=subject, message=message)
        data.save()
        messages.success(request, "Your message was sent successfully.Thanks to you")
        return redirect('home')
        #print(name, email, subject, message)
    else:
        project = Project.objects.all()
        paginator = Paginator(project, 4)
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
    paginator = Paginator(project, 4)
    page = request.GET.get('page')
    project = paginator.get_page(page)
    context = {
        'project':project,
    }
    return render(request, 'education.html', context)           
