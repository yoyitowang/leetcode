#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # TC: O(n)
        # SC: O(1)
        n = len(nums)
        res = [1] * n
        
        left_product = 1
        for i in range(n):
            res[i] *= left_product
            left_product *= nums[i]
        
        right_product = 1
        for i in range(n-1, -1, -1):
            res[i] *= right_product
            right_product *= nums[i]

        return res  
# @lc code=end

