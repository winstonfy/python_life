#__author__ = 'Winston'
#date: 2020/4/10
# 模板简介
# 在刚刚介绍完的视图层中我们提到，浏览器发送的请求信息会转发给视图函数进行处理，
# 而视图函数在经过一系列处理后必须要有返回信息给浏览器。如果我们要返回html标签、
# css等数据给浏览器进行渲染，我们可以在视图函数中这么做

# def current_datetime(request):
#     now = datetime.datetime.now()
#     html = "<html><body>It is now %s.</body></html>" % now
#     return HttpResponse(html)

# 上例所示，我们直接将HTML代码放到视图函数里，然后进行返回，
# 这可以使我们很直观地看清楚浏览器从发送请求到看到前端界面内容的这个
# 过程中视图函数的基本工作原理，但是这种将前端代码与后端代码耦合到了一起开发方式，会存在以下问题

# 1、程序的可维护性与可扩展性问题
# 前端界面一旦需要重新设计、修改，则必须对后端的Python代码进行相应的修改。
# 然而前端界面的修改往往比后端 Python 代码的修改要频繁得多，
# 因此如果可以在不进行 Python 代码修改的情况下变更前端界面的设计，那将会方便得多。
#
# 2、开发效率问题
# Python 代码编写和 HTML 设计是两项不同的工作，
# 大多数专业的网站开发环境都将它们分配给不同的人员（甚至不同部门）来完成。
# 专门的程序员去编写 Python代码、

# 于上述原因，将前端页面和Python的代码分离是一种不错的开发模式。
# 为此 Django专门提供了模板系统 (Template System，即模板层)来实现这种模式

# django的模板=HTML代码+模板语法
# 存放于templates目录下的html文件称之为模板文件，
# 如果我们想要返回的html页面中的数据是动态的，那么必须在html页面中嵌入变量，
# 这便用到了django的模板语法，具体来说，django的模板语法有以下重点

# 一、变量：{{ 变量名 }}
# 	1.1 深度查询：句点符的应用
#     1.2 过滤器
# 二、标签：{% 标签名 %}
# 三、自定义标签和过滤器
# 四、模板的导入和继承

# 变量的基本使用
# 如果html代码中的数据不是固定死的，而是动态变化的，则必须在html中嵌入变量，
# 为此，模板语法提供了变量的概念，允许我们在html代码中嵌入变量，
# 我们只需要在视图函数中用render方法为html文件中指定的变量赋值即可，具体用法如下

# test.html
#
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <title>Title</title>
# </head>
# <body>
# <p>{{ msg }}</p>
# <p>{{ dic }}</p>
# <p>{{ obj }}</p>
# <p>{{ li }}</p>
# </body>
# </html>

# 我们需要在视图函数中为模板test.html的变量名msg、li、dic、obj、obj_li赋值,views.py内容如下
# from django.shortcuts import render
#
# def test(request):
#     # 传给模板的变量值可以是任意python类型，如下
#     msg='hello world'
#     dic={'k1':1,'k2':2}
#     class Person(object):
#         def __init__(self,name,age):
#             self.name=name
#             self.age=age
#
#     obj=Person('egon',18)
#     li = [1,'aaa',obj]
#
#     return render(request,'test.html',{'msg':msg,'dic':dic,'obj':obj,'li':li})
#     # 注意：
#     # 1、render函数的第三个参数包含了要传给模板的变量值，是一个字典类型，该字典中的key必须与模板文件中的变量名相对应，render函数会去templates目录下找到模板文件，然后根据字典中的key对应到模板文件中的变量名进行赋值操作，最后将赋值后的模板文件内容返回给浏览器
#     # 2、可以将render函数的第三个参数简写为locals(),如下
#     return render(request,'test.html',locals()) #locals()会将函数test内定义的名字与值转换为字典中的k与v

