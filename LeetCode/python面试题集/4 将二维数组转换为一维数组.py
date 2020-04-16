#__author__ = 'Winston'
#date: 2020/4/12

lst=[[1,2,3],[4,5,6],[7,8,9]]

# 方法一
print(sum(lst,[]))

# 方法二
print([i for j in lst for i in j])

# 方法三
import operator
from functools import reduce

print(reduce(operator.add, lst))

# 方法四
from itertools import chain
print(list(chain.from_iterable(lst)))