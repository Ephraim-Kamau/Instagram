from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile,Comments,Image

# Create your tests here.
class TestProfile(TestCase):
    def setUp(self):
        self.ephraim=Profile(image="gtr.jpg",bio="fast")

    def test_save(self):
        self.ephraim.save_profile()
        prof=Profile.objects.all()
        self.assertTrue(len(prof)>0)

    def test_delete(self):
        self.ephraim.delete_profile()
        prof=Profile.objects.all()
        self.assertEqual(len(prof),0)    
   

class TestImage(TestCase):
    def setUp(self):
        self.comment=Comments(image=1,comment='this is dope')

    def test_instance(self):
        self.assertTrue(isinstance(self.comment,Comments))

    def test_image_save(self):
        self.image.save_image()
        prof=Image.objects.all()
        self.assertTrue(len(prof)>0)    

  