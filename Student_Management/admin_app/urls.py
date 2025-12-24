"""
URL configuration for Student_Management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hh',views.home,name="home"),
    path('home_redirect',views.home_redirect,name="home_redirect"),
    path('home1',views.home1,name="home1"),
    path('index',views.index,name="index"),
    path('data',views.data,name="data"),
    path('students',views.students,name="students"),
    path('marks',views.marks,name="marks"),
    path('index2',views.index2,name="index2"),
    path('teachers',views.teachers,name="teachers"),
    path('subject',views.subject,name="subject"),
    path('students',views.students,name="students"),
]       


