#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
import sys

def check_code(request):
    import io
    import check_code as CheckCode

    stream = io.BytesIO()
    # img图片对象,code在图像中写的内容
    img, code = CheckCode.create_validate_code()
    img.save(stream, "png")

    # 图片页面中显示,立即把session中的CheckCode更改为目前的随机字符串值
    request.session["CheckCode"] = code
    return HttpResponse(stream.getvalue(), "png")

    # 代码：生成一张图片，在图片中写文件
    # request.session['CheckCode'] =  图片上的内容

    # 自动生成图片，并且将图片中的文字保存在session中
    # 将图片内容返回给用户

def yanzhengma(request):
    import io
    import check_code as CheckCode

    stream = io.BytesIO()
    img, code = CheckCode.create_validate_code()
    img.save(stream, "png")
    request.session["CheckCode"] = code
    return HttpResponse(stream.getvalue())

def login(request):
    if request.method == 'POST':
        input_code = request.POST.get('check_code')
        print(input_code.upper(),request.session['CheckCode'].upper())
    return render(request, 'login.html')
