class Solution:
    def fourSum(self, nums, target: int): # -> List[List[int]]:
        nums.sort()    
        result = set([])
        l = 0
        r = len(nums) - 1
        i = 1
        j = len(nums) - 2
        while (l < r):
            l += 1
            r -= 1        
        return [[]]

s = Solution()
nums = [1, 0, -1, 0, -2, 2]
target = 0
res = s.fourSum(nums, target)
print(res)
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]