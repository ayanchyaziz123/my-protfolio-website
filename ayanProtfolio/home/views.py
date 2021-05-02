from django.shortcuts import redirect, render
from .models import *
from django.core.paginator import Paginator
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

# Create your views here.

def home(request):
    project = Project.objects.all()
    paginator = Paginator(project, 8)
    page = request.GET.get('page')
    project = paginator.get_page(page)
    myself = MySelf.objects.all()
    recom = Recommendation.objects.all()
    total_recom = recom.count()
    context = {
        'project':project,
        'myself': myself,
        'recom':recom,
        'total_recom': total_recom,
    }
    return render(request, 'home.html', context)
def fullProject(request, slug):
    projects = Project.objects.filter(id=slug).first()  
    project = Project.objects.all()
    paginator = Paginator(project, 8)
    page = request.GET.get('page')
    project = paginator.get_page(page)
    context = {
        'projects':projects,
        'project':project,
    }
    return render(request, 'fullProject.html', context)

def skill(request):
    project = Project.objects.all()
    paginator = Paginator(project, 8)
    page = request.GET.get('page')
    project = paginator.get_page(page)
    data = Skill.objects.all()
    context = {
        'project':project,
        'data': data,
    }
    return render(request, 'body.html', context)    



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
        paginator = Paginator(project, 8)
        page = request.GET.get('page')
        project = paginator.get_page(page)
        context = {
            'project':project,
        }
    return render(request, 'contact.html', context)  

def education(request):
    project = Project.objects.all()
    paginator = Paginator(project, 8)
    page = request.GET.get('page')
    project = paginator.get_page(page)
    data = Education.objects.all()
    context = {
        'project':project,
        'data': data,
    }
    return render(request, 'body.html', context)          

def certificate(request):
    project = Project.objects.all()
    paginator = Paginator(project, 8)
    page = request.GET.get('page')
    project = paginator.get_page(page)
    data = Certificate.objects.all()
    context = {
        'project':project,
        'data': data,
    }
    return render(request, 'body.html', context)  

def testimonial(request):
    project = Project.objects.all()
    paginator = Paginator(project, 8)
    page = request.GET.get('page')
    project = paginator.get_page(page)
    data = Testimonial.objects.all()
    context = {
        'project':project,
        'data': data,
    }
    return render(request, 'body.html', context) 

def research_paper(request):
    project = Project.objects.all()
    paginator = Paginator(project, 8)
    page = request.GET.get('page')
    project = paginator.get_page(page)
    data = ResearchPaper.objects.all()
    context = {
        'project':project,
        'data': data,
    }
    return render(request, 'body.html', context) 

def exprience(request):
    project = Project.objects.all()
    paginator = Paginator(project, 8)
    page = request.GET.get('page')
    project = paginator.get_page(page)
    data = Exprience.objects.all()
    context = {
        'project':project,
        'data': data,
    }
    return render(request, 'body.html', context) 

def achievement(request):
    project = Project.objects.all()
    paginator = Paginator(project, 8)
    page = request.GET.get('page')
    project = paginator.get_page(page)
    data = Achievement.objects.all()
    context = {
        'project':project,
        'data': data,
    }
    return render(request, 'body.html', context) 

