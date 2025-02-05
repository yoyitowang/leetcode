#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # TC: O(n^target/min(candidates))
        # SC: O(target/min) maximum depth of the tree

        candidates.sort() # O(n log n)
        self.ans = []

        def backtracking(start, path):
            if sum(path) == target:
                self.ans.append(path[:])
                return
            
            for i in range(start, len(candidates)):
                if sum(path) + candidates[i] > target:
                    return
                path.append(candidates[i])
                backtracking(i, path)
                path.pop()
        backtracking(0, [])

        return self.ans    
# @lc code=end

