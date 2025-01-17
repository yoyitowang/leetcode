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
            if char in table:
                ele = st.pop() if st else "#"
                if table[char] != ele:
                    return False
            else:
                st.append(char)
        
        return not st
        
# @lc code=end

