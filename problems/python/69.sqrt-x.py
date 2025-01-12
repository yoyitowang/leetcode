#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        # TC: O(log n)
        # SC: O(1)
        if x == 0 or x == 1:
            return x
        left, right = 0, x
        while left <= right:
            mid = (left + right) // 2
            if (res:=mid*mid) == x:
                return mid
            elif res < x:
                left = mid + 1
            else:
                right = mid - 1
        return right
        
# @lc code=end

