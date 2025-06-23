from common import *

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        odd = head
        prev_even = None
        head_even = None
        while odd:
            if odd.next:
                even = odd.next
                if prev_even:
                    prev_even.next = even
                else:
                    head_even = even
                prev_even = even
                odd.next = even.next
                even.next = None
                if odd.next:
                    odd = odd.next
                else:
                    odd.next = head_even
                    break
            else:
                odd.next = head_even
                break
        return head


print_listnode(Solution().oddEvenList(to_listnode([2,1,3,5,6,4,7])))