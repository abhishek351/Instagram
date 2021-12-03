"""instagram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from instagramclone import views


from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login', views.login_user, name='login_user'),
    path('signup', views.signup, name='signup'),
    path('Profile/<int:pk>/', views.Profile, name='Profile'),
    path('Profile/<int:pk>/followers/add', views.follow, name='add-follower'),
    path('Profile/<int:pk>/followers/remove', views.remove, name='remove-follower'),
  
    path('add_comment/<int:pk>/',views.add_comment, name='add_comment'),
    path('post/<int:pk>/like',views.AddLike,name="like"),
    
  
    path('postcreate', views.postcreate, name='postcreate'),
    path('messages', views.messages, name='messages'),
    path('logout', views.logout_user, name='logout_user'),
    path('postshow', views.postshow, name='postshow'),
    path('edit', views.edit, name='edit'),
    path('passwordchange', views.passwordchange, name='passwordchange'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="reset_password.html"), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="password_reset_done.html"),name="password_reset_done"),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"),name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"),name="password_reset_complete"),
   


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


