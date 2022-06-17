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
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


