from django.shortcuts import render
# Create your views here.
from .models import About,Services,Education,Portfolio,Client
from django.core.mail import send_mail
from django.conf import settings


def IndexView(request):
    
    about=About.objects.all()
    services=Services.objects.all()
    education=Education.objects.all()
    portfolios=Portfolio.objects.all()
    clients=Client.objects.all()
    message_sent = False
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        send_mail(
            subject,
            message,
            email,
            [settings.EMAIL_HOST_USER],
            fail_silently=False,
        )

        message_sent = True
    
   
    context={ 
        'about':about,
        'services':services,
        'education':education,
        'portfolios':portfolios,
        'clients':clients,
        'message_sent': message_sent,
    }
    return render(request, 'index.html',context )