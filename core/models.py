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
                                      processors=[ResizeToFill(100, 100)],
                                      format='JPEG',
                                      options={'quality': 60})
    
    
class Skills(models.Model):
    name=models.CharField(max_length=100)
    icon=models.ImageField(upload_to='Skills')
    
    def __str__ (self):
        return self.name
    
    
class Services(models.Model):
    title=models.CharField(max_length=100)
    desription=models.TextField()
    
    def __str__ (self):
        return self.title