#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # TC: O(mxn)
        # SC: O(mxn)
        dp = [[0 for _ in range(n)] for _ in range(m)]

        # init
        dp[0][0] = 1

        for i in range(m):
            for j in range(n):
                if i > 0:
                    dp[i][j] += dp[i-1][j]
                if j > 0:
                    dp[i][j] += dp[i][j-1]
        return dp[-1][-1]
# @lc code=end

