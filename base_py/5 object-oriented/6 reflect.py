#__author__ = 'Winston'
#date: 2020/4/2

# 反射

# 在Python中，反射指的是通过字符串来操作对象的属性，
# 涉及到四个内置函数的使用（Python中一切皆对象，类和对象都可以用下述四个方法

class Teacher:
    def __init__(self,full_name):
        self.full_name =full_name

t=Teacher('Winston')

# hasattr(object,'name')
hasattr(t,'full_name') # 按字符串'full_name'判断有无属性t.full_name

# getattr(object, 'name', default=None)
getattr(t,'full_name',None) # 等同于t.full_name,不存在该属性则返回默认值None

# setattr(x, 'y', v)
setattr(t,'age',18) # 等同于t.age=18

# delattr(x, 'y')
delattr(t,'age') # 等同于del t.age

#基于反射可以十分灵活地操作对象的属性，比如将用户交互的结果反射到具体的功能执行
class FtpServer:
    def serve_forever(self):
        while True:
            inp=input('input your cmd>>: ').strip()
            cmd,file=inp.split()
            if hasattr(self,cmd): # 根据用户输入的cmd，判断对象self有无对应的方法属性
                func=getattr(self,cmd) # 根据字符串cmd，获取对象self对应的方法属性
                func(file)
    def get(self,file):
        print('Downloading %s...' %file)
    def put(self,file):
        print('Uploading %s...' %file)

server=FtpServer()
server.serve_forever()
#input your cmd>>: get a.txt
#Downloading a.txt...
#input your cmd>>: put a.txt
#Uploading a.txt...


# 内置方法

# Python的Class机制内置了很多特殊的方法来帮助使用者高度定制自己的类，
# 这些内置方法都是以双下划线开头和结尾的，会在满足某种条件时自动触发，

# __str__
# __str__方法会在对象被打印时自动触发，print功能打印的就是它的返回值，
# 我们通常基于方法来定制对象的打印信息，该方法必须返回字符串类型
class People:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return '<Name:%s Age:%s>' %(self.name,self.age) #返回类型必须是字符串

p=People('Winston',18)
print(p) #触发p.__str__()，拿到返回值后进行打印 <Name:Winston Age:18>

# __del__
# __del__会在对象被删除时自动触发。由于Python自带的垃圾回收机制会自动清理Python程序的资源，
# 所以当一个对象只占用应用程序级资源时，完全没必要为对象定制__del__方法，
# 但在产生一个对象的同时涉及到申请系统资源（比如系统打开的文件、网络连接等）的情况下，
# 关于系统资源的回收，Python的垃圾回收机制便派不上用场了
import pymysql

class MySQL:
    def __init__(self,ip,port):
        self.conn=pymysql.connect(ip,port) # 伪代码，发起网络连接，需要占用系统资源
    def __del__(self):
        self.conn.close() # 关闭网络连接，回收系统资源

obj=MySQL('127.0.0.1',3306) # 在对象obj被删除时，自动触发obj.__del__()


# __doc__ 表示类的描述信息
class Func:
    """ 这里显示的是描述信息 """

    def func(self):
        pass
print(Func.__doc__)

# 该属性无法被继承
class Foo:
    '我是描述信息'
    pass

class Bar(Foo):
    pass
print(Bar.__doc__) #该属性无法继承给子类

