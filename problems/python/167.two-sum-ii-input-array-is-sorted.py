#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # TC: O(n)
        # SC: O(1)
        left, right = 0, len(numbers)-1
        while left < right:
            s = numbers[left] + numbers[right]
            if s == target:
                return [left+1, right+1]
            elif s > target:
                right -= 1
            else:
                left += 1
# @lc code=end

