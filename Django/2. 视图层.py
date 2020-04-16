#__author__ = 'Winston'
#date: 2020/4/10
# 视图函数，简称视图，属于Django的视图层，默认定义在views.py文件中，
# 是用来处理web请求信息以及返回响应信息的函数，所以研究视图函数只需熟练掌握两个对象即可：
# 请求对象(HttpRequest)和响应对象(HttpResponse)

# django将http协议请求报文中的请求行、首部信息、
# 内容主体封装到了HttpRequest对象中（类似于我们自定义框架的environ参数）。
# django会将HttpRequest对象当做参数传给视图函数的第一个参数request，
# 在视图函数中，通过访问该对象的属性便可以提取http协议的请求数据

# HttpRequest对象常用属性part1

# 一.HttpRequest.method
# 　　获取请求使用的方法（值为纯大写的字符串格式）。例如："GET"、"POST"
#    应该通过该属性的值来判断请求方法
#
# 二.HttpRequest.GET
# 　　值为一个类似于字典的QueryDict对象，封装了GET请求的所有参数，可通过HttpRequest.GET.get('键')获取相对应的值
#
# 三.HttpRequest.POST
#    值为一个类似于字典的QueryDict对象，封装了POST请求所包含的表单数据，可通过HttpRequest.POST.get('键')获取相对应的值
#
#    针对表单中checkbox类型的input标签、select标签提交的数据，键对应的值为多个，需要用：HttpRequest.POST.getlist("hobbies")获取存有多个值的列表,同

# from django.urls import re_path
# from app01 import views
#
# urlpatterns = [
#     re_path(r'^login/$',views.login),
# ]

# from django.shortcuts import render,HttpResponse
#
# def login(request):
#     if request.method == 'GET':
#         # 当请求url为：http://127.0.0.1:8001/login/?a=1&b=2&c=3&c=4&c=5
#         # 请求方法是GET，?后的请求参数都存放于request.GET中
#         print(request.GET)
#         # 输出<QueryDict: {'a': ['1'], 'b': ['2'], 'c': ['3', '4', '5']}>
#
#         # 获取？后参数的方式为
#         a=request.GET.get('a') # 1
#         b=request.GET.get('b') # 2
#         c=request.GET.getlist('c') # ['3', '4', '5']
#
#         return render(request,'login.html')
#     elif request.method == 'POST':
#         # 在输入框内输入用户名egon、年龄18，选择爱好，点击提交
#         # 请求方法为POST，表单内的数据都会存放于request.POST中
#         print(request.POST)
#         # 输出<QueryDict: {..., 'name': ['egon'], 'age': ['18'], 'hobbies': ['music', 'read']}>
#
#         # 获取表单中数据的方式为
#         name=request.POST.get('name') # egon
#         age=request.POST.get('age') # 18
#         hobbies=request.POST.getlist('hobbies') # ['music', 'read']
#
#         return HttpResponse('提交成功')

# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <title>登录页面</title>
# </head>
# <body>
#
# <!--
# method="post"代表在提交表单时会以POST方法提交表单数据
# action="/login/" 代表表单数据的提交地址为http://127.0.0.1:8001/login/,可以简写为action="/login/",或者action=""
# -->
# <form action="http://127.0.0.1:8001/login/" method="post">
#     {% csrf_token %} <!--强调：必须加上这一行，后续我们会详细介绍-->
#     <p>用户名：<input type="text" name="name"></p>
#     <p>年龄：<input type="text" name="age"></p>
#     <p>
#         爱好：
#         <input type="checkbox" name="hobbies" value="music">音乐
#         <input type="checkbox" name="hobbies" value="read">阅读
#         <input type="checkbox" name="hobbies" value="dancing">跳舞
#     </p>
#     <p><input type="submit" value="提交"></p>
#
# </form>
# </body>
# </html>

# HttpRequest对象常用属性part2

