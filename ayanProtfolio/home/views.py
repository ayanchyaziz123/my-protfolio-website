from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')
def skill(request):
    return render(request, 'skill.html')    
def contact(request):
    return render(request, 'contact.html')     
