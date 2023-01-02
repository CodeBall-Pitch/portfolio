from django.urls import path
from .views import Home


app_name='portfolio'


urlpatterns = [
    path('', Home, name='home'),
]