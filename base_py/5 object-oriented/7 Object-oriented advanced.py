#__author__ = 'Winston'
#date: 2020/4/2

#isinstance(obj,cls)检查是否obj是否是类 cls 的对象
# isinstance() 与 type() 区别：
# type() 不会认为子类是一种父类类型，不考虑继承关系。
# isinstance() 会认为子类是一种父类类型，考虑继承关系。
# 如果要判断两个类型是否相同推荐使用 isinstance()。
class Foo1(object):
    pass

obj = Foo1()

isinstance(obj, Foo1)


# ssubclass(sub, super)检查sub类是否是 super 类的派生类
class Foo2(object):
    pass

class Bar(Foo2):
    pass

issubclass(Bar, Foo2)

# 解析反射 (详见6 reflect.py)
# 好处一：实现可插拔机制
# 好处二：动态导入模块（基于反射当前模块成员）

# __setattr__,__getattr__,__delattr__
class Foo:
    x=1
    def __init__(self,y):
        self.y=y

    def __getattr__(self, item):
        print('----> from getattr:你找的属性不存在')


    def __setattr__(self, key, value):
        print('----> from setattr')
        # self.key=value #这就无限递归了,你好好想想
        # self.__dict__[key]=value #应该使用它

    def __delattr__(self, item):
        print('----> from delattr')
        # del self.item #无限递归了
        self.__dict__.pop(item)

#__setattr__添加/修改属性会触发它的执行
f1=Foo(10)
print(f1.__dict__) # 因为你重写了__setattr__,凡是赋值操作都会触发它的运行,你啥都没写,就是根本没赋值,除非你直接操作属性字典,否则永远无法赋值
f1.z=3
print(f1.__dict__)

#__delattr__删除属性的时候会触发
f1.__dict__['a']=3#我们可以直接修改属性字典,来完成添加/修改属性的操作
del f1.a
print(f1.__dict__)

#__getattr__只有在使用点调用属性且属性不存在的时候才会触发
#f1.xxxxxx



# 包装
# python为大家提供了标准数据类型，以及丰富的内置方法，
# 其实在很多场景下我们都需要基于标准数据类型来定制我们自己的数据类型，
# 新增/改写方法，这就用到了我们刚学的继承/派生知识（其他的标准类型均可以通过下面的方式进行二次加工）

class List1(list): #继承list所有的属性，也可以派生出自己新的，比如append和mid
    def append(self, p_object):
        ' 派生自己的append：加上类型检查'
        if not isinstance(p_object,int):
            raise TypeError('must be int')
        super().append(p_object)

    @property
    def mid(self):
        '新增自己的属性'
        index=len(self)//2
        return self[index]

l=List1([1,2,3,4])
print(l)
l.append(5)
print(l)
# l.append('1111111') #报错，必须为int类型

print(l.mid)

#其余的方法都继承list的
l.insert(0,-123)
print(l)
l.clear()
print(l)


class List2(list):
    def __init__(self,item,tag=False):
        super().__init__(item)
        self.tag=tag
    def append(self, p_object):
        if not isinstance(p_object,str):
            raise TypeError
        super().append(p_object)
    def clear(self):
        if not self.tag:
            raise PermissionError
        super().clear()

l=List2([1,2,3],False)
print(l)
print(l.tag)

l.append('saf')
print(l)

# l.clear() #异常

l.tag=True
l.clear()


# 授权
# 授权是包装的一个特性, 包装一个类型通常是对已存在的类型的一些定制,
# 这种做法可以新建,修改或删除原有产品的功能。其它的则保持原样。
# 授权的过程,即是所有更新的功能都是由新类的某部分来处理,但已存在的功能就授权给对象的默认属性。
# 实现授权的关键点就是覆盖__getattr__方法
# 示例一
import time
class FileHandle:
    def __init__(self,filename,mode='r',encoding='utf-8'):
        self.file=open(filename,mode,encoding=encoding)
    def write(self,line):
        t=time.strftime('%Y-%m-%d %T')
        self.file.write('%s %s' %(t,line))

    def __getattr__(self, item):
        return getattr(self.file,item)

f1=FileHandle('b.txt','w+')
f1.write('你好啊')
f1.seek(0)
print(f1.read())
f1.close()

