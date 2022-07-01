# TODO:总结一下前序递归和后序递归的不同写法

# Definition of the linked list
class ListNode:
    def __init__(self, val , next):
        self.val = val
        self.next = next


class Solution:
    def reverseLinkedList(self, head):
        # 双指针法（迭代完成）
        # prev = None
        # curr = head
        # while curr:
        #     next = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = next
        # return prev

        # 递归写法:递归三要素（1.基本结束条件；2.调用自身；3.规模缩小）
        # def reverse(pre, cur):
        #     if not cur:
        #         return pre
        #     next = cur.next
        #     cur.next = pre
        #     return reverse(cur, next)
        # return reverse(None, head)
        
        # 前序遍历的递归写法
        # def dfs(pre, head):
        #     if not head:
        #         return pre
        #     next = head.next  # 主逻辑在前
        #     head.next = pre
        #     return dfs(head, next)
        # return dfs(None, head)
        
        # 后续遍历的递归写法
        def dfs(head):
            if not head or not head.next:
                return head
            res = dfs(head.next)
            head.next.next = head
            head.next = None
            return res
        return dfs(head)
            
        
        
        
