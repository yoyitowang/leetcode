#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#

# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # TC: O(n*target)
        # SC: O(n*target)
        n = len(nums)
        cap = sum(nums)
        if cap % 2:
            return False
        cap //= 2

        # recursive
        # @cache
        # def dfs(i, c):
        #     if i < 0:
        #         return True if c == 0 else False
        #     if nums[i] > c:
        #         return dfs(i-1, c)
        #     return dfs(i-1, c) or dfs(i-1, c-nums[i])

        # return dfs(n-1, cap)

        # TC: O(n*cap)
        # SC: O(n*cap)
        # dp array
        dp = [[False for _ in range(cap+1)] for _ in range(n+1)]
        # init
        dp[0][0] = True
        for i, num in enumerate(nums):
            for c in range(cap+1):
                if num > c:
                    dp[i+1][c] = dp[i][c]
                else:
                    dp[i+1][c] = dp[i][c] or dp[i][c-num]
        return dp[n][cap]

# @lc code=end