# 示例二
__author__ = 'Winston'
#我们来加上b模式支持
import time
class FileHandle:
    def __init__(self,filename,mode='r',encoding='utf-8'):
        if 'b' in mode:
            self.file=open(filename,mode)
        else:
            self.file=open(filename,mode,encoding=encoding)
        self.filename=filename
        self.mode=mode
        self.encoding=encoding

    def write(self,line):
        if 'b' in self.mode:
            if not isinstance(line,bytes):
                raise TypeError('must be bytes')
        self.file.write(line)

    def __getattr__(self, item):
        return getattr(self.file,item)

    def __str__(self):
        if 'b' in self.mode:
            res="<_io.BufferedReader name='%s'>" %self.filename
        else:
            res="<_io.TextIOWrapper name='%s' mode='%s' encoding='%s'>" %(self.filename,self.mode,self.encoding)
        return res
f1=FileHandle('b.txt','wb')
# f1.write('你好啊啊啊啊啊') #自定制的write,不用在进行encode转成二进制去写了,简单,大气
f1.write('你好啊'.encode('utf-8'))
print(f1)
f1.close()

#  __getattribute__

# 回顾__getattr__
class Foo:
    def __init__(self,x):
        self.x=x

    def __getattr__(self, item):
        print('执行的是我')
        # return self.__dict__[item]

f1=Foo(10)
print(f1.x)
f1.xxxxxx #不存在的属性访问，触发__getattr__

# __getattribute__
class Foo:
    def __init__(self,x):
        self.x=x

    def __getattribute__(self, item):
        print('不管是否存在,我都会执行')

f1=Foo(10)
f1.x
f1.xxxxxx

# __getattr__与__getattribute__二者同时出现
class Foo:
    def __init__(self,x):
        self.x=x

    def __getattr__(self, item):
        print('执行的是我')
        # return self.__dict__[item]
    def __getattribute__(self, item):
        print('不管是否存在,我都会执行')
        raise AttributeError('哈哈')

f1=Foo(10)
f1.x
f1.xxxxxx
#只会执行__getattrbute__,除非__getattribute__在执行过程中抛出异常AttributeError


#-------------------------------------------------------------------------------------------------------------
# 描述符(__get__,__set__,__delete__)
# __get__():调用一个属性时,触发
# __set__():为一个属性赋值时,触发
# __delete__():采用del删除属性时,触发

# 定义一个描述符
class Foo: #在python3中Foo是新式类,它实现了三种方法,这个类就被称作一个描述符
    def __get__(self, instance, owner):
        pass
    def __set__(self, instance, value):
        pass
    def __delete__(self, instance):
        pass

# 作用：
# 用来代理另外一个类的属性的(必须把描述符定义成这个类的类属性，不能定义到构造函数中)

# 数据描述符:至少实现了__get__()和__set__()
class Foox:
    def __set__(self, instance, value):
        print('set')
    def __get__(self, instance, owner):
        print('get')

# 非数据描述符:没有实现__set__()
class Fooa:
    def __get__(self, instance, owner):
        print('get')

# 一 描述符本身应该定义成新式类,被代理的类也应该是新式类
# 二 必须把描述符定义成这个类的类属性，不能为定义到构造函数中
# 三 要严格遵循该优先级,优先级由高到底分别是
# 1.类属性
# 2.数据描述符
# 3.实例属性
# 4.非数据描述符


# #类属性>数据描述符
#描述符Str
class Str:
    def __get__(self, instance, owner):
        print('Str调用')
    def __set__(self, instance, value):
        print('Str设置...')
    def __delete__(self, instance):
        print('Str删除...')

class People:
    name=Str()
    def __init__(self,name,age): #name被Str类代理,age被Int类代理,
        self.name=name
        self.age=age


#基于上面的演示,我们已经知道,在一个类中定义描述符它就是一个类属性,存在于类的属性字典中,而不是实例的属性字典

#那既然描述符被定义成了一个类属性,直接通过类名也一定可以调用吧,没错
print(People.name) #恩,调用类属性name,本质就是在调用描述符Str,触发了__get__()

People.name='Winston' #那赋值呢,我去,并没有触发__set__()
del People.name #赶紧试试del,我去,也没有触发__delete__()
#结论:描述符对类没有作用-------->傻逼到家的结论

'''
原因:描述符在使用时被定义成另外一个类的类属性,因而类属性比二次加工的描述符伪装而来的类属性有更高的优先级
People.name #恩,调用类属性name,找不到就去找描述符伪装的类属性name,触发了__get__()

People.name='Winston' #那赋值呢,直接赋值了一个类属性,它拥有更高的优先级,相当于覆盖了描述符,肯定不会触发描述符的__set__()
del People.name #同上
'''

