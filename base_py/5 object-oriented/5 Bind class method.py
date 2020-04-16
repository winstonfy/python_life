#__author__ = 'Winston'
#date: 2020/4/2



# 类中定义的函数分为两大类：绑定方法和非绑定方法

# 其中绑定方法又分为绑定到对象的对象方法和绑定到类的类方法。

# 在类中正常定义的函数默认是绑定到对象的，而为某个函数加上装饰器@classmethod后，该函数就绑定到了类


# 配置文件settings.py的内容
#HOST='127.0.0.1'
#PORT=3306

# 类方法的应用
#import settings

# class MySQL:
#     def __init__(self,host,port):
#         self.host=host
#         self.port=port

#    @classmethod
#    def from_conf(cls): # 从配置文件中读取配置进行初始化
#        return cls(settings.HOST,settings.PORT)

#print(MySQL.from_conf) # 绑定到类的方法 <bound method MySQL.from_conf of <class ‘__main__.MySQL'>>
#conn=MySQL.from_conf() # 调用类方法，自动将类MySQL当作第一个参数传给cls

# 绑定到类的方法就是专门给类用的，但其实对象也可以调用，
# 只不过自动传入的第一个参数仍然是类，也就是说这种调用是没有意义的，
# 并且容易引起混淆，这也是Python的对象系统与其他面向对象语言对象系统的区别之一


# 为类中某个函数加上装饰器@staticmethod后，该函数就变成了非绑定方法，
# 也称为静态方法。该方法不与类或对象绑定，类与对象都可以来调用它，
# 但它就是一个普通函数而已，因而没有自动传值那么一说
import uuid

class MySQL:
    def __init__(self,host,port):
        self.id=self.create_id()
        self.host=host
        self.port=port
    @staticmethod # 静态方法，没有绑定，就是一个函数
    def create_id():
        return uuid.uuid1()

conn=MySQL('127.0.0.1',3306)
print(conn.id) #65933ca8-7493-11ea-8b9b-c8ff28cb206c

# UUID（Universally Unique Identifier）是通用唯一识别码，在许多领域用作标识，
# 比如我们常用的数据库也可以用它来作为主键，原理上它是可以对任何东西进行唯一的编码的

# uuid1()：根据当前的时间戳和MAC地址生成，最后12个字符对应的就是MAC地址。
# uuid4()：这是基于随机数的uuid，既然是随机就有可能真的遇到相同的，但这就像中奖似的，几率超小.
# uuid5(uuid.NAMESPACE_DNS, 'yuanlin')：这个看起来和uuid3()貌似并没有什么不同，
# 写法一样，也是由用户来指定namespace和字符串，不过这里用的散列并不是MD5，而是SHA1.

# 类或对象来调用create_id发现都是普通函数，而非绑定到谁的方法
print(MySQL.create_id) #<function MySQL.create_id at 0x00000000022AF400>
print(conn.create_id)  #<function MySQL.create_id at 0x00000000022AF400>

# 总结绑定方法与非绑定方法的使用：若类中需要一个功能，
# 该功能的实现代码中需要引用对象则将其定义成对象方法、
# 需要引用类则将其定义成类方法、无需引用类或对象则将其定义成静态方法。