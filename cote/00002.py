# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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

def print_listnode(l: ListNode):
    while l:
        print(l.val)
        l = l.next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = None
        temp = None
        add = 0
        while True:
            if l1:
                if l2:
                    sum = l1.val + l2.val + add
                    if sum >= 10:
                        add = 1
                        sum -= 10
                    else:
                        add = 0
                    l1 = l1.next
                    l2 = l2.next

                    if temp:
                        temp.next = ListNode(sum)
                        temp = temp.next
                    else:
                        temp = ListNode(sum)
                        head = temp
                else:
                    sum = l1.val + add
                    if sum >= 10:
                        add = 1
                        sum -= 10
                    else:
                        add = 0
                    l1 = l1.next

                    if temp:
                        temp.next = ListNode(sum)
                        temp = temp.next
                    else:
                        temp = ListNode(sum)
                        head = temp
            else:
                if l2:
                    sum = l2.val + add
                    if sum >= 10:
                        add = 1
                        sum -= 10
                    else:
                        add = 0
                    l2 = l2.next

                    if temp:
                        temp.next = ListNode(sum)
                        temp = temp.next
                    else:
                        temp = ListNode(sum)
                        head = temp
                else:
                    if add > 0:
                        temp.next = ListNode(add)
                    break
        return head

# l1 = [2,4,3]
# l2 = [5,6,4]

# l1 = [0]
# l2 = [0]

l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]

print_listnode(Solution().addTwoNumbers(to_listnode(l1), to_listnode(l2)))