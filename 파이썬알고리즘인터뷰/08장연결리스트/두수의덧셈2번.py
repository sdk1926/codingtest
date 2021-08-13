
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import *
# 내가 한 풀이 연결리스트로 변환을 못해서 실패 
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list1 = []
        list2 = []
        while l1 and l2:
            list1.append(str(l1.val))
            l1 = l1.next
            list2.append(str(l2.val))
            l2 = l2.next
        list1.reverse()
        list2.reverse()
        list1 = int(''.join(list1))
        list2 = int(''.join(list2))
        list3 = list(str(list1 + list2))
        list3.reverse()
        list3 = list(int(i) for i in list3) 
        return list3

# 상길선생님의 풀이 
class Solution:
    # 연결리스트 뒤집기 
    def reverseList(self, head: ListNode) -> ListNode:
        node, prev = head, None

        while node:
            next, node.next = node.next, prev 
            prev, node = node, next
        
        return prev 
    
    # 연결리스트를 파이썬 리스트로 변환
    def toList(self, node: ListNode) -> List:
        list: List = []
        while node:
            list.append(node.val)
            node = node.next
        return list 

    # 파이썬 리스트를 연결 리스트로 변환 
    def toReversedLinkedList(self, result:str) -> ListNode:
        prev: ListNode = None
        for r in result:
            node = ListNode(r)
            node.next = prev
            prev = node
        return node 

    # 두 연결 리스트의 덧셈
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a = self.toList(self.reverseList(l1))
        b = self.toList(self.reverseList(l2))

        resultStr = int(''.join(str(e) for e in a)) + \
                    int(''.join(str(e) for e in b))
        
        # 최종 계산 결과 연결 리스트 변환 
        return self.toReversedLinkedList(str(resultStr))

# 전가산기 풀이 자릿수 올림 
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = head = ListNode(0)

        carry = 0 #자릴수 올림수 
        while l1 or l2 or carry: # l1 or l2 or carry 셋 중 하나라도 안비었으면 계속 ㄱ 
            sum = 0
            # 두 입력값의 합 계산 
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2: 
                sum = l2.val
                l2 = l2.next
            
            # 몫(자리올림수)과 나머지(값) 계산
            carry, val = divmod(sum + carry, 10)
            head.next = ListNode(val)
            head = head.next
    
        return root.next

