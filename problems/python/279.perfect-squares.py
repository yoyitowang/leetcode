#
# @lc app=leetcode id=279 lang=python3
#
# [279] Perfect Squares
#

# @lc code=start
class Solution:
    def numSquares(self, n: int) -> int:
        # TC: O(n*size)
        # TC: O(n)
        nums = [i*i for i in range(1, int(n**(0.5))+1)]
        
        f = [0] + [inf] * n
        f[0] = 0
        for num in nums:
            for j in range(num, n+1):
                f[j] = min(f[j], f[j-num] +1)

        return f[n]
# @lc code=end

