from django.shortcuts import render
from  .models import Portfolio, Education, Skills, About, Services, Contact
# Create your views here.
def Home(request):
   
    return render(request, 'index.html',data)