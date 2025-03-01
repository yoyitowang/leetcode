#
# @lc app=leetcode id=1035 lang=python3
#
# [1035] Uncrossed Lines
#

# @lc code=start
class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)
        @cache
        def dfs(i, j):
            # when one is empty -> no connection
            if i < 0 or j < 0:
                return 0
            # when nums are matched -> choose
            if nums1[i] == nums2[j]:
                return dfs(i-1, j-1) + 1
            return max(dfs(i-1, j), dfs(i, j-1))

        return dfs(n1-1, n2-1)
# @lc code=end

