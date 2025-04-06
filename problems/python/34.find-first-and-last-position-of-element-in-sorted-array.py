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

        # -- [left, right]
        def lower_bound(nums, target):
            n = len(nums)
            left, right = 0, n-1

            while left <= right:
                mid = (left+right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left
            
        # -- [left, right)
        def lower_bound2(nums, target):
            n = len(nums)
            left, right = 0, n

            while left < right:
                mid = (left+right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            return left
            
        # -- (left, right)
        def lower_bound3(nums, target):
            n = len(nums)
            left, right = -1, n

            while left + 1 < right:
                mid = (left+right) // 2
                if nums[mid] < target:
                    left = mid
                else:
                    right = mid
            return right
        
        first = lower_bound3(nums, target)
        if first == len(nums) or nums[first] != target:
            return [-1, -1]
        last = lower_bound3(nums, target+1) - 1
        return [first, last]

# # @lc code=end

