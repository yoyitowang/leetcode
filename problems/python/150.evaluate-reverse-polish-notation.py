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
        ht = {"+", "-", "*", "/"}
        st = []
        # num -> stack
        # when symbol -> take 2 num from stack
        for token in tokens:
            if token not in ht:
                st.append(int(token))
            else:
                num2 = st.pop()
                num1 = st.pop()
                match token:
                    case "+":
                        new = num1 + num2
                    case "-":
                        new = num1 - num2
                    case "*":
                        new = num1 * num2
                    case "/":
                        new = int(num1 / num2)
                st.append(new)
        return st.pop() if st else 0
    
# @lc code=end

