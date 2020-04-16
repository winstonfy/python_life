# import time
# #
# #
# # def deco_limit(s):
# #
# #     def wrpper(func):
# #         name = func.__name__
# #         func_identify ={name: 0, 'second': s}
# #         def inner(*args, **kwargs):
# #             useable_time = func_identify[name] + func_identify['second']
# #             time_now = time.time()
# #             remain_time = useable_time-time_now
# #             if time_now > useable_time:
# #                 func_identify[name] = time_now #设置调用时间
# #                 res = func(*args,**kwargs)
# #             else:
# #                 print('\033[32;1mFunction \033[31;1m{0} \033[0m'\
# #                       .format(name)+'\033[32;1mcan be used after {0:.2f} seconds later\033[0m'\
# #                       .format(remain_time))
# #                 res = None
# #             return res
# #         return inner
# #     return wrpper
# #
# #
# #
# #
# # #以下为被装饰函数foo1
# # @deco_limit(5)     #在这儿参数为设置调用间隔时间
# # def foo1(*args, **kwargs):
# #     print('执行foo1--everything is ok')
# #
# #
# # print(list(filter(lambda x:x%2==0,range(101))))
# #
# # print([i for i in range(0,101,2)])

str1 = '10.3.9.12'
list2 =[]
list1=str1.split('.')
for i in list1:
    list2.append(bin(int(i,10))[2:])
print(list2)