from django.shortcuts import render
# Create your views here.
from .models import About,Services

def IndexView(request):
    
    about=About.objects.all()
    services=Services.objects.all()
   
    context={ 
        'about':about,
        'services':services
    }
    return render(request, 'index.html',context )