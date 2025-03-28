# forms.py
from django import forms

class MyForm(forms.Form):
    leg_name = forms.CharField(label='法定姓名', max_length=100)
    com_name = forms.CharField(label='法定姓名')
    mobile = forms.CharField(label='个人电话')
    gender = forms.CharField(label='性别')
    email = forms.EmailField(label='邮箱')
    age = forms.IntegerField(label='年龄')
    bio = forms.CharField(label='个人简介')
    region = forms.CharField(label='国家/地区')
    
