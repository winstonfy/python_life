#__author__ = 'Winston'
#date: 2020/4/1

# 函数对象
# 函数对象指的是函数可以被当做’数据’来处理，具体可以分为四个方面的使用
# 函数可以被引用
def add_x(x):
    return x*x
add_fun = add_x
add_fun(2)
# 函数可以作为容器类型的元素
dic = {'add_x':add_fun,'n':12}
nf=dic['add_x'](dic['n'])
# 函数可以作为参数传入另外一个函数
def sun_x(func,n):
    na = func(n)
    print(na)
sun_x(dic['add_x'],13)
# 函数的返回值可以是一个函数
def fun_x():
    return add_x
fun_a=fun_x()(3)


# 闭包函数
# 基于函数对象的概念，可以将函数返回到任意位置去调用，
# 但作用域的关系是在定义完函数时就已经被确定了的，与函数的调用位置无关。
xax=1
def ff1():
    def ff2():
        print(xax) # 1

    return ff2

def ff3():
    xax=3
    ff2=ff1() #调用f1()返回函数f2
    ff2() #需要按照函数定义时的作用关系去执行，与调用位置无关

ff3() #结果为1

# 基于函数对象的概念，可以将函数返回到任意位置去调用，
# 但作用域的关系是在定义完函数时就已经被确定了的，与函数的调用位置无关。

# 函数被当做数据处理时，始终以自带的作用域为准。若内嵌函数包含对外部函数作用域
# （而非全局作用域）中变量的引用，那么该’内嵌函数’就是闭包函数

# 闭包的用途
import requests
def page(url):
    def get():
        return requests.get(url).text
    return get