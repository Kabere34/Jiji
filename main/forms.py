from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm

class SignupForm(UserCreationForm):
  email=forms.EmailField(max_length=250, help_text='Required. Inform a valid email address.')
  class Meta:
    model=User
    fields=('username','email','password1','password2')


class PostForm(forms.ModelForm):
  class Meta:
    model=Post
    exclude=["user"]

class BsnForm(forms.ModelForm):
  class Meta:
    model=Business
    exclude=["user", "neighbourhood"]

class HoodForm(forms.ModelForm):
  class Meta:
    model=Neighbourhood
    exclude=["user"]

class ProfileForm(forms.ModelForm):
  class Meta:
        model = Profile
        exclude = ('user', 'neighbourhood')