# 深度查询之句点符的使用
# 当视图函数传给模板的值中包含多个元素时，若想取出其中的单个元素，就必须使用句点符了。
#
# 句点符既可以引用容器类型的元素，也可以引用对象的方法，如下

# test.html
#
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <title>Title</title>
# </head>
# <body>
#
# <!--调用字符串对象的upper方法，注意不要加括号-->
# <p>{{ msg.upper }}</p>
#
# <!--取字典中k1对应的值-->
# <p>{{ dic.k1 }}</p>
#
# <!--取对象的name属性-->
# <p>{{ obj.name }}</p>
#
# <!--取列表的第2个元素,然后变成大写-->
# <p>{{ li.1.upper }}</p>
#
# <!--取列表的第3个元素，并取该元素的age属性-->
# <p>{{ li.2.age }}</p>
#
#
# </body>
# </html>

# 过滤器类似于python的内置函数，用来把视图传入的变量值加以修饰后再显示
# {{ 变量名|过滤器名:传给过滤器的参数 }}

# 常用内置过滤器
#
# #1、default
# #作用：如果一个变量值是False或者为空，使用default后指定的默认值，否则，使用变量本身的值，如果value=’‘则输出“nothing”
# {{ value|default:"nothing" }}
#
# #2、length
# #作用：返回值的长度。它对字符串、列表、字典等容器类型都起作用，如果value是 ['a', 'b', 'c', 'd']，那么输出是4
# {{ value|length }}
#
# #3、filesizeformat
# #作用：将值的格式化为一个"人类可读的"文件尺寸(如13KB、4.1 MB、102bytes等等），如果 value 是 12312312321，输出将会是 11.5 GB
# {{ value|filesizeformat }}
#
# #4、date
# #作用：将日期按照指定的格式输出，如果value=datetime.datetime.now(),按照格式Y-m-d则输出2019-02-02
# {{ value|date:"Y-m-d" }}　　
#
# #5、slice
# #作用：对输出的字符串进行切片操作，顾头不顾尾,如果value=“egon“，则输出"eg"
# {{ value|slice:"0:2" }}　
#
# #6、truncatechars
# #作用：如果字符串字符多于指定的字符数量，那么会被截断。截断的字符串将以可翻译的省略号序列（“...”）结尾，如果value=”hello world egon 嘎嘎“，则输出"hello...",注意8个字符也包含末尾的3个点
# {{ value|truncatechars:8 }}
#
# #7、truncatewords
# #作用：同truncatechars，但truncatewords是按照单词截断，注意末尾的3个点不算作单词，如果value=”hello world egon 嘎嘎“，则输出"hello world ..."
# {{ value|truncatewords:2 }}
#
# #8、safe
# #作用：出于安全考虑，Django的模板会对HTML标签、JS等语法标签进行自动转义,例如value="<script>alert(123)</script>"，模板变量{{ value }}会被渲染成&lt;script&gt;alert(123)&lt;/script&gt;交给浏览器后会被解析成普通字符”<script>alert(123)</script>“，失去了js代码的语法意义，但如果我们就想让模板变量{{ value }}被渲染的结果又语法意义，那么就用到了过滤器safe，比如value='<a href="https://www.baidu.com">点我啊</a>'，在被safe过滤器处理后就成为了真正的超链接，不加safe过滤器则会当做普通字符显示’<a href="https://www.baidu.com">点我啊</a>‘
# {{ value|safe }}

# 其他过滤器（了解）

