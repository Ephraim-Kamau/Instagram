from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url(r'^$',views.images_today,name='imagesToday'),
    url(r'^search/', views.search_results, name='search_results'),   
    url(r'^profile/', views.profile, name='profile'),
    url(r'uploads$',views.uploads,name='uploads'), 
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)