# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if (head == None or head.next == None): return head
        slow = head
        el = head.next
        while (el != None):
            print(f"el: {el.val}, slow: {slow.val}")
            if (el.val != slow.val):
                slow.next = el
                slow = el
            el = el.next
        slow.next = None
        return head

s = Solution()
l = ListNode(1)
l.next = ListNode(3)
l.next.next = ListNode(3)
l.next.next.next = ListNode(3)
l.next.next.next.next = ListNode(3)
l.next.next.next.next.next = ListNode(4)
res = s.deleteDuplicates(l)
print("Result:")
while (res != None):
    print(res.val)
    res = res.next