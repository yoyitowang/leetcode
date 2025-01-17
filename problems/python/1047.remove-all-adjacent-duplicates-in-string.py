#
# @lc app=leetcode id=1047 lang=python3
#
# [1047] Remove All Adjacent Duplicates In String
#

# @lc code=start
class Solution:
    def removeDuplicates(self, s: str) -> str:
        # TC: O(n)
        # SC: O(n) worst case
        st = []
        for char in s:
            if st and st[-1] == char:
                st.pop()
            else:
                st.append(char)
        return ''.join(st)     
# @lc code=end

