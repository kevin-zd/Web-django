from django.http import QueryDict
from django.shortcuts import render
from django.http.response import HttpResponse
from django.http.response import JsonResponse

# Create your views here.
# QueryDict
def index(request):
    print(request.GET)

    # 获取单个查询参数
    print(request.GET.get("name"))
    print(request.GET.get("pwd"))

    # 获取多个查询参数，结果是一个列表
    print(request.GET.getlist("lve"))

    # 当客户端没有传递参数时，可以使用get或者getlist的第二个参数default设置默认中
    print(request.GET.get("size", 0))

    # 业务代码，调用数据，for循环之类的
    data = "okkkkk!!!   坚持，相信可以学会的"
    return HttpResponse(data)

def index2(request):
    # 获取请求体数据，注意：request.POST只能获取POST的请求体，不能获取PUT/PATCH的请求体
    # print(request.POST)

    #  获取耽搁属性值
    # print(request.POST.get("name"))
    # print(request.POST.get("age"))
    # print(request.POST.get("pwd"))
    # print(request.GET)

    # # 获取多个属性值
    # print(request.POST.getlist("lve"))

    # request.body 获取请求体数据
    print(request.body)

    # 接收客户端发送的json的格式
    import json
    data = json.loads(request.body)
    print(data)

    return HttpResponse("ok index2")


def index3(request):

    """ 获取包括系统环境，客户端环境和http请求的请求头等元信息 """
    # print(request.META)   # 获取原生请求头
    # print(request.method)  # 获取客户端的请求方法

    """ 获取http请求中的请求头 """
    # print(request.headers)
    """
    {   'Content-Length': '', 
        'Content-Type': 'text/plain', 
        'Host': '127.0.0.1:8000', 
        'Connection': 'keep-alive', 
        'Sec-Ch-Ua': '"Not(A:Brand";v="99", 
        "Google Chrome";v="133", "Chromium";v="133"', 
        'Sec-Ch-Ua-Mobile': '?0', 
        'Sec-Ch-Ua-Platform': '"macOS"', 
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 
        'Sec-Fetch-Site': 'none', 
    }
    """

    """ 获取自定义的http请求头"""
    print(request.META.get("HTTP_COMPANY"))
    print(request.headers.get("company"))
    return HttpResponse("ok, goods index3")


def index4(request):

    """ 获取客户端上传的文件 可以接收多个文件"""
    print(request.FILES)     # request.FILES只能接受POST请求上传的文件，其他请求无法获取
    # file = request.FILES.get("avatar")
    # print(file, type(file))

    # 一次性处理多个上传文件
    import os
    print(os.path.dirname(__file__))
    for file in request.FILES.getlist("avatar"):
        with open(f"{os.path.dirname(__file__)}/{file.name}", "wb") as f:
            f.write(file.read())
        print(file.name)

    return HttpResponse("ok, index4文件上传")


def index5(request):

    """ 响应： html数据 """
    return HttpResponse("<h1>html代码</h1>", content_type="text/html")

import json

def index6(request):
    """ 响应 json数据"""
    # 字典格式
    data = {
        "id": 101,
        "title": "《浪潮之巅》",
        "content": "程序猿的一天生活",
        "price": 9.9
    }

    # 列表格式
    data2 = [
        {"id": 1, "name": "小明"},
        {"id": 2, "name": "小灰"},
    ]

    json_data = json.dumps(data)
    json_data2 = json.dumps(data2)

    return HttpResponse(content=json_data2, content_type="text/json")


def index7(request):
    """ 直接返回json数据 """
    # 字典格式
    data = {
        "id": 101,
        "title": "《浪潮之巅》",
        "content": "程序猿的一天生活",
        "price": 9.9
    }

    # 列表格式
    data2 = [
        {"id": 1, "name": "小明"},
        {"id": 2, "name": "小灰"},
    ]
    # JsonResponse 并不直接支持列表转换成json格式，需要关闭安全监测，把safe参数的值设置为False
    # return JsonResponse(data)
    return JsonResponse(data2, safe=False)


def index8(request):
    """ 返回图片格式信息 """
    with open("./tian.png", "rb") as f:
        img = f.read()
    return HttpResponse(content=img, content_type="image/png")


def index9(request):
    """ 返回压缩包格式 """
    import os
    with open(f"{os.path.dirname(__file__)}/code.zip", "rb") as f:
        content = f.read()
    return HttpResponse(content, content_type="application/zip")

def index10(request):
    """ 自定义响应头 """
    response = HttpResponse("ok index10")
    response["company"] = "baidu"
    return response


""" 跳转/重定向 """
from django.http.response import HttpResponseRedirect
def index11(request):

    response = HttpResponse(status=301)
    response["Location"] = "https://www.163.com"
    return response

    # return HttpResponseRedirect("https://www.qq.com")

""" 站内跳转 """
from django.shortcuts import redirect
from django.urls import reverse
def index12(request):
    # 除了要跳转正则路由以外，其他路径直接写上去即可，不需要使用reverse进行解析
    url = reverse("goods:index3")   # reverse("namespace:name") namespace就是路径的前缀命名空间，name就是路径别名
    return redirect(url)

    # return redirect("/goods/index3")