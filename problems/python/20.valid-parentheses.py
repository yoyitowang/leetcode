#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        st = []
        table = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        for char in s:
            if char in table.keys() and len(st) > 0:
                if table[char] != st.pop():
                    return False
            else:
                st.append(char)
        
        return False if len(st) > 0 else True
        
# @lc code=end

