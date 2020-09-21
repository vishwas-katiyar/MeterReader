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
    path('register/', views.register ,name='register'),
    path('email_verification/', views.email_verification ,name='email_verification'),
    path('forgotpassword/', views.forgotpassword ,name='forgotpassword'),
    path('password/', views.password ,name='password'),
    path('dashboard/', views.dashboard ,name='dashboard'),
    path('adminlogin/', views.adminlogin ,name='adminlogin'),
    path('opencamera/', views.opencamera ,name='opencamera'),
    path('opencamera/success/', views.success ,name='success'),
    path('generated_bill/',views.generated_bill,name="generated_bill"),
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),

]
