class Solution(object):
    def majorityElement(self, nums):

        def majorityElementRec(lo, hi):

            if lo == hi: return nums[lo]

            mid = (hi-lo)//2 + lo
            left = majorityElementRec(lo, mid)
            right = majorityElementRec(mid + 1, hi)

            if left == right: return left

            left_count = sum(1 for i in range(lo, hi + 1) if nums[i] == left)
            right_count = sum(1 for i in range(lo, hi + 1) if nums[i] == right)

            return left if left_count > right_count else right

        return majorityElementRec(0, len(nums) - 1)

s = Solution()
nums = [22,11,11,0,22,2,0,10]
res = s.majorityElement(nums)
print(res)