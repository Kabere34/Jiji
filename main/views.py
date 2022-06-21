from django.shortcuts import get_object_or_404, render
from django.contrib.auth import login as user_login, authenticate
from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *
# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})



def index(request):
  current_user=request.user
  posts=Post.objects.all()
  context={
    "posts":posts
  }
  return render(request,'main/index.html',context)


def hoods(request):
  all_hoods = Neighbourhood.objects.all()
  all_hoods = all_hoods[::-1]
  context = {
      'all_hoods': all_hoods,
  }
  return render(request, 'main/all_hoods.html', context)


@login_required(login_url='login')
def new_hood(request):
  form=HoodForm()
  current_user=request.user
  if request.method == 'POST':
    form=HoodForm(request.POST, request.FILES)
    if form.is_valid():
      hood=form.save(commit=False)
      hood.user_profile=current_user
      hood.save()
    return redirect('all_hoods')
  else:
    form=HoodForm()
  return render(request, 'main/new_hood.html',{ "form":form})

def single_hood(request,hood_id):

    hood = Neighbourhood.objects.get(id=hood_id)
    business = Business.objects.filter(neighbourhood=hood)
    posts = Post.objects.filter(hood=hood)
    posts = posts[::-1]
    if request.method == 'POST':
        form = BsnForm(request.POST)
        if form.is_valid():
            b_form = form.save(commit=False)
            b_form.neighbourhood = hood
            b_form.user = request.user
            b_form.save()
            return redirect('single_hood', hood.id)
    else:
        form = BsnForm()
    params = {
        'hood': hood,
        'business': business,
        'form': form,
        'posts': posts
    }
    return render(request, 'main/single_hood.html', params)

def hood_members(request,hood_id):
  hood=Neighbourhood.objects.get(id=hood_id)
  members=Profile.objects.filter(neighbourhood=hood)
  return render(request,'main/members.html',{"members":members})

@login_required(login_url='login')
def new_post(request,hood_id):
  hood=Neighbourhood.objects.get(id=hood_id)
  if request.method == 'POST':
    form=PostForm(request.POST,request.FILES)
    if form.is_valid():
      post=form.save(commit=False)
      post.hood=hood
      post.user=request.user.profile
      post.save()
    return redirect('single_hood',hood.id)
  else:
    form=PostForm()
  return render(request, 'main/new_post.html',{ "form":form})


@login_required(login_url='login')
def join_hood(request, id):
  neighbourhood = get_object_or_404(Neighbourhood, id=id)
  print (neighbourhood, 'neighbour')
  request.user.profile.neighbourhood = neighbourhood
  print (neighbourhood, 'neighbour save')
  request.user.profile.save()
  return redirect('all_hoods')


@login_required(login_url='login')
def leave_hood(request, id):
    hood = get_object_or_404(Neighbourhood, id=id)
    request.user.neighbourhood = None
    request.user.save()
    return redirect('all_hoods')


def profile(request, username):
    return render(request, 'main/profile.html')

@login_required(login_url='login')
def edit_profile(request, username):
    user = User.objects.get(username=username)
    print (username, 'hhhhhhhhhhhhhh')

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        print(request.user.profile, 'jjjjjjjjjjjj')
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'main/editprofile.html', {'form': form})


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


def search_bsn(request):
  if "business" in request.GET and request.GET["business"]:
    search_term = request.GET.get["business"]
    searched_business=Business.search_by_name(search_term)
    message=f"{search_term}"
    context={
      "searched_business": searched_business,
      "message": message
    }
    return render(request,'main/search.html',context)
  else:
    message="You haven't searched for any business"
    return render(request,'main/search.html',{"message": message})
