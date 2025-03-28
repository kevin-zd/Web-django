
from django.urls import path, re_path

from . import views
app_name = "goods"


# 创建子路由
urlpatterns = [
    path("", views.index, name="index"),
    path("index2", views.index2),
    path("index3", views.index3, name="index3"),
    path("index4", views.index4),
    path("index5", views.index5),
    path("index6", views.index6),
    path("index7", views.index7),
    path("index8", views.index8),
    path("index9", views.index9),
    path("index10", views.index10),
    path("index11", views.index11),
    path("index12", views.index12, name="index12")    # name 设置路由别名

]
