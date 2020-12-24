"""MeterReader URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from MeterReaderApp import views

from django.views.static import serve
from django.conf.urls import url
from . import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login ,name='login'),
    path('register/', views.register, name='register'),
    path('test/', views.test, name='test'),
    path('new_user_request/', views.new_user_request ,name='new_user_request'),
    path('logout/', views.logout ,name='logout'),
    path('update_user_profile/', views.update_user_profile ,name='update_user_profile'),
    path('user_bill/', views.user_bill ,name='user_bill'),
    path('password/', views.password ,name='password'),
    path('user_register_view/', views.user_register_view ,name='user_register_view'),
    path('email_verification/', views.email_verification ,name='email_verification'),
    path('add_new_user_request/', views.add_new_user_request ,name='add_new_user_request'),
    path('Not_Verify_user/', views.Not_Verify_user ,name='Not_Verify_user'),
    path('search_user/', views.search_user ,name='search_user'),
    path('user_profile/', views.user_profile ,name='user_profile'),
    path('all_user/', views.all_user ,name='all_user'),
    path('AdminProfile/', views.AdminProfile ,name='AdminProfile'),
    path('AddAdmin/', views.AddAdmin ,name='AddAdmin'),
    path('complaints/', views.complaints ,name='complaints'),
    path('forgotpassword/', views.forgotpassword ,name='forgotpassword'),
    path('adminlogin/', views.adminlogin ,name='adminlogin'),
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),

]
handler404 = views.handler404
handler500 = views.handler500
