# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from math import pow

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode):
        return self._addTwoNumbers(l1, l2, 0)

    def _addTwoNumbers(self, l1: ListNode, l2: ListNode, spill):
        if not l1 and not l2:
            return spill
        else:
            summed = (l1.val if l1 else 0) + (l2.val if l2 else 0) + (spill.val if spill else 0)
            res = ListNode(summed) if summed < 10 else ListNode(summed - 10)
            res.next = self._addTwoNumbers(l1.next if l1 else None, l2.next if l2 else None, ListNode(1) if summed >= 10 else None)
            return res


# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

s = Solution()
l1 = ListNode(1)
# l1.next = ListNode(8)
# l1.next.next = ListNode(3)
# l2 = None
l2 = ListNode(9)
l2.next = ListNode(9)
# l2.next.next = ListNode(4)
res = s.addTwoNumbers(l1, l2)
while res:
    print(res.val)
    res = res.next