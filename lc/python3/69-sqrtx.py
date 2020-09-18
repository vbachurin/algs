class Solution:
    def mySqrt(self, x: int) -> int:
        return self.binSearch(x) if x > 0 else 0

    def binSearch(self, target: int):
        l = 1
        r = target
        while (r - l > 1):
            mid = (l + r) // 2
            print(f"l = {l}, r = {r}, mid = {mid}")
            if (mid * mid == target):
                return mid
            elif (mid * mid > target):
                r = mid
            else:
                l = mid
        return l


s = Solution()
res = s.mySqrt(4)
print(res)