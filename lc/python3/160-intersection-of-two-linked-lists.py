# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        aSum = 0
        _headA = headA
        while _headA:
            aSum += _headA.val
            _headA = _headA.next
        bSum = 0
        _headB = headB
        while _headB:
            bSum += _headB.val
            _headB = _headB.next

        def recur(headA, aSum, headB, bSum):
            # print(f"aSum {aSum} headA {headA.val}, bSum {bSum} headB {headB.val}")
            if not headA or not headB:
                return None
            if aSum > bSum:
                return recur(headA.next, aSum - headA.val, headB, bSum)
            elif aSum < bSum:
                return recur(headA, aSum, headB.next, bSum - headB.val)
            elif aSum == bSum:
                print(f"remainders equal, {headA.val} == {headB.val} => {headA == headB}")
                if headA == headB:
                    return headA 
                elif headA.val == 0:
                    return recur(headA.next, aSum - headA.val, headB, bSum)
                elif headB.val == 0:
                    return recur(headA, aSum, headB.next, bSum - headB.val)
                else:
                    return recur(headA.next, aSum - headA.val, headB.next, bSum - headB.val)
            else:
                return None

        return recur(headA, aSum, headB, bSum)

s = Solution()
# listA = [4,1,8,4,5], listB = [5,0,1,8,4,5]
# headA = ListNode(4)
# headA.next = ListNode(1)
# intersect = ListNode(8)
# headA.next.next = intersect
# headB = ListNode(5)
# headB.next = ListNode(0)
# headB.next.next = ListNode(1)
# headB.next.next.next = intersect
# intersect.next = ListNode(4)
# intersect.next.next = ListNode(5)
# listA = [0,9,1,2,4], listB = [3,2,4]
headA = ListNode(0)
headA.next = ListNode(9)
headA.next.next = ListNode(1)
intersect = ListNode(2)
# headA.next.next.next = intersect
headA.next.next.next = ListNode(2)
headB = ListNode(5)
headB.next = ListNode(3)
headB.next.next = intersect
intersect.next = ListNode(4)
res = s.getIntersectionNode(headA, headB)
print(res.val if res else None)