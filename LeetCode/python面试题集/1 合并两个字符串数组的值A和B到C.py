#__author__ = 'Winston'
#date: 2020/4/12
a = ['a,1',
     'b,3,22',
     'c,3,4',
     'e,9',
     ]

b = [
    'a,2',
    'b,1',
    'd,2',
    'e,10',
]
# 将a,b合并为c这种形式
# c = [
#     'a,1,2',
#     'b,3,22,1',
#     'c,3,4',
#     'd,2'
# ]

def add_lists(a,b):
    dict1={}; dict2={};list1=[]
    len_a = len(a);len_b = len(b)

    for i in range(max(len_a,len_b)):
        if i<len_a:
            dict1[a[i][0]]= a[i][1:].strip(',')
        if i<len_b:
            dict2[b[i][0]] = b[i][1:].strip(',')

    for k,v in dict2.items():
        if k in dict1.keys():
            dict1[k] += ','+v
        else:
            dict1[k] = v

    for k,v in dict1.items():
        list1.append(k+','+v)
    return list1

print(add_lists(a,b))