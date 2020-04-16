#__author__ = 'Winston'
#date: 2020/4/1

# 开放封闭原则
# 一个软件实体如类、模块和函数应该对扩展开放，对修改关闭。即软件实体应尽量在不修改原有代码的情况下进行扩展。

# 装饰器
# 软件包含的所有功能的源代码以及调用方式，都应该避免修改，否则一旦改错，则极有可能产生连锁反应，
# 最终导致程序崩溃，而对于上线后的软件，新需求或者变化又层出不穷，我们必须为程序提供扩展的可能性，这就用到了装饰器。

# 不修改被装饰对象源代码和调用方式的前提下为被装饰对象添加额外的功能
# 插入日志、性能测试、事务处理、缓存、权限校验等应用场景

# 添加统计index函数的执行时间功能
import time

def index():
    time.sleep(3)
    print('Welcome to the index page')
    return 200

def tag(func):
    def wrapper(*args,**kwargs):
        print('开始执行')
        res=func(*args,**kwargs)
        print('结束执行')
        return res
    return wrapper

def timer(func):
    def wrapper(*args,**kwargs):
        start_time=time.time()
        res=func(*args,**kwargs)
        stop_time=time.time()
        print('run time is %s' %(stop_time-start_time))
        return res
    return wrapper


# 第一种调用方式
#index=timer(index)
#index()

# 第二种调用方式
@tag # index = tag(timer(index))
@timer
def index():
    time.sleep(3)
    print('Welcome to the index page')
    return 200

print(help(index))

# 分别统计两个函数的执行时间
import time

def timer(parameter):

    def outer_wrapper(func):

        def wrapper(*args, **kwargs):
            if parameter == 'task1':
                start = time.time()
                func(*args, **kwargs)
                stop = time.time()
                print("the task1 run time is :", stop - start)
            elif parameter == 'task2':
                start = time.time()
                func(*args, **kwargs)
                stop = time.time()
                print("the task2 run time is :", stop - start)

        return wrapper

    return outer_wrapper

@timer(parameter='task1')
def task1():
    time.sleep(2)
    print("in the task1")

@timer(parameter='task2')
def task2():
    time.sleep(2)
    print("in the task2")

task1()
task2()


# 实现保留原函数属性，functools模块下提供一个装饰器wraps专门用来帮我们实现这件事
from functools import wraps
# 使用 @wraps(func)

from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        start_time=time.time()
        res=func(*args,**kwargs)
        stop_time=time.time()
        print('run time is %s' %(stop_time-start_time))
        return res
    return wrapper