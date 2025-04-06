#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # TC: O(log n)
        # SC: O(1)
        # blue(true): target and the right side values
        #             shrink the right side -> left -> right = mid -1
        #             if all values in list are blue -> all values are <= target
        #             check the first value in blue is target or not
        # red(false): left side of target value
        #             expand the left side -> right -> left = mid + 1
        #             if all values in list are red -> all values are < target
        #             none of the value in list is the answer
        def isBlue(i: int):
            x = nums[i] # mid
            if x > nums[-1]:
                return target > nums[-1] and x >= target
            return target > nums[-1] or x >= target


        n = len(nums)
        left, right = 0, n-1

        while left <= right:
            mid = (left + right)//2

            # right
            if isBlue(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left if left < n and nums[left] == target else -1
# @lc code=end

