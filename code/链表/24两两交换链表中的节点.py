# Definition of the linked list
class ListNode:
    def __init__(self, val=0 , next=None):
        self.val = val
        self.next = next

def exchangeNode(head):
    if not head or not head.next:
        return head
    
    dummy_node = ListNode(next=head)
    pre = dummy_node
    while pre.next and pre.next.next:
        curr = pre.next
        post = pre.next.next
        curr.next = post.next
        post.next = curr
        pre.next = post

        pre = pre.next.next
    return dummy_node.next

def swapPairs(head):
    dummyNode = ListNode(next=head)
    pre = dummyNode
    
    # 必须有pre的下一个和下下个才能交换，否则说明已经交换结束了
    while pre.next and pre.next.next:
        cur = pre.next
        post = pre.next.next
        
        # pre,cur,post对应最左，中间的，最右边的节点
        cur.next = post.next
        post.next = cur
        pre.next = post
        
        pre = pre.next.next  # TODO:画两幅图就可以看出里面的逻辑了！
        
    return dummyNode.next
    
    