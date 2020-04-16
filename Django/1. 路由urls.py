#__author__ = 'Winston'
#date: 2020/4/10
#---project name files
#--app1 files
#--app2 files
#--templates files
#--static files
#--project name files
#- __init__.py
#-settings.py
#-urls.py 当前位置 ✔ 路由层
#-wsgi.py


from django.urls import re_path

#由一条条映射关系组成的urlpatterns这个列表称之为路由表
urlpatterns = [
    re_path('^index/$', view, kwargs=None, name=None), # url本质就是一个函数
]
#函数url关键参数介绍
# regex：正则表达式,用来匹配url地址的路径部分，
		# 例如url地址为：http://127.0.0.1:8001/index/，正则表达式要匹配的部分是index/
# view：通常为一个视图函数，用来处理业务逻辑
# kwargs：略（用法详见有名分组）
# name：略（用法详见反向解析）

# 匹配的最后的斜杠问题
# 刚刚我们在浏览器输入：http://127.0.0.1:8001/index/，Django会拿着路径部分index/去路由表中自上而下匹配正则表达式，一旦匹配成功，则立即执行其后的视图函数，不会继续往下匹配，此处匹配成功的正则表达式是 r'^index/$'。
#
# 注意二：
#
# 但是我们在浏览器输入：http://127.0.0.1:8001/index，Django同样会拿着路径部分index去路由表中自上而下匹配正则表达式，貌似并不会匹配成功任何正则表达式（ r'^index/$'匹配的是必须以 / 结尾，所以不会匹配成功index），但实际上仍然会看到结果 index page...，原因如下：
#
# 在配置文件settings.py中有一个参数APPEND_SLASH，该参数有两个值True或False
#
# 当APPEND_SLASH=True（如果配置文件中没有该配置，APPEND_SLASH的默认值为True），并且用户请求的url地址的路径部分不是以 / 结尾，例如请求的url地址是 http://127.0.0.1:8001/index，Django会拿着路径部分（即index）去路由表中匹配正则表达式，发现匹配不成功，那么Django会在路径后加 / （即index/）再去路由表中匹配，如果匹配失败则会返回路径未找到，如果匹配成功，则会返回重定向信息给浏览器，要求浏览器重新向 http://127.0.0.1:8001/index/地址发送请求。
#
# 当APPEND_SLASH=False时，则不会执行上述过程，即一旦url地址的路径部分匹配失败就立即返回路径未找到，不会做任何的附加操作
# ps：注意！！！在末尾加/然后重新发起请求，这是浏览器的功能，如果是在终端直接执行curl http://127.0.0.1:8901/index，则没有该功能

# 分组
# 无名分组 url(r'^aritcle/(\d+)/$',views.article),
# 下述正则表达式会匹配url地址的路径部分为:article/数字/，
# 匹配成功的分组部分会以位置参数的形式传给视图函数，有几个分组就传几个位置参数

# 有名分组 url(r'^aritcle/(?P<article_id>\d+)/$',views.article),
# 该正则会匹配url地址的路径部分为:article/数字/，匹配成功的分组部分会以关键字参数（article_id=匹配成功的数字）
# 的形式传给视图函数，有几个有名分组就


# 路由分发
# 随着项目功能的增加，app会越来越多，路由也越来越多，每个app都会有属于自己的路由，
# 如果再将所有的路由都放到一张路由表中，会导致结构不清晰，不便于管理，所以我们应该将app自己的路由交由自己管理，然后在总路由表中做分发

# from django.conf.urls import url, include
# from django.contrib import admin
#
# # 总路由表
# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
#
#     # 新增两条路由，注意不能以$结尾
#     # include函数就是做分发操作的，当在浏览器输入http://127.0.0.1:8001/app01/index/时，会先进入到总路由表中进行匹配，正则表达式r'^app01/'会先匹配成功路径app01/，然后include功能会去app01下的urls.py中继续匹配剩余的路径部分
#     url(r'^app01/', include('app01.urls')),
#     url(r'^app02/', include('app02.urls')),
# ]

