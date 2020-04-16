#__author__ = 'Winston'
#date: 2020/4/1


# 定义:  函数是指将一组语句的集合通过一个名字(函数名)封装起来，要想执行这个函数，只需调用其函数名即可。

# 特性：减少重复代码、使程序变的可扩展、使程序变得易维护

# def pass
# 函数名： 有名  匿名函数 lambda
# 参数：无参  有参
# 普通参数（位置参数） 关键字参数 key=value 关键字参数在位置参数后面 默认参数
# 可变长参数 *args 元组  **kwargs 字典 函数留有这两个参数，通常用来日后方便做扩展
# 命名关键字参数 *之后 ，**之前
# 想要限定函数的调用者必须以key=value的形式传值，Python3提供了专门的语法：
# 需要在定义形参时，用*作为一个分隔符号，号之后的形参称为命名关键字参数。
# 对于这类参数，在函数调用时，必须按照key=value的形式为其传值，且必须被传值
def username(age,name=None,sex='male',*args,school,**kwargs): #
    print(age,name,sex,school)
    print(locals())  # 查看局部作用域名字
    pass

username(18,name='NB',sex='female',school='XB') # 实参 可以是常量、变量、表达式的任意组合


# 名称空间
# 内建名称空间
print(max) # <built-in function max>

# 全局名称空间
# 伴随python文件的开始执行/执行完毕而产生/回收，是第二个被加载的名称空间

# 局部名称空间
# 伴随函数的调用/结束而临时产生/回收，函数的形参、函数内定义的名字都会被存放于该名称空间中

# 名称空间的加载顺序是：内置名称空间->全局名称空间->局部名称空间，
# 而查找一个名字，必须从三个名称空间之一找到，查找顺序为：局部名称空间->全局名称空间->内置名称空间。

# 作用域
# 全局作用域:位于全局名称空间、内建名称空间中的名字属于全局范围，
# 该范围内的名字全局存活（除非被删除，否则在整个文件执行过程中存活）、全局有效（在任意位置都可以使用）

# 局部作用域:位于局部名称空间中的名字属于局部范围。该范围内的名字临时存活
# （即在函数调用时临时生成，函数调用结束后就释放）、局部有效（只能在函数内使用）

# 查找优先级
# 在局部作用域查找名字时，起始位置是局部作用域，所以先查找局部名称空间，没有找到，再去全局作用域查找：
# 先查找全局名称空间，没有找到，再查找内置名称空间，最后都没有找到就会抛出异常

# 提示：可以调用内建函数locals()和globals()来分别查看局部作用域和全局作用域的名字
# ，查看的结果都是字典格式。在全局作用域查看到的locals()的结果等于globals()
print(globals()) # 全局作用域名字

# 嵌套函数中查找的优先级
# 在内嵌的函数内查找名字时，会优先查找自己局部作用域的名字，
# 然后由内而外一层层查找外部嵌套函数定义的作用域，没有找到，则查找全局作用域

# 若要在函数内修改全局名称空间中名字的值，当值为不可变类型时，则需要用到global关键字
x=1
def foo1():
    global x #声明x为全局名称空间的名字
    x=2
foo1()
print(x) #结果为2

# 当实参的值为可变类型时，函数体内对该值的修改将直接反应到原值，
num_list=[1,2,3]
def foo2(nums):
    nums.append(5)

foo2(num_list)
print(num_list)
#结果为 [1, 2, 3, 5]

# 对于嵌套多层的函数，使用nonlocal关键字可以将名字声明为来自外部嵌套函数定义的作用域（非全局）
# nonlocal x会从当前函数的外层函数开始一层层去查找名字x，若是一直到最外层函数都找不到，则会抛出异常。
def  foo3():
    ax=2
    def fo4():
        nonlocal ax
        ax=3
    fo4() #调用fo4(),修改foo3作用域中名字ax的值
    print(ax) #在foo3作用域查看ax

foo3() #结果 3