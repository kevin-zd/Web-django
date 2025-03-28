from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def set_session(request):
    """ 保存session """
    request.session["name"] = "xiaoming"
    request.session["id"] = 123

    return HttpResponse("set_session")

def get_session(request):
    """ 读取session """
    print(request.session)

    # 提取单个session
    print(request.session.get("name"))
    print(request.session.get("id"))

    # 提取所有session
    print(request.session.items())
    print(dict(request.session.items()))

    # 提取当前session的默认有效期
    print(request.session.get_session_cookie_age())   # 默认14天

    return HttpResponse("get_session")


def del_session(request):
    """ 删除session """

    # 删除单个session，使用pop删除不存在的session，会报错。所以加判断免报错
    # print(request.session.pop("name"))

    if request.session.get("name"):
        request.session.pop("name")

    # 方法二：删除单个指定名称的session
    try:
        request.session.pop("id")
    except KeyError:
        pass

    # 清空session
    request.session.clear()

    return HttpResponse("del_session")