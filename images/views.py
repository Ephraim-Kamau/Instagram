from django.shortcuts import render,redirect,Http404
import datetime as dt
from .models import Image
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url='/accounts/login/')
def images_today(request):
    
    images = Image.objects.all()
    
    return render(request, 'today-images.html', {"images":images})

def profile(request):
    images = Image.objects.all()

    return render(request, 'profile.html', {"images":images})

def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_articles = Article.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-images/search.html',{"message":message,"image": searched_image})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-images/search.html',{"message":message})   

def edit(request):
    current_user_id=request.user.id
    profile=Profile.objects.filter(userId=current_user_id)
    if len(profile)<1:

        if request.method=='POST':
            form=EditProfile(request.POST,request.FILES)
            if form.is_valid():
                profile=form.save(commit=False)
                profile.userId=current_user_id
                profile.save()
            return redirect("profile")
        else:
            form=EditProfile()
            return render(request,"edit.html",{"form":form})
    else:
        if request.method=='POST':
            form=EditProfile(request.POST,request.FILES )
            if form.is_valid():
                profile=form.save(commit=False)
                bio=form.cleaned_data['bio']
                pic=form.cleaned_data['pic']
                update=Profile.objects.filter(userId=current_user_id).update(bio=bio,pic=pic)
                profile.userId=current_user_id
                profile.save(update)
            return redirect("profile")
        else:

            form=EditProfile()

            return render(request,"edit.html",{"form":form})   

def uploads(request):
    title='Upload'
    current_user=request.user
    current_user_id=request.user.id
    if request.method=='POST':
        form=PostImage(request.POST,request.FILES)
        if form.is_valid():
            image=form.save(commit=False)
            image.user=current_user
            image.userId=current_user_id
            image.profile=current_user_id
            image.save()
        return redirect("profile")
    else:
        form=PostImage()
    return render(request,"upload.html",{"title":title,"form":form})          