# 数据描述符>实例属性
#描述符Str
class Str1:
    def __get__(self, instance, owner):
        print('Str调用')
    def __set__(self, instance, value):
        print('Str设置...')
    def __delete__(self, instance):
        print('Str删除...')

class People1:
    name=Str1()
    def __init__(self,name,age): #name被Str类代理,age被Int类代理,
        self.name=name
        self.age=age


p1=People1('Winston',18)

#如果描述符是一个数据描述符(即有__get__又有__set__),那么p1.name的调用与赋值都是触发描述符的操作,于p1本身无关了,相当于覆盖了实例的属性
p1.name='Winstonnnn'
print(p1.name)
print(p1.__dict__)#实例的属性字典中没有name,因为name是一个数据描述符,优先级高于实例属性,查看/赋值/删除都是跟描述符有关,与实例无关了
del p1.name


# 实例属性>非数据描述符
class Foo2:
    def func2(self):
        print('我胡汉三又回来了')
f2=Foo2()
f2.func2() #调用类的方法,也可以说是调用非数据描述符
#函数是一个非数据描述符对象(一切皆对象么)
print(dir(Foo2.func2))
print(hasattr(Foo2.func2,'__set__'))
print(hasattr(Foo2.func2,'__get__'))
print(hasattr(Foo2.func2,'__delete__'))
#有人可能会问,描述符不都是类么,函数怎么算也应该是一个对象啊,怎么就是描述符了
#笨蛋哥,描述符是类没问题,描述符在应用的时候不都是实例化成一个类属性么
#函数就是一个由非描述符类实例化得到的对象
#没错，字符串也一样

f2.func2='这是实例属性啊'
print(f2.func2)

del f2.func2 #删掉了非数据
f2.func2()

# 再次验证：实例属性>非数据描述符
class Foo3:
    def __set__(self, instance, value):
        print('set')
    def __get__(self, instance, owner):
        print('get')
class Room3:
    name=Foo3()
    def __init__(self,name,width,length):
        self.name=name
        self.width=width
        self.length=length


#name是一个数据描述符,因为name=Foo()而Foo实现了get和set方法,因而比实例属性有更高的优先级
#对实例的属性操作,触发的都是描述符的
r1=Room3('厕所',1,1)
r1.name
r1.name='厨房'



class Foo4:
    def __get__(self, instance, owner):
        print('get')
class Room4:
    name=Foo4()
    def __init__(self,name,width,length):
        self.name=name
        self.width=width
        self.length=length


#name是一个非数据描述符,因为name=Foo()而Foo没有实现set方法,因而比实例属性有更低的优先级
#对实例的属性操作,触发的都是实例自己的
r1=Room4('厕所',1,1)
r1.name
r1.name='厨房'

# 非数据描述符>找不到
class Foo:
    def func(self):
        print('我胡汉三又回来了')

    def __getattr__(self, item):
        print('找不到了当然是来找我啦',item)
f1=Foo()

f1.xxxxxxxxxxx

# 描述符使用
# 众所周知，python是弱类型语言，即参数的赋值没有类型限制，下面我们通过描述符机制来实现类型限制功能
# 牛刀小试

class Str:
    def __init__(self,name):
        self.name=name
    def __get__(self, instance, owner):
        print('get--->',instance,owner)
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        print('set--->',instance,value)
        instance.__dict__[self.name]=value
    def __delete__(self, instance):
        print('delete--->',instance)
        instance.__dict__.pop(self.name)


class People:
    name=Str('name')
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary

p1=People('Winston',18,3231.3)

#调用
print(p1.__dict__)
p1.name

#赋值
print(p1.__dict__)
p1.name='Winstonnnn'
print(p1.__dict__)

#删除
print(p1.__dict__)
del p1.name
print(p1.__dict__)


# 拔刀相助
class Str:
    def __init__(self,name):
        self.name=name
    def __get__(self, instance, owner):
        print('get--->',instance,owner)
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        print('set--->',instance,value)
        instance.__dict__[self.name]=value
    def __delete__(self, instance):
        print('delete--->',instance)
        instance.__dict__.pop(self.name)


class People:
    name=Str('name')
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary

#疑问:如果我用类名去操作属性呢
People.name #报错,错误的根源在于类去操作属性时,会把None传给instance

#修订__get__方法
class Str:
    def __init__(self,name):
        self.name=name
    def __get__(self, instance, owner):
        print('get--->',instance,owner)
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        print('set--->',instance,value)
        instance.__dict__[self.name]=value
    def __delete__(self, instance):
        print('delete--->',instance)
        instance.__dict__.pop(self.name)


