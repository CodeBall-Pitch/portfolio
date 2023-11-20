from django.shortcuts import render
# Create your views here.
from .models import About

def IndexView(request):
    
    about=About.objects.all()
   
    context={ 
        'about':about
    }
    return render(request, 'index.html',context )