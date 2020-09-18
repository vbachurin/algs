class Solution:
    def rotate(self, nums, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        nums[:] = nums[n-k:] + nums[:n-k]


# Input: [1,2,3,4,5,6,7] and k = 3
# Output: [5,6,7,1,2,3,4]           
        

s = Solution()
nums = [1,2,3,4,5,6,7]
s.rotate(nums, 3)
print(nums)