class People:
    name=Str('name')
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
print(People.name) #完美,解决



# 磨刀霍霍
class Str:
    def __init__(self,name,expected_type):
        self.name=name
        self.expected_type=expected_type
    def __get__(self, instance, owner):
        print('get--->',instance,owner)
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        print('set--->',instance,value)
        if not isinstance(value,self.expected_type): #如果不是期望的类型，则抛出异常
            raise TypeError('Expected %s' %str(self.expected_type))
        instance.__dict__[self.name]=value
    def __delete__(self, instance):
        print('delete--->',instance)
        instance.__dict__.pop(self.name)


class People:
    name=Str('name',str) #新增类型限制str
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary

p1=People(123,18,3333.3)#传入的name因不是字符串类型而抛出异常

# 大刀阔斧
class Typed:
    def __init__(self,name,expected_type):
        self.name=name
        self.expected_type=expected_type
    def __get__(self, instance, owner):
        print('get--->',instance,owner)
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        print('set--->',instance,value)
        if not isinstance(value,self.expected_type):
            raise TypeError('Expected %s' %str(self.expected_type))
        instance.__dict__[self.name]=value
    def __delete__(self, instance):
        print('delete--->',instance)
        instance.__dict__.pop(self.name)


class People:
    name=Typed('name',str)
    age=Typed('name',int)
    salary=Typed('name',float)
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary

p1=People(123,18,3333.3)
p1=People('Winston','18',3333.3)
p1=People('Winston',18,3333)


# 大刀阔斧之后我们已然能实现功能了，但是问题是，如果我们的类有很多属性，你仍然采用在定义一堆类属性的方式去实现，low
# 类的装饰器:无参
def decorate(cls):
    print('类的装饰器开始运行啦------>')
    return cls

@decorate #无参:People=decorate(People)
class People:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary

p1=People('Winston',18,3333.3)


# 类的装饰器：有参
def typeassert(**kwargs):
    def decorate(cls):
        print('类的装饰器开始运行啦------>',kwargs)
        return cls
    return decorate
@typeassert(name=str,age=int,salary=float) #有参:1.运行typeassert(...)返回结果是decorate,此时参数都传给kwargs 2.People=decorate(People)
class People:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary

p1=People('Winston',18,3333.3)


# 刀光剑影

class Typed:
    def __init__(self,name,expected_type):
        self.name=name
        self.expected_type=expected_type
    def __get__(self, instance, owner):
        print('get--->',instance,owner)
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        print('set--->',instance,value)
        if not isinstance(value,self.expected_type):
            raise TypeError('Expected %s' %str(self.expected_type))
        instance.__dict__[self.name]=value
    def __delete__(self, instance):
        print('delete--->',instance)
        instance.__dict__.pop(self.name)

def typeassert(**kwargs):
    def decorate(cls):
        print('类的装饰器开始运行啦------>',kwargs)
        for name,expected_type in kwargs.items():
            setattr(cls,name,Typed(name,expected_type))
        return cls
    return decorate
@typeassert(name=str,age=int,salary=float) #有参:1.运行typeassert(...)返回结果是decorate,此时参数都传给kwargs 2.People=decorate(People)
class People:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary

print(People.__dict__)
p1=People('egon',18,3333.3)

#描述符是可以实现大部分python类特性中的底层魔法,包括@classmethod,@staticmethd,@property甚至是__slots__属性

#描述符是很多高级库和框架的重要工具之一,描述符通常是使用到装饰器或者元类的大型框架中的一个组件.

# 利用描述符原理完成一个自定制@property,实现延迟计算（本质就是把一个函数属性利用装饰器原理做成一个描述符：
# 类的属性字典中函数名为key，value为描述符类产生的对象

# @property回顾
class Room:
    def __init__(self,name,width,length):
        self.name=name
        self.width=width
        self.length=length

    @property
    def area(self):
        return self.width * self.length

r1=Room('Winston',1,1)
print(r1.area)

# 自己做一个@property
class Lazyproperty:
    def __init__(self,func):
        self.func=func
    def __get__(self, instance, owner):
        print('这是我们自己定制的静态属性,r1.area实际是要执行r1.area()')
        if instance is None:
            return self
        return self.func(instance) #此时你应该明白,到底是谁在为你做自动传递self的事情

class Room:
    def __init__(self,name,width,length):
        self.name=name
        self.width=width
        self.length=length

    @Lazyproperty #area=Lazyproperty(area) 相当于定义了一个类属性,即描述符
    def area(self):
        return self.width * self.length

