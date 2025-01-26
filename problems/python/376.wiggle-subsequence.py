#
# @lc app=leetcode id=376 lang=python3
#
# [376] Wiggle Subsequence
#

# @lc code=start
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        # TC: O(n)
        # SC: O(1)
        if len(nums) <= 1:
            return len(nums)
        cnt = 1
        prev = 0
        for i in range(1, len(nums)):
            cur = nums[i]-nums[i-1]
            if (cur > 0 and prev <= 0) or (cur < 0 and prev >= 0):
                cnt += 1
                prev = cur
        return cnt
# @lc code=end

