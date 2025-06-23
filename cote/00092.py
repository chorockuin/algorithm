from common import *


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        i = 1
        while head:
            head = head.next
            i += 1
            print(i)
        return head

print_listnode(Solution().reverseBetween(to_listnode([1,2,3,4,5]), 2, 4))