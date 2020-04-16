#__author__ = 'Winston'
#date: 2020/3/26

from abc import ABCMeta,abstractmethod


class Payment(metaclass=ABCMeta): # 抽象产品角色
    @abstractmethod
    def pay(self,money):
        pass


class AliPay(Payment):
    def pay(self,money):
        print('支付宝支付%s元'%money)


class WeChatPay(Payment):  #具体产品角色
    def pay(self,money):
        print('微信支付%s元'%money)


class UnionPay(Payment):  #具体产品角色
    def pay(self,money):
        print('银联支付%s元'%money)

# 需要新增一个支付类，但是函数名称和参数都不同,原有接口无法实现，且该支付类不能被更改（有其他模块在调用），例如：

class InstallmentPay:
    def amortization(self,money):  # 待适配类
        print('分期乐支付%s元'%money)

# class NewInstallmentPay(InstallmentPay,Payment): # 类适配器
#     def pay(self,money):
#         self.amortization(money)

# 待适配类，比较多时，用类适配器就十分麻烦
# 升级版：基于对象的适配器
#-----------------------------------------------------------------------------------------------------------------------
class PaymentAdopter(Payment): #对象适配器
    def __init__(self,p):
        self.payment = p

    def pay(self,money):
        self.payment.amortization(money)

p = PaymentAdopter(InstallmentPay())
p.pay(299)



# 内容：将一个类的接口转换成客户希望的另一个接口。适配器模式使得原本由于接口不兼容而不能一起工作的那些类可以一起工作。

# 角色：
# 目标接口（Target）
# 待适配的类（Adaptee）
# 适配器（Adapter）

# 两种实现方式：
# 类适配器：使用多继承
# 对象适配器：使用组合

# 适用场景：
# 想使用一个已经存在的类，而它的接口不符合你的要求
# （对象适配器）想使用一些已经存在的子类，但不可能对每一个都进行子类化以匹配它们的接口。对象适配器可以适配它的父类接口。
