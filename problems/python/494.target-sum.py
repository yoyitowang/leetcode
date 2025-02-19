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

        # recursive
        # n = len(nums)
        # @cache
        # def dfs(i, c):
        #     if i < 0:
        #         return 1 if c == 0 else 0
        #     if nums[i] > c:
        #         return dfs(i-1, c)
        #     return dfs(i-1, c) + dfs(i-1, c-nums[i])
        # return dfs(n-1, target)

        # DP - 2 dim
        # TC: O(n*target)
        # SC: O(n*target)
        # f[i][c] = f[i-1][c] + f[i-1][c-nums[i]]
        # f[i+1][c] = f[i][c] + f[i][c-nums[i]]
        # n = len(nums)
        # f = [[0 for _ in range(target+1)] for _ in range(n+1)]
        # f[0][0] = 1
        # for i, num in enumerate(nums):
        #     for c in range(target+1):
        #         if c < num:
        #             f[i+1][c] = f[i][c]
        #         else:
        #             f[i+1][c] = f[i][c] + f[i][c-num]
        
        # return f[n][target]

        # TC: O(n*target)
        # SC: O(2*target)
        # n = len(nums)
        # f = [[0 for _ in range(target+1)] for _ in range(2)]
        # f[0][0] = 1
        # for i, num in enumerate(nums):
        #     for c in range(target+1):
        #         if c < num:
        #             f[(i+1)%2][c] = f[i%2][c]
        #         else:
        #             f[(i+1)%2][c] = f[i%2][c] + f[i%2][c-num]
        
        # return f[n%2][target]

        # TC: O(n*target)
        # SC: O(1)
        n = len(nums)
        f = [0 for _ in range(target+1)]
        f[0] = 1
        for num in nums:
            for c in range(target, num-1, -1):
                f[c] = f[c] + f[c-num]

        return f[target]

        
# @lc code=end

