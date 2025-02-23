#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        # TC: O(n+n)
        # SC: O(1)
        n = len(nums)
        if n <= 2:
            return max(nums)
        ans = 0
        # first taken: 2~n-2
        f0 = f1 = 0
        for i in range(2, n-1):
            f0, f1 = f1, max(f1, f0+nums[i])
        ans += f1 + nums[0]

        # first not taken : 1~n-1
        f0 = f1 = 0
        for i in range(1, n):
            f0, f1 = f1, max(f1, f0+nums[i])
        ans = max(ans, f1)

        return ans     
# @lc code=end

