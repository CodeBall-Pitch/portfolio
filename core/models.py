from django.db import models

# Create your models here.
class About(models.Model):
    aboutme=models.TextField()
    description=models.TextField()
    image=models.ImageField(upload_to='imgaes')
    
    def __str__ (self):
        return self.aboutme
    
    
class Skills(models.model):
    name=models.CharField(max_length=100)
    icon=models.ImageField(upload_to='Skills')
    
    def __str__ (self):
        return self.name
    
    
class Services(models.Model):
    title=models.CharField(max_length=100)
    desription=models.TextField()
    
    def __str__ (self):
        return self.title