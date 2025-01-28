#
# @lc app=leetcode id=278 lang=python3
#
# [278] First Bad Version
#

# @lc code=start
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # TC: O(log n)
        # SC: O(1)
        left, right = 1, n
        while left <= right:
            mid = left + (right - left) // 2
            # bad version: right moves to mid
            if isBadVersion(mid):
                right = mid - 1
            # not bad version: left moves to mid+1
            else:
                left = mid + 1
                
        return left
        
# @lc code=end

