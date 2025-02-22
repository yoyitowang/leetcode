#
# @lc app=leetcode id=518 lang=python3
#
# [518] Coin Change II
#

# @lc code=start
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # TC: O(n*amount)
        # SC: O(amount)
        
        # @cache
        # def dfs(i, c):
        #     if i < 0:
        #         return 1 if c == 0 else 0
        #     if coins[i] > c:
        #         return dfs(i-1, c)
        #     return dfs(i-1, c) + dfs(i, c-coins[i])
        # n = len(coins)
        # return dfs(n-1, amount)


        # TC: O(n*amount)
        # SC: O(amount)
        n = len(coins)

        f = [0] * (amount+1)
        f[0] = 1

        for coin in coins:
            for j in range(coin, amount+1):
                f[j] += f[j-coin]
        return f[amount]
# @lc code=end

