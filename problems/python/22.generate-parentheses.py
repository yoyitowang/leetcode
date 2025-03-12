#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # TC: O(n*2)
        # SC: O(n*2)

        ans = []
        st = []

        def backtracking(openN, closeN):
            if openN == closeN == n:
                ans.append(''.join(st[:]))
                return
            if openN < n:
                st.append("(")
                backtracking(openN+1, closeN)
                st.pop()
            if openN > closeN:
                st.append(")")
                backtracking(openN, closeN+1)
                st.pop()
        
        backtracking(0, 0)
        return ans
            
# @lc code=end

