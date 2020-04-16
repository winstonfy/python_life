#__author__ = 'Winston'
#date: 2020/3/25

# 保证一个类只有一个实例，并提供一个访问它的全局访问点

# 当类只能有一个实例而且客户可以从一个众所周知的访问点访问它时


class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,"_instance"):
            cls._instance = super(Singleton,cls).__new__(cls)
        return cls._instance


class MyClass(Singleton):
    def __init__(self,name = None):
        if name is not None:
            self.name = name


a = MyClass('a')

print(a)
print(a.name)

b = MyClass('b')

print(b.name)

print(a.name)















# 适用场景：日志对象，数据库连接对象，文件系统

# 优点：
# 对唯一实例的受控访问
# 单例相当于全局变量，但防止了命名空间被污染
# 与单例模式功能相似的概念：全局变量、静态变量（方法）