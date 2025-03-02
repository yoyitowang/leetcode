#
# @lc app=leetcode id=115 lang=python3
#
# [115] Distinct Subsequences
#

# @lc code=start
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # # TC: O(n1*n2)
        # # SC: O(n1*n2)
        # n1, n2 = len(t), len(s)

        # @cache
        # def dfs(i, j):
        #     if i < 0:
        #         return 1
        #     if j < 0:
        #         return 0
        #     if t[i] == s[j]:
        #         return dfs(i-1, j-1) + dfs(i, j-1)
        #     return dfs(i, j-1)
        
        # return dfs(n1-1, n2-1)
    
        # 2-dim DP
        # TC: O(n1*n2)
        # SC: O(n1*n2)
        n1, n2 = len(t), len(s)
        f = [[0] * (n2+1) for _ in range(n1+1)]
        for j in range(n2+1):
            f[0][j] = 1
        
        for i, x in enumerate(t):
            for j, y in enumerate(s):
                if x == y:
                    f[i+1][j+1] = f[i][j] + f[i+1][j]
                else:
                    f[i+1][j+1] = f[i+1][j]

        return f[n1][n2]

# @lc code=end

