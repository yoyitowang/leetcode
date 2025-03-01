#
# @lc app=leetcode id=1035 lang=python3
#
# [1035] Uncrossed Lines
#

# @lc code=start
class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        # n1, n2 = len(nums1), len(nums2)
        # @cache
        # def dfs(i, j):
        #     # when one is empty -> no connection
        #     if i < 0 or j < 0:
        #         return 0
        #     # when nums are matched -> choose
        #     if nums1[i] == nums2[j]:
        #         return dfs(i-1, j-1) + 1
        #     return max(dfs(i-1, j), dfs(i, j-1))

        # return dfs(n1-1, n2-1)

        # # DP - 1
        # # TC: O(n1*n2)
        # # TC: O(n1*n2)
        # n1, n2 = len(nums1), len(nums2)
        # f = [[0] * (n2+1) for _ in range(n1+1)]
        # for i, num1 in enumerate(nums1):
        #     for j, num2 in enumerate(nums2):
        #         if num1 == num2:
        #             f[i+1][j+1] = f[i][j] + 1
        #         else:
        #             f[i+1][j+1] = max(f[i][j+1], f[i+1][j])
        # return f[n1][n2]
    
        # DP - 2
        # TC: O(n1*n2)
        # TC: O(n2)
        n1, n2 = len(nums1), len(nums2)
        f = [0] * (n2+1)
        for _, num1 in enumerate(nums1):
            prev = f[0]
            for j, num2 in enumerate(nums2):
                prev, f[j+1] = f[j+1], prev + 1 if num1 == num2 else max(f[j+1], f[j])
        return f[n2]

# @lc code=end

