#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        # Use slow-fast pointer can imporve this performance
        # Circular question -> slow-fast
        # TC: O(log n)
        # SC: O(k)
        ht = set()
        while n not in ht:
            ht.add(n)
            n = str(n)
            _sum = 0      
            for i in n:
                _sum += int(i)**2
            if _sum == 1: return True
            n = _sum
        return False
        
# @lc code=end

