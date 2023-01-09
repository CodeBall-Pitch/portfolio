from django.shortcuts import render
from portfolio.models import Portfolio,About,Services,Skills,Contact,Education,Services
# Create your views here.


def IndexView(request):
    portfolios = Portfolio.objects.all()
    educations = Education.objects.all()
    skills = Skills.objects.all()
    abouts = About.objects.all()
    services = Services.objects.all()
    contacts = Contact.objects.all()
    context={
        
     
        'portfolios': portfolios,
        'educations': educations,
        'skills': skills,
        'abouts': abouts,
        'services': services,
        'contacts': contacts,  
    }
    return render(request, 'index.html',context )