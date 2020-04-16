#__author__ = 'Winston'
#date: 2020/4/2

# 异常处理
# AttributeError       试图访问一个对象没有的树形，比如foo.x，但是foo没有属性x
# FileNotFoundError    输入/输出异常；基本上是无法打开文件
# ImportError          无法引入模块或包；基本上是路径问题或名称错误
# IndentationError     语法错误（的子类） ；代码没有正确对齐
# IndexError           下标索引超出序列边界，比如当x只有三个元素，却试图访问x[5]
# KeyError             试图访问字典里不存在的键
# KeyboardInterrupt    Ctrl+C被按下
# NameError            使用一个还未被赋予对象的变量
# SyntaxError          Python代码非法，代码不能编译(个人认为这是语法错误，写错了）
# TypeError            传入对象类型与要求的不符合
# UnboundLocalError    试图访问一个还未被设置的局部变量，基本上是由于另有一个同名的全局变量，导致你以为正在访问它
# ZeroDivisionError    除数不能为0
# ValueError           传入一个调用者不期望的值，即使值的类型是正确的

#print(x)

# Traceback(异常的追踪信息) (most recent call last):
#   File "F:/pyth/python_life/base_py/6 exception handling.py", line 6, in <module>
#     print(x)
# NameError(异常类型): name 'x' is not defined(异常的值)

# 错误的种类：
# 语法错误
#if:
#   File "F:/pyth/python_life/base_py/6 exception handling.py", line 28
#     if:
#       ^
# SyntaxError: invalid syntax

# 逻辑错误(x那个)

# 异常处理
# try:
#     被检测的代码块
# except 异常类型：
#     检测到异常，就执行这个位置的逻辑

# 别用不同的逻辑处理，
# 需要用到多分支的except（类似于多分支的elif，从上到下依次匹配，匹配成功一次便不再匹配其他）

# try:
#     被检测的代码块
# except NameError:
#     触发NameError时对应的处理逻辑
# except IndexError:
#     触发IndexError时对应的处理逻辑
# except KeyError:
#     触发KeyError时对应的处理逻辑


# 多种类型的异常统一用一种逻辑处理，可以将多个异常放到一个元组内，用一个except匹配
# try:
#     被检测的代码块
# except (NameError,IndexError,TypeError):
#     触发NameError或IndexError或TypeError时对应的处理逻辑

# 捕获所有异常并用一种逻辑处理，Python提供了一个万能异常类型Exception
# try:
#     被检测的代码块
# except NameError:
#     触发NameError时对应的处理逻辑
# except IndexError:
#     触发IndexError时对应的处理逻辑
# except Exception:
#     其他类型的异常统一用此处的逻辑处理

# 在多分支except之后还可以跟一个else（else必须跟在except之后，不能单独存在），
# 只有在被检测的代码块没有触发任何异常的情况下才会执行else的子代码块
# try:
#     被检测的代码块
# except 异常类型1:
#     pass
# except 异常类型2:
#     pass
# ......
# else:
#     没有异常发生时执行的代码块



# try还可以与finally连用，从语法上讲finally必须放到else之后，
# 但可以使用try-except-finally的形式，也可以直接使用try-finally的形式。
# 无论被检测的代码块是否触发异常，都会执行finally的子代码块，
# 因此通常在finally的子代码块做一些回收资源的操作，比如关闭打开的文件、关闭数据库连接
# try:
#    被检测的代码块
# except 异常类型1:
#    pass
# except 异常类型2:
#    pass
# ......
# else:
#    没有异常发生时执行的代码块
# finally:
#    无论有无异常发生都会执行的代码块



# raise
# 不符合Python解释器的语法或逻辑规则时，是由Python解释器主动触发的各种类型的异常，
# 而对于违反程序员自定制的各类规则，则需要由程序员自己来明确地触发异常，
# 这就用到了raise语句，raise后必须是一个异常的类或者是异常的实例
class Student:
    def __init__(self,name,age):
        if not isinstance(name,str):
            raise TypeError('name must be str')
        if not isinstance(age,int):
            raise TypeError('age must be int')

        self.name=name
        self.age=age

stu1=Student(4573,18) # TypeError: name must be str
stu2=Student('egon','18') # TypeError: age must be int


# 在内置异常不够用的情况下，我们可以通过继承内置的异常类来自定义异常类

class PoolEmptyError(Exception): # 可以通过继承Exception来定义一个全新的异常
    def __init__(self,value='The proxy source is exhausted'): # 可以定制初始化方法
        super(PoolEmptyError,self).__init__()
        self.value=value

    def __str__(self): # 可以定义该方法用来定制触发异常时打印异常值的格式
        return '< %s >' %self.value


class NetworkIOError(IOError): # 也可以在特定异常的基础上扩展一个相关的异常
    pass


raise PoolEmptyError # __main__.PoolEmptyError: < The proxy source is exhausted >
raise NetworkIOError('连接被拒绝') # __main__.NetworkIOError: 连接被拒绝

# assert
#语句assert expression，断定表达式expression成立，
# 否则触发异常AssertionError，与raise-if-not的语义相同，如下
age='18'

# 若表达式isinstance(age,int)返回值为False则触发异常AssertionError
assert isinstance(age,int)

# 等同于
if not isinstance(age,int):
    raise AssertionError


# 何时使用异常处理
# 尽可能多地为程序加上try...except...，这其是在过度消费程序的可读性
# 错误发生的条件是“可预知的”，我们应该用if来进行”预防”
age=input('input your age>>: ').strip()
if age.isdigit(): # 可预知只有满足字符串age是数字的条件，int(age)才不会触发异常，
    age=int(age)
else:
    print('You must enter the number')

# 错误发生的条件“不可预知”，即异常一定会触发，
# 那么我们才应该使用try...except语句来处理。
# 例如我们编写一个下载网页内容的功能，网络发生延迟之类的异常是很正常的事，
# 而我们根本无法预知在满足什么条件的情况下才会出现延迟，因而只能用异常处理机制了

import requests
from requests.exceptions import ConnectTimeout # 导入requests模块内自定义的异常

def get(url):
    try:
        response=requests.get(url,timeout=3)#超过3秒未下载成功则触发ConnectTimeout异常
        res=response.text
    except ConnectTimeout:
        print('连接请求超时')
        res=None
    except Exception:
        print('网络出现其他异常')
        res=None
    return res

get('https://www.python.org')