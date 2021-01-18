from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

from MyDjangoWeb import updata_mysql
from MyDjangoWeb.updata_mysql import inser_user_info
import tkinter
import tkinter.messagebox

#注册
def index(request):
    username = request.POST.get('username')
    psd = request.POST.get('password')
    #判断用户名是否存在
    boolean = updata_mysql.find_username(username)
    if boolean:
        updata_mysql.inser_user_data(username,psd)
        request.session['username'] = username
        return render(request, 'index.html')
    else:
        #弹窗提示
        root = tkinter.Tk()
        root.withdraw()
        tkinter.messagebox.showerror('提示','用户名已存在!!!')
        return render(request,'sign.html')
        root.mainloop()

#登录页
def login1(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    result = updata_mysql.sel_user_data(username,password)
    if result is True:
        #将用户存到session中
        request.session['username'] = username
        print("用户信息存在，登录成功")
        return render(request, 'index.html')
    else:
        print("用户信息错误！！！")
        return render(request,'erro.html')


def login(request):
    return render(request, 'login.html')

def sign(request):

    return render(request,'sign.html')

#录入用户个人信息
def lodding_user_info(request):
    user_info = {}
    user_info['name'] = request.POST.get("name")
    user_info['age'] = request.POST.get("age")
    user_info['sex'] = request.POST.get("sex")
    user_info['hobby'] = request.POST.get("hobby")
    user_info['city'] = request.POST.get("city")
    user_info['addr'] = request.POST.get("addr")
    boolen = inser_user_info(user_info)
    if boolen:
        return render(request,'success.html')
    else:
        return render(request,'erro.html')

