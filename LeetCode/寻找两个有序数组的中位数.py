#__author__ = 'Winston'
#date: 2020/2/20
s1 = [2]
s2 = [1,3]


def sss(s1,s2):
    s1.extend(s2)
    s1.sort()
    half = len(s1) // 2
    return (s1[half] + s1[~half]) / 2

print(sss(s1,s2))