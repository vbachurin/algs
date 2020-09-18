class Solution:
    def isPalindrome(self, x: int) -> bool:
        digits = [n for n in str(x)]
        i = 0
        j = len(digits) - 1
        while (i < j):
            if (digits[i] != digits[j]):
                return False
            else:
                i+=1
                j-=1
        return True

s = Solution()
print(s.isPalindrome(101))