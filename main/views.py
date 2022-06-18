from django.shortcuts import render
from django.contrib.auth import login as user_login, authenticate
from django.shortcuts import render,redirect
from django.contrib.auth import login

from .models import *
from .forms import *
# Create your views here.

def signup(request):
  form=SignupForm()
  if request.method=="POST":
    form=SignupForm(request.POST)
    if form.is_valid():
      form.save()
      username=form.cleaned_data.get["username"]
      raw_password=form.cleaned_data.get["password"]
      user=authenticate(username=username,raw_password=raw_password)
      user_login=(request,user)
      return redirect('login')
    else:
      form=SignupForm()
  return render(request,'registration/signup.html',{'form':form})



def index(request):
  current_user=request.user
  posts=Post.objects.all()
  context={
    "posts":posts
  }
  return render(request,'main/index.html',context)

def hood(request):
  current_user=request.user
  hoods=Neighbourhood.objects.all()
  context={
    "hoods":hoods
  }
  return render(request,'main/hood.html',context)


def new_post(request):
  current_user=request.user
  if request.method == 'POST':
    form=PostForm(request.POST,request.FILES)
    if form.is_valid():
      post=form.save(commit=False)
      post.user=current_user
      post.save()
    return redirect('index')
  else:
    form=PostForm()
  return render(request, 'main/new_post.html',{ "form":form})

def new_bsn(request):
  current_user=request.user
  if request.method=='POST':
    form=BsnForm(request.POST,request.FILES)
    if form.is_valid():
      bsn=form.save(commit=False)
      bsn.user=current_user
      # bsn.neighbourhood=current_user
      bsn.save()
    return redirect('index')
  else:
    form=BsnForm()
  return render(request, 'main/new_bsn.html',{ "form":form})


def new_hood(request):
  form=HoodForm()
  current_user=request.user
  if request.method == 'POST':
    form=HoodForm(request.POST, request.FILES)
    if form.is_valid():
      hood=form.save(commit=False)
      hood.user=current_user
      hood.save()
    return redirect('hood')
  else:
    return render(request, 'main/new_hood.html',{ "form":form})


def profile(request):
  current_user = request.user
  print(current_user, 'heey')
  user=User.objects.all()
  profile=Profile.objects.filter(user=request.user.pk)
  print(profile, 'hello')
  context={
    "current_user": current_user,
    "profile": profile
  }
  return render(request, 'main/profile.html',context)
