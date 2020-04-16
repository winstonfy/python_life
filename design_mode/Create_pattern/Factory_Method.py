#__author__ = 'Winston'
#date: 2020/3/25

from abc import ABCMeta,abstractmethod

class Payment(metaclass=ABCMeta): # 抽象产品角色
    @abstractmethod
    def pay(self,money):
        pass


class AliPay(Payment):  #具体产品角色
    def __init__(self,use_huabei = False):
        self.use_huabei = use_huabei

    def pay(self,money):
        if self.use_huabei:
            print('花呗支付%s元'%money)
        else:
            print('支付宝支付%s元'%money)


class WeChatPay(Payment):  #具体产品角色
    def pay(self,money):
        print('微信支付%s元'%money)


class UnionPay(Payment):  #具体产品角色
    def pay(self,money):
        print('银联支付%s元'%money)


class ApplePay(Payment):  #具体产品角色
    def pay(self,money):
        print('苹果支付%s元'%money)



class PaymentFactory:    # 工厂角色

    def create_payment(self,method):
        method = method

        switch = {'AliPay':AliPay,
                  'huabei':AliPay,
                  'WeChatPay':WeChatPay,
                  'UnionPay':UnionPay,
                  'ApplePay':ApplePay}

        if switch.get(method):
            if method == 'huabei':
                return switch.get(method)(use_huabei=True)
            else:
                return switch.get(method)()
        else:
            raise NameError(method)

pf = PaymentFactory()
p = pf.create_payment('huabei')
p.pay(100)

# 简单工厂
# 不直接向客户端暴露对象创建的实现细节，而是通过一个工厂类来负责创建产品类的实例。

# 角色：
# 工厂角色（Creator）
# 抽象产品角色（Product）
# 具体产品角色（Concrete Product）

# 优点：
# 隐藏了对象创建的实现细节（比如支付宝中还需要用花呗支付，直接就可以在工厂中进行更改，不需要调用者知道实现的细节）
# 客户端不需要修改代码

# 缺点：
# 违反了单一职责原则，将创建逻辑集中到一个工厂类里
# 当添加新产品时，需要修改工厂类代码，违反了开闭原则

#-----------------------------------------------------------------------------------------------------------------------
# 简单工厂升级版：工厂方法
# 定义一个用于创建对象的接口（工厂接口），让子类决定实例化哪一个产品类

# 角色：
# 抽象工厂角色（Creator）
# 具体工厂角色（Concrete Creator）
# 抽象产品角色（Product）
# 具体产品角色（Concrete Product）

from abc import ABCMeta,abstractmethod
"""
class Payment(metaclass=ABCMeta): # 抽象产品角色
    @abstractmethod
    def pay(self,money):
        pass


class AliPay(Payment):  #具体产品角色
    def pay(self,money):
        print('支付宝支付%s元'%money)


class WeChatPay(Payment):  #具体产品角色
    def pay(self,money):
        print('微信支付%s元'%money)


class UnionPay(Payment):  #具体产品角色
    def pay(self,money):
        print('银联支付%s元'%money)


class ApplePay(Payment):  #具体产品角色
    def pay(self,money):
        print('苹果支付%s元'%money)


class PaymentFactory(metaclass=ABCMeta): # 抽象工厂
    @ abstractmethod
    def create_payment(self):
        pass

class AliPayFactory(PaymentFactory): #具体工厂
    def create_payment(self):
        return AliPay()


class WeChatPayFactory(PaymentFactory): #具体工厂
    def create_payment(self):
        return WeChatPay()

class UnionPayFactory(PaymentFactory): #具体工厂
    def create_payment(self):
        return UnionPay()

class ApplePayFactory(PaymentFactory): #具体工厂
    def create_payment(self):
        return ApplePay()

pf = AliPayFactory()
p = pf.create_payment()
p.pay(100)

"""
# 适用场景：
# 需要生产多种、大量复杂对象的时候
# 需要降低耦合度的时候
# 当系统中的产品种类需要经常扩展的时候

# 优点：
# 每个具体产品都对应一个具体工厂类，不需要修改工厂类代码
# 隐藏了对象创建的实现细节

