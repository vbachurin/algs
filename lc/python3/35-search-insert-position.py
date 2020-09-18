class Solution:
    def searchInsert(self, nums, target: int) -> int:
        if (not nums):
            return 0
        l = 0
        r = len(nums)
        while (r - l > 1):
            mid = (l + r) // 2 
            print(f"l = {l}, r = {r}, mid = {mid}, nums[mid] = {nums[mid]}")
            if (nums[mid] <= target):
                l = mid
            else:
                r = mid
        if (nums[l] >= target):
            return l
        else: 
            return r

a = [1,3,5,6]
b = 7
# b = 5
res = Solution().searchInsert(a, b)
print(res)