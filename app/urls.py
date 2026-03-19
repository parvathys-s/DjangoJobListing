"""
URL configuration for multiuser project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from app import views
app_name = 'app'

urlpatterns = [
    path('',views.Home.as_view(),name='home'),
    path('adminhome',views.AdminHome.as_view(),name='adminhome'),
    path('userhome',views.UserHome.as_view(),name='userhome'),
    path('register',views.Register.as_view(),name='register'),
    path('login',views.Login.as_view(),name='login'),
    path('logout',views.Logout.as_view(),name='logout'),
    path('delete/<int:i>',views.Delete.as_view(),name='delete'),
    path('add',views.Add.as_view(),name='add'),
    path('update/<int:i>',views.Update.as_view(),name='update'),
]
