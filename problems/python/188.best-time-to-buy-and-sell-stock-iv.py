#
# @lc app=leetcode id=188 lang=python3
#
# [188] Best Time to Buy and Sell Stock IV
#

# @lc code=start
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # TC: O(n*k)
        # SC: O(n*k)
        n = len(prices)
        f = [[0] * (2*k+1) for _ in range(n+1)]
        
        for i in range(1, 2*k+1):
            if i % 2 == 1:
                f[0][i] = -prices[0]
            else:
                f[0][i] = 0
        
        for i in range(1, n+1):
            price = prices[i-1]
            for j in range(1, 2*k+1):
                # f[1][1] = max(f[0][1], f[0][0]-price)
                if j % 2 == 1:
                    f[i][j] = max(f[i-1][j], f[i-1][j-1]-price)
                # f[1][2] = max(f[0][2], f[0][1]+price)
                else:
                    f[i][j] = max(f[i-1][j], f[i-1][j-1]+price)
        return f[-1][-1]
# @lc code=end

