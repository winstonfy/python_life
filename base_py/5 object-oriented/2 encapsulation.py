#__author__ = 'Winston'
#date: 2020/4/1

# 面向对象编程有三大特性：封装、继承、多态，其中最重要的一个特性就是封装
# 封装

# 隐藏属性
# Python的Class机制采用双下划线开头的方式将属性隐藏起来（设置成私有的），
# 但其实这仅仅只是一种变形操作，类中所有双下滑线开头的属性都会在类定义阶段、检测语法时自动变成“_类名__属性名”的形式

class Foo1:
    __N = 0  # 变形为_Foo__N

    def __init__(self):  # 定义函数时，会检测函数语法，所以__开头的属性也会变形
        self.__x = 10  # 变形为self._Foo__x

    def __f1(self):  # 变形为_Foo__f1
        print('__f1 run')

    def f2(self):  # 定义函数时，会检测函数语法，所以__开头的属性也会变形
        self.__f1()  # 变形为self._Foo__f1()


#print(Foo.__N)  # 报错AttributeError:类Foo没有属性__N

obj = Foo1()
#print(obj.__x)  # 报错AttributeError:对象obj没有属性__x

# 在类外部无法直接访问双下滑线开头的属性，但知道了类名和属性名就可以拼出名字：_类名__属性，
# 然后就可以访问了，如Foo._A__N，所以说这种操作并没有严格意义上地限制外部访问，仅仅只是一种语法意义上的变形。
#print(Foo.__dict__)
#print(Foo._Foo__N)
#print(obj._Foo__x)
#print(obj._Foo__N)

# 在类内部是可以直接访问双下滑线开头的属性的，比如self.__f1()，
# 因为在类定义阶段类内部双下滑线开头的属性统一发变形操作只在类定义阶段发生一次,在类定义之后的赋值操作，不会变形生了变形。
obj.f2()

# 变形操作只在类定义阶段发生一次,在类定义之后的赋值操作，不会变形
Foo1.__ab =100
obj.__y=20
#print(Foo.__dict__) # 找到 '__ab': 100
#print(obj.__dict__) # 找到 '__y': 20
#print(obj.__y) # 20

# 隐藏数据属性
# 将数据隐藏起来就限制了类外部对数据的直接操作，
# 然后类内应该提供相应的接口来允许类外部间接地操作数据，接口之上可以附加额外的逻辑来对数据的操作进行严格地控制
class Teacher:
    def __init__(self,name,age): #将名字和年纪都隐藏起来
        self.__name=name
        self.__age=age
    def tell_info(self): #对外提供访问老师信息的接口
        print('姓名:%s,年龄:%s' %(self.__name,self.__age))
    def set_info(self,name,age): #对外提供设置老师信息的接口，并附加类型检查的逻辑
        if not isinstance(name,str):
            raise TypeError('姓名必须是字符串类型')
        if not isinstance(age,int):
            raise TypeError('年龄必须是整型')
        self.__name=name
        self.__age=age

#t=Teacher('lili',18)
#t.set_info('LiLi','19') # 年龄不为整型，抛出异常
#t.tell_info() # 查看老师的信息

# 隐藏函数属性
#目的的是为了隔离复杂度，例如ATM程序的取款功能,该功能有很多其他功能组成，
#比如插卡、身份认证、输入金额、打印小票、取钱等，
#而对使用者来说,只需要开发取款这个功能接口即可,其余功能我们都可以隐藏起来
class ATM:
    def __card(self): #插卡
       print('插卡')
    def __auth(self): #身份认证
        print('用户认证')
    def __input(self): #输入金额
        print('输入取款金额')
    def __print_bill(self): #打印小票
        print('打印账单')
    def __take_money(self): #取钱
        print('取款')
    def withdraw(self): #取款功能
        self.__card()
        self.__auth()
        self.__input()
        self.__print_bill()
        self.__take_money()


obj=ATM()
obj.withdraw()

# 总结隐藏属性与开放接口，本质就是为了明确地区分内外，
# 类内部可以修改封装内的东西而不影响外部调用者的代码；而类外部只需拿到一个接口，
# 只要接口名、参数不变，则无论设计者如何改变内部实现代码，使用者均无需改变代码。
# 这就提供一个良好的合作基础，只要接口这个基础约定不变，则代码的修改不足为虑

#@property
# 装饰器property，可以将类中的函数“伪装成”对象的数据属性，
# 对象在访问该特殊属性时会触发功能的执行，然后将返回值作为本次访问的结果，
class People:
    def __init__(self,name,weight,height):
        self.name=name
        self.weight=weight
        self.height=height
    @property
    def bmi(self):
        return self.weight / (self.height**2)


objx=People('lili',75,1.85)
print(objx.bmi) #触发方法bmi的执行，将obj自动传给self，执行后返回值作为本次引用的结果
# 使用property有效地保证了属性访问的一致性。另外property还提供设置和删除属性的功能，
class Foo:
    def __init__(self,val):
        self.__NAME=val #将属性隐藏起来
    @property
    def name(self):
        return self.__NAME
    @name.setter
    def name(self,value):
        if not isinstance(value,str):  #在设定值之前进行类型检查
            raise TypeError('%s must be str' %value)
        self.__NAME=value #通过类型检查后,将值value存放到真实的位置self.__NAME
    @name.deleter
    def name(self):
        raise PermissionError('Can not delete')

f=Foo('lili')
print(f.name) #lili
f.name='LiLi' #触发name.setter装饰器对应的函数name(f,’Egon')
f.name=123 #触发name.setter对应的的函数name(f,123),抛出异常TypeError
del f.name #触发name.deleter对应的函数name(f),抛出异常PermissionError