# app01下的路由
# from django.conf.urls import url
# # 导入app01的views
# from app01 import views
#
# urlpatterns = [
#     url(r'^index/$',views.index),
# ]

# 反向解析
# 在软件开发初期，url地址的路径设计可能并不完美，后期需要进行调整，如果项目中很多地方使用了该路径，一旦该路径发生变化，就意味着所有使用该路径的地方都需要进行修改，这是一个非常繁琐的操作。
#
# 解决方案就是在编写一条url(regex, view, kwargs=None, name=None)时，可以通过参数name为url地址的路径部分起一个别名，项目中就可以通过别名来获取这个路径。以后无论路径如何变化别名与路径始终保持一致。
#
# 上述方案中通过别名获取路径的过程称为反向解析
# from django.conf.urls import url
# from django.contrib import admin
# from app01 import views
#
# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
#
#     url(r'^login/$', views.login, name='login_page'),  # 路径login/的别名为login_page
#     url(r'^index/$', views.index, name='index_page'),  # 路径index/的别名为index_page
# ]

# 在views.py中，反向解析的使用：
# 	url = reverse('index_page')
# 在模版login.html文件中，反向解析的使用
# 	{% url 'login_page' %}

# 路径存在分组的反向解析使用
# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
#
#     url(r'^aritcle/(\d+)/$', views.article, name='article_page'),  # 无名分组
#     url(r'^user/(?P<uid>\d+)/$', views.article, name='user_page'),  # 有名分组
# ]

# 1 针对无名分组，比如我们要反向解析出：/aritcle/1/ 这种路径，写法如下
# 在views.py中，反向解析的使用：
# 	url = reverse('article_page',args=(1,))
# 在模版login.html文件中，反向解析的使用
# 	{% url 'article_page' 1 %}
#
#
# # 2 针对有名分组，比如我们要反向解析出：/user/1/ 这种路径，写法如下
# 在views.py中，反向解析的使用：
# 	url = reverse('user_page',kwargs={'uid':1})
# 在模版login.html文件中，反向解析的使用
# 	{% url 'user_page' uid=1 %}

# 名称空间
#当我们的项目下创建了多个app，并且每个app下都针对匹配的路径起了别名，
# 如果别名存在重复，那么在反向解析时则会出现覆盖，如下
# 总urls.py在路由分发时，指定名称空间
# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
#
#     # 传给include功能一个元组，元组的第一个值是路由分发的地址，第二个值则是我们为名称空间起的名字
#     url(r'^app01/', include(('app01.urls','app01'))),
#     url(r'^app02/', include(('app02.urls','app02'))),
# ]

# 修改每个app下的view.py中视图函数，针对不同名称空间中的别名'index_page'做反向解析
# app01 下view
# def index(request):
#     url=reverse('app01:index_page') # 解析的是名称空间app01下的别名'index_page'
#     return HttpResponse('app01的index页面，反向解析结果为%s' %url)


# 1、在视图函数中基于名称空间的反向解析，用法如下
# url=reverse('名称空间的名字:待解析的别名')
#
# 2、在模版里基于名称空间的反向解析，用法如下
# <a href="{% url '名称空间的名字:待解析的别名'%}">哈哈</a>


# re_path、path
# Django2.0中的re_path与django1.0的url一样，传入的第一个参数都是正则表达式
# path功能，用来解决：数据类型转换问题与正则表达式冗余问题，如下
# from django.urls import re_path
#
# from app01 import views
#
# urlpatterns = [
#     # 问题一：数据类型转换
#     # 正则表达式会将请求路径中的年份匹配成功然后以str类型传递函数year_archive，在函数year_archive中如果想以int类型的格式处理年份，则必须进行数据类型转换
#     re_path(r'^articles/(?P<year>[0-9]{4})/$', views.year_archive),
#
#     # 问题二：正则表达式冗余
#     # 下述三个路由中匹配article_id采用了同样的正则表达式，重复编写了三遍，存在冗余问题，并且极不容易管理，因为一旦article_id规则需要改变，则必须同时修改三处代码
#
#     re_path(r'^article/(?P<article_id>[a-zA-Z0-9]+)/detail/$', views.detail_view),
#     re_path(r'^articles/(?P<article_id>[a-zA-Z0-9]+)/edit/$', views.edit_view),
#     re_path(r'^articles/(?P<article_id>[a-zA-Z0-9]+)/delete/$', views.delete_view),
# ]

