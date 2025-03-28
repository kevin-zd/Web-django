
from django.urls import path, re_path

from . import views
app_name = "cookie"

# 创建子路由
urlpatterns = [
    # path("", views.index, name="index"),
    path("set", views.set_cookie),
    path("get", views.get_cookie),
    path("del", views.del_cookie)
    

]
