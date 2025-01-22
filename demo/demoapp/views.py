from django.http import HttpResponse
from django.urls import reverse


# Create your views here.

# 创建视图函数
def index(request):

    # 获取当前的路由是多少 namespace name
    # 1. 有namespace
    # print(reverse("demoapp:index"))
    
    # 2.没有namespace
    print(reverse('index'))

    # 返回响应对象
    return HttpResponse('这是第一个子应用的视图函数功能展示')


# 创建视图函数
def indextwo(request):

    # 返回响应对象
    return HttpResponse('这是第二个子应用的视图函数功能展示')
