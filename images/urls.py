from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.images_today,name='imagesToday'),
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_images,name = 'pastImages')
]