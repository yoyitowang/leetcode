#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        # TC: O(n)
        # SC: O(1)
        if n <= 2:
            return n
        f0 = 1
        f1 = 2
        for i in range(3, n+1):
            f0, f1 = f1, f0 + f1

        return f1
# @lc code=end

