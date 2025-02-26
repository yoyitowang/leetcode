#
# @lc app=leetcode id=309 lang=python3
#
# [309] Best Time to Buy and Sell Stock with Cooldown
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        # i-th buy: i-1 can't buy
        # i-th not buy: 
        @cache
        def dfs(i, hold):
            if i < 0:
                return -inf if hold else 0
            if hold:
                return max(dfs(i-1, True), dfs(i-2, False)-prices[i])
            return max(dfs(i-1, False), dfs(i-1, True)+prices[i])
        
        return dfs(n-1, False)    
# @lc code=end

