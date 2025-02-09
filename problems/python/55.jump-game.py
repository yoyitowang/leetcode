#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # TC: O(n)
        # SC: O(1)
        n = len(nums)
        cover = 0
        if n == 1:
            return True

        idx = 0
        while idx <= cover:
            cover = max(cover, idx+nums[idx])
            if cover >= n-1:
                return True
            idx += 1

        return False   
# @lc code=end

