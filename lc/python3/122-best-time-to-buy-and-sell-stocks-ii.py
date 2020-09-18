class Solution:
    def maxProfit(self, prices) -> int:
        if len(prices) < 2: return 0
        else:
            profit = 0
            minPrice = prices[0]
            for i in range(1, len(prices)):
                if prices[i] <= prices[i-1]:
                    profit += prices[i-1] - minPrice
                    minPrice = prices[i]
                print(f"prices[i] = {prices[i]}, profit = {profit}, minPrice = {minPrice}")
            return profit + max(prices[i] - minPrice, 0)

# hold as long as the price grows
# drop when price stops growing

# Example 1:

# Input: [7,1,5,3,6,4]
# Output: 7
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
#              Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
# Example 2:

# Input: [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
#              Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
#              engaging multiple transactions at the same time. You must sell before buying again.
# Example 3:

# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.


s = Solution()
# prices = [1,2,3,4,5]
prices = [7,1,4,4,9,5]
# prices = [7,6,4,3,1]
# prices = [7,1,5,3,6,4]
res = s.maxProfit(prices)
print(res)