class Solution:
    def removeElement(self, nums, val: int) -> int:
        if (len(nums) == 1 and nums[0] == val) or len(nums) == 0:
            return 0
        delta = 0
        cnt = 0
        for i in range(len(nums)):
            print(nums) 
            if (nums[i] == val):
                delta += 1
            else:
                nums[delta] = nums[i]
                cnt += 1
            print(f"nums[{i}] = {nums[i]}, delta = {delta}, cnt = {cnt}")
            print("========")
        return cnt       

s = Solution()
a = [0,1,2,2,3,0,4,2]
# a = [3, 2, 2, 3]
# a = [0,4,4,0,4,4,4,0,2]
# a = [0,4,4,4,0]
# print(a)
res = s.removeElement(a, 2)
print(a[:res])

