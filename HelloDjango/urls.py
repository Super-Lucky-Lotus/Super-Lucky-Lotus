"""HelloDjango URL Configuration

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
from django.urls import path,include
from app import views
from app import testdb

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('login/', views.login),
    # path('register/', views.register),
    path('profile/', views.profile),
    path('testdb/', testdb.testdb),
    path('get/', views.getMessage),
    path('post/', views.postMessage),
    path('upload/', views.uploadMessage),
    # path('accounts/', include('users.urls')),

# '^'代表开始， '/'代表结尾，'$'代表任意字符，如r'^$' 则代表默认首页路径
]