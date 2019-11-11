"""project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import include, re_path
from django.contrib.auth import views as auth_views

from s3objects.views import home, account, upload_file, update_file, delete_file, register

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^$', home, name='home'),
    re_path(r'^login/$', auth_views.LoginView.as_view(template_name='s3objects/registration/login.html'), name='login'),
    re_path(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    re_path(r'^oauth/', include('social_django.urls', namespace='social')),
    re_path(r'^account_detail/', account, name='account_detail'),
    re_path(r'^upload_file/$', upload_file, name='upload_file'),
    re_path(r'^update_file/(?P<id>[\w-]+)/$', update_file, name='update_file'),
    re_path(r'^delete_file/(?P<id>[\w-]+)/$', delete_file, name='delete_file'),
    re_path(r'^accounts/$', include('django.contrib.auth.urls')),
    re_path(r'^register/$', register, name='register')
]