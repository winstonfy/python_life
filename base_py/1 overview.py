# __author__ = 'Winston'
# date: 2020/3/31
# 解释型✔ 编译型 静态类型 动态类型定义语言✔ 强类型定义语言✔ 弱类型

# 优点： 简单易学习 开源 高级语言 可移植性 面向对象 可扩展性 丰富的第三方库 规范性强
# 缺点： 运行速度 资料匮乏 架构选择多

# 编码 unicode utf-8

# 关键字
import keyword

k = keyword.kwlist
print(len(k))

"""
False   None    True    and    as   assert
async   await  break    class  continue
def    del    elif    else    except
finally    for    from    global    if
import    in    is    lambda    nonlocal
not    or    pass    raise    return
try    while    with    yield
"""

# 注释

# 格式化输出 %c %s %d %0 %x %f

# 变量

# 算数运算符

# 逻辑运算符

# 数据类型转化

# 判断 if elif else

# 循环 while for   break和continue
#----------------------------------
# 深浅拷贝  copy  copy.deepcopy

#不可变对象的赋值 不会跟着你变
a=1
b=a
a=2
print(b) # 1
#可变对象的赋值  跟着变
al = [1,2]
bl = al
al.append(3)
print(bl) # [1,2,3]

#------------------------------------
import copy
# 浅拷贝：只拷贝顶级的对象，或者说：父级对象

# 深拷贝：拷贝所有对象，顶级对象及其嵌套对象。或者说：父级对象及其子对象

#第一种：如果字典只有顶级对象（没有带嵌套）
d = {'name':'derek','age':'22'}
c1 = copy.copy(d)       #浅拷贝
c2 = copy.deepcopy(d)   #深拷贝

print(id(d),id(c1),id(c2))   #5794912 5794984 31939824   三个不同对象

d['age'] = 25
print(d,c1,c2)
#{'name': 'derek', 'age': 25}
# {'name': 'derek', 'age': '22'}
# {'name': 'derek', 'age': '22'}

#源对象修改值的时候，深浅拷贝的对象值没有改变

#第二种，字典中有嵌套
d = {'name':{'first':'zhang','last':'derek'},
    'job':['IT','HR']}
c1 = copy.copy(d)
c2 = copy.deepcopy(d)
print(id(d),id(c1),id(c2))    #31157416 31940256 35946856

d['job'][0] = 'tester'
print(d,c1,c2)
# {'name': {'first': 'zhang', 'last': 'derek'}, 'job': ['tester', 'HR']}
# {'name': {'first': 'zhang', 'last': 'derek'}, 'job': ['tester', 'HR']}
# {'name': {'first': 'zhang', 'last': 'derek'}, 'job': ['IT', 'HR']}
#源对象修改值的时候，浅拷贝的值跟着改变，深拷贝的值没变

# 总结：
# 深浅拷贝都是对源对象的复制，占用不同的内存空间
# 如果源对象只有一级目录的话，源做任何改动，不影响深浅拷贝对象
# 如果源对象不止一级目录的话，源做任何改动，都要影响浅拷贝，但不影响深拷贝
# 序列对象的切片其实是浅拷贝，即只拷贝顶级的对象
