#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        # recursive
        # TC: O(n)
        # SC: O(n)
        # steal or not
        # dfs(i) = max(dfs(i-2)+nums[i], dfs(i-1))
        n = len(nums)        

        @cache
        def dfs(n):
            if n < 0:
                return 0
                
            return max(dfs(n-2) + nums[n], dfs(n-1))
        
        return dfs(n-1) 
    
        # TC: O(n)
        # SC: O(n)
        n = len(nums)
        dp = [0] * (n+2)
        for i in range(n):
            dp[i+2] = max(dp[i+1], dp[i]+nums[i])
        return dp[n+1]
# @lc code=end

