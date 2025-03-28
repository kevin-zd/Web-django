
from django.urls import path, re_path

from . import views


# 创建子路由
urlpatterns = [

    # path("路由url","视图函数","路由别名")

    path("set_session", views.set_session),
    path("get_session", views.get_session),
    path("del_session", views.del_session),
    

]
