#__author__ = 'Winston'
#date: 2020/3/26

# 组合模式

# 将对象组合成树形结构以表示“部分-整体”的层次结构。组合模式使得用户对单个对象和组合对象的使用具有一致性

# 角色：
# 抽象组件（Component）
# 叶子组件（Leaf）
# 复合组件（Composite）
# 客户端（Client）

# 适用场景：
# 表示对象的“部分-整体”层次结构（特别是结构是递归的）
# 希望用户忽略组合对象与单个对象的不同，用户统一地使用组合结构中的所有对象

# 优点：
# 定义了包含基本对象和组合对象的类层次结构
# 简化客户端代码，即客户端可以一致地使用组合对象和单个对象
# 更容易增加新类型的组件

# 缺点：
# 很难限制组合中的组件

from abc import ABCMeta,abstractmethod

class Graphic(metaclass=ABCMeta):
    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def get_children(self):
        pass

class Point(Graphic):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def draw(self):
        print(self)

    def add(self,graphic):
        raise TypeError

    def get_children(self):
        raise TypeError

    def __str__(self):
        return '点(%s,%s)'% (self.x,self.y)


class Line(Graphic):
    def __init__(self,p1,p2):
        self.p1 = p1
        self.p2 = p2


    def draw(self):
        print(self)

    def add(self,graphic):
        raise TypeError

    def get_children(self):
        raise TypeError

    def __str__(self):
        return "线段（%s,%s）"%(self.p1,self.p2)

class Picture(Graphic):
    def __init__(self):
        self.children = []

    def add(self,graphic):
        self.children.append(graphic)

    def get_children(self):
        return self.children

    def draw(self):
        print('----------复合图形-------------')
        for g in self.children:
            g.draw()
        print('--------------end-------------')


pic1 = Picture()
pic1.add(Point(2,3))
pic1.add(Line(Point(1,2),Point(4,5)))
pic1.add(Line(Point(0,1),Point(2,1)))

pic2 = Picture()
pic2.add(Point(-2,-1))
pic2.add(Line(Point(0,0),Point(1,1)))

pic = Picture()
pic.add(pic1)
pic.add(pic2)
pic.draw()