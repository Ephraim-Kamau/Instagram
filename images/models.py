from django.db import models

# Create your models here.

class Profile(models.Model):
    bio = models.TextField()

class Comments(models.Model):
    comment = models.TextField()   

class Image(models.Model):
    name = models.CharField(max_length=30)
    caption = models.TextField()
    profile = models.ForeignKey(Profile)
    comments = models.ForeignKey(Comments)


 
