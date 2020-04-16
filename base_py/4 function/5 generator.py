#__author__ = 'Winston'
#date: 2020/4/1

# 生成器
# 若函数体包含yield关键字，再调用函数，并不会执行函数体代码，得到的返回值即生成器对象
def my_range(start,stop,step=1):
    print('start...')
    while start < stop:
        yield start
        start+=step
    print('end...')
g = my_range(0,3)
print(type(g)) # <class 'generator'>
# 生成器内置有__iter__和__next__方法，所以生成器本身就是一个迭代器
#print(next(g),next(g),next(g))

# 既然生成器对象属于迭代器，那么必然可以使用for循环迭代
#for i in g:
#    print(i)

# 有了yield关键字，我们就有了一种自定义迭代器的实现方式。yield可以用于返回值，
# 但不同于return，函数一旦遇到return就结束了，而yield可以保存函数的运行状态挂起函数，用来返回多次值
def eater1():
    print('Ready to eat')
    while True:
        food=yield
        print('get the food: %s, and start to eat' %food)

food_x=eater1()
next(food_x) # 需要事先”初始化”一次，让函数挂起在food=yield，等待调用g.send()方法为其传值
food_x.send('包子')
food_x.send('鸡腿')
# 针对表达式形式的yield，生成器对象必须事先被初始化一次，
# 让函数挂起在food=yield的位置，等待调用g.send()方法为函数体传值，food_x.send(None)等同于next(food_x)

# 可以编写装饰器来完成为所有表达式形式yield对应生成器的初始化操作
def init(func):
    def wrapper(*args,**kwargs):
        g=func(*args,**kwargs)
        next(g)
        return g
    return wrapper

@init
def eater2():
    print('Ready to eat')
    while True:
        food=yield
        print('get the food: %s, and start to eat' %food)

# 表达式形式的yield也可以用于返回多次值，即变量名=yield 值的形式，如下
def eater3():
    print('Ready to eat')
    food_list=[]
    while True:
        food=yield food_list
        food_list.append(food)

exx=eater3()
next(exx)
exx.send('蒸羊羔')
exx.send('蒸熊掌')
print(exx.send('蒸鹿尾儿'))


# 三元表达式
# res = 条件成立时返回的值 if 条件 else 条件不成立时返回的值
aax = 12 if (True if True else (False if True else False)) else 15  # aax=12


# 列表生成式
egg_list=['鸡蛋%s' %i for i in range(10)]

# 生成器表达式
# 创建一个生成器对象有两种方式，
# 一种是调用带yield关键字的函数，另一种就是生成器表达式，
# 与列表生成式的语法格式相同，只需要将[]换成()
# 对比列表生成式返回的是一个列表，生成器表达式返回的是一个生成器对象
egg_list_generator=('鸡蛋%s' %i for i in range(10)) # 生成器对象

# 读取一个大文件的字节数，应该基于生成器表达式的方式完成
with open('db.txt','rb') as f:
    print(len(f.read())) # 26

with open('db.txt','rb') as f:
    nums=(len(line) for line in f)
    total_size=sum(nums) # 依次执行next(nums)，然后累加到一起得到结果
    print(total_size) # 26