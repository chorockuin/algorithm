import collections

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return False

        n = head
        bn = ListNode(n.val, None)
        while n:
            if n.next:
                bn = ListNode(n.next.val, bn)
            n = n.next

        n = head
        while n:
            if n.val != bn.val:
                return False

            n = n.next
            bn = bn.next
        return True

#head = ListNode(1, ListNode(2))
head = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
print(Solution().isPalindrome(head))
