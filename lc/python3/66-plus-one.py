class Solution:
    def plusOne(self, digits):
        res = self._plusOne(digits, len(digits) - 1)
        return res

    def _plusOne(self, digits, r):
        if (digits[r] == 9):
            digits[r] = 0
            self._plusOne(digits, r - 1)
        else:
            if (r >= 0):
                digits[r] += 1
            else:
                digits.insert(0, 1)
        return digits

s = Solution()
r = s.plusOne([2])
# r = s.plusOne([9, 9, 9])
print(r)
