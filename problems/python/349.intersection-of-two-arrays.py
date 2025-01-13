#
# @lc app=leetcode id=349 lang=python3
#
# [349] Intersection of Two Arrays
#

# @lc code=start
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # TC: O(m+n)
        # SC: O(m+n)
        return list(set(nums1)&set(nums2))
# @lc code=end

