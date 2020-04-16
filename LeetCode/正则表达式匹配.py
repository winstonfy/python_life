#__author__ = 'Winston'
#date: 2020/2/21
#
# from collections import deque
# class Solution:
# 	def isMatch(self,s,p):
#         legt_s=len(s)
#         s+=" " #需要配合\U0001f6a9处一起看
#         _p_=deque() #先把要匹配的东西集中处理一下8 省得之后会比较麻烦
#         cnt=len(p)-1 #从尾巴开始的好处是匹配x(x表示任意一个非*的符号)*比较方便
#         while cnt>=0:
#             t=p[cnt]
#             if t=="*":
#                 cnt-=1
#                 t=p[cnt]+t
#             _p_.appendleft(t) #因为要头插所以_p_用的是deque 用list也可以 直接insert(0,t)
#             cnt-=1
#         alter=[-1] #_p_[:i]的内容可以匹配的所有s的从头开始的子串的尾索引
#         #一开始啥都没有匹配但为了_p_[0]能和_p_[x](x!=1)们统一处理 所以初始化为[-1]
#         for i in _p_: #外层循环是每一个需要匹配的字符
#             if not alter: #如果已经没有什么能匹配的了 直接就是false
#                 return False
#             elif alter[-1]==legt_s:
#                 alter.pop() #\U0001f6a9
#             #主要就是有些时候i还没到头就能匹配完整个s了 一般来说直接try:alter.remove(legt_s-1) except:pass就可以了
#             #但是这个问题中有着x(x为任意不为*的单个合法字符)*这种可以什么都不匹配的情况 所以前面说的这种情况有保留的价值
#             #但是留着就可能出现访问s的某个元素时出现index出界的问题 所以我在s的最后添加了一个字符" " 同时又删掉了alter
#             #中可能存在的legt_s这个索引 这样子就比较简洁的达成了我的目的
#             new=[]
#             if i==".*": #处理掉第一种特殊情况 这种是全能的匹配所以直接就如下操作了
#                 new=list(range(alter.pop(0),legt_s) if alter else []) #因为".*"也可以啥都不匹配 所以start_index是alter.pop(0)
#             elif i==".": #处理掉第二种特殊情况
#                 #new=[i+1 for i in alter if i+1<legt_s]
#                 new=[i+1 for i in alter] #因为s尾巴加了一个字符同时每轮都把可能出现的legt_s删了 所以有潜在的出界可能
#             elif i[-1]=="*": #处理第三种特殊情况
#                 visited,sign=set(),i[0] #visited其实就是暂时收集可能的尾index 最后有一个sorted()处理 为了避免重复 所以用set
#                 for j in alter:
#                     visited.add(j) #".*"的注意点 这种可以一个字符都不匹配 所以这句不能少
#                     j+=1
#                     while j<legt_s and s[j]==sign: #贪婪添加
#                         visited.add(j)
#                         j+=1
#                 new=sorted(visited) #排序主要是因为上面有一个alter.pop()这是要取最小的index <- 当然min()也行 但通常还是升序习惯了
#             else: #最普通的情况
#                 new=[j+1 for j in alter if s[j+1]==i] #和第二种情况一样的 不可能出界
#             alter=new
# return legt_s-1 in alter

memo = dict()  # 备忘录


# def dp(i, j):
#     if (i, j) in memo: return memo[(i, j)]
#     if j == len(pattern): return i == len(text)
#
#     first = i < len(text) and pattern[j] in {text[i], '.'}
#
#     if j <= len(pattern) - 2 and pattern[j + 1] == '*':
#         ans = dp(i, j + 2) or \
#               first and dp(i + 1, j)
#     else:
#         ans = first and dp(i + 1, j + 1)
#
#     memo[(i, j)] = ans
#     return ans
# #
#
# return dp(0, 0)
#
# return re.match(p + '$', s)