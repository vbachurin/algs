class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        elif len(nums) <= 2:
            return max(nums)
        else:
            a = [0] * len(nums)
            a[0] = nums[0]
            a[1] = max(nums[0], nums[1])
            for i in range(2, len(nums), 1):
                c = a[i-2] + nums[i]
                a[i] = c if c > a[i-1] else a[i-1]
            return a[-1]

s = Solution()
nums = [2,7,9,13,10,2]
res = s.rob(nums)
print(res)