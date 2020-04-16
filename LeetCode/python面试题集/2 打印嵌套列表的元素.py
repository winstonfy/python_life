#__author__ = 'Winston'
#date: 2020/4/12

A=[1,2,[3,4,["434",[1,2,[23,24]]]]]

def list_ele(A):
    for i in A:
        if isinstance(i,list):
            return list_ele(i)
        else:
            print(i)

list_ele(A)