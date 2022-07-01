# TODO:双链表的实现！

class ListNode:
    def __init__(self, val, next):
        self.val = val
        self.next = next

class MyLinkedList:
    def __init__(self):
        self._head = ListNode(0)  # 虚拟头部节点
        self._count = 0  # 添加的节点数
    
    def get(self, index):
        '''
        Get the value of the index-th node in the linked list. If the index is invalid, return -1
        '''
        if 0 <= index < self._count:
            node = self._head
            for _ in range(index+1):
                node = node.next
            return node.val
        else:
            return -1
        
    def addAtHead(self, val):
        '''
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        '''
        self.addAtIndex(0, val)
        
    def addAtTail(self, val):
        '''
        Append a node of value val to the last element of the linked list.
        '''
        self.addAtIndex(self._count, val)
        
    def addAtIndex(self, index, val):
        '''
        Add a node of value val before the index-th node in the liinked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted. 
        '''
        if index < 0:
            index = 0
        elif index > self._count:
            return
        
        # 计数累加
        self._count += 1
        
        add_node = ListNode(val)
        prev_node, current_node = None, self._head
        for _ in range(index + 1):  # TODO:为什么是index + 1?
            prev_node, current_node = current_node, current_node.next
        else:
            prev_node.next, add_node.next = add_node, current_node  # NOTE:在for循环完整完成后才执行else；如果中途从break跳出，则连else一起跳出。
    
    def deleteAtIndex(self, index):
        '''
        Delete the index-th node in the linked list, if the index is valid.
        '''
        if 0 <= index < self._count:
            # 计数-1
            self._count -= 1
            prev_node, current_node = None, self._head
            for _ in range(index + 1):
                prev_node, current_node = current_node, current_node.next
            else:
                prev_node.next, current_node.next = current_node.next, None
                
        
        
    
        
    
    