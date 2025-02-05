#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # TC: O(4^n)
        # SC: O(n)
        ht = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        self.ans = []

        if digits == "":
            return self.ans

        def backtracking(start, path):
            if len(path) == len(digits):
                self.ans.append("".join(path))
                return
            
            for i in range(start, len(digits)):
                num = digits[i]
                if num in ht:
                    for alphabet in ht[num]:
                        path.append(alphabet)
                        backtracking(i+1, path)
                        path.pop()
        
        backtracking(0, [])
        return self.ans     
# @lc code=end

