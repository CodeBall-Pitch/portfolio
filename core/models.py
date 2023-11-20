from django.db import models

# Create your models here.
class About(models.Model):
    aboutme=models.TextField()
    description=models.TextField()
    image=models.ImageField(upload_to='imgaes')
    
    def __str__ (self):
        return self.aboutme
    
    
class Services(models.Model):
    title=models.CharField()
    desription=models.TextField()
    
    def __str__ (self):
        return self.title