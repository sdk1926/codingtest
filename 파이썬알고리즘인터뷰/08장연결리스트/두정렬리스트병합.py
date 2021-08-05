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