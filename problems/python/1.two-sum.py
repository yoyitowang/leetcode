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
            c = target - num
            if c in ht:
                return [ht[c], idx]
            ht[num] = idx
        
# @lc code=end

