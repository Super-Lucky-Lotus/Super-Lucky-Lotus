import json
import os

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

from HelloDjango.settings import BASE_DIR
from app.models import User


def index(request):
    return render(request , 'Base.html')

# def login(request):
#     return render(request, 'login.html')
#
# def register(request):
#     return render(request, 'regiseter.html')

def profile(request):
    return render(request,'profile.html')

def getMessage(request):
    if (request.method == 'GET'):
        print("parseData : " + "get data !")
        # 用get方式请求数据
        username = request.GET.get('username', "")
        password = request.GET.get('password', "")
        email = request.GET.get('email', "")
        phone = request.GET.get('phone', "")

        user = User()
        user.username = username
        user.password = password
        user.email = email
        user.phone = phone

        # 保存一条用户数据
        user.save()
        print("getData",
              "username : " + username + ":password : " + password + ":email : " + email + ":phone:" + phone)
        # 作为json 数组返回给客户端
        data = {}
        data['username'] = username
        data['password'] = password
        data['email'] = email
        data['phone'] = phone

        list = {}
        list['data'] = data
        list['state'] = 1
        list['msg'] = "Get 正常"
        response = json.dumps(list,ensure_ascii=False)
        print(response)
        return HttpResponse(response)

def postMessage(request):
    if(request.method == 'POST'):
        print("parseData : " + "post data !")
        # postBody = request.body
        username = request.POST.get('username', "")
        password = request.POST.get('password', "")
        email = request.POST.get('email', "")
        phone = request.POST.get('phone', "")

        user = User()
        user.username = username
        user.password = password
        user.email = email
        user.phone = phone

        #添加保存到数据库
        user.save()
        print("cx postData" , "username : " + user.username +":password : " + user.password + ":email : " + user.email + ":phone:" + user.phone)
        #作为json 数组返回给客户端
        data = {}
        data['username'] = user.username
        data['password'] = user.password
        data['email'] = user.email
        data['phone'] = user.phone

        list = {}
        list['data'] = data
        list['state'] = 1
        list['msg'] = "Post 正常"
        response = json.dumps(list, ensure_ascii=False)
        return HttpResponse(response)

def uploadMessage(request):
    if(request.method == 'POST'):
        print("parseData : " + "post data !")
        myFile = request.FILES.get("filename", None)

        list = {}
        list['state'] = 1
        list['msg'] = "Post 正常，服务端已收到文件"
        response = json.dumps(list, ensure_ascii=False)
        return HttpResponse(response)

