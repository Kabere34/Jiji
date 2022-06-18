from django.shortcuts import render
from django.contrib.auth import login as user_login, authenticate
from django.shortcuts import render,redirect
from django.contrib.auth import login

from .models import *
from .forms import *
# Create your views here.

def signup(request):
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



def hood(request):
  current_user=request.user
  hoods=Neighbourhood.objects.all()
  context={
    "hoods":hoods
  }
  return render(request,'main/hood.html',context)
