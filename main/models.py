
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Neighbourhood(models.Model):
  name = models.CharField(max_length=50)
  location=models.CharField(max_length=50,default="e.g Nairobi, Juja, Kiambu etc")
  occupants=models.IntegerField(default=0,blank=True)
  admin = models.ForeignKey("Profile", on_delete=models.CASCADE, related_name='hood')
  hood_img=models.ImageField(upload_to='hood_images/')
  description = models.TextField()
  health_tell = models.IntegerField(null=True, blank=True)
  police_number = models.IntegerField(null=True, blank=True)

  def __str__(self):
    return f'{self.name} jiji'

  def create_neighborhood(self):
        self.save()

  def delete_neighborhood(self):
        self.delete()



class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
  name= models.CharField(max_length=50)
  bio= models.CharField(max_length=250, blank=True,default="My Bio")
  avatar=models.ImageField(upload_to='avatars/', default='default.png')
  location=models.CharField(max_length=50, blank=True, null=True)
  neighbourhood=models.ForeignKey(Neighbourhood, on_delete=models.SET_NULL,null=True,related_name='members', blank=True)

  def __str__(self):
    return f'{self.user.username} profile'


class Business(models.Model):
  name = models.CharField(max_length=60)
  description=models.TextField()
  email = models.EmailField(max_length=70, blank=True)
  neighbourhood= models.ForeignKey(Neighbourhood,on_delete=models.CASCADE,related_name='business',null=True)
  user=models.ForeignKey(User, on_delete=models.CASCADE,related_name='owner')

  def __str__(self):
        return f'{self.name} Business'

  @classmethod
  def search_by_name(cls, search_term):
    business=cls.objects.filter(name__icontains=search_term)
    return business

class Post(models.Model):
  title=models.CharField(max_length=120, null=True)
  post=models.TextField()
  date=models.DateTimeField(auto_now_add=True)
  user=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
  image=models.ImageField(upload_to='images',null=True)
  hood=models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, null=True)
