#
# @lc app=leetcode id=216 lang=python3
#
# [216] Combination Sum III
#

# @lc code=start
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # TC: O(c(9, k))
        # SC: O(k)
        self.ans = []
        
        def backtracking(start, path):
            if len(path) == k:
                if sum(path) == n:
                    self.ans.append(path[:])
                return
            
            for i in range(start, 9-(k-len(path))+2):
                # prune
                if sum(path) + i > n:
                    return

                path.append(i)
                backtracking(i+1, path)
                path.pop()
        
        backtracking(start=1, path=[])
        
        return self.ans      
# @lc code=end

