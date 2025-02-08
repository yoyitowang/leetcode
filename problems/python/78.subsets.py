#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # TC: O(2^n)
        # SC: O(n*2^n)
        self.ans = []

        def backtracking(start, path):
            self.ans.append(path[:])
            if start == len(nums):
                return
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtracking(i+1, path)
                path.pop()

        backtracking(0, [])
        return self.ans 
    
        # iterative
        result = [[]]

        for num in nums:
            result += [res + [num] for res in result]
        return result
# @lc code=end

