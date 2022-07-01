'''
在进行数学推导时，区间的长度定义需要遵循一个原则才不至于混乱。这里假设采用左开右闭原则。
'''
# Definition for singly-linked list
from email.quoprimime import header_decode


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def detectCycle(self, head):
        # slow = fast = head
        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next
        #     if slow == fast:
        #         p = head
        #         q = slow
        #         while p != q:
        #             p = p.next
        #             q = q.next
        #         return p
        # return None
        
        slow, fast = head, head
        while True:
            if not fast or not fast.next:
                return None
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                break
        fast = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return fast
                
        
        