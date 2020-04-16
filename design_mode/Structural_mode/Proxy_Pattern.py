#__author__ = 'Winston'
#date: 2020/3/26

# 为其他对象提供一种代理以控制对这个对象的访问。


# 虚代理实例
from abc import ABCMeta,abstractmethod

class Subject(metaclass=ABCMeta):
    @abstractmethod
    def get_content(self):
        pass

class RealSubject(Subject):
    def __init__(self,filename):
        print('读取%s文件内容'%filename)
        f = open(filename)
        self.content = f.read()
        f.close()

    def get_content(self):
        return self.content


class ProxyB(Subject):
    def __init__(self,filename):
        self.filename = filename
        self.subj = None

    def get_content(self):
        if not self.subj:
            self.subj = RealSubject(self.filename)
        return self.subj.get_content()


A = RealSubject('abc.txt')
print(A.get_content())



# P = ProxyB('abc.txt') # 适用虚代理
# print(P.get_content())























# 角色：
# 抽象实体（Subject）
# 实体（RealSubject）
# 代理（Proxy）

# 适用场景：
# 远程代理：为远程的对象提供代理
# 虚代理：根据需要创建很大的对象
# 保护代理：控制对原始对象的访问，用于对象有不同访问权限时

# 优点：
# 远程代理：可以隐藏对象位于远程地址空间的事实
# 虚代理：可以进行优化，例如根据要求创建对象
# 保护代理：允许在访问一个对象时有一些附加的内务处理