r1=Room('alex',1,1)
print(r1.area)


# 实现延迟计算功能
class Lazyproperty:
    def __init__(self,func):
        self.func=func
    def __get__(self, instance, owner):
        print('这是我们自己定制的静态属性,r1.area实际是要执行r1.area()')
        if instance is None:
            return self
        else:
            print('--->')
            value=self.func(instance)
            setattr(instance,self.func.__name__,value) #计算一次就缓存到实例的属性字典中
            return value

class Room:
    def __init__(self,name,width,length):
        self.name=name
        self.width=width
        self.length=length

    @Lazyproperty #area=Lazyproperty(area) 相当于'定义了一个类属性,即描述符'
    def area(self):
        return self.width * self.length

r1=Room('alex',1,1)
print(r1.area) #先从自己的属性字典找,没有再去类的中找,然后出发了area的__get__方法
print(r1.area) #先从自己的属性字典找,找到了,是上次计算的结果,这样就不用每执行一次都去计算



# 一个小的改动，延迟计算的美梦就破碎了
#缓存不起来了
class Lazyproperty:
    def __init__(self,func):
        self.func=func
    def __get__(self, instance, owner):
        print('这是我们自己定制的静态属性,r1.area实际是要执行r1.area()')
        if instance is None:
            return self
        else:
            value=self.func(instance)
            instance.__dict__[self.func.__name__]=value
            return value
        # return self.func(instance) #此时你应该明白,到底是谁在为你做自动传递self的事情
    def __set__(self, instance, value):
        print('hahahahahah')

class Room:
    def __init__(self,name,width,length):
        self.name=name
        self.width=width
        self.length=length

    @Lazyproperty #area=Lazyproperty(area) 相当于定义了一个类属性,即描述符
    def area(self):
        return self.width * self.length

print(Room.__dict__)
r1=Room('alex',1,1)
print(r1.area)
print(r1.area)
print(r1.area)
print(r1.area)
#缓存功能失效,每次都去找描述符了,为何,因为描述符实现了set方法,它由非数据描述符变成了数据描述符,
# 数据描述符比实例属性有更高的优先级,因而所有的属性操作都去找描述符了


# 利用描述符原理完成一个自定制@classmethod
class ClassMethod:
    def __init__(self,func):
        self.func=func

    def __get__(self, instance, owner): #类来调用,instance为None,owner为类本身,实例来调用,instance为实例,owner为类本身,
        def feedback():
            print('在这里可以加功能啊...')
            return self.func(owner)
        return feedback

class People:
    name='Winston'
    @ClassMethod # say_hi=ClassMethod(say_hi)
    def say_hi(cls):
        print('你好啊,帅哥 %s' %cls.name)

People.say_hi()

p1=People()
p1.say_hi()
#疑问,类方法如果有参数呢,好说,好说

class ClassMethod:
    def __init__(self,func):
        self.func=func

    def __get__(self, instance, owner): #类来调用,instance为None,owner为类本身,实例来调用,instance为实例,owner为类本身,
        def feedback(*args,**kwargs):
            print('在这里可以加功能啊...')
            return self.func(owner,*args,**kwargs)
        return feedback

class People:
    name='winston'
    @ClassMethod # say_hi=ClassMethod(say_hi)
    def say_hi(cls,msg):
        print('你好啊,帅哥 %s %s' %(cls.name,msg))

People.say_hi('你是那偷心的贼')

p1=People()
p1.say_hi('你是那偷心的贼')



# 利用描述符原理完成一个自定制的@staticmethod
class StaticMethod:
    def __init__(self,func):
        self.func=func

    def __get__(self, instance, owner): #类来调用,instance为None,owner为类本身,实例来调用,instance为实例,owner为类本身,
        def feedback(*args,**kwargs):
            print('在这里可以加功能啊...')
            return self.func(*args,**kwargs)
        return feedback

class People:
    @StaticMethod# say_hi=StaticMethod(say_hi)
    def say_hi(x,y,z):
        print('------>',x,y,z)

People.say_hi(1,2,3)

p1=People()
p1.say_hi(4,5,6)



# 一个静态属性property本质就是实现了get，set，delete三种方法

# 用法一
class Foo:
    @property
    def AAA(self):
        print('get的时候运行我啊')

    @AAA.setter
    def AAA(self,value):
        print('set的时候运行我啊')

    @AAA.deleter
    def AAA(self):
        print('delete的时候运行我啊')

#只有在属性AAA定义property后才能定义AAA.setter,AAA.deleter
f1=Foo()
f1.AAA
f1.AAA='aaa'
del f1.AAA


