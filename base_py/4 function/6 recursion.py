#__author__ = 'Winston'
#date: 2020/4/1

# 递归函数
# 函数的递归调用指的是在调用一个函数的过程中又直接或间接地调用该函数本身
# 可以使用sys.getrecursionlimit()去查看递归深度，默认值为1000，虽然可以使用
# sys.setrecursionlimit()去设定该值，但仍受限于主机操作系统栈大小的限制
import sys
print(sys.getrecursionlimit())

# 请谨慎使用递归 一定要有结束条件，否则会报错

# 面向过程总结：
# 面向过程“核心是“过程”二字，“过程”指的是解决问题的步骤，即先干什么再干什么......，
# 基于面向过程开发程序就好比在设计一条流水线，是一种机械式的思维方式，
# 这正好契合计算机的运行原理：任何程序的执行最终都需要转换成cpu的指令流水按过程调度执行，
# 即无论采用什么语言、无论依据何种编程范式设计出的程序，最终的执行都是过程式的。

# 将复杂的问题流程化，进而简单化
# 扩展性差


# 函数式编程总结：
# 函数式编程并非用函数编程这么简单，而是将计算机的运算视为数学意义上的运算，
# 比起面向过程，函数式更加注重的是执行结果而非执行的过程，
# 代表语言有：Haskell、Erlang。而python并不是一门函数式编程语言，
# 但是仍为我们提供了很多函数式编程好的特性

# 内置函数
# 查看内置函数
import builtins
#print(dir(builtins)) # 针对导入的其他模块，也可以使用dir()查看所有函数
# dir() 不带参数时返回当前范围内的变量，方法和定义的类型列表，带参数时返回参数的属性，方法列表
# ['ArithmeticError', 'AssertionError', 'AttributeError',
#  'BaseException', 'BlockingIOError', 'BrokenPipeError',
#  'BufferError', 'BytesWarning', 'ChildProcessError',
#  'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError',
#  'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EnvironmentError',
#  'Exception', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning',
# 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError',
#  'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError',
#  'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented',
# 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError',
# 'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError',
# 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError',
#  'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError',
# 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError',
#  'Warning', 'WindowsError', 'ZeroDivisionError', '__build_class__', '__debug__', '__doc__', '__import__',
# '__loader__', '__name__', '__package__', '__spec__', 'abs', 'all', 'any', 'ascii', 'bin', 'bool',
#  'breakpoint', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright',
#  'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float',
#  'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int',
#  'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview',
#  'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr',
# 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple',
# 'type', 'vars', 'zip']

# 查看某函数的具体用法 help
#print(help(zip))

# 常使用内置函数
# lambda
b=lambda x : x+x
#print(b(1))
# max min sum 都支持迭代器协议
salaries={
	'siry':3000,
	'tom':7000,
	'lili':10000,
	'jack':2000
}
max(salaries,key=lambda k:salaries[k])
min(salaries,key=lambda k:salaries[k])
sum(salaries.values())

# 排序 sorted
sort_name=sorted(salaries,key=lambda k:salaries[k],reverse=False)
print(sort_name)


# bool()布尔函数
# bytes()  将一个字符串转化为字节类型
# str() 将字符类型/数值类型等转换为字符串类型
# complex() 复数
# divmod()　　分别取商和余数.二个参数x和y，输出元组（x//y,x%y）
# enumerate()　　返回一个可以枚举的对象，该对象的next()方法将返回一个元组
# complie()　　将字符串编译成python能识别或可以执行的代码，也可以将文字读成字符串再编译
# eval()　　将字符串str中的表达式提取出来并运行
# exec()　　执行字符串或complie方法编译过的字符串，没有返回值

#exec：三个参数
#参数一：包含一系列python代码的字符串
#参数二：全局作用域（字典形式），如果不指定，默认为globals()
#参数三：局部作用域（字典形式），如果不指定，默认为locals()
#可以把exec命令的执行当成是一个函数的执行，会将执行期间产生的名字存放于局部名称空间中
g={
    'x':1,
    'y':2
}
l={}

exec('''
global x,z
x=100
z=200

m=300
''',g,l)

print(g) #{'x': 100, 'y': 2,'z':200,......}
print(l) #{'m': 300}


# format()　　格式化输出字符串，format(value, format_spec)实质上是调用了value的__format__(format_spec)方法
# getattr(object, name [, defalut])　　获取对象的属性
# hasattr(object，name) 判断对象object是否包含名为name的特性
# hash()　　哈希值
# hex()   十进制转化为十六进制
# oct()   十进制转化为八进制
# bin()   转化为二进制
# id()  查看唯一标识的身份
# input()  获取用户输入内容
# isinstance()　　检查对象是否是类的对象，返回True或False
# issubclass()　　检查一个类是否是另一个类的子类。返回True或False
# iter() 把可迭代对象转化为一个迭代器
# map()       映射，第一个参数为函数，第二个参数为可迭代对象
array=[1,2,3,4,5]
res1=map(lambda x:pow(x,2),array)
print(list(res1))
# round() 四舍五入
# pow()　　幂函数
#  reduce()         合并，第一个参数为函数，第二个参数为可迭代对象。第三个参数可有可无，默认初始值
from functools import reduce
res2=reduce(lambda x,y:x+y,array)

# filter()　　过滤器，构造一个序列，等价于[ item for item in iterables if function(item)]，
# 在函数中设定过滤条件，逐一循环迭代器中的元素，将返回值为True时的元素留下，形成一个filter类型数据
res3=filter(lambda x:x>3,array)
print(list(res3))
# slice  切片