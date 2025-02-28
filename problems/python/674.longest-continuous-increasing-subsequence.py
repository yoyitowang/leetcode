#
# @lc app=leetcode id=674 lang=python3
#
# [674] Longest Continuous Increasing Subsequence
#

# @lc code=start
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        # TC: O(n)
        # SC: O(1)
        n = len(nums)
        ans = 0
        l = 0
        for i in range(n):
            # when not incremental, update the left index
            if i > 0 and nums[i-1] >= nums[i]:
                l = i
            ans = max(ans, i-l+1)
        
        return ans
# @lc code=end

