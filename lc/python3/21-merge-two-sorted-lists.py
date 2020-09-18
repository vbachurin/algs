# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if (not l1):
            return l2
        elif (not l2):
            return l1
        elif (l1.val < l2.val):
            res = ListNode(l1.val)
            res.next = self.mergeTwoLists(l1.next, l2) if (l1.next) else l2
            return res
        else:
            res = ListNode(l2.val)
            res.next = self.mergeTwoLists(l1, l2.next) if (l2.next) else l1
            return res

l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)
l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

s = Solution()
res = s.mergeTwoLists(l1, l2)


while (res.next):
    print(res.val)
    res = res.next
print(res.val)
