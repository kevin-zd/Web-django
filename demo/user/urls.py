
from django.urls import path, re_path

from . import views, converters


# 创建子路由
urlpatterns = [

    # path("url路径","视图函数/视图类", name="路由别名")
    path("index", views.index),

    # re_path(r"^url路径/(?P<参数变量名>正则模式)/$", 视图函数/视图类)
    re_path(r"^info/(?P<id>\d+)/$", views.info),
    re_path(r"^goods/(?P<cat_id>\d+)/(?P<attr_id>\d+)/$", views.goods),

    path("img/", views.img),
    path("rev/<int:num>/", views.inbuild_reverse),
    path("rev/<uuid:ustr>/", views.inbuild_uuid),
    path("rev/<str:content>/", views.inbuild_content),
    # path("rev/<uuid:ustr>/", views.inbuild_uuid),     # str会保护uuid的模式，避免str和uuid同时使用时，str必须写在后面

    path("rev2/<mob:mobile>/", views.setting_reverse),    # 自定义路由转换器，注意被前面的覆盖

]
