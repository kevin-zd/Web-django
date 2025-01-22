
from django.urls import path

from . import views

# 创建子路由
urlpatterns = [
    path("index", views.index, name="index"),
    path("indextwo", views.indextwo, name="indextwo")
]