# pper	以大写方式输出	{{ user.name | upper }}
# add	给value加上一个数值	{{ user.age | add:”5” }}
# addslashes	单引号加上转义号
# capfirst	第一个字母大写	{{ ‘good’| capfirst }} 返回”Good”
# center	输出指定长度的字符串，把变量居中	{{ “abcd”| center:”50” }}
# cut	删除指定字符串	{{ “You are not a Englishman” | cut:”not” }}
# date	格式化日期
# default	如果值不存在，则使用默认值代替	{{ value | default:”(N/A)” }}
# default_if_none	如果值为None, 则使用默认值代替
# dictsort	按某字段排序，变量必须是一个dictionary	{% for moment in moments | dictsort:”id” %}
# dictsortreversed	按某字段倒序排序，变量必须是dictionary
# divisibleby	判断是否可以被数字整除	{{ 224 | divisibleby:2 }} 返回 True
# escape	按HTML转义，比如将”<”转换为”&lt”
# filesizeformat	增加数字的可读性，转换结果为13KB,89MB,3Bytes等	{{ 1024 | filesizeformat }} 返回 1.0KB
# first	返回列表的第1个元素，变量必须是一个列表
# floatformat	转换为指定精度的小数，默认保留1位小数	{{ 3.1415926 | floatformat:3 }} 返回 3.142 四舍五入
# get_digit	从个位数开始截取指定位置的数字	{{ 123456 | get_digit:’1’}}
# join	用指定分隔符连接列表	{{ [‘abc’,’45’] | join:’’ }} 返回 abc45
# length	返回列表中元素的个数或字符串长度
# length_is	检查列表，字符串长度是否符合指定的值	{{ ‘hello’| length_is:’3’ }}
# linebreaks	用
# 或
# 标签包裹变量
#
# {{ “Hi\n\nDavid”|linebreaks }} 返回
# Hi
#
# David
#
# linebreaksbr	用
# 标签代替换行符
# linenumbers	为变量中的每一行加上行号
# ljust	输出指定长度的字符串，变量左对齐	{{‘ab’|ljust:5}}返回 ‘ab ’
# lower	字符串变小写
# make_list	将字符串转换为列表
# pluralize	根据数字确定是否输出英文复数符号
# random	返回列表的随机一项
# removetags	删除字符串中指定的HTML标记	{{value | removetags: “h1 h2”}}
# rjust	输出指定长度的字符串，变量右对齐
# slice	切片操作， 返回列表	{{[3,9,1] | slice:’:2’}} 返回 [3,9] {{ 'asdikfjhihgie' | slice:':5' }} 返回 ‘asdik’
# slugify	在字符串中留下减号和下划线，其它符号删除，空格用减号替换	{{ '5-2=3and5 2=3' | slugify }} 返回 5-23and5-23
# stringformat	字符串格式化，语法同python
# time	返回日期的时间部分
# timesince	以“到现在为止过了多长时间”显示时间变量	结果可能为 45days, 3 hours
# timeuntil	以“从现在开始到时间变量”还有多长时间显示时间变量
# title	每个单词首字母大写
# truncatewords	将字符串转换为省略表达方式	{{ 'This is a pen' | truncatewords:2 }}返回``This is ...
# truncatewords_html	同上，但保留其中的HTML标签	{{ '<p>This is a pen</p>' | truncatewords:2 }}返回``<p>This is ...</p>
# urlencode	将字符串中的特殊字符转换为url兼容表达方式	{{ ‘http://www.aaa.com/foo?a=b&b=c’ | urlencode}}
# urlize	将变量字符串中的url由纯文本变为链接
# wordcount	返回变量字符串中的单词数
# yesno	将布尔变量转换为字符串yes, no 或maybe	{{ True | yesno }}{{ False | yesno }}{{ None | yesno }} ``返回 ``yes``no ``maybe


# 模板语法之标签

# 标签是为了在模板中完成一些特殊功能,语法为{% 标签名 %}，一些标签还需要搭配结束标签 {% endtag %}
# 常用标签之for标签
#1、遍历每一个元素：
# {% for person in person_list %}
#     <p>{{ person.name }}</p>
# {% endfor %}

#2、可以利用{% for obj in list reversed %}反向循环。

