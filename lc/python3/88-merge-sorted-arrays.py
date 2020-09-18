class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:

        # def merge0(i: int, m: int, n: int):
        #     print(nums1)
        #     print(f"nums1[{m}] {nums1[m]}, nums2[{n}] {nums2[n]}")
        #     if (m < 0 and n < 0): return
        #     elif (m < 0): merge0(i-1, -1, n-1)
        #     elif (n < 0): merge0(i-1, m-1, -1)
        #     elif (nums1[m] > nums2[n]):
        #         nums1[i] = nums1[m]
        #         merge0(i-1, m-1, n)
        #     elif (nums1[m] <= nums2[n]):
        #         nums1[i] = nums2[n]
        #         merge0(i-1, m, n-1)


        # if (not nums2): return
        # merge0(m+n-1, m-1, n-1)
        # print(nums1)
        mm = m - 1
        nn = n - 1
        if (not nums2): return
        for i in range(n+m-1, -1, -1): 
            print(f"nums1[{mm}] {nums1[mm]}, nums2[{nn}] {nums2[nn]}")
            if (mm < 0 and nn < 0): return
            elif (mm < 0): 
                nums1[i] = nums2[nn]
                nn -= 1
            elif (nn < 0): 
                nums1[i] = nums1[mm]
                mm -= 1
            elif (nums1[mm] > nums2[nn]):
                nums1[i] = nums1[mm]
                mm -= 1
            elif (nums1[mm] <= nums2[nn]):
                nums1[i] = nums2[nn]
                nn -= 1 
            print(nums1)

        
s = Solution()
nums1 = [1]
m = 1
nums2 = []
n = 0
# nums1 = [2, 0]
# m = 1
# nums2 = [1]
# n = 1

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
s.merge(nums1, m, nums2, n)
print(nums1)

        
    # def swap(this, j: int, k: int):
    #     temp = nums1[j]
    #     nums1[j] = nums1[k]
    #     nums1[k] = temp