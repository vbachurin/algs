class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        mul = 0
        res = 0
        import math
        for elem in s[ : :-1]:
            res += (ord(elem) - 64) * math.pow(26, mul)
            mul += 1
        return res

# Input: "A"
# Output: 1
# Input: "AB"
# Output: 28
# Input: "ZY"
# Output: 701
# Input: "AAA"
# Output: 703

s = Solution()
res = s.titleToNumber("AB")
print(res)