#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        # TC: O(n)
        # SC: O(1)
        ans = 0
        cover = 0
        cur = 0
        idx = 0
        if len(nums) == 1:
            return ans

        while idx <= cover:
            cover = max(cover, idx + nums[idx])
            if idx == cur:
                cur = cover
                ans += 1
                if cover >= len(nums) - 1:
                    break
            idx += 1

        return ans     
# @lc code=end

