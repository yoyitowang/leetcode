#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # TC: O(log n)
        # SC: O(1)
        def findLeft(nums, target):
            left, right = 0, len(nums)-1
            while left <= right:
                mid = (left+right)//2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            if left < len(nums) and nums[left] == target:
                return left
            return -1
        def findRight(nums, target):
            left, right = 0, len(nums)-1
            while left <= right:
                mid = (left+right)//2
                if nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            if right >= 0 and nums[right] == target:
                return right
            return -1
            
        return [findLeft(nums, target), findRight(nums, target)]
# # @lc code=end

