# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_node = l1
        l2_node = l2
        head = ListNode(0)
        node = head

        while l1_node or l2_node:
            if not l1_node:
                node.next = l2_node
                break
            if not l2_node:
                node.next = l1_node
                break
            if l1_node.val < l2_node.val:
                node.next = ListNode(l1_node.val)
                node = node.next
                l1_node = l1_node.next
            elif l1_node.val == l2_node.val:
                node.next = ListNode(l1_node.val)
                node.next.next = ListNode(l2_node.val)
                node = node.next.next
                l1_node = l1_node.next
                l2_node = l2_node.next
            else:
                node.next = ListNode(l2_node.val)
                node = node.next
                l2_node = l2_node.next
        head = head.next
        return head

def print_node(ln: ListNode):
    while ln:
        print(ln.val)
        ln = ln.next

l1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
l2 = ListNode(1, ListNode(5, ListNode(9)))
print_node(Solution().mergeTwoLists(l1, l2))

