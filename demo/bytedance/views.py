from django.shortcuts import render
from django.http import JsonResponse
import requests
# Create your views here.
from .forms import MyForm

def index(request):

    # return HttpResponse("hello")

    print(request)

    return render(request, "bytedance.html", locals())


def submit(request):

    print(request.body)

    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            # 获取表单数据
            leg_name = form.cleaned_data['leg_name']
            com_name = form.cleaned_data['com_name']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']
            gender = form.cleaned_data['gender']
            bio = form.cleaned_data['bio']
            mobile = form.cleaned_data['mobile']
            region = form.cleaned_data['region']
            # 进行后续处理（如保存到数据库等）
            print(leg_name)
            print(email)
            print(age)
            print(bio)
            print(mobile)
            
            return render(request, "submit.html", locals())
            # return render(request, 'success.html', {'name': name, 'email': email})
    else:
        form = MyForm()

    return render(request, "submit.html", locals())


def post_data(request):
    if request.method == 'POST':
        # 目标 URL
        url = 'https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal'
        
        # 准备请求体数据，包括 app_secret
        data = {
            'app_secret': 'uYlti7bnCm6ni8tanSRY1e2wkjTOLSO5',  # 替换为你的 app_secret
            'app_id': 'cli_a281ffc317b8d00e',
            'param1': request.POST.get('msg'),  # 获取其他参数
            'param2': request.POST.get('tenant_access_token'),
        }

        # 发送 POST 请求，使用 JSON 格式发送数据
        response = requests.post(url, json=data)
        print(response)

        # 检查响应状态
        if response.status_code == 200:
            response_data = response.json()  # 将响应内容解析为 JSON
            print('response请求数据：', response_data)
            return JsonResponse(response_data)  # 返回 JSON 响应
        else:
            return JsonResponse({'error': '无法获取数据'}, status=response.status_code)
        
    
    return JsonResponse({'error': '只支持 POST 请求'}, status=400)


def fetch_data(request):
    if request.method == 'GET':
        # 目标 URL
        url = 'https://open.feishu.cn/open-apis/hire/v1/applications/'  # 替换为你的目标 URL
        
        # 你的 token 值
        token = 't-g1043jlOXG4GR66CY6REAZOVPMG4ACQIABEYYSWK'  # 替换为你的 token
        
        # 设置请求头，包含 Authorization
        headers = {
            'Authorization': f'Bearer {token}',  # 使用 Bearer 认证
            'Content-Type': 'application/json',   # 设置内容类型
        }

        # 获取请求参数
        param1 = request.GET.get('application_id', '7182193854001727805')

        # 发送 GET 请求
        response = requests.get(url, headers=headers,  params=param1)
        print('response获取的数据:', response)

        # 检查响应状态
        if response.status_code == 200:
            response_data = response.json()  # 将响应内容解析为 JSON
            print(response_data)
            # return JsonResponse(response_data)  # 返回 JSON 响应
            items = response_data.items
            return render(request, "submit.html", locals())
        else:
            return JsonResponse({'error': '无法获取数据'}, status=response.status_code)
    
    # return JsonResponse({'error': '只支持 GET 请求'}, status=400)
    return render(request, "submit.html", locals())


