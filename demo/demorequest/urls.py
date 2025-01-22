
from django.urls import path, re_path

from . import views

# 创建子路由
urlpatterns = [
    # path("index/(\d+)/([a-z]+)", views.index, name="index"),
    path("index/<int:year>/<str:city>", views.index, name="index"),



]