# 用法二
class Foo:
    def get_AAA(self):
        print('get的时候运行我啊')

    def set_AAA(self,value):
        print('set的时候运行我啊')

    def delete_AAA(self):
        print('delete的时候运行我啊')
    AAA=property(get_AAA,set_AAA,delete_AAA) #内置property三个参数与get,set,delete一一对应

f1=Foo()
f1.AAA
f1.AAA='aaa'
del f1.AAA

# 怎么用
# 案例一
class Goods:

    def __init__(self):
        # 原价
        self.original_price = 100
        # 折扣
        self.discount = 0.8

    @property
    def price(self):
        # 实际价格 = 原价 * 折扣
        new_price = self.original_price * self.discount
        return new_price

    @price.setter
    def price(self, value):
        self.original_price = value

    @price.deleter
    def price(self):
        del self.original_price


obj = Goods()
obj.price         # 获取商品价格
obj.price = 200   # 修改商品原价
print(obj.price)
del obj.price     # 删除商品原价


# 案例二
#实现类型检测功能
#第一关：
class People:
    def __init__(self,name):
        self.name=name

    @property
    def name(self):
        return self.name

# p1=People('alex') #property自动实现了set和get方法属于数据描述符,比实例属性优先级高,所以你这面写会触发property内置的set,抛出异常


#第二关：修订版

class People:
    def __init__(self,name):
        self.name=name #实例化就触发property

    @property
    def name(self):
        # return self.name #无限递归
        print('get------>')
        return self.DouNiWan

    @name.setter
    def name(self,value):
        print('set------>')
        self.DouNiWan=value

    @name.deleter
    def name(self):
        print('delete------>')
        del self.DouNiWan

p1=People('alex') #self.name实际是存放到self.DouNiWan里
print(p1.name)
print(p1.name)
print(p1.name)
print(p1.__dict__)

p1.name='egon'
print(p1.__dict__)

del p1.name
print(p1.__dict__)


#第三关:加上类型检查
class People:
    def __init__(self,name):
        self.name=name #实例化就触发property

    @property
    def name(self):
        # return self.name #无限递归
        print('get------>')
        return self.DouNiWan

    @name.setter
    def name(self,value):
        print('set------>')
        if not isinstance(value,str):
            raise TypeError('必须是字符串类型')
        self.DouNiWan=value

    @name.deleter
    def name(self):
        print('delete------>')
        del self.DouNiWan

p1=People('alex') #self.name实际是存放到self.DouNiWan里
p1.name=1


#----------------------------------------------------------------------------------------------------------------


# __setitem__,__getitem,__delitem__

class Foo:
    def __init__(self,name):
        self.name=name

    def __getitem__(self, item):
        print(self.__dict__[item])

    def __setitem__(self, key, value):
        self.__dict__[key]=value
    def __delitem__(self, key):
        print('del obj[key]时,我执行')
        self.__dict__.pop(key)
    def __delattr__(self, item):
        print('del obj.key时,我执行')
        self.__dict__.pop(item)

f1=Foo('sb')
f1['age']=18
f1['age1']=19
del f1.age1
del f1['age']
f1['name']='alex'
print(f1.__dict__)

#------------------------------------------------------------------------------------------------
# __str__,__repr__,__format__
# 改变对象的字符串显示__str__,__repr__
# 自定制格式化字符串__format__

#_*_coding:utf-8_*_
__author__ = 'Linhaifeng'
format_dict={
    'nat':'{obj.name}-{obj.addr}-{obj.type}',#学校名-学校地址-学校类型
    'tna':'{obj.type}:{obj.name}:{obj.addr}',#学校类型:学校名:学校地址
    'tan':'{obj.type}/{obj.addr}/{obj.name}',#学校类型/学校地址/学校名
}
class School:
    def __init__(self,name,addr,type):
        self.name=name
        self.addr=addr
        self.type=type

    def __repr__(self):
        return 'School(%s,%s)' %(self.name,self.addr)
    def __str__(self):
        return '(%s,%s)' %(self.name,self.addr)

    def __format__(self, format_spec):
        # if format_spec
        if not format_spec or format_spec not in format_dict:
            format_spec='nat'
        fmt=format_dict[format_spec]
        return fmt.format(obj=self)

s1=School('oldboy1','北京','私立')
print('from repr: ',repr(s1))
print('from str: ',str(s1))
print(s1)

