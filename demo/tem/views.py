import os.path
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

# Create your views here.
def index(request):
    """在视图中调用模版引擎提供的渲染函数实现前后端不分离"""
    # data = {"name":"习近平", "age":"25"}

    # return render(request, template_name="index.html", context=data)
    # return render(request, "index.html", data)

    # name = "赵乐际"
    # age = 55
    # return render(request, "index.html", locals())


    name = "张一鸣"
    age = 43

    # 判断是否有缓存页面，如果有缓存页面，就加载缓存页面
    from django.template.loader import get_template
    template_name = "index.html"
    # if os.path.exists(settings.BASE_DIR / "index.html"):
    if os.path.isfile(str(settings.BASE_DIR / "cache" / template_name)):
        with open("index.html", "r") as f:
            content = f.read()
    else:
        print("走了数据库")
        # 获取模版引擎对象
        template = get_template("index.html")
        # 使用模版引擎对象的渲染函数对模版进行渲染
        content = template.render(locals(), request)
        with open(f"cache/{template_name}", "w") as f:
            f.write(content)
    return HttpResponse(content)


def index2(request):

    data1 = {1, 2, 3}
    data2 = {1, 2, 3, 4}
    data3 = [1, 2, 3, 4, 5]

    data4 = {"name":"xiaowang", "age":"23"}
    data5 = settings

    book_list = [
        {"id": 10, "price": 9.90, "name": "python3入门到精通"},
        {"id": 10, "price": 9.90, "name": "python3入门到精通"}
    ]

    import time
    data6 = time 

    return render(request, "index.html", locals())

def index3(request):
    """使用模版引擎提供的标签完成判断/循环输出"""
    name = "root333"

    book_list = [
        {"id": 11, "name": "python基础入门1", "price": 130.21},
        {"id": 12, "name": "python基础入门2", "price": 130.22},
        {"id": 13, "name": "python基础入门3", "price": 130.23},
        {"id": 14, "name": "python基础入门4", "price": 130.24},
        {"id": 15, "name": "python基础入门5", "price": 130.25},
        {"id": 16, "name": "python基础入门6", "price": 130.26},
        {"id": 17, "name": "python基础入门7", "price": 130.27},
        {"id": 18, "name": "python基础入门8", "price": 130.28},
 
    ]
    return render(request, "index3.html", locals())


def index4(request):
    """模版分离技术"""
    return render(request, "index2.html", locals())


""" 模版继承技术 """
def user(request):
    """模版继承技术"""
    return render(request, "user.html", locals())

def home(request):
    """模版继承技术"""
    return render(request, "home.html", locals())

def goods(request):
    """模版继承技术"""
    return render(request, "goods.html", locals())

def index6(request):

    return render(request, "index6.html", locals())