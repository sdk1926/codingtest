from typing import *
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def mergeTwoLists(self, l1: ListNode, l2:ListNode) -> ListNode:
    if (not l1) or (l2 and l1.val):
        l1, l2 = l2, l1
    if l1:
        l1.next = self.mergeTwoLists(l1.next,12)
    return l1

# 내풀이 (리스 노를 따 만들어서 실패)
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        list1 = []
        list2 = []
        while l1:
            list1.append(l1.val)
            l1 = l1.next
        while l2:
            list1.append(l2.val)
            l2 = l2.next
        list1 = list1 + list2
        list1.sort()
        prev = None
        node = ListNode()
        while list1:
            node = ListNode(list1.pop())
            node.next = prev
            prev = node
        
        return node
        