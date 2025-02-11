#
# @lc app=leetcode id=844 lang=python3
#
# [844] Backspace String Compare
#

# @lc code=start
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # TC: O(n/m)
        # SC: O(n+m)

        ans = []
        ans2 = []
        for i in range(len(s)):
            if s[i] == "#":
                if ans:
                    ans.pop()
            else:
                ans.append(s[i])
        
        for i in range(len(t)):
            if t[i] == "#":
                if ans2:
                    ans2.pop()
            else:
                ans2.append(t[i])
        
        return ans == ans2
            
# @lc code=end

