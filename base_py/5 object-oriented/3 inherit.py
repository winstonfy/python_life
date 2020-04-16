#__author__ = 'Winston'
#date: 2020/4/2

# 继承

# 继承是一种创建新类的方式，在Python中，新建的类可以继承一个或多个父类，
# 新建的类可称为子类或派生类，父类又可称为基类或超类
class ParentClass1: #定义父类
    pass

class ParentClass2: #定义父类
    pass

class SubClass1(ParentClass1): #单继承
    pass

class SubClass2(ParentClass1,ParentClass2): #多继承
    pass

print(SubClass2.__bases__) #查看此类继承的所有父类

# 显式地继承object的类，以及该类的子类，都是新式类。而在Python3中，即使没有显式地继承object，也会默认继承该类
print(ParentClass1.__bases__,ParentClass2.__bases__) # (<class 'object'>,) (<class 'object'>,)
# 在Python3中统一都是新式类


# 继承与抽象
# 子类可以继承／遗传父类所有的属性，因而继承可以用来解决类与类之间的代码重用性问题。
class People11:
    school = '华中科技大学文华学院'

    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age


class Student(People11):
    def choose(self):
        print('%s is choosing a course' % self.name)


class Teacher11(People11):
    def teach(self):
        print('%s is teaching' % self.name)

teacher1=Teacher11('lili','male',18)
print(teacher1.school,teacher1.name,teacher1.sex,teacher1.age)

# 属性查找
# 有了继承关系，对象在查找属性时，先从对象自己的__dict__中找，如果没有则去子类中找，然后再去父类中找
class Foo1:
    def f1(self):
        print('Foo.f1')
    def f2(self):
        print('Foo.f2')
        self.f1()

class Bar1(Foo1):
    def f1(self):
        print('bar1.f1')

b=Bar1()
b.f2()
#Foo.f2
#bar1.f1

# 父类如果不想让子类覆盖自己的方法，可以采用双下划线开头的方式将方法设置为私有的
class Foo2:
    def __f1(self): # 变形为_Foo__fa
        print('Foo.f1')
    def f2(self):
        print('Foo.f2')
        self.__f1() # 变形为self._Foo__fa,因而只会调用自己所在的类中的方法

class Bar2(Foo2):
    def __f1(self): # 变形为_Bar__f1
        print('Bar2.f1')


b=Bar2()
b.f2() #在父类中找到f2方法，进而调用b._Foo__f1()方法，同样是在父类中找到该方法
#Foo.f2
#Foo.f1

# 继承的实现原理
# 对于你定义的每一个类，Python都会计算出一个方法解析顺序(MRO)列表，该MRO列表就是一个简单的所有基类的线性顺序列表
print(Bar2.mro()) # 新式类内置了mro方法可以查看线性列表的内容，经典类没有该内置该方法

# MRO列表的构造是通过一个C3线性化算法来实现的，我们无需深究该算法的数学原理,它实际上就是合并所有父类的MRO列表，且在查找属性时，
# Python会基于MRO列表按照从左到右的顺序依次查找基类,直到找到第一个匹配这个属性的类为止。



# 派生与方法重用
# 子类可以派生出自己新的属性，在进行属性查找时，子类中的属性名会优先于父类被查找，
# 例如每个老师还有职称这一属性，我们就需要在Teacher类中定义该类自己的__init__覆盖父类的

class People1:
    school='华中科技大学文华学院'

    def __init__(self,name,sex,age):
        self.name=name
        self.sex=sex
        self.age=age

class Teacher1(People1):
    def __init__(self,name,sex,age,title): # 派生
        self.name=name
        self.sex=sex
        self.age=age
        self.title=title
    def teach(self):
        print('%s is teaching' %self.name)

obj1=Teacher1('aaaa','male',20,'superman') #只会找自己类中的__init__，并不会自动调用父类的
print(obj1.name,obj1.sex,obj1.age,obj1.title)
# ('honghong', 'male', 20, 'superman')

# 很明显子类Teacher中__init__内的前三行又是在写重复代码，若想在子类派生出的方法内重用父类的功能，有两种实现方式

# 方式一：指名道姓”地调用某一个类的函数 不建议使用
class Teacher2(People1):
    def __init__(self,name,sex,age,title):
        People1.__init__(self,name,age,sex) #调用的是函数,因而需要传入self
        self.title=title
    def teach(self):
        print('%s is teaching' %self.name)

obj2=Teacher2('bbbb',20,'male','superman') #只会找自己类中的__init__，并不会自动调用父类的
print(obj2.name,obj2.sex,obj2.age,obj2.title)

# 方式二：调用super()会得到一个特殊的对象，该对象专门用来引用父类的属性，且严格按照MRO规定的顺序向后查找
class Teacher3(People1):
    def __init__(self,name,sex,age,title):
        super().__init__(name,age,sex) #调用的是绑定方法，自动传入self
        self.title=title
    def teach(self):
        print('%s is teaching' %self.name)

obj3=Teacher3('cccc',20,'male','superman') #只会找自己类中的__init__，并不会自动调用父类的
print(obj2.name,obj3.sex,obj3.age,obj3.title)


# 方式一与方式二的区别：方式一是跟继承没有关系的，而方式二的super()是依赖于继承的，
# 并且即使没有直接继承关系，super()仍然会按照MRO继续往后查找
class A:  #A没有继承B
    def test(self):
        super().test()

class B:
    def test(self):
        print('from B')

class C(A,B):
    pass

c=C() # C.mro()
print(C.mro()) # [<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>,<class ‘object'>]
c.test() # from B


# 组合
# 在一个类中以另外一个类的对象作为数据属性，称为类的组合
# 组合与继承都是用来解决代码的重用性问题

# 组合则是一种“有”的关系，比如老师有生日，老师有多门课程，
# 当类之间有显著不同，并且较小的类是较大的类所需要的组件时，应该使用组合

class Course:
    def __init__(self,name,period,price):
        self.name=name
        self.period=period
        self.price=price
    def tell_info(self):
        print('<%s %s %s>' %(self.name,self.period,self.price))

class Date:
    def __init__(self,year,mon,day):
        self.year=year
        self.mon=mon
        self.day=day
    def tell_birth(self):
       print('<%s-%s-%s>' %(self.year,self.mon,self.day))

class People:
    school='华中科技大学'
    def __init__(self,name,sex,age):
        self.name=name
        self.sex=sex
        self.age=age

#Teacher类基于继承来重用People的代码，基于组合来重用Date类和Course类的代码
class Teacher(People): #老师是人
    def __init__(self,name,sex,age,title,year,mon,day):
        super().__init__(name,age,sex)
        self.birth=Date(year,mon,day) #老师有生日
        self.courses=[] #老师有课程，可以在实例化后，往该列表中添加Course类的对象
    def teach(self):
        print('%s is teaching' %self.name)


python=Course('python','3mons',3000.0)
linux=Course('linux','5mons',5000.0)
teacher1=Teacher('lili','female',28,'博士生导师',1990,3,23)

# teacher1有两门课程
teacher1.courses.append(python)
teacher1.courses.append(linux)

# 重用Date类的功能
teacher1.birth.tell_birth()

# 重用Course类的功能
for obj in teacher1.courses:
    obj.tell_info()