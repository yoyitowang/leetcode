#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        # TC: O(n*1)
        # SC: O(1)
        if n <= 2:
            return n
        dp = [0, 1, 2]
        for i in range(3, n+1):
            dp[0], dp[1], dp[2] = dp[1], dp[2], dp[1]+dp[2]
        
        return dp[2]  
# @lc code=end

