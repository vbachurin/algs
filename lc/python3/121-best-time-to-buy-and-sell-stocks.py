class Solution:
    def maxProfit(self, prices) -> int:
        # if not prices: return 0
        maxx = 0
        minPrice = prices[0]

        for i in range(1, len(prices)):
            minPrice = min(prices[i-1], minPrice)
            maxx = max(maxx, prices[i] - minPrice)
        return maxx


# Example 1:

# Input: [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
#              Not 7-1 = 6, as selling price needs to be larger than buying price.
# Example 2:

# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.


s = Solution()
prices = [7,1,5,3,6,4]
res = s.maxProfit(prices)
print(res)