from django.shortcuts import render,redirect,Http404
import datetime as dt

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def images_today(request):
    date = dt.date.today()
    return render(request, 'all-images/today-images.html', {"date": date,})


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

    return render(request, 'all-images/past-images.html', {"date": date})