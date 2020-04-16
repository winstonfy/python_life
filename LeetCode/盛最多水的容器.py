#__author__ = 'Winston'
#date: 2020/2/22

def maxArea(height):
    left_h = 0
    right_h = -1
    sc = len(height)-1
    max_s= 0
    while sc != 0:
        if height[left_h] > height[right_h]:
            area = sc * height[right_h]
            right_h -= 1
        else:
            area = sc * height[left_h]
            left_h += 1
        sc -= 1
        max_s=max(area,max_s)
    return max_s









if __name__ == '__main__':
    list3=[2,3,4,5,18,17,6]
    list2=[1,1]
    list1 = [1,8,6,2,5,4,8,3,7]
    aa=maxArea(list2)
    print(aa)