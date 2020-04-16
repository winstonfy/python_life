#__author__ = 'Winston'
#date: 2020/2/21

def reversex(x):
    chars = list(str(x))  # 将输入数字转换成为字符串列表
    if x < 0:
        chars.remove('-')  # 去除负号
        chars.reverse()  # 逆序
        r = ''.join(chars)  # 合并成字符串
        r = - int(r)  # 返回结果
    else:
        chars.reverse()  # 逆序
        r = ''.join(chars)  # 合并成字符串
        r = int(r)  # 返回结果

    if not -pow(2, 31) <= r <= pow(2, 31) - 1:
        r = 0

    return r


# res = 0
# news = abs(x)
# while news != 0:
#     temp = news % 10
#     res = res * 10 + temp
#     news = news // 10
# if x < 0:
#     if -res >= -2 ** 31:
#         return -res
#     else:
#         return 0
# else:
#     if res <= 2 ** 31 - 1:
#         return res
#     else:
#         return 0







if __name__ == '__main__':
    x = -12345450
    a = reversex(x)
    print(a)