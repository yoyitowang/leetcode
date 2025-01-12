#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # TC: O(n) not fullfill O(log n)
        # SC: O(1)

        
        left, right = 0, len(nums)-1
        res = [-1, -1]
        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                for i in range(mid, -1, -1):
                    if nums[i] == target:
                        res[0] = i
                for i in range(mid, len(nums)):
                    if nums[i] == target:
                        res[1] = i
                break
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return res
# # @lc code=end

