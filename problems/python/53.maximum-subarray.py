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
# @lc code=end