# from django.urls import path,re_path
#
# from app01 import views
#
# urlpatterns = [
#     # 问题一的解决方案：
#     path('articles/<int:year>/', views.year_archive), # <int:year>相当于一个有名分组，其中int是django提供的转换器，相当于正则表达式，专门用于匹配数字类型，而year则是我们为有名分组命的名，并且int会将匹配成功的结果转换成整型后按照格式（year=整型值）传给函数year_archive
#
#
#     # 问题二解决方法：用一个int转换器可以替代多处正则表达式
#     path('articles/<int:article_id>/detail/', views.detail_view),
#     path('articles/<int:article_id>/edit/', views.edit_view),
#     path('articles/<int:article_id>/delete/', views.delete_view),
# ]

# #1、path与re_path或者1.0中的url的不同之处是，传给path的第一个参数不再是正则表达式，
# 而是一个完全匹配的路径，相同之处是第一个参数中的匹配字符均无需加前导斜杠
#
# #2、使用尖括号(<>)从url中捕获值，相当于有名分组
#
# #3、<>中可以包含一个转化器类型（converter type），比如使用 <int:name>
# 使用了转换器int。若果没有转化器，将匹配任何字符串，当然也包括了 / 字符

# 转换器支持的模式
# django默认支持一下5种转换器（Path converters）
# str,匹配除了路径分隔符（/）之外的非空字符串，这是默认的形式
# int,匹配正整数，包含0。
# slug,匹配字母、数字以及横杠、下划线组成的字符串。
# uuid,匹配格式化的uuid，如 075194d3-6885-417e-a8a8-6c931e272f00。
# path,匹配任何非空字符串，包含了路径分隔符（/）（不能用？）

# 自定义转换器流程
# 转化器是一个类或接口，它的要求有三点：
#
# regex 类属性，字符串类型
#
# to_python(self, value) 方法，value是由类属性 regex 所匹配到的字符串，返回具体的Python变量值，以供Django传递到对应的视图函数中。
#
# to_url(self, value) 方法，和 to_python 相反，value是一个具体的Python变量值，返回其字符串，通常用于url反向引用。

# 1.在app01下新建文件path_ converters.py,文件名可以随意命名
# class MonthConverter:
#     regex='\d{2}' # 属性名必须为regex
#
#     def to_python(self, value):
#         return int(value)
#
#     def to_url(self, value):
#         return value # 匹配的regex是两个数字，返回的结果也必须是两个数字

# 2.在urls.py中，使用register_converter 将其注册到URL配置中：
#
# from django.urls import path,register_converter
# from app01.path_converts import MonthConverter
#
# register_converter(MonthConverter,'mon')
#
# from app01 import views
#
#
# urlpatterns = [
#     path('articles/<int:year>/<mon:month>/<slug:other>/', views.article_detail, name='aaa'),
#
# ]

# 3.views.py中的视图函数article_detail
#
# from django.shortcuts import render,HttpResponse,reverse
#
# def article_detail(request,year,month,other):
#     print(year,type(year))
#     print(month,type(month))
#     print(other,type(other))
#     print(reverse('xxx',args=(1988,12,'hello'))) # 反向解析结果/articles/1988/12/hello/
#     return HttpResponse('xxxx')

# 4.测试
# 1、在浏览器输入http://127.0.0.1:8000/articles/2009/12/hello/，path会成功匹配出参数year=2009,month=12,other='hello'传递给函数article_detail
# 2、在浏览器输入http://127.0.0.1:8000/articles/2009/123/hello/，path会匹配失败，因为我们自定义的转换器mon只匹配两位数字，