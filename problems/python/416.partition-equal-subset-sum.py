#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#

# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        cap = sum(nums)
        if cap % 2:
            return False
        cap //= 2
        
        @cache
        def dfs(i, c):
            if i < 0:
                return True if c == 0 else False
            if nums[i] > c:
                return dfs(i-1, c)
            return dfs(i-1, c) or dfs(i-1, c-nums[i])

        return dfs(n-1, cap)   
# @lc code=end

