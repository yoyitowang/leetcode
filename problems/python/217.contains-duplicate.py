#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # TC: O(n)
        # SC: O(n)
        ht = {}
        for num in nums:
            if num in ht:
                return True
            ht[num] = 1
        return False
              
# @lc code=end

