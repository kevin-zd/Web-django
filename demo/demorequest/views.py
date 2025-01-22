from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
"""
# 2.1 URL 路径参数 案例
def index(request, year, city):

    # 1.接收从路径传入的参数
    print("年份:{}".format(year))
    print("城市:{}".format(city))

    # 返回的响应对象
    return HttpResponse('请求对象 request：路径传惨/10/100/xiaoming')
"""

"""
# 2.2 查询字符串query string
def index(request, year, city):
    
    # 1.接收查询参数 request.GET --> QueryDict
    params = request.GET
    
    # 取出 key A的值，如果值有多个，返回最后一个
    result = params.get('a')

    # 取出A对象的多值
    result = params.get_list('a')
    print(result)

    # print(params)
    
    # 返回的响应对象
    return HttpResponse('请求对象 request：查询参数：?a=1&b=2&c=3')
"""
def index(request, year, city):
    
    # 接收从请求体，传过来的form表单参数
    form_data = request.POST

    print(form_data)
    
    
    # 返回的响应对象
    return HttpResponse('请求对象 request：请求体-form:')