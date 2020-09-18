class Solution:
    def removeDuplicates(self, nums) -> int:
        if (len(nums) <= 1):
            return len(nums)
        prev = nums[0]
        dupBeginIndex = 1
        for i in range(1, len(nums)):
            if (nums[i] == prev and nums[dupBeginIndex] > prev):
                dupBeginIndex = i
            elif (nums[i] > prev):
                if (dupBeginIndex != i):
                    # print(f"swap {nums[dupBeginIndex]} and {nums[i]}")
                    nums[dupBeginIndex] = nums[i]
                dupBeginIndex += 1
            # print(nums)
            # print(f"i: {i}, nums[i]: {nums[i]}, dupBeginIndex: {dupBeginIndex}, prev: {prev}")
            prev = nums[i]
        return dupBeginIndex
        
s = Solution()
a = [10,11,20,20,30,40]
# a = [10,10,11,11,11,20,20,30,30,40]
res = s.removeDuplicates(a)
print(res)



            # if (nums[i] != prev):
            #     nums[dupBeginIndex] = nums[i]
            # else:
            #     dupBeginIndex = i
            # print(f"i: {i}, nums[i]: {nums[i]}, dupBeginIndex: {dupBeginIndex}, prev: {prev}")
            # print(nums)
            # prev = nums[i]

    # def removeDuplicates(self, nums) -> int:
    #     size = len(nums)
    #     print(nums)
    #     prev = None
    #     for i in range(size):
    #         if (nums[i] == prev):
    #             j = self.findNextBigger(nums, i)
    #             print(f"j {j}")
    #             temp = nums[j]
    #             nums[j] = nums[i]
    #             nums[i] = temp
    #         print(nums)
    #         prev = nums[i]  
    #     return 0


    # def findNextBigger(self, nums, start) -> int:
    #     print(f"start: {start}")
    #     l = start
    #     r = len(nums) - 1
    #     while (l < r):
    #         mid = (l + r) // 2 
    #         if (nums[mid] > nums[start]):
    #             r = mid 
    #         else:
    #             l = mid + 1
    #         # print(f"l: {l}, r: {r}")
    #     return r

