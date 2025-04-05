#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # TC: O(log n)
        # SC: O(1)
        n = len(nums)
        left, right = 0, n-1

        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

            if left == n:
                return -1

        return left if nums[left] == target else -1
# @lc code=end

