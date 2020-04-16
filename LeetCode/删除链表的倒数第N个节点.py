#__author__ = 'Winston'
#date: 2020

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None



class Solution:
    def removeNthFromEnd(self,head,n):
        root = ListNode(-1)
        root.next = head
        left = right = root
        while n:
            right = right.next
            n -= 1

        while right.next:
            right = right.next
            left = left.next

        left.next = left.next.next

        return root.next




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
    head = generateList([9, 1, 2, 9])
    printList(head)
    s = Solution()
    sum1 = s.removeNthFromEnd(head,n=2)
    printList(sum1)