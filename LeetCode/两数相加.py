#__author__ = 'Winston'
#date: 2020/2/20


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None



class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        prenode = ListNode(0)
        lastnode = prenode
        val = 0
        while l1 or l2 or val:
            val,cur = divmod(val+(l1.val if l1 else 0)+(l2.val if l2 else 0),10)
            lastnode.next = ListNode(cur)
            lastnode = lastnode.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return prenode.next


    #     return self.add_two(l1, l2)
    #
    # def add_two(self,l1,l2,add_value=0):
    #     if not l1  and not l2  and add_value==0:
    #         return None
    #
    #     l1_value = l1.val if l1 else 0
    #     l2_value = l2.val if l2 else 0
    #
    #     node_val = l1_value + l2_value + add_value
    #
    #     l1_next = l1.next if l1 else None
    #     l2_next = l2.next if l2 else None
    #
    #     if node_val >= 10:
    #         result_node = ListNode(node_val - 10)
    #         result_node.next = self.add_two(l1_next, l2_next, 1)
    #
    #     else:
    #         result_node = ListNode(node_val)
    #         result_node.next = self.add_two(l1_next, l2_next)
    #
    #
    #     return result_node
    #     prenode = ListNode(0)
    #     lastnode = prenode
    #     val = 0
    #     while val or l1 or l2:
    #         val, cur = divmod(val + (l1.val if l1 else 0) + (l2.val if l2 else 0), 10)
    #         lastnode.next = ListNode(cur)
    #         lastnode = lastnode.next
    #         l1 = l1.next if l1 else None
    #         l2 = l2.next if l2 else None
    #     return prenode.next



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
    l1 = generateList([4, 5, 8])
    l2 = generateList([9, 1, 2, 9])
    printList(l1)
    printList(l2)
    s = Solution()
    sum1 = s.addTwoNumbers(l1, l2)
    printList(sum1)


# return self.add_two(l1, l2)
#
#     def add_two(self, l1, l2, add_value=0):
#         if not l1 and not l2 and add_value == 0:
#             return None
#
#         l1_value = l1.val if l1 else 0
#         l2_value = l2.val if l2 else 0
#         node_val = l1_value + l2_value + add_value
#
#         l1_next = l1.next if l1 else None
#         l2_next = l2.next if l2 else None
#
#         if node_val >= 10:
#             result_node = ListNode(node_val - 10)
#             result_node.next = self.add_two(l1_next, l2_next, 1)
#         else:
#             result_node = ListNode(node_val)
#             result_node.next = self.add_two(l1_next, l2_next)
#
#         return result_node
#
# class Solution:
#     def addTwoNumbers(self,l1,l2):
#         prenode = ListNode(0)
#         lastnode = prenode
#         val = 0
#         while val or l1 or l2:
#             val, cur = divmod(val + (l1.val if l1 else 0) + (l2.val if l2 else 0), 10)
#             lastnode.next = ListNode(cur)
#             lastnode = lastnode.next
#             l1 = l1.next if l1 else None
#             l2 = l2.next if l2 else None
#         return prenode.next





#
# class Solution(object):
# 	def addTwoNumbers(self, l1, l2):
# 		# 定义一个进位标志
# 		a,b,p,carry = l1,l2,None,0
# 		while a or b:
# 			# a和b节点的值相加，如果有进位还要加上进位的值
# 			val = (a.val if a else 0)+(b.val if b else 0)+carry
# 			# 根据val判断是否有进位,不管有没有进位，val都应该小于10
# 			carry,val = val/10 if val>=10 else 0,val%10
# 			p,p.val = a if a else b,val
# 			# a和b指针都前进一位
# 			a,b = a.next if a else None,b.next if b else None
# 			# 根据a和b是否为空，p指针也前进一位
# 			p.next = a if a else b
# 		# 不要忘记最后的边界条件，如果循环结束carry>0说明有进位需要处理这个条件
# 		if carry:
# 			p.next = ListNode(carry)
# 		# 每次迭代实际上都是将val赋给a指针的，所以最后返回的是l1
# 		return l1
#
#
# class Solution:
#     def addTwoNumbers(self,l1,l2):
#         n = l1.val + l2.val
#         l3 = ListNode(n % 10)
#         l3.next = ListNode(n // 10)
#         p1 = l1.next
#         p2 = l2.next
#         p3 = l3
#         while True:
#             if p1 and p2:
#                 sum = p1.val + p2.val + p3.next.val
#                 p3.next.val = sum % 10
#                 p3.next.next = ListNode(sum // 10)
#                 p1 = p1.next
#                 p2 = p2.next
#                 p3 = p3.next
#             elif p1 and not p2:
#                 sum = p1.val + p3.next.val
#                 p3.next.val = sum % 10
#                 p3.next.next = ListNode(sum // 10)
#                 p1 = p1.next
#                 p3 = p3.next
#             elif not p1 and p2:
#                 sum = p2.val + p3.next.val
#                 p3.next.val = sum % 10
#                 p3.next.next = ListNode(sum // 10)
#                 p2 = p2.next
#                 p3 = p3.next
#             else:
#                 if p3.next.val == 0:
#                     p3.next = None
#                 break
