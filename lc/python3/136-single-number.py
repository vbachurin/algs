class Solution:
    def singleNumber(self, nums) -> int:
        met = set()
        for num in nums:
            if num in met: met.remove(num)
            else: met.add(num)
        return met.pop()

s = Solution()
nums = [5,2,1,1,2,3,4,4,5]
# nums = [4,1,2,1,2]
res = s.singleNumber(nums)
print(res)