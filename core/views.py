from django.shortcuts import render
# Create your views here.
from .models import About,Services,Skills

def IndexView(request):
    
    about=About.objects.all()
    services=Services.objects.all()
    skills=Skills.objects.all()
   
    context={ 
        'about':about,
        'services':services,
        'skills':skills
    }
    return render(request, 'index.html',context )