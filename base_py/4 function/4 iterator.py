#__author__ = 'Winston'
#date: 2020/4/1


# 迭代器

# 可迭代对象
# 可迭代对象(Iterable)。
# 从语法形式上讲，内置有__iter__方法的对象都是可迭代对象，
# 字符串、列表、元组、字典、集合、打开的文件都是可迭代对象：
list1 = [1,2,3,4]
aa = iter(list1)  # 返回一个迭代器对象
a=list1.__iter__() # 本质调用__iter__() <list_iterator object at 0x00000000027172B0>

print(aa,next(aa),next(aa),next(aa),next(aa)) # 本质就是在调用i.__next__()
print(a,a.__next__(),a.__next__(),a.__next__(),a.__next__()) # 再往后面就是StopIteration


# for 循环的原理
goods=['mac','lenovo','acer','dell','sony']
i=iter(goods) #每次都需要重新获取一个迭代器对象
while True:
    try:
        print(next(i))
    except StopIteration: #捕捉异常终止循环
        break

goods=['mac','lenovo','acer','dell','sony']
for item in goods:
    print(item)

# for循环在工作时，首先会调用可迭代对象goods内置的__iter__方法拿到一个迭代器对象，
# 然后再调用该迭代器对象的__next__方法将取到的值赋给item,执行循环体完成一次循环，
# 周而复始，直到捕捉StopIteration异常，结束迭代。

# 总结：
# 优点：
# 惰性计算：迭代器对象表示的是一个数据流，可以只在需要时才去调用__next__来计算出一个值，
# 就迭代器本身来说，同一时刻在内存中只有一个值，因而可以存放无限大的数据流，
# 而对于其他容器类型，如列表，需要把所有的元素都存放于内存中，受内存大小的限制，可以存放的值的个数是有限的。
# 缺点：
# 除非取尽，否则无法获取迭代器的长度