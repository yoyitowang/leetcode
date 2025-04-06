#
# @lc app=leetcode id=162 lang=python3
#
# [162] Find Peak Element
#

# @lc code=start
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # TC: O(log n)
        # SC: O(1)
        n = len(nums)
        # [0, n-2] -> (-1, n-1)
        left, right = 0, n - 2
        while left <= right:
            mid = (left+right)//2

            if nums[mid] > nums[mid+1]: # blue
                right = mid - 1
            else:
                left = mid + 1
        return left

# @lc code=end

