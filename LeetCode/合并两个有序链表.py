#__author__ = 'Winston'
#date: 2020/2/22

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None



class Solution:
    def mergeTwoLists(self,l1,l2):

        if l1 is None:
            return l2

        if l2 is None:
            return l1

        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2







def generateList(l: list) -> ListNode:
    prenode = ListNode(0)
    lastnode = prenode
    for val in l:
        lastnode.next = ListNode(val)
        lastnode = lastnode.next
    return prenode.next

def printList(l: ListNode):
    while l:
        print("%d, " % (l.val), end='')
        l = l.next
    print('')



if __name__ == "__main__":
    l1 = generateList([1, 2, 3])
    l2 = generateList([1, 3])
    printList(l1)
    printList(l2)
    s = Solution()
    sum1 = s.mergeTwoLists(l1,l2)
    printList(sum1)