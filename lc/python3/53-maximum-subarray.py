class Solution:
    def maxSubArray(self, nums) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        maxx = dp[0]

        for i in range(1, len(nums)):
            dp[i] = nums[i] + (dp[i-1] if (dp[i-1] > 0) else 0)
            maxx = max(maxx, dp[i])

        return max
a = [-2,1,-3,4,-1,2,1,-5,4]
res = Solution().maxSubArray(a)
print(res)