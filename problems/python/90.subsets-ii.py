#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.ans = []

        def backtracking(nums, start, path):
            self.ans.append(path[:])
            n = len(nums)
            for i in range(start, n):
                if i > start and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                backtracking(nums, i+1, path)
                path.pop()
        backtracking(nums, 0, [])
        return self.ans     
# @lc code=end

