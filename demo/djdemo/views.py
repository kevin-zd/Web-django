from django.shortcuts import render

# Create your views here.

def index1(request):

    num1 = 100
    num2 = 99.3
    num3 = 97.352

    return render(request, "index1.html", locals())