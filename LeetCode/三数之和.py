#__author__ = 'Winston'
#date: 2020/2/22


def threeSum(nums):
    n = len(nums)
    if not nums or n < 3:
        return []
    nums.sort()
    res = []
    for i in range(n):
        if nums[i] > 0:
            return res
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        L = i + 1  # 令左指针 L=i+1L=i+1
        R = n - 1  # 令右指针 R=n-1R=n−1
        while L < R: # 当 L<R 时，执行循环
            if nums[i] + nums[L] + nums[R] == 0:  # 判断左界和右界是否和下一位置重复，去除重复解。并同时将 L,R 移到下一位置，寻找新的解
                res.append([nums[i], nums[L], nums[R]])
                while L < R and nums[L] == nums[L + 1]:
                    L = L + 1
                while L < R and nums[R] == nums[R - 1]:
                    R = R - 1
                L = L + 1
                R = R - 1
            elif nums[i] + nums[L] + nums[R] > 0: # 若和大于0,说明nums[R]太大,R左移
                R = R - 1
            else:         #若和小于 0，说明 nums[L]太小，L 右移
                L = L + 1
    return res














if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    nums=threeSum(nums)
    print(nums)

