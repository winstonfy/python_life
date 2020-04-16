#__author__ = 'Winston'
#date: 2020/2/21

str1 = "---123"
import re
def myAtoi(str):
    # charsx = ''
    # flag = 1
    # str = str.lstrip(' ')
    # if str.startswith('-'):
    #     flag = 0
    # if str.startswith('+'):
    #     flag = 1
    # if str.startswith('-+') or str.startswith('++') or str.startswith('--') or str.startswith('+-'):
    #     return 0
    # for line in str.lstrip('-').lstrip('+'):
    #     if line.isdigit():
    #         charsx = charsx+line
    #     else:
    #         break
    # if charsx == '':
    #     return 0
    # if flag == 1:
    #     res = int(charsx)
    # else:
    #     res = -int(charsx)
    # if res < 0:
    #     if res  >= -2 ** 31:
    #         return res
    #     else:
    #         return -2 ** 31
    # else:
    #     if res <= 2 ** 31 - 1:
    #         return res
    #     else:
    #         return 2 ** 31 - 1

    return res if -2147483648 < res < 2147483647 else 0

    return max(min(int(*re.findall('^[\+\-]?\d+', str.lstrip())), 2**31 - 1), -2**31)

aa = myAtoi(str1)
print(aa)