#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Time: O(logn)
        # Space: O(1)
        n = len(nums)
        l, r = 0, n-1
        # not rotation list
        if nums[l] < nums[r] or n == 1:
            return nums[l]

        while l < r:
            mid = l + ((r-l)>>1)
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        return nums[l]
# @lc code=end

