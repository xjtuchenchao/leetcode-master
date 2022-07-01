# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head, n):
        # 1.方法一：不限制扫描的次数  反转链表 -> 删除第n个节点 -> 反转链表
        # def reverse(head):
        #     pre = None
        #     cur = head
        #     while cur:
        #         next = cur.next
        #         cur.next = pre
        #         pre = cur
        #         cur = next
        #     return pre
        
        # head = reverse(head)
        # dummyNode = ListNode(next=head)
        # pre = dummyNode
        # for i in range(n-1):
        #     pre = pre.next
        # pre.next = pre.next.next
        # head = reverse(dummyNode.next)
        # return head
        
        # 2.方法二：只使用一次扫描
        dummy_node = ListNode(next=head)
        slow = fast = dummy_node
        for i in range(n):
            fast = fast.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy_node.next
            
            
    