#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # TC: O(c(n, k))
        # SC: O(k)
        self.path = []
        self.ans = []
        self.backtracking(n, k, 1)

        return self.ans
        
    def backtracking(self, n, k, start):
        # stop condition
        if len(self.path) == k:
            self.ans.append(self.path.copy())
            return
        # start
        for i in range(start, n-(k-len(self.path))+2):
            self.path.append(i)
            self.backtracking(n, k, i+1)
            self.path.pop()
         
# @lc code=end

