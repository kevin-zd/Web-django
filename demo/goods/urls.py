
from django.urls import path, re_path

from . import views

# 创建子路由
urlpatterns = [
    path("", views.index, name="index"),

]