# 一.HttpRequest.body
#    当浏览器基于http协议的POST方法提交数据时，数据会被放到请求体中发送给django，django会将接收到的请求体数据存放于HttpRequest.body属性中，因为该属性的值为Bytes类型，所以通常情况下直接处理Bytes、并从中提取有用数据的操作是复杂而繁琐的，好在django会对它做进一步的处理与封装以便我们更为方便地提取数据，比如
#    对于form表单来说，提交数据的常用方法为GET与POST
#    1：如果表单属性method='GET',那么在提交表单时，表单内数据不会存放于请求体中，而是会将表单数据按照k1=v1&k2=v2&k3=v3的格式放到url中，然后发送给django，django会将这些数据封装到request.GET中，注意此时的request.body为空、无用
#    2：如果表单属性method='POST'，那么在提交表单时，表单内的所有数据都会存放于请求体中，在发送给django后会封装到request.body里，此时django为了方便我们提取数据，会request.body的数据进行进一步的处理，具体如何处理呢，需要从form表单提交数据的编码格式说起：
# 	form表单对提交的表单数据有两种常用的编码格式，可以通过属性enctype进行设置，如下
#     编码格式1(默认的编码格式):enctype="application/x-www-form-urlencoded"
#     编码格式2(使用form表单上传文件时只能用该编码):enctype="multipart/form-data"
#     如果form表单提交数据是按照编码格式1,那么request.body中数据的格式类似于GET方法的数据格式，如k1=v1&k2=v2，此时django会将request.body中的数据提取出来封装到request.POST中方便我们提取
#     如果form表单提交数据是按照编码格式2,那么request.body中数据的格式为b'------WebKitFormBoundaryKtcwuksQltpNprep\r\nContent-Disposition: form-data;......',，此时django会将request.body中的数据提取出来封装到request.POST中，将上传的文件数据专门提取出来封装到request.FILES属性中
#     强调：毫无疑问，编码格式2的数据量要大于编码格式1，如果无需上传文件，还是推荐使用更为精简的编码格式1
#
#     我们除了可以采用form表单向django提交数据外，还可以采用ajax技术，ajax可以提交的数据格式有：1、编码格式1 2、编码格式2 3、json，当ajax采用POST方法提交前两种格式的数据时，django的处理方案同上，但是当ajax采用POST方法提交json格式的数据时，django会将接收到的数据存放于HttpRequest.body，此时需要我们自己对HttpRequest.body属性值做反序列化操作，
# 具体的，我们在讲解ajax时再做具体介绍
#
# 二.HttpRequest.FILES
#    如果使用form表单POST上传文件的话，文件数据将包含在HttpRequest.FILES属性中。
#
# 　　该属性值为一个类似于字典的对象，可以包含多组key:value（对应多个上传的文件），其中每个key为<input type="file" name="" /> 中name属性的值，而value则为对应的文件数据
# 　　强调：HttpRequest.FILES 只有在请求的方法为POST 且提交的<form> 带有enctype="multipart/form-data" 的情况下才会包含数据。否则，FILES 将为一个空

# 一.HttpRequest.path
# 　　获取url地址的路径部分，只包含路径部分
#
# 二.HttpRequest.get_full_path()
# 　　获取url地址的完整path，既包含路径又包含参数部分
#
# 如果请求地址是http://127.0.0.1:8001/order/?name=egon&age=10#_label3，
# HttpRequest.path的值为"/order/"
# HttpRequest.get_full_path()的值为"/order/?name=egon&age=10"

# 一.HttpRequest.META
#  　 值为包含了HTTP协议的请求头数据的Python字典，字典中的key及期对应值的解释如下
#     CONTENT_LENGTH —— 请求的正文的长度（是一个字符串）。
#     CONTENT_TYPE —— 请求的正文的MIME类型。
#     HTTP_ACCEPT —— 响应可接收的Content-Type。
#     HTTP_ACCEPT_ENCODING —— 响应可接收的编码。
#     HTTP_ACCEPT_LANGUAGE —— 响应可接收的语言。
#     HTTP_HOST —— 客服端发送数据的目标主机与端口
#     HTTP_REFERER —— Referring 页面。
#     HTTP_USER_AGENT —— 客户端使用的软件版本信息
#     QUERY_STRING —— 单个字符串形式的查询字符串（未解析过的形式）。
#     REMOTE_ADDR —— 客户端的IP地址。
#     REMOTE_HOST —— 客户端的主机名。
#     REMOTE_USER —— 服务器认证后的用户。
#     REQUEST_METHOD —— 一个字符串，例如"GET" 或"POST"。
#     SERVER_NAME —— 服务器的主机名。
#     SERVER_PORT —— 服务器的端口（是一个字符串）。
#  　　从上面可以看到，除 CONTENT_LENGTH 和 CONTENT_TYPE 之外，HTTP协议的请求头数据转换为 META 的键时，
#     都会
#     1、将所有字母大写
#     2、将单词的连接符替换为下划线
#     3、加上前缀HTTP_。
#     所以，一个叫做 X-Bender 的头部将转换成 META 中的 HTTP_X_BENDER 键。
#
# 注意：下述常用属性暂且了解即可，待我们讲到专门的知识点时再专门详细讲解
# 二.HttpRequest.COOKIES
# 　　一个标准的Python 字典，包含所有的cookie。键和值都为字符串。
#
# 三.HttpRequest.session
#  　一个既可读又可写的类似于字典的对象，表示当前的会话。只有当Django 启用会话的支持时才可用。
#
# 11.HttpRequest.user(用户认证组件下使用)
#
# 　　一个 AUTH_USER_MODEL 类型的对象，表示当前登录的用户。
#
# 2.HttpRequest.is_ajax()
#
# 　　如果请求是通过XMLHttpRequest 发起的，则返回True，方法是检查 HTTP_X_REQUESTED_WITH 相应的首部是否是字符串'XMLHttpRequest'。
#
# 　　大部分现代的 JavaScript 库都会发送这个头部。如果你编写自己的 XMLHttpRequest 调用（在浏览器端），你必须手工设置这个值来让 is_ajax() 可以工作。
#
# 　　如果一个响应需要根据请求是否是通过AJAX 发起的，并且你正在使用某种形式的缓存例如Django 的 cache middleware，
#    你应该使用 vary_on_headers('HTTP_X_REQUESTED_WITH') 装饰你的视图以让响应能够正确地缓存。

