#
# @lc app=leetcode id=509 lang=python3
#
# [509] Fibonacci Number
#

# @lc code=start
class Solution:
    def fib(self, n: int) -> int:
        dp = [0, 1]
        if n <= 1:
            return dp[n]
        for i in range(2, n+1):
            dp[0], dp[1] = dp[1], dp[0]+dp[1]
        return dp[1]    
# @lc code=end

