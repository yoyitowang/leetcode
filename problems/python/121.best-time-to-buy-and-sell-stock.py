#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # TC: O(n)
        # SC: O(1)
        min_p = float('inf')
        profit = 0
        for price in prices:
            min_p = min(min_p, price)
            profit = max(profit, price-min_p)
        return profit

        # dp 
        # buy / not buy
        f0 = -prices[0]
        f1 = 0
        for i in range(1, len(prices)):
            f0 = max(f0, -prices[i])
            f1 = max(f0+prices[i], f1)

        return f1   
# @lc code=end

