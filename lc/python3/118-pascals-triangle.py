class Solution:
    def generate(self, numRows: int): # -> List[List[int]]:
        dp = [[1], [1, 1]]
        for i in range(2, numRows):
            xs = [1] * (i + 1)
            for j in range(1, len(xs) // 2 + 1):
                xs[j] = xs[len(xs) - j - 1] = dp[i-1][j-1] + dp[i-1][j]
            dp.append(xs)
        return dp[:numRows]

# Input: 5
# Output:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]

s = Solution()
res = s.generate(10)
for i in range(len(res)):
    print(res[i])      