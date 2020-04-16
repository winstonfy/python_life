#__author__ = 'Winston'
#date: 2020/2/20

def convert(s,numRows):
    if numRows < 2: return s
    res = ["" for _ in range(numRows)] # ['', '', '', '']
    i, flag = 0, -1 # i 行索引  flag方向
    for c in s:
        res[i] += c
        if i == 0 or i == numRows - 1: flag = -flag
        i += flag
    return "".join(res)


if __name__ == '__main__':
    s = 'aaaaaaaaaaaaaaa'
    ss = convert(s, 4)
    print(ss)
