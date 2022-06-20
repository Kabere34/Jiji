from django.urls import path,include
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
     path('signup/', views.signup, name='signup'),
     path('login/', views.login, name='login'),
     path('account/', include('django.contrib.auth.urls')),
     path('', views.index, name='index'),
     path('<hood_id>/new_post/', views.new_post, name='new_post'),
     path('new_hood/', views.new_hood, name='new_hood'),
     path('<hood_id>/members', views.hood_members, name='members'),
     path('profile/', views.profile, name='profile'),
     path('profile/<username>/edit/', views.edit_profile, name='edit-profile'),
     path('all_hoods/', views.hoods, name='all_hoods'),
     path('single_hood/<hood_id>', views.single_hood, name='single_hood'),
     path('join_hood/<id>', views.join_hood, name='join-hood'),
     path('leave_hood/<id>', views.leave_hood, name='leave-hood'),
     path('search_bsn/', views.search_bsn, name='search_bsn'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


