#
# @lc app=leetcode id=474 lang=python3
#
# [474] Ones and Zeroes
#

# @lc code=start
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # TC: O(len(strs)*m*n)
        # SC: O(m*n)
        count = [(s.count('0'), s.count('1')) for s in strs]
        size = len(strs)

        dp = [[0] * (n+1) for _ in range(m+1)]
        for zero, one in count:        
            for i in range(m, zero-1, -1):
                for j in range(n, one-1, -1):
                    dp[i][j] = max(dp[i][j], dp[i-zero][j-one] + 1)
        
        return dp[m][n]
# @lc code=end

