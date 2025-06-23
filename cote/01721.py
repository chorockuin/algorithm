# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def get_nodes_size(self, head):
        size = 0
        while head != None:
            size += 1
            head = head.next
        return size
    
    def swapNodes(self, head, k):
        size = self.get_nodes_size(head)
        half_size = size/2
        if size%2 == 1:
            half_size += 1
        if k > half_size:
            k = size - k + 1
            
        t = head
        i = 1
        c = 1
        source_n = None
        target_n = None
        while t != None:
            if k == i:
                source_n = t
                target_n = t
                c = -1
            t = t.next
            if i <= 0:
                target_n = target_n.next
            i += c

        p = source_n.val
        source_n.val = target_n.val
        target_n.val = p
        return head
        
h = ListNode(1)
t = h
for i in range(2, 10**5+1):
    n = ListNode(i%101)
    t.next = n
    t = n
    
Solution().swapNodes(h, 2)
