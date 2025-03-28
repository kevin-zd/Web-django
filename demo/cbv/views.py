from django.views import View
from django.http.response import HttpResponse


class UserView(View):
    def post(self, request):
        """ 添加操作 """
        return HttpResponse("User-->post")
    

    def get(self, request):
        """ 获取操作 """
        return HttpResponse("User-->get")
    

    def put(self, request):
        """ 更新操作 """
        return HttpResponse("User-->put")
    
    def patch(self, request):
        """ 更新操作 """
        return HttpResponse("User-->patch")
    
    def delete(self, request):
        """ 删除操作"""
        return HttpResponse("User-->delete")