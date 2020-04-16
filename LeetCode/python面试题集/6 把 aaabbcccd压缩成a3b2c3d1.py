#__author__ = 'Winston'
#date: 2020/4/13

s='aaabbcccd'
#方法一：Counter计数
from collections import Counter
s1=''.join([i+str(j) for i,j in Counter(s).items()])
print(s1)

print(Counter(s).items())


#方法二：集合去重
print(''.join({i+str(s.count(i)) for i in s}))