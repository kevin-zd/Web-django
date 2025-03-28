from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.

def set_cookie(request):

    """ 设置cookie """
    response = HttpResponse("set_cookie")
    response.set_cookie("name", "xiaoming", max_age=30)   # max_age  设置过期时间
    return response

def get_cookie(request):

    """ 读取cookie """
    print(request.COOKIES)
    print(request.COOKIES.get("name"))
    return HttpResponse("get_cookie")


def del_cookie(request):
    """ 删除cookie """
    response = HttpResponse("del_cookie")
    response.set_cookie("name", "xiaoming", max_age=0)
    return response