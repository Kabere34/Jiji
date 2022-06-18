from django.urls import path,include
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
     path('signup/', views.signup, name='signup'),
     path('login/', views.login, name='login'),
     path('account/', include('django.contrib.auth.urls')),
     path('', views.index, name='index'),
     path('hood/', views.hood, name='hood'),
     path('new_post/', views.new_post, name='new_post'),
     path('new_bsn/', views.new_bsn, name='new_bsn'),
     path('new_hood/', views.new_hood, name='new_hood'),
     path('profile/', views.profile, name='profile'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


