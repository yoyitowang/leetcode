#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # TC: O(logn)
        # SC: O(1)
        n = len(nums)
        left, right = -1, n
        while left + 1 < right:
            mid = left + ((right - left)>>1)
            if nums[mid] < target:
                left = mid
            else:
                right = mid
        return right
        
# @lc code=end

