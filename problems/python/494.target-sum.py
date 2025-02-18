#
# @lc app=leetcode id=494 lang=python3
#
# [494] Target Sum
#

# @lc code=start
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # TC: O(n*target)
        # SC: O(n*target)

        # p: positive
        # s-p: sum-positive=negative
        # p-(s-p)=t -> 2p=s+t -> p=(s+t)/2

        target += sum(nums)
        if target < 0 or target % 2:
            return 0
        # p=capacity
        target //= 2

        n = len(nums)

        @cache
        def dfs(i, c):
            if i < 0:
                return 1 if c == 0 else 0
            if nums[i] > c:
                return dfs(i-1, c)
            return dfs(i-1, c) + dfs(i-1, c-nums[i])
        
        return dfs(n-1, target)
# @lc code=end

