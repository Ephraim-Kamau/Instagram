from django.db import models
import datetime as dt

# Create your models here.

class Profile(models.Model):
    bio = models.TextField()

class Comments(models.Model):
    comment = models.TextField()   

class Image(models.Model):
    name = models.CharField(max_length=30)
    caption = models.TextField()
    profile = models.ForeignKey(Profile, blank =True)
    comments = models.ForeignKey(Comments, blank =True)
    pub_date = models.DateTimeField(auto_now_add=True)
    image_image = models.ImageField(upload_to = 'pix/')

    @classmethod
    def search_by_name(cls,search_term):
        images = cls.objects.filter(title__icontains=search_term)
        return images


 
