#__author__ = 'Winston'
#date: 2020/2/21

def isPalindrome(x):

    if str(x)==str(x)[::-1]:
        return True
    else:
        return False





if __name__ == '__main__':
    x = 11211
    a =isPalindrome(x)
    print(a)