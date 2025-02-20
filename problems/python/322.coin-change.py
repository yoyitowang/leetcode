#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # TC: O(n*capacity)
        # SC: O(n*capacity)
        
        # def unbounded_knapsack(capacity: int, w: List[int], v: List[int]) -> int:
        #     n = len(w)
        #     @cache
        #     def dfs(i, c):
        #         if i < 0:
        #             return 0 if c == 0 else inf
        #         # weight > capacity: not able to pick this item
        #         if w[i] > c:
        #             return dfs(i-1, c)

        #         return min(dfs(i-1, c), dfs(i, c-w[i])+v[i])
            
        #     return dfs(n-1, capacity)
        
        # ans = unbounded_knapsack(amount, coins, [1]*len(coins))
        # return ans if ans < inf else -1

        # dp
        # TC: O(n*amount)
        # SC: O(n*amount)
        
        n = len(coins)
        f = [[inf] * (amount+1) for _ in range(n+1)]
        f[0][0] = 0

        for i, coin in enumerate(coins):
            for j in range(amount+1):
                if coin > j:
                    f[i+1][j] = f[i][j]
                else:
                    f[i+1][j] = min(f[i][j], f[i+1][j-coin]+1)
        
        ans = f[-1][-1]
        return ans if ans < inf else -1
   
# @lc code=end

