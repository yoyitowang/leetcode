#
# @lc app=leetcode id=309 lang=python3
#
# [309] Best Time to Buy and Sell Stock with Cooldown
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        # # i-th buy: i-1 can't buy
        # # i-th not buy: 
        # @cache
        # def dfs(i, hold):
        #     if i < 0:
        #         return -inf if hold else 0
        #     if hold:
        #         return max(dfs(i-1, True), dfs(i-2, False)-prices[i])
        #     return max(dfs(i-1, False), dfs(i-1, True)+prices[i])
        
        # return dfs(n-1, False)
    

        # # TC: O(2n)
        # # SC: O(2n)
        # f = [[0] * 2 for _ in range(n+1)]
        # f[0][1] = -inf

        # for i, p in enumerate(prices):
        #     # not hold
        #     f[i+1][0] = max(f[i][0], f[i][1]+p)
        #     # hold
        #     f[i+1][1] = max(f[i][1], f[i-1][0]-p if i > 0 else -p)
        
        # return f[n][0]
    
        # TC: O(n)
        # SC: O(1)
        n = len(prices)

        # f0: freeze, f1: not hold, f2: hold
        f0 = f1 = 0
        f2 = -inf

        for i, p in enumerate(prices):
            f0, f1, f2 = f1, max(f1, f2+p), max(f2, f0-p)

        return f1
# @lc code=end

