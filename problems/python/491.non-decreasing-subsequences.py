#
# @lc app=leetcode id=491 lang=python3
#
# [491] Non-decreasing Subsequences
#

# @lc code=start
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        # TC: O(2^n) taken or not taken
        # SC: O(n+2^n)
        self.ans = []

        def backtracking(start, nums, path):
            if len(path) > 1:
                self.ans.append(path[:])

            used = set()            
            for i in range(start, len(nums)):
                if i > start and nums[i] in used:
                    continue
                if not path or nums[i] >= path[-1]:
                    used.add(nums[i])
                    path.append(nums[i])
                    backtracking(i+1, nums, path)
                    path.pop()
        
        backtracking(0, nums, [])
        return self.ans
# @lc code=end

