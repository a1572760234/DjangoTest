from django.shortcuts import render
from django.http import HttpRequest,HttpResponse

# Create your views here.
# 视图,就是python函数
# 视图函数有两个要求:
#   1.接收请求,这个请求就是HttpRequest的类对象
#   2.必须返回一个响应

#我们期望用户访问/index/来访问视图函数
def index(request):
    return HttpResponse('ok')