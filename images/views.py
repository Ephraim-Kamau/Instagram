from django.shortcuts import render,redirect,Http404
import datetime as dt
from .models import Image
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url='/accounts/login/')
def images_today(request):
    
    images = Image.objects.all()
    
    return render(request, 'today-images.html', {"images":images})


def past_images(request,past_date):
    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False    

    if date == dt.date.today():
       return redirect(images_today)

    return render(request, 'all-images/past-images.html', {"date": date,"images":images})

def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_articles = Article.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-images/search.html',{"message":message,"image": searched_image})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-images/search.html',{"message":message})    