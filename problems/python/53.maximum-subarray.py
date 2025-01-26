#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # TC: O(n)
        # SC: O(1)
        res = float('-inf')
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            if total > res:
                res = total
            if total < 0:
                total = 0
        return res
    
        # # DP
        # # TC: O(n)
        # # SC: O(n)
        # dp = [0] * len(nums)
        # dp[0] = nums[0]
        # for i in range(1, len(nums)):
        #     if dp[i-1] < 0:
        #         dp[i] = nums[i]
        #     else:
        #         dp[i] = dp[i-1] + nums[i]
        # return max(dp)      
# @lc code=end

