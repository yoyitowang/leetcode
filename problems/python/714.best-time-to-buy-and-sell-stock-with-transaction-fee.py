#
# @lc app=leetcode id=714 lang=python3
#
# [714] Best Time to Buy and Sell Stock with Transaction Fee
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # TC: O(n*2)
        # SC: O(n*2)
        n = len(prices)

        f = [[0] * 2 for _ in range(n)]
        # hold
        f[0][0] = -(prices[0])

        for i in range(1, n):
            price = prices[i]
            f[i][0] = max(f[i-1][0], f[i-1][1]-price)
            f[i][1] = max(f[i-1][1], f[i-1][0]+price-fee)

        return f[-1][-1]

# @lc code=end

