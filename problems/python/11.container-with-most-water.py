#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # TC: O(n)
        # SC: O(1)
        left, right = 0, len(heights)-1
        ans = 0
        while left < right:
            h = min(heights[left], heights[right])
            w = right - left
            ans = max(ans, h*w)
            if heights[left] > heights[right]:
                right -= 1 
            else:
                left += 1
        return ans
# @lc code=end

