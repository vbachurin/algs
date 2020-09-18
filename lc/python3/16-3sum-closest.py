class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        if len(nums) < 3: return
        nums.sort()
        result = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
          l, r = i + 1, len(nums) - 1
          while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s == target:
                return s
            if abs(s - target) < abs(result - target):
                result = s
            if s < target:
                l += 1
            elif s > target:
                r -= 1
        return result


s = Solution()
nums = [3,0,-2,-1,1,2]
# nums = [-1, 2, 1, -4]
# nums = [1, 1, 1, 0]
target = 100
# target = 1
res = s.threeSumClosest(nums, target)
print(res)