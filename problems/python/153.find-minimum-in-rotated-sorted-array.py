#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # TC: O(log n)
        # SC: O(1)
        # red(left): minmum of left side
        # blue(right): maxmum of right side
        # find the blue range which means the minimum and the minmum of right side
        # [0, n-2] -> (-1, n-1)
        n = len(nums)
        left, right = 0, n-2
        while left <= right:
            mid = (left+right) // 2
            # find the blue range
            if nums[mid] < nums[-1]:
                right = mid - 1
            else:
                left = mid + 1
        return nums[left]
# @lc code=end

