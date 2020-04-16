#__author__ = 'Winston'
#date: 2020/4/12

lst = [1,2,4,8,16,32,64,128,256,512,1024,32769,65536,4294967296]

# {
#     1:[1,2,3,8],
#     2:[16,32,64],
#     3:[128,256,512],
#     4:[1024,],
#     5:[32769,65536],
#     6:[4294967296]
# }

def lis_dic(lst):
    dic = {}
    for i in lst:
        key=len(str(i))
        if dic.get(key):
            dic[key] += ','+str(i)
        else:
            dic[key] = str(i)
    for k,v in dic.items():
        dic[k] = list(map(int,v.split(',')))
    return dic
print(lis_dic(lst))