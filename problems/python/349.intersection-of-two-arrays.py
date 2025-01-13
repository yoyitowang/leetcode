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
        ht = set()
        res = []
        for n in nums1:
            ht.add(n)

        for n in nums2:
            if n in ht:
                ht.remove(n)
                res.append(n)
        return res
# @lc code=end

