#
# @lc app=leetcode id=455 lang=python3
#
# [455] Assign Cookies
#

# @lc code=start
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # TC: O(n log n + m log m)
        # SC: O(1)
        s.sort() # O(n log n)
        g.sort() # O(m log m)
        res = 0
        index = len(s)-1
        for child in range(len(g)-1, -1, -1):
            if index >= 0 and s[index] >= g[child]:
                res += 1
                index -= 1

        return res
    
# @lc code=end

