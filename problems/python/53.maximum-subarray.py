#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # # TC: O(n)
        # # SC: O(1)
        # ans = -inf
        # acc = 0
        # for num in nums:
        #     acc += num
        #     ans = max(ans, acc)
        #     if acc < 0: acc = 0
        # return ans
    
        # TC: O(n)
        # SC: O(n)
        n = len(nums)
        
        @cache
        def dfs(i):
            if i < 0:
                return 0
            return max(nums[i], dfs(i-1)+nums[i])

        return max(dfs(i) for i in range(n))
    
        # # DP
        # # TC: O(n)
        # # SC: O(n)
        # dp = [0] * len(nums)
        # dp[0] = nums[0]
        # for i in range(1, len(nums)):
        #     if dp[i-1] < 0:
        #         dp[i] = nums[i]
        #     else:
        #         dp[i] = dp[i-1] + nums[i]
        # return max(dp)      
# @lc code=end

