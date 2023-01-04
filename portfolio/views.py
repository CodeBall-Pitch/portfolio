from django.shortcuts import render
from  .models import Portfolio, Education, Skills, About, Services, Contact
# Create your views here.
def Home(request):
    portfolios = Portfolio.objects.all()
    educations = Education.objects.all()
    skills = Skills.objects.all()
    abouts = About.objects.all()
    services = Services.objects.all()
    contacts = Contact.objects.all()
        
    data={
        'portfolios': portfolios,
        'educations': educations,
        'skills': skills,
        'abouts': abouts,
        'services': services,
        'contacts': contacts,
    }
    return render(request, 'index.html',data)