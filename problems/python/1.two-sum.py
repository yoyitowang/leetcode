#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # TC: O(n)
        # SC: O(n)
        ht = {}
        for idx, num in enumerate(nums):
            if num in ht:
                return [ht[num], idx]
            ht[target-num] = idx
        
# @lc code=end

