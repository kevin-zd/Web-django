
from django.urls import path, re_path

from . import views


# 创建子路由
urlpatterns = [

    # path("路由url","视图函数","路由别名")

    path('student/', views.StudentView.as_view())
    

]
