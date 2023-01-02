from django.db import models

# Create your models here.
class Portfolio(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.title
    
    
    
class Education(models.Model):
    institution = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.title
class Skills(models.Model):
    skill = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.title