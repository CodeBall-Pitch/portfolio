from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# Create your models here.
class About(models.Model):
    aboutme=models.TextField()
    description=models.TextField()
    image=models.ImageField(upload_to='imgaes')
    
    def __str__ (self):
        return self.aboutme
    
class Portfolio(models.Model):
    name=models.CharField(max_length=150)
    image = models.ImageField(upload_to='images')
    image_thumbnail = ImageSpecField(source='image',
                                      processors=[ResizeToFill(500, 500)],
                                      format='JPEG',
                                      options={'quality': 60})
    
    
class Education(models.Model):
    name=models.CharField(max_length=100)
    timeframe=models.CharField(max_length=100)
    description=models.TextField()
    
    def __str__ (self):
        return self.name
    
    
class Services(models.Model):
    
    title=models.CharField(max_length=100)
    desription=models.TextField()
    
    def __str__ (self):
        return self.title
    
    
class Client(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    name=models.CharField(max_length=100)
    subtitle=models.CharField(max_length=100)
    avatar_image=models.ImageField(upload_to='images')
    
    def __str__ (self):
        return self.title