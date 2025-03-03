from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.

def index(request):
    # 业务代码，调用数据，for循环之类的
    data = "okkkkk!!!"
    return HttpResponse(data)