#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        # TC: O(n)
        # SC: O(n)
        ht = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        ans = []
        for char in s:
            ans.append(ht[char])
        
        for i in range(1, len(ans)):
            if ans[i] > ans[i-1]:
                ans[i-1] = -ans[i-1]
        
        return sum(ans)
             
# @lc code=end

