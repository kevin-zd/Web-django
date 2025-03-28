
from django.urls import path, re_path

from . import views


# 创建子路由
urlpatterns = [

    # path("路由url","视图函数","路由别名")

    path("index/", views.index),
    path("index2", views.index2),
    path("index3/", views.index3),
    path("index4/", views.index4),
    path("user/", views.user),
    path("home/", views.home),
    path("goods/", views.goods),
    path("index6/", views.index6)


    

]
