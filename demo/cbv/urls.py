
from django.urls import path, re_path

from . import views


# 创建子路由
urlpatterns = [

    # path("路由url","视图函数","路由别名")
    # django类视图的路由绑定
    # path("路径/", views.视图类名.as_view()),   # as_view获取客户端本次HTTP请求，POST，GET，PUT
    path("user/", views.UserView.as_view()),   # as_view获取客户端本次HTTP请求，POST，GET，PUT
    

]
