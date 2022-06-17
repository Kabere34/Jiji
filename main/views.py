from django.shortcuts import render
from django.contrib.auth import login as user_login, authenticate
from django.shortcuts import render,redirect

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
