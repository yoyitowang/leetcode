#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0, 1, 2]
        if n < 3:
            return n
        for i in range(2, n):
            dp[0], dp[1] = dp[1], dp[2]
            dp[2] = dp[1] + dp[0]
        return dp[2]     
# @lc code=end