'''
str函数或者print函数--->obj.__str__()
repr或者交互式解释器--->obj.__repr__()
如果__str__没有被定义,那么就会使用__repr__来代替输出
注意:这俩方法的返回值必须是字符串,否则抛出异常
'''
print(format(s1,'nat'))
print(format(s1,'tna'))
print(format(s1,'tan'))
print(format(s1,'asfdasdffd'))


# 自定义format练习
date_dic={
    'ymd':'{0.year}:{0.month}:{0.day}',
    'dmy':'{0.day}/{0.month}/{0.year}',
    'mdy':'{0.month}-{0.day}-{0.year}',
}
class Date:
    def __init__(self,year,month,day):
        self.year=year
        self.month=month
        self.day=day

    def __format__(self, format_spec):
        if not format_spec or format_spec not in date_dic:
            format_spec='ymd'
        fmt=date_dic[format_spec]
        return fmt.format(self)

d1=Date(2016,12,29)
print(format(d1))
print('{:mdy}'.format(d1))

# issubclass和isinstance

class A:
    pass

class B(A):
    pass

print(issubclass(B,A)) #B是A的子类,返回True

a1=A()
print(isinstance(a1,A)) #a1是A的实例
#-------------------------------------------------------------------------------------------------

# __slots__ 使用
'''
1.__slots__是什么:是一个类变量,变量值可以是列表,元祖,或者可迭代对象,也可以是一个字符串(意味着所有实例只有一个数据属性)
2.引子:使用点来访问属性本质就是在访问类或者对象的__dict__属性字典(类的字典是共享的,而每个实例的是独立的)
3.为何使用__slots__:字典会占用大量内存,如果你有一个属性很少的类,但是有很多实例,为了节省内存可以使用__slots__取代实例的__dict__
当你定义__slots__后,__slots__就会为实例使用一种更加紧凑的内部表示。实例通过一个很小的固定大小的数组来构建,而不是为每个实例定义一个
字典,这跟元组或列表很类似。在__slots__中列出的属性名在内部被映射到这个数组的指定小标上。使用__slots__一个不好的地方就是我们不能再给
实例添加新的属性了,只能使用在__slots__中定义的那些属性名。
4.注意事项:__slots__的很多特性都依赖于普通的基于字典的实现。另外,定义了__slots__后的类不再 支持一些普通类特性了,比如多继承。大多数情况下,你应该
只在那些经常被使用到 的用作数据结构的类上定义__slots__比如在程序中需要创建某个类的几百万个实例对象 。
关于__slots__的一个常见误区是它可以作为一个封装工具来防止用户给实例增加新的属性。尽管使用__slots__可以达到这样的目的,但是这个并不是它的初衷。           更多的是用来作为一个内存优化工具。

'''


class Foo:
    __slots__ = 'x'


f1 = Foo()
f1.x = 1
f1.y = 2  # 报错
print(f1.__slots__)  # f1不再有__dict__


class Bar:
    __slots__ = ['x', 'y']


n = Bar()
n.x, n.y = 1, 2
n.z = 3  # 报错

# 刨根问底
class Foo:
    __slots__=['name','age']

f1=Foo()
f1.name='alex'
f1.age=18
print(f1.__slots__)

f2=Foo()
f2.name='egon'
f2.age=19
print(f2.__slots__)

print(Foo.__dict__)
#f1与f2都没有属性字典__dict__了,统一归__slots__管,节省内存

#-------------------------------------------------------------------------------------------------------

# __next__和__iter__实现迭代器协议

# 简单示范
class Foo:
    def __init__(self,x):
        self.x=x

    def __iter__(self):
        return self

    def __next__(self):
        n=self.x
        self.x+=1
        return self.x

f=Foo(3)
for i in f:
    print(i)

# 简单示范二
class Foo:
    def __init__(self,start,stop):
        self.num=start
        self.stop=stop
    def __iter__(self):
        return self
    def __next__(self):
        if self.num >= self.stop:
            raise StopIteration
        n=self.num
        self.num+=1
        return n

f=Foo(1,5)
from collections import Iterable,Iterator
print(isinstance(f,Iterator))

for i in Foo(1,5):
    print(i)

# 练习：简单模拟range，加上步长
class Range:
    def __init__(self,n,stop,step):
        self.n=n
        self.stop=stop
        self.step=step

    def __next__(self):
        if self.n >= self.stop:
            raise StopIteration
        x=self.n
        self.n+=self.step
        return x

    def __iter__(self):
        return self

for i in Range(1,7,3): #
    print(i)


