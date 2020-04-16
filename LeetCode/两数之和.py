#__author__ = 'Winston'
#date: 2020/2/19
list_a = [1,0,1,1,4,3,9,3,15]
# 暴力循环 超时
# def two_sum(list_a,num):
#     for i in range(0,len(list_a)):
#         for j in range(i+1,len(list_a)):
#             if list_a[i]+list_a[j] == num:
#                 return [i,j]
# a=two_sum(list_a,0)
# print(a)

## 字典求值
# def two_sum(list_b,num):
#     dict_a = {}
#     for index in range(0,len(list_b)):
#         w = num-list_b[index]
#         if dict_a.get(w) is not None:
#             j =dict_a.get(w)
#             return [j,index]
#         else:
#             dict_a[list_b[index]] = index


# dict_a = {}
#         for index,value in enumerate(nums):
#             w = target-value
#             if dict_a.get(w) is not None:
#                 j =dict_a.get(w)
#                 return [j,index]
#             else:
#                 dict_a[value] = index
# def two_sum(nums, target):
#     dict1 = {}
#     for i in range(0, len(nums)):
#         num = target - nums[i]
#
#         if num not in dict1:
#             dict1[nums[i]] = i
#         #如果在字典中则返回
#         return [dict1[num], i]

# def two_sum(nums, target):
#     dict1 = {}
#     for i, num in enumerate(nums):
#         if dict1.get(target - num) is not None:
#             return [dict1.get(target - num),i]
#         dict1[num] = i
def two_sum(nums, target):
    dict1= {}
    for i,j in enumerate(nums):
        if j in dict1:
            return [dict1.get(j),i]
        dict1[target - j] = i

# class Solution:
#     def twoSum(self,nums,target):
#         dicts = {}
#         for index, value in enumerate(nums):
#             temp = target - value
#             if temp in dicts:
#                 return [dicts[temp], index]
#             else:
#                 dicts[value] = index

a=two_sum(list_a,15)
print(a)