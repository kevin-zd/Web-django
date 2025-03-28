
from django.urls import path, re_path

from . import views

# 创建子路由
urlpatterns = [
    path("", views.index, name="index"),
    path("index2", views.index2),
    path("index3", views.index3),
    path("index4", views.index4),
    path("index5", views.index5),
    path("index6", views.index6),
    path("index7", views.index7),
    path("index8", views.index8),
    path("index9", views.index9)

]
