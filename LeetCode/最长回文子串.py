#__author__ = 'Winston'
#date: 2020/2/20

class Solution:
    def longestPalindrome(self,s):
        if len(s) <= 1:
            return s

        # 每个字符之间插入 #
        ss = '$#' + '#'.join([x for x in s]) + '#`'
        p = [1] * len(ss)  # R[]的初始化
        center = 0
        mx = 0  # mx 则为 center + R[center]，也就是这个子串的右边界
        max_str = ''
        for i in range(1, len(p)-1):

            if i < mx:
                j = 2 * center - i # i 关于 center 的对称点
                p[i] = min(p[j],mx-i)

            # 尝试继续向两边扩展，更新 p[i]
            while ss[i - p[i] ] == ss[i + p[i] ]: # 不必判断是否溢出，因为首位均有特殊字符，肯定会退出
                p[i] += 1

            # 更新中心
            if i + p[i] - 1 > mx:
                mx = i + p[i] - 1
                center = i

            # 更新最长串
            if 2 * p[i]-1 > len(max_str):
                max_str = ss[i - p[i]+1 : i + p[i]]

        return max_str.replace('#', '')




if __name__ == '__main__':
    ss = [1]*22
    print(ss)