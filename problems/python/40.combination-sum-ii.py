#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # TC: O(n log n + 2^n)
        # SC: O(n)
        candidates.sort()
        ans = []

        def backtracking(start, path):
            if sum(path) == target:
                ans.append(path[:])
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                if sum(path) + candidates[i] > target:
                    return
                path.append(candidates[i])
                backtracking(i+1, path)
                path.pop()
        
        backtracking(0, [])
        return ans  
# @lc code=end