# 响应对象主要有三种形式:HttpResponse,render,redirect

# render(request, template_name[, context]）
# 参数：
# 	1、request：用于生成响应的请求对象，固定必须传入的第一个参数
#
#     2、template_name：要使用的模板的完整名称，必须传入，render默认会去templates目录下查找模板文件
#
#     3、context：可选参数，可以传入一个字典用来替换模块文件中的变量
#
# 综上，render的功能可以总结为：根据给定字典渲染模板文件，并返回一个渲染后的 HttpResponse对象。

# # 返回重定向信息
# def my_view(request):
#     ...
#     return redirect('/some/url/')
#
# # 重定向的地址也可以是一个完整的URL：
# def my_view(request):
#     ...
#     return redirect('http://www.baidu.com/')　

# 2、不同之处：
# 301表示旧地址A的资源已经被永久地移除了，即这个资源不可访问了。
# 搜索引擎在抓取新内容的同时也将旧的网址转换为重定向之后的地址；

# 302表示旧地址A的资源还在，即这个资源仍然可以访问，
# 这个重定向只是临时地从旧地址A跳转到地址B，搜索引擎会抓取新的内容、
# 并且会保存旧的网址。 从SEO层面考虑

# import json
#
# def my_view(request):
#     data=['egon','kevin']
#     return HttpResponse(json.dumps(data) )

# from django.http import JsonResponse
#
# def my_view(request):
#     data=['egon','kevin']
#     return JsonResponse(data,safe=False)
#     #默认safe=True代表只能序列化字典对象，safe=False代表可以序列化字典以外的对象

# FBV与FCV
# django的视图层由两种形式构成：FBV和CBV
#
# 1、FBV基于函数的视图（Function base view），我们之前一直介绍的都是FBV
#
# 2、CBV基于类的视图(Class base view)

# 案例
# urls.py
# from django.urls import path,register_converter,re_path
# from app01 import views
#
# urlpatterns = [
#     re_path(r'^login/',views.LoginView.as_view()), # 必须调用类下的方法as_view

# views.py
# from django.shortcuts import render,HttpResponse,redirect
# from django.views import View
#
# class LoginView(View):
#     def dispatch(self, request, *args, **kwargs): # 可在该方法内做一些预处理操作
#         # 当请求url为：http://127.0.0.1:8008/login/会先触发dispatch的执行
#         # 如果http协议的请求方法为GET，则调用下述get方法
#         # 如果http协议的请求方法为POST，则调用下述post方法
#         obj=super().dispatch(request, *args, **kwargs) # 必须继承父类的dispatch功能
#         return obj # 必须返回obj
#
#     def get(self,request):
#         return render(request,'login.html')
#
#     def post(self,request):
#         name=request.POST.get('name')
#         pwd=request.POST.get('pwd')
#         if name  == 'egon' and pwd == '123':
#             res='登录成功'
#         else:
#             res='用户名或密码错误'
#         return HttpResponse(res)

# 测试
# python manage.py runserver 8001
# # 验证GET请求：在浏览器输入：http://127.0.0.1:8001/login/
# # 验证POST请求：在表单内输入数据然后提交
# 采用CBV可以引入面向对象的思想对数据进行更高程度的封装，此处简单了解即可，我们将在后续的项目中详细介绍它的应用于强大之处