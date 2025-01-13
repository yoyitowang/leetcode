#
# @lc app=leetcode id=454 lang=python3
#
# [454] 4Sum II
#

# @lc code=start
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        # TC: O(n^2)
        # SC: O(1)

        res = 0
        from collections import defaultdict
        ht = defaultdict(int)
        for num1 in nums1:
            for num2 in nums2:
                _sum = num1+num2
                ht[_sum] += 1

        for num3 in nums3:
            for num4 in nums4:
                if (_sum2 := (num3+num4)*(-1)) in ht:
                    res += ht[_sum2]
        return res
        
# @lc code=end