# 缺点：
# 每增加一个具体产品类，就必须增加一个相应的具体工厂类

#-----------------------------------------------------------------------------------------------------------------------
# 工厂方法升级版：抽象工厂
# 定义一个工厂类接口，让工厂子类来创建一系列相关或相互依赖的对象。
"""
class PhoneShell(metaclass=ABCMeta):
    @abstractmethod
    def show_shell(self):
        pass


class CPU(metaclass=ABCMeta):
    @abstractmethod
    def show_cpu(self):
        pass

class OS(metaclass=ABCMeta):
    @abstractmethod
    def show_os(self):
        pass

class PhoneFactory(metaclass=ABCMeta):
    @abstractmethod
    def make_shell(self):
        pass

    @abstractmethod
    def make_cpu(self):
        pass

    @abstractmethod
    def make_os(self):
        pass

#------------------------------------------------
class SmallShell(PhoneShell):
    def show_shell(self):
        print('普通手机小手机壳')

class BigShell(PhoneShell):
    def show_shell(self):
        print('普通手机大手机壳')

class AppleShell(PhoneShell):
    def show_shell(self):
        print('苹果手机壳')

#-----------------------------------------------------------------------------------------------------------------------
class SnapdragonCPU(CPU):
    def show_cpu(self):
        print('骁龙cpu')

class KirinCPU(CPU):
    def show_cpu(self):
        print('麒麟cpu')

class MediatekCPU(CPU):
    def show_cpu(self):
        print('联发科cpu')

class AppleCPU(CPU):
    def show_cpu(self):
        print('苹果cpu')

#-----------------------------------------------------------------------------------------------------------------------
class Android(OS):
    def show_os(self):
        print('安卓系统')


class IOS(OS):
    def show_os(self):
        print('苹果系统')

#-----------------------------------------------------------------------------------------------------------------------

class MiFactory(PhoneFactory):
    def make_cpu(self):
        return SnapdragonCPU()

    def make_os(self):
        return Android()

    def make_shell(self):
        return BigShell()

class HuaWeiFactory(PhoneFactory):
    def make_cpu(self):
        return KirinCPU()

    def make_os(self):
        return Android()

    def make_shell(self):
        return SmallShell()

class IPhoneFactory(PhoneFactory):
    def make_cpu(self):
        return AppleCPU()

    def make_os(self):
        return IOS()

    def make_shell(self):
        return AppleShell()

#-----------------------------------------------------------------------------------------------------------------------

class Phone:
    def __init__(self,cpu,os,shell):
        self.cpu = cpu
        self.os = os
        self.shell = shell

    def show_info(self):
        print('手机信息：')
        self.cpu.show_cpu()
        self.os.show_os()
        self.shell.show_shell()

def make_phone(factory):
    cpu = factory.make_cpu()
    os = factory.make_os()
    shell = factory.make_shell()
    return Phone(cpu,os,shell)

# 生产一部手机，需要手机壳、CPU、操作系统三类对象进行组装，其中每类对象都有不同的种类。对每个具体工厂，分别生产一部手机所需要的三个对象。


mi= make_phone(MiFactory())
huawei = make_phone(HuaWeiFactory())
apple = make_phone(IPhoneFactory())
print('---------------小米------------------')
mi.show_info()
print('---------------华为------------------')
huawei.show_info()
print('---------------苹果------------------')
apple.show_info()
"""
# 角色：
# 抽象工厂角色（Creator）
# 具体工厂角色（Concrete Creator）
# 抽象产品角色（Product）
# 具体产品角色（Concrete Product）
# 相比工厂方法模式，抽象工厂模式中的每个具体工厂都生产一套产品。

# 适用场景：
# 系统要独立于产品的创建与组合时
# 强调一系列相关的产品对象的设计以便进行联合使用时
# 提供一个产品类库，想隐藏产品的具体实现时

# 优点：
# 将客户端与类的具体实现相分离
# 每个工厂创建了一个完整的产品系列，使得易于交换产品系列
# 有利于产品的一致性（即产品之间的约束关系）

# 缺点
# 难以支持新种类的（抽象）产品（比如要在上面的实例中加一个Tof人脸识别模块，所有都要改）
