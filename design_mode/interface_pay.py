#__author__ = 'Winston'
#date: 2020/3/25

#-----------------------------------------------------------------------------------------------------------------------
#面向对象回顾
# 封装
# 继承
# 多态（python是隐式语言（不同于java，属于显式语言），本身就是多态，没有提供非多态的实现方式）


#-----------------------------------------------------------------------------------------------------------------------
# 实现接口的支付示例
from abc import ABCMeta,abstractmethod

class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self,money):
        pass


class AliPay(Payment):
    def pay(self,money):
        print('支付宝支付%s元'%money)


class WeChatPay(Payment):
    def pay(self,money,arg): # 没有按照接口中要求的参数实现，给出了警告
        print('微信支付%s元'%money)


class UnionPay(Payment):
    def pay(self,money):
        print('银联支付%s元'%money)


class ApplePay(Payment):
    def pay(self,money):
        print('苹果支付%s元'%money)

# 函数签名：函数名、参数个数和类型、返回值类型
# 接口：一种特殊的类，声明了若干方法，要求实现该接口的类必须实现这些方法
# 作用：限制继承接口的类的方法的名称及调用方式；隐藏了类的内部实现(python不行，C++中可以只提供二进制的接口文件)
# 总结：接口就是一种抽象的基类（父类），限制继承它的类必须实现接口中定义的某些方法

# python中对实现接口不严谨的示例
a = WeChatPay()
a.pay(200,12) # 并没有报错，对方法中的参数个数及类型没有如java，C++中那样严格限制

#-----------------------------------------------------------------------------------------------------------------------
# 设计模式中的六大原则

# 开放闭合原则
# 一个软件实体如类、模块和函数应该对扩展开放，对修改关闭。即软件实体应尽量在不修改原有代码的情况下进行扩展。
# 总结：修改代码不行（关键代码不能改），添加代码可以

# 里氏（Liskov）替换原则
# 所有引用基类（父类）的地方必须能透明地使用其子类的对象。

# 依赖倒置原则
# 高层模块不应该依赖低层模块，二者都应该依赖其抽象；抽象不应该依赖细节；细节应该依赖抽象。换言之，要针对接口编程，而不是针对实现编程。

# 接口隔离原则
# 使用多个专门的接口，而不使用单一的总接口，即客户端（高层的模块或代码）不应该依赖那些它不需要的接口。

"""
class Animal(metaclass=ABCMeta):
    @abstractmethod
    def walk(self):
        pass

    @abstractmethod
    def fly(self):
        pass

    @abstractmethod
    def swim(self):
        pass

class Tiger(Animal):
    pass

class Swan(Animal):
    pass

class Whale(Animal):
    pass
"""

# 上面的老虎类，天鹅类，鲸鱼类都必须实现动物接口的所有方法，不满足接口隔开原则

# 改进如下，把单一总接口，改为多个专用接口：
class WalkAnimal(metaclass=ABCMeta):
    @abstractmethod
    def walk(self):
        pass

class FlyAnimal(metaclass=ABCMeta):
    @abstractmethod
    def fly(self):
        pass

class SwimAnimal(metaclass=ABCMeta):

    @abstractmethod
    def swim(self):
        pass

class Tiger(WalkAnimal):
    def walk(self):
        pass

class Swan(WalkAnimal,FlyAnimal):
    def walk(self):
        pass

    def fly(self):
        pass

class Whale(SwimAnimal):
    def swim(self):
        pass

# python中多继承，常用在多实现接口时使用，而java是单继承（只能继承一个父类）多实现接口（但可以实现多个接口）

# 迪米特法则
# 一个软件实体应当尽可能少地与其他实体发生相互作用。解耦，依赖越少越好

# 单一职责原则
# 不要存在多于一个导致类变更的原因。通俗的说，即一个类只负责一项职责。