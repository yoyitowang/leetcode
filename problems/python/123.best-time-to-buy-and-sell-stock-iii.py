#
# @lc app=leetcode id=123 lang=python3
#
# [123] Best Time to Buy and Sell Stock III
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # TC: O(n)
        # SC: O(n)
        n = len(prices)
        f = [[0] * 5 for _ in range(n)]
        # 1: hold
        # 2: no hold
        # 3: hold
        # 4: no hold
        f[0][1] = f[0][3] = -prices[0]

        for i in range(1, n):
            f[i][0] = f[i-1][0]
            f[i][1] = max(f[i-1][1], f[i-1][0]-prices[i])
            f[i][2] = max(f[i-1][2], f[i-1][1]+prices[i])
            f[i][3] = max(f[i-1][3], f[i-1][2]-prices[i])
            f[i][4] = max(f[i-1][4], f[i-1][3]+prices[i])

        return f[-1][4]

        # TC: O(n)
        # SC: O(1)
        n = len(prices)
        f = [0] * 5
        # 1: hold
        # 2: no hold
        # 3: hold
        # 4: no hold
        f[1] = f[3] = -prices[0]

        for i in range(1, n):
            f[4] = max(f[4], f[3]+prices[i])
            f[3] = max(f[3], f[2]-prices[i])
            f[2] = max(f[2], f[1]+prices[i])
            f[1] = max(f[1], f[0]-prices[i])
            f[0] = f[0]

        return f[-1]
# @lc code=end