#3、遍历一个字典：
# {% for key,val in dic.items %}
#     <p>{{ key }}:{{ val }}</p>
# {% endfor %}
#
# #4、循环序号可以通过{{ forloop }}显示　
# forloop.counter            当前循环的索引值（从1开始）
# forloop.counter0           当前循环的索引值（从0开始）
# forloop.revcounter         当前循环的倒序索引值（从1开始）
# forloop.revcounter0        当前循环的倒序索引值（从0开始）
# forloop.first              当前循环是第一次循环则返回True，否则返回False
# forloop.last               当前循环是最后一次循环则返回True，否则返回False
# forloop.parentloop         本层循环的外层循环
#
# #5、for标签可以带有一个可选的{% empty %} 从句，在变量person_list为空或者没有被找到时，则执行empty子句
# {% for person in person_list %}
#     <p>{{ person.name }}</p>
#
# {% empty %}
#     <p>sorry,no person here</p>
# {% endfor %}

# 常用标签之if标签
# # 1、注意：
# {% if 条件 %}条件为真时if的子句才会生效，条件也可以是一个变量，if会对变量进行求值，在变量值为空、或者视图没有为其传值的情况下均为False
#
# # 2、具体语法
# {% if num > 100 or num < 0 %}
#     <p>无效</p>
# {% elif num > 80 and num < 100 %}
#     <p>优秀</p>
# {% else %}
#     <p>凑活吧</p>
# {% endif %}
#
# #3、if语句支持 and 、or、==、>、<、!=、<=、>=、in、not in、is、is not判断。

# 常用标签之with标签
# # with标签用来为一个复杂的变量名起别名,如果变量的值来自于数据库，在起别名后只需要使用别名即可，无需每次都向数据库发送请求来重新获取变量的值
# {% with li.1.upper as v %}
#     {{ v }}
# {% endwith %}

# 常用标签之csrf_token标签

# # 当用form表单提交POST请求时必须加上标签{% csrf_token%}，该标签用于防止跨站伪造请求
# <form action="" method="POST">
#     {% csrf_token %}
#     <p>用户名：<input type="text" name="name"></p>
#     <p>密码：<input type="password" name="pwd"></p>
#     <p><input type="submit" value="提交"></p>
# </form>
# # 具体工作原理为：
# # 1、在GET请求到form表单时，标签{% csrf_token%}会被渲染成一个隐藏的input标签，该标签包含了由服务端生成的一串随机字符串,如<input type="hidden" name="csrfmiddlewaretoken" value="dmje28mFo...OvnZ5">
# # 2、在使用form表单提交POST请求时，会提交上述随机字符串，服务端在接收到该POST请求时会对比该随机字符串，对比成功则处理该POST请求，否则拒绝，以此来确定客户

# 自定义过滤器和标签
# 当内置的过滤器或标签无法满足我们需求时，我们可以自定义，具体操作步骤如下
#
# 1、在settings中的INSTALLED_APPS添加当前app的名字，不然django无法找到自定义的过滤器或标签

# settings.py
# 在settings.py中找到该列表，然后加以配置
# INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     'app01.apps.App01Config',
#     'app01', # 添加当前app的名字
# ]

# 2、在文件夹app01中创建子文件夹templatetags(文件夹名只能是templatetags)
#
# 3、在templatetags新建任意.py文件，如my_tags.py，在该文件中自定义过滤器或标签，文件内容如下
# from django import template
# register = template.Library() # 注意变量名必须为register,不可改变
#
# #1、自定义过滤器
# @register.filter
# def my_multi_filter(v1 ,v2): # 自定义的过滤器只能定义最多两个参数，针对{{ value1 | filter_multi:value2 }}，参数传递为v1=value1,v2=value2
#     return  v1 * v2
#
# #2、自定义标签
# @register.simple_tag
# def my_multi_tag(v1, v2): # 自定义的标签可以定义多个参数
#     return v1 * v2
#
#
# #3、自定义标签扩展之mark_safe
# # 注释：我们可以用内置的标签safe来让标签内容有语法意义，如果我们想让自定义标签处理的结果也有语法意义，则不能使用内置标签safe了，需要使用mark_safe，可以实现与内置标签safe同样的功能
# from django.utils.safestring import mark_safe
#
# @register.simple_tag
# def my_input_tag(id, name):
#     res = "<input type='text' id='%s' name='%s' />" % (id, name)
#     return mark_safe(res)

