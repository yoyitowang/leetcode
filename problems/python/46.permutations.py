#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # TC: O(n*n!)
        # SC: O(n*n!)
        self.n = len(nums)
        self.ans = []

        def backtracking(path, used):
            if len(path) == self.n:
                self.ans.append(path[:])
                return
                
            for i in range(self.n):
                if used[i]:
                    continue
                used[i] = True
                path.append(nums[i])
                backtracking(path, used)
                path.pop()
                used[i] = False

        backtracking([], [False] * self.n)
        return self.ans    
# @lc code=end

