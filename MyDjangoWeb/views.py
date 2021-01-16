from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from MyDjangoWeb import updata_mysql


def index(request):
    username = request.POST.get('username')
    psd = request.POST.get('password')
    updata_mysql.inser_user_data(username,psd)
    info = {
        "username": username,
        "password": psd
    }
    return render(request, 'index.html', info)

#登录页
def login1(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    info = {
        "username":username,
        "password":password
    }
    result = updata_mysql.sel_user_data(username,password)
    if result is True:
        print("用户信息存在，登录成功")
        return render(request, 'index.html',info)
    else:
        print("用户信息错误！！！")
        return render(request,'erro.html')


def login(request):
    return render(request, 'login.html')

def sign(request):

    return render(request,'sign.html')