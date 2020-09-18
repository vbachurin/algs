class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # import math
        # f = math.factorial(n)
        # def isPossible(x):
        #     res = f % (10 ** x)
        #     print(f"{f} % {10 ** x} == 0 is {res == 0}")
        #     return res == 0

        # l = 0
        # r = n
        # while r - l > 1:
        #     mid = (l + r) // 2
        #     print(f"({l} + {r}) // 2 = {mid}")
        #     if isPossible(mid):
        #         l = mid
        #     else:
        #         r = mid
        # return l
        print(int(n))
        return 0 if n == 0 else n // 5 + self.trailingZeroes(n // 5)

s = Solution()
res = s.trailingZeroes(8836)
print(res)