from django.shortcuts import render
from .models import *

# Create your views here.
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