# 4、自定义过滤器或标签必须重新启动django方可生效
#
# 5、自定义过滤器或标签的使用
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <title>Title</title>
# </head>
# <body>
#
# <!--必须先加载存有自定义过滤器和标签的文件-->
# {% load my_tags %}
#
# <!--salary的值为10，经过滤器my_multi_filter的处理结果为120-->
# {{ salary|my_multi_filter:12 }}
#
# <!--结果为2-->
# {% my_multi_tag 1 2 %}
#
# <!--
# 结果为一个input标签，该表的属性id="inp1" name="username"
# 注意：input的属性值均为字符串类型，所以my_input_tag后的两个值均为字符串类型
# -->
# {% my_input_tag "inp1" "username" %}
#
# </body>
# </html>

# 对比自定义标签与自定义过滤器

# #1、自定义过滤器只能传两个参数，而自定义标签却可以传多个参数
#
# #2、过滤器可以用于if判断，而标签不能
# {% if salary|my_multi_filter:12 > 200 %}
#     <p>优秀</p>
# {% else %}
#     <p>垃圾</p>
# {% endif %}

# 五 模板的导入和继承
# 在实际开发中，模板文件彼此之间可能会有大量冗余代码，
# 为此django提供了专门的语法来解决这个问题,主要围绕三种标签的使用：include标签、extends标签、block标签

# 模板的导入之include标签
# #作用：在一个模板文件中，引入/重用另外一个模板文件的内容，
# {% include '模版名称' %}
# 把广告栏写到专门的文件里advertise.html

# <div class="adv">
#     <div class="panel panel-default">
#         <div class="panel-heading">
#             <h3 class="panel-title">Panel title</h3>
#         </div>
#         <div class="panel-body">
#             Panel content
#         </div>
#     </div>
#     <div class="panel panel-danger">
#         <div class="panel-heading">
#             <h3 class="panel-title">Panel title</h3>
#         </div>
#         <div class="panel-body">
#             Panel content
#         </div>
#     </div>
#     <div class="panel panel-warning">
#         <div class="panel-heading">
#             <h3 class="panel-title">Panel title</h3>
#         </div>
#         <div class="panel-body">
#             Panel content
#         </div>
#     </div>
# </div>
# 然后在base.html文件中用include标签引入advertise.html文件的内容
#
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <title>Title</title>
#     <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@3.3.7/dist/css/bootstrap.min.css"
#           integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
#     <style>
#         * {
#             margin: 0;
#             padding: 0;
#         }
#
#         .header {
#             height: 50px;
#             width: 100%;
#             background-color: black;
#         }
#
#     </style>
# </head>
# <body>
# <div class="header"></div>
# <div class="container">
#     <div class="row">
#         <div class="col-md-3">
#             <!--在base.html引入advertise.html文件的内容-->
#             {% include "advertise.html" %}
#         </div>
#         <div class="col-md-9"></div>
#     </div>
# </div>
# </body>
# </html>

# 模板的继承\派生之extends标签、block标签
# #作用：在一个模板文件中，引入/重用另外一个模板文件的内容
# {% extends "模版名称" %}
# #  也就是说include有的功能extends全都有，但是extends可以搭配一个block标签，用于在继承的基础上定制新的内容

