#
# @lc app=leetcode id=516 lang=python3
#
# [516] Longest Palindromic Subsequence
#

# @lc code=start
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # n = len(s)

        # @cache
        # def dfs(i, j):
        #     if i > j:
        #         return 0
        #     if i == j:
        #         return 1
        #     if s[i] == s[j]:
        #         return dfs(i+1, j-1) + 2
        #     return max(dfs(i+1, j), dfs(i, j-1))
        # return dfs(0, n-1)    

        # TC: O(n^2)
        # TC: O(n^2)
        n = len(s)

        f = [[0] * (n) for _ in range(n)]
        for i in range(n):
            f[i][i] = 1

        # f[i][j] = f[i+1][j-1] + 2
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if s[i] == s[j]:
                    f[i][j] = f[i+1][j-1] + 2
                else:
                    f[i][j] = max(f[i+1][j], f[i][j-1])

        return f[0][n-1]
# @lc code=end

