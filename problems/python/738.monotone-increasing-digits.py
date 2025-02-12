#
# @lc app=leetcode id=738 lang=python3
#
# [738] Monotone Increasing Digits
#

# @lc code=start
class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        # TC: O(n)
        # SC: O(n)
        
        ns = str(n)
        n = len(ns)
        flag = n

        for i in range(n-1, 0, -1):
            if ns[i-1] > ns[i]:
                flag = i
                ns = ns[: i-1] + str(int(ns[i-1]) - 1) + ns[i:]
        n -= flag
        ns = ns[: flag] + '9'*n
        return int(ns)   
# @lc code=end

