#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # TC: O(n*n!)
        # SC: O(k*n+n)
        ans = []

        def backtracking(path, used):
            if (n := len(nums)) == len(path):
                ans.append(path[:])
                return
            
            used_num = set()
            for i in range(n):
                if used[i]:
                    continue
                if nums[i] in used_num:
                    continue
                used[i] = True
                used_num.add(nums[i])
                path.append(nums[i])
                backtracking(path, used)
                path.pop()
                used[i] = False

        backtracking([], [False]*len(nums))
        return ans      
# @lc code=end

