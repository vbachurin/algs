# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        met = set()
        while(head):
            if head in met:
                return True
            else:
                met.add(head)
            head = head.next
        return False

        
s = Solution()
# Input: head = [3,2,0,-4], pos = 1
head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(0)
head.next.next.next = ListNode(-4)
# head.next.next.next.next = head.next
res = s.hasCycle(head)
print(res)