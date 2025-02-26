#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # TC: O(n)
        # SC: O(1)
        profit = 0
        for i in range(1, len(prices)):
            profit += max(0, prices[i]-prices[i-1])

        return profit
    
        # dp solution
        # TC: O(n)
        # SC: O(1)
        # hold/not hold
        f0 = -prices[0]
        f1 = 0
        for i in range(1, len(prices)):
            f0 = max(f0, f1-prices[i])
            f1 = max(f0+prices[i], f1)
        return max(f0, f1)
    
        # dfs
        # TC: O(n)
        # SC: O(n)
        @cache
        def dfs(i, hold):
            if i < 0:
                return -inf if hold else 0
            if hold:
                return max(dfs(i-1, True), dfs(i-1, False)-prices[i])
            
            return max(dfs(i-1, False), dfs(i-1, True)+prices[i])

        n = len(prices)
        return dfs(n-1, False)
# @lc code=end

