'''
理论分析：
    设第一个公共节点是node，链表A的节点数为a，链表B的节点数为b，两链表公共的部分节点数为c。
    1.指针A先遍历完链表A，再开始遍历链表B，当走到node节点时，走了：a+(b-c)步
    2.指针B先遍历完链表B，再开始遍历链表A，当走到node节点时，走了：b+(a-c)步
    a+(b-c) == b+(a-c)
    
    1.若两链表有公共部分，则同时走到node处。
    2.若两链表没有公共部分，则同时走到null。
'''
# Definition for singly-linked list.
from curses import A_HORIZONTAL


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def getIntersectionNode(self, headA, headB):
        A = headA
        B = headB
        while A != B:
            if A:  # TODO:判断条件到底是if A还是if A.next?
                A = A.next
            else:
                A = headB
            if B:
                B = B.next
            else:
                B = headA
        return A
        
        # A = headA
        # B = headB
        # while A != B:
        #     if A.next:  # TODO:判断条件到底是if A还是if A.next?
        #         A = A.next
        #     else:
        #         A = headB
        #     if B.next:
        #         B = B.next
        #     else:
        #         B = headA
        # return A