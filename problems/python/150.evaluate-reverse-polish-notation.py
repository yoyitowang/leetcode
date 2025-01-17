#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # TC: O(n)
        # SC: O(n)
        op = {"+", "-", "*", "/"}
        st = []
        for token in tokens:
            if token not in op:
                st.append(int(token))
            else:
                n2 = st.pop()
                n1 = st.pop()
                if token == "+":
                    st.append(n1+n2)
                elif token == "-":
                    st.append(n1-n2)
                elif token == "*":
                    st.append(n1*n2)
                elif token == "/":
                    st.append(int(n1/n2))
        
        return st.pop()
    
# @lc code=end