# Django模版引擎中最复杂且最强大的部分就是模版继承了。我们以先创建一个基本的“骨架”模版，它包含我们站点中的全部元素，并且可以定义多处blocks ，例如我们创建base.html内容如下
#
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <title>
#         {% block title %}自定义title名{% endblock %}
#     </title>
#
#     <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@3.3.7/dist/css/bootstrap.min.css"
#           integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
#     <style>
#         * {
#             margin: 0;
#             padding: 0;
#         }
#
#         .header {
#             height: 50px;
#             width: 100%;
#             background-color: #919191;
#             margin-bottom: 20px;
#         }
#
#     </style>
#
# </head>
# <body>
# <div class="header"></div>
#
# <div class="container">
#     <div class="row">
#         <div class="col-md-3">
#             <div class="list-group">
#                 {% block sidebar %}
#                     <a href="#" class="list-group-item active">服装城</a>
#                     <a href="#" class="list-group-item">美妆馆</a>
#                     <a href="#" class="list-group-item">超市</a>
#                     <a href="#" class="list-group-item">全球购</a>
#                     <a href="#" class="list-group-item">闪购</a>
#                     <a href="#" class="list-group-item">团购</a>
#                 {% endblock %}
#
#             </div>
#         </div>
#
#         <div class="col-md-9">
#             {% block content %}
#                 base.html页面内容
#             {% endblock %}
#         </div>
#     </div>
#
# </div>
#
# </body>
# </html>
# 模板base.html 定义了一个可以用于两列排版页面的简单HTML骨架。我们新建子模板index.html的主要工作就是继承base.html然后填充/覆盖其内部的blocks。
#
# {% extends "base.html" %}
#
# <!--用新内容完全覆盖了父模板内容-->
# {% block title %}
#     index页面
# {% endblock %}
#
#
# {% block sidebar %}
#     <!--该变量会将父模板中sidebar中原来的内容继承过来，然后我们可以在此基础上新增，否则就是纯粹地覆盖-->
#     {{ block.super }}
#
#     <!--在继承父模板内容的基础上新增的标签-->
#     <a href="#" class="list-group-item">拍卖</a>
#     <a href="#" class="list-group-item">金融</a>
# {% endblock %}
#
# {% block content %}
#     <!--用新内容完全覆盖了父模板内容-->
#     <p>index页面内容</p>
# {% endblock %}
# 我们通过django访问index.html看到内容如下(block标签的内容都完成了替换或更新)
#
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <title>
#         index页面
#     </title>
#
#     <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@3.3.7/dist/css/bootstrap.min.css"
#           integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
#     <style>
#         * {
#             margin: 0;
#             padding: 0;
#         }
#
#         .header {
#             height: 50px;
#             width: 100%;
#             background-color: #919191;
#             margin-bottom: 20px;
#         }
#
#     </style>
#
# </head>
# <body>
# <div class="header"></div>
#
# <div class="container">
#     <div class="row">
#         <div class="col-md-3">
#             <div class="list-group">
#                 <!--该变量会将父模板中sidebar中原来的内容继承过来，然后我们可以在此基础上新增，否则就是纯粹地覆盖-->
#                 <a href="#" class="list-group-item active">服装城</a>
#                 <a href="#" class="list-group-item">美妆馆</a>
#                 <a href="#" class="list-group-item">超市</a>
#                 <a href="#" class="list-group-item">全球购</a>
#                 <a href="#" class="list-group-item">闪购</a>
#                 <a href="#" class="list-group-item">团购</a>
#
#
#                 <!--在继承父模板内容的基础上新增的标签-->
#                 <a href="#" class="list-group-item">拍卖</a>
#                 <a href="#" class="list-group-item">金融</a>
#             </div>
#         </div>
#
#         <div class="col-md-9">
#             <!--用新内容完全覆盖了父模板内容-->
#             <p>index页面内容</p>
#         </div>
#     </div>
#
# </div>
#
# </body>
# </html>
# 总结与注意
#
# #1、标签extends必须放在首行，base.html中block越多可定制性越强
#
# #2、include仅仅只是完全引用其他模板文件，而extends却可以搭配block在引用的基础上进行扩写
#
# #3、变量{{ block.super }} 可以重用父类的内容，然后在父类基础上增加新内容，而不是完全覆盖
#
# #4、为了提升可读性，我们可以给标签{% endblock %} 起一个名字 。例如：
#     {% block content %}
#     ...
#     {% endblock content %}　　
# #5、在一个模版中不能出现重名的block标签。

