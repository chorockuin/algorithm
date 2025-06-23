# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head.next == None:
            return head

        r_head = ListNode(head.val)
        head = head.next
        temp = None
        while head != None:
            temp = head
            head = head.next
            temp.next = r_head
            r_head = temp
        return temp


n = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
rn = Solution().reverseList(n)

while rn != None:
    print(rn.val)
    rn = rn.next