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
        prev = 0
        cnt = 1

        for i in range(1, len(nums)):
            diff = nums[i] - nums[i-1]
            if diff != 0 and prev * diff <= 0:
                cnt += 1
                prev = diff

        return cnt 
# @lc code=end

