"""
URL configuration for demo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include

import demoapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('demoapp/', include("demoapp.urls")),
    path('polls/', include("polls.urls")),
    path('goods/', include("goods.urls", namespace="goods")),      # 路由前缀的别名，也叫命名空间


    # 设置路由的第二种方式：直接在总路由配置
    # path('demoapp/', demoapp.views.index)

    # 请求参数的获取
    path('demorequest/', include("demorequest.urls")),   
    path('cookie/', include('mycookie.urls')),
    path('sess/', include("sess.urls")),     # session功能学习
    path('user/', include("user.urls")),
    path('tem/', include("tem.urls")),
    path('djdemo/', include("djdemo.urls")),
    path('bytedance/', include("bytedance.urls")),
    path('cbv/', include("cbv.urls")),
    path('student/', include("student.urls")),

]
