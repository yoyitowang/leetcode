#
# @lc app=leetcode id=746 lang=python3
#
# [746] Min Cost Climbing Stairs
#

# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # # TC: O(n)
        # # SC: O(n)
        # n = len(cost)
        # dp = [0] * (n+1)

        # for i in range(2, n+1):
        #     dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])

        # return dp[-1] 

        # dp
        # TC: O(n)
        # SC: O(1)
        n = len(cost)
        f0 = f1 = 0
        for i in range(2, n+1):
            f0, f1 = f1, min(f0 + cost[i-2], f1 + cost[i-1])
        
        return f1
# @lc code=end

