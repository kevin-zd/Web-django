from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):

    return HttpResponse("ok index正则")


def info(request, id):
    # id = 100
    return HttpResponse(f"id={id}的用户资料")


def goods(request, cat_id, attr_id):
    return HttpResponse(f"cat_id={cat_id}, attr_id={attr_id}")

""" 关于url路径末尾是否加/的说明 
前后端不分离情况下，加了斜杠会导致客户端使用相对路径的静态资源会以/末段作为目录起点，导致静态资源路径发送变化
前后端分离情况下，实际上加不加斜杠没什么影响

"""
def img(request):
    return HttpResponse("<img src='./1.png'>")


""" 路由转换器 """
def inbuild_reverse(request, num):
    """内置路由转换器"""
    return HttpResponse(f"num={num}")


def inbuild_content(request, content):
    """内置路由转换器"""
    return HttpResponse(f"content={content}")

def inbuild_uuid(request, ustr):
    return HttpResponse(f"ustr={ustr}")



def setting_reverse(request, mobile):
    """自定义路由转换器"""
    return HttpResponse(f"mobile={mobile}")