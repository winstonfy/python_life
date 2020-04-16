#__author__ = 'Winston'
#date: 2020/2/22





def isValid(s):
    dic = {'{': '}',  '[': ']', '(': ')', '?': '?'}
    stack = ['?']
    for c in s:
        if c in dic: stack.append(c)
        elif dic[stack.pop()] != c: return False
    return len(stack) == 1



aa=isValid('([)]')
print(aa)