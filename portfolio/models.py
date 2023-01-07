from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
# Create your models here.
class Portfolio(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=200)
    image_thumbnail = ImageSpecField(source='image',
                                        processors=[ResizeToFill(100, 50)],
                                        format='JPEG',
                                        options={'quality': 60})


    def __str__(self):
        return self.name
    
class Services(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=200)
    image_service = ImageSpecField(source='image',
                                        processors=[ResizeToFill(100, 50)],
                                        format='JPEG',
                                        options={'quality': 60})


    def __str__(self):
        return self.title
    
class Education(models.Model):
    institution = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=200)
    image_education = ImageSpecField(source='image',
                                        processors=[ResizeToFill(100, 50)],
                                        format='JPEG',
                                        options={'quality': 60})


    def __str__(self):
        return self.institution
class Skills(models.Model):
    course_name=models.CharField(max_length=200)
    percentage=models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
    
class About(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=200)
    image_about = ImageSpecField(source='image',
                                        processors=[ResizeToFill(100, 50)],
                                        format='JPEG',
                                        options={'quality': 60})


    def __str__(self):
        return self.name
    

    
class Contact(models.Model):
        phone = models.CharField(max_length=200)
        email = models.CharField(max_length=200)
        subject = models.CharField(max_length=200)
        description = models.CharField(max_length=200)
        
        def __str__(self):
            return self.email
        
        
class Blog(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=200)
    image_blog = ImageSpecField(source='image',
                                        processors=[ResizeToFill(100, 50)],
                                        format='JPEG',
                                        options={'quality': 60})
        

    def __str__(self):
        return self.title