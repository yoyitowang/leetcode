#
# @lc app=leetcode id=377 lang=python3
#
# [377] Combination Sum IV
#

# @lc code=start
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # TC: O(n*target)
        # SC: O(target)
        # @cache
        # def dfs(i):
        #     if i == 0:
        #         return 1
        #     return sum(dfs(i-x) for x in nums if i >= x)

        # return dfs(target)

        # dp
        # TC: O(n*target)
        # SC: O(n)

        n = len(nums)
        f = [0] * (target+1)
        f[0] = 1
        
        for i in range(target+1):
            for num in nums:
                if i >= num:
                    f[i] += f[i-num]
        return f[target]
# @lc code=end

