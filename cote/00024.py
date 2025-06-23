# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # temp = head
        # prev = None
        # while True:
        #     if not temp:
        #         break
        #
        #     if temp.next:
        #         jump = temp.next.next
        #         a = temp
        #         b = temp.next
        #         b.next = a
        #         a.next = jump
        #         temp = jump
        #
        #         if prev:
        #             prev.next = b
        #
        #         if a == head:
        #             head = b
        #
        #         prev = a
        #     else:
        #         break
        # return head
        if head:
            if head.next:
                j = head.next
                head.next = self.swapPairs(j.next)
                j.next = head
                return j
            else:
                return head
        else:
            return None


def print_listnode(list_node: ListNode):
    while list_node:
        print(list_node.val)
        list_node = list_node.next

def to_listnode(l: list) -> ListNode:
    if len(l) == 0:
        return None

    head = ListNode(l[0])
    temp = head
    for i in range(1, len(l)):
        node = ListNode(l[i])
        temp.next = node
        temp = node
    return head

l = [1,2,3,4]
# l = [1]
print_listnode(Solution().swapPairs(to_listnode(l)))