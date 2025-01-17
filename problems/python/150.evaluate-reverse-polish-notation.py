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
        op = [
            "+",
            "-",
            "*",
            "/"
        ]
        st = []
        for token in tokens:
            if token not in op:
                st.append(token)
            elif len(st) >= 2:
                n2 = st.pop()
                n1 = st.pop()
                st.append(str(int(eval(n1+token+n2))))
        
        return int(st.pop())
    
# @lc code=end