# 斐波那契数列
class Fib:
    def __init__(self):
        self._a=0
        self._b=1

    def __iter__(self):
        return self

    def __next__(self):
        self._a,self._b=self._b,self._a + self._b
        return self._a

f1=Fib()

print(f1.__next__())
print(next(f1))
print(next(f1))

for i in f1:
    if i > 100:
        break
    print('%s ' %i,end='')
#-------------------------------------------------------------------------------------------------------


# __module__和__class__

# 　　__module__ 表示当前操作的对象在那个模块
# 　　__class__     表示当前操作的对象的类是什么


# lib/aa.py
class C:

    def __init__(self):
        self.name = 'NB'

# lib/bb.py

from lib.aa import C

obj = C()
print(obj.__module__) # 输出 lib.aa 即输出模块
print(obj.__class__) # 输出 lib.aa.C 即输出类


# -----------------------------------------------------------------------------------
#__del__
#析构方法，当对象在内存中被释放时，自动触发执行。

#注：如果产生的对象仅仅只是python程序级别的（用户级），那么无需定义__del__,
# 如果产生的对象的同时还会向操作系统发起系统调用，
# 即一个对象有用户级与内核级两种资源，比如（打开一个文件，创建一个数据库链接），
# 则必须在清除对象的同时回收系统资源，这就用到了__del__

# -------------------------------------------------------------------------------------

# __enter__和__exit__
# 我们知道在操作文件对象的时候可以这么写 with open xxxx as f:
# 述叫做上下文管理协议，即with语句，为了让一个对象兼容with语句，
# 必须在这个对象的类中声明__enter__和__exit__方法

# 上下文管理协议
class Open:
    def __init__(self,name):
        self.name=name

    def __enter__(self):
        print('出现with语句,对象的__enter__被触发,有返回值则赋值给as声明的变量')
        # return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('with中代码块执行完毕时执行我啊')


with Open('a.txt') as f:
    print('=====>执行代码块')
    # print(f,f.name)

# _exit__()中的三个参数分别代表异常类型，
# 异常值和追溯信息,with语句中代码块出现异常，则with后的代码都无法执行

class Open:
    def __init__(self,name):
        self.name=name

    def __enter__(self):
        print('出现with语句,对象的__enter__被触发,有返回值则赋值给as声明的变量')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('with中代码块执行完毕时执行我啊')
        print(exc_type)
        print(exc_val)
        print(exc_tb)



with Open('a.txt') as f:
    print('=====>执行代码块')
    raise AttributeError('***着火啦,救火啊***')
print('0'*100) #------------------------------->不会执行

# 如果__exit()返回值为True,那么异常会被清空，就好像啥都没发生一样，with后的语句正常执行
class Open:
    def __init__(self,name):
        self.name=name

    def __enter__(self):
        print('出现with语句,对象的__enter__被触发,有返回值则赋值给as声明的变量')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('with中代码块执行完毕时执行我啊')
        print(exc_type)
        print(exc_val)
        print(exc_tb)
        return True



with Open('a.txt') as f:
    print('=====>执行代码块')
    raise AttributeError('***着火啦,救火啊***')
print('0'*100) #------------------------------->会执行

# 练习：模拟Open
class Open:
    def __init__(self,filepath,mode='r',encoding='utf-8'):
        self.filepath=filepath
        self.mode=mode
        self.encoding=encoding

    def __enter__(self):
        # print('enter')
        self.f=open(self.filepath,mode=self.mode,encoding=self.encoding)
        return self.f

    def __exit__(self, exc_type, exc_val, exc_tb):
        # print('exit')
        self.f.close()
        return True
    def __getattr__(self, item):
        return getattr(self.f,item)

with Open('a.txt','w') as f:
    print(f)
    f.write('aaaaaa')
    f.wasdf #抛出异常，交给__exit__处理


# 使用with语句的目的就是把代码块放入with中执行，with结束后，自动完成清理工作，无须手动干预
# 在需要管理一些资源比如文件，网络连接和锁的编程环境中，
# 可以在__exit__中定制自动释放资源的机制，你无须再去关系这个问题，这将大有用处


#---------------------------------------------------------------------------------------

# __call__
# 对象后面加括号，触发执行。
# 注：构造方法的执行是由创建对象触发的，即：对象 = 类名() ；
# 而对于 __call__ 方法的执行是由对象后加括号触发的，即：对象() 或者 类()()

class Foo:

    def __init__(self):
        pass

    def __call__(self, *args, **kwargs):
        print('__call__')


obj = Foo()  # 执行 __init__
obj()  # 执行 __call__