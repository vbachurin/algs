class Solution:
    def maxArea(self, height) -> int:

        def area(i, j):
            a = min(height[i], height[j]) * (j - i)
            print(f"{i} {j} => {a}")
            return a

        print(height)

        i = I = 0
        j = J = len(height) - 1
        marea = area(i, j)

        while (I < J):
            # MOVE THE INDEX POINTING TO THE SHORTER LINE
            if height[I] > height[i]:
                marea = max(area(I, j), marea)
                i = I
            elif height[J] > height[j]:
                marea = max(area(i, J), marea)
                j = J
            else:
                if height[I] < height[J]:
                    I += 1
                else:
                    J -= 1
        return marea
        # while (i < j and I < J):
        #     # MOVE THE INDEX POINTING TO THE SHORTER LINE
        #     if height[I] > height[i]:
        #         marea = max(area(I, j), marea)
        #         i = I
        #     else:
        #         I += 1
        #     if height[J] > height[j]:
        #         marea = max(area(i, J), marea)
        #         j = J
        #     else:
        #         J -= 1
        # return marea



# Input: [1,8,6,2,5,4,8,3,7]
# Output: 49
        
s = Solution()
height = [1,8,6,2,5,4,8,3,7]
# height = [1,1]
# height = [1,1,10,0,11,1,1,1]
# height = [2,3,4,5,18,17,6] # expected 17
res = s.maxArea(height)
print(res)