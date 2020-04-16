#__author__ = 'Winston'
#date: 2020/4/1

# 类与对象
class Student:
    school = '清华大学'

    # 该方法会在对象产生之后自动执行，专门为对象进行初始化操作，可以有任意代码，但一定不能返回非None的值
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age

    def choose(self):
        print('%s is choosing a course' % self.name)

# 类体最常见的是变量的定义和函数的定义，但其实类体可以包含任意Python代码，
# 类体的代码在类定义阶段就会执行，因而会产生新的名称空间用来存放类中定义的名字，
# 可以打印Student.__dict__来查看类这个容器内盛放的东西

print(Student.__dict__) # 查看类变量、函数名信息
#print(dir(Student)) # 查看类中的所有方法

stu1=Student('李建刚','男',28)  # 一个实例(对象)
stu2=Student('王大力','女',18)
stu3=Student('牛嗷嗷','男',38)
print(stu1.__dict__) # 查看类变量、函数名信息

# 操作类的属性
aax=Student.school # 访问数据属性，等同于Student.__dict__['school']
aab=Student.choose # 访问函数属性，等同于Student.__dict__['choose']
Student.tag=123    #修改或新增属性
# del Student.school #删除属性

#操作对象的属性
bbx=stu1.name # 查看，等同于stu1.__dict__[‘name']
stu1.course='python' # 新增，等同于stu1.__dict__[‘course']='python'
stu1.age=38 # 修改，等同于stu1.__dict__[‘age']=38
del stu1.course # 删除，等同于del stu1.__dict__['course']

# 属性查找顺序与绑定方法
# 对象在访问属性时，会优先从对象本身的__dict__中查找，未找到，则去类的__dict__中查找

# 类中定义的变量是类的数据属性，是共享给所有对象用的，指向相同的内存地址
if id(stu1.school) ==id(stu2.school)==id(stu3.school):
    print(True)

# 类中定义的函数主要是给对象使用的，而且是绑定给对象的，
# 虽然所有对象指向的都是相同的功能，但是绑定到不同的对象就是不同的绑定方法，内存地址各不相同

# 绑定到对象的方法特殊之处在于，绑定给谁就应该由谁来调用，谁来调用，就会将’谁’本身当做第一个参数自动传入
stu1.choose() # 实质 Student.choose(stu1)

#注意：绑定到对象方法的这种自动传值的特征，
# 决定了在类中定义的函数都要默认写一个参数self，self可以是任意名字，但命名为self是约定俗成的。

# Python中一切皆为对象，且Python3中类与类型是一个概念，因而绑定方法我们早就接触过
print(list)
#实例化的到3个对象l1,l2,l3
l1=list([2,1,3])
l2=list(['a','b','c'])
l3=list(['x','y'])

l1.append(4) #操作绑定方法l1.append(4),就是在往l1添加4,绝对不会将4添加到l2或l3
#<built-in method append of list object at 0x10b482b48>
l2.append('d')
#<built-in method append of list object at 0x10b482b88>
l3.append('z')
#<built-in method append of list object at 0x10b482bc8>

l1.sort() # 本质 list.sort(l1)
list.append(l1,8) # l1.append(8)
print(l1)
# 类中定义的函数主要是给对象使用的，而且是绑定给对象的

