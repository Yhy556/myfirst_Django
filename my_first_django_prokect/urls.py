"""my_first_django_prokect URL Configuration

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

from MyDjangoWeb import views
#配置前端路径，访问的对应的方法
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',views.index),    #首页
    path('login/',views.login),
    path('',views.login),
    path('sign/',views.sign),
    path('login1/',views.login1),
    path('lodding_user_info/',views.lodding_user_info),

]