# 静态文件配置
# 我们在编写模板文件时，需要大量引用css、js、图片等静态文件，如果我们将这些文件在服务端存放的路径都固定写死那么将非常不利于后期的扩展，我们可以这么做
#
# 1、settings.py
#
# STATIC_URL = '/static/' # 找到这一行，然后新增下述代码
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'statics'),# 获取静态文件在服务端的绝对路径
# ]
# #STATIC_URL = '/static/'就是为静态文件的绝对路径起了一个别名，以后我们只需要用路径/static/即可

# 在项目根目录下新增文件夹statics，为了更便于管理，可以在statics下新建子文件夹css、js、img等

# 3、新建模板文件index.html,在该文件中对静态文件的引用如下
#
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <title>Title</title>
#     <link rel="stylesheet" href="/static/css/my.css">
# </head>
# <body>
# <h4>我是红色的，点我就绿</h4>
# <img src="/static/img/rb.jpeg" alt="">
#
#
# <script src="/static/js/jquery-3.3.1.min.js"></script>
# <script src="/static/js/my.js"></script>
#
# </body>
# </html>
# 综上，在配置完settings.py后，所有的静态文件路径都可以采用别名/static/作为起始，这在一定程度上会有利于程序的扩展性，但如果我们在项目后期维护时，连/static/这个值也需要修改，那意味着所有模板文件中也都需要跟着改了，扩展性依然很差，为此，django在一个名为static.py的文件中定义了标签static、get_static_prefix，二者都可以解决该问题
#
# test.html
#
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <title>Title</title>
#     <!--注意：必须先加载文件static.py-->
#     {% load static %}
#     <!--注意：此处的static是一个定义在static.py中的一个标签，名字与文件名一样而已，不要搞混-->
#     <link rel="stylesheet" href="{% static 'css/my.css' %}">
# </head>
# <body>
# <h4>我是红色的，点我就绿</h4>
# <img src="{% static 'img/rb.jpeg' %}" alt="">
#
#
# {% load static %}
# <script src="{% static 'js/jquery-3.3.1.min.js' %}"></script>
# <script src="{% static 'js/my.js' %}"></script>
#
# </body>
# </html>
# 标签static会接收传入的参数，然后这根据settings.py中变量STATIC_URL的值拼接出一个完整的路径，如果STATIC_URL = '/static/'，那么href="{% static 'css/my.css' %}"会被渲染成href="/static/css/my.css"，如果STATIC_URL = '/static123/'，那么href="{% static 'css/my.css' %}"会被渲染成href="/static123/css/my.css"。
#
# 标签get_static_prefix也可以完成同样的效果，只不过用法不同。我们不能为标签get_static_prefix传参，因为标签get_static_prefix代表的只是settings.py中STATIC_URL的值，所以我们需要做的是在get_static_prefix的基础上自行拼接路径，如下
#
# test.html
#
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <title>Title</title>
#     <!--注意：同样需要先加载文件static.py-->
#     {% load static %}
#     <!--使用标签get_static_prefix拼接路径-->
#     <link rel="stylesheet" href="{% get_static_prefix %}css/my.css">
# </head>
# <body>
# <h4>我是红色的，点我就绿</h4>
# <img src="{% get_static_prefix %}img/rb.jpeg" alt="">
#
#
# {% load static %}
# <script src="{% get_static_prefix %}js/jquery-3.3.1.min.js"></script>
# <script src="{% get_static_prefix %}js/my.js"></script>
#
# </body>
# </html>
# 如果STATIC_URL = '/static/'，那么href="{% get_static_prefix %}css/my.css"会被渲染成href="/static/css/my.css"，其它同理
