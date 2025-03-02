#
# @lc app=leetcode id=647 lang=python3
#
# [647] Palindromic Substrings
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        # # TC: O(n^2)
        # # SC: O(n^2)
        # self.cnt = 0
        # n = len(s)

        # # s[i] ~ s[j] isPalidorma -> s[i-1] ~ s[j-1] isPalidroma
        # @cache
        # def dfs(i, j):
        #     if i > j:
        #         return 0
        #     if i == j:
        #         self.cnt += 1
        #         return 1
        #     if j-i == 1 and s[i] == s[j]:
        #         self.cnt += 1
        #         return 1
        #     if s[i] == s[j] and dfs(i+1, j-1):
        #         self.cnt += 1
        #         return 1
        
        # for i in range(n):
        #     for j in range(i, n):
        #         dfs(i, j)
        # return self.cnt


        # DP
        # TC: O(n^2)
        # SC: O(n^2)
        self.cnt = 0
        n = len(s)

        f = [[0] * (n) for _ in range(n)]
        for j, x in enumerate(s):
            for i in range(j+1):
                y = s[i]
                if i == j:
                    f[i][j] = 1
                    self.cnt += 1
                elif j-i == 1 and x == y:
                    f[i][j] = 1
                    self.cnt += 1
                elif j-i > 1 and x == y and f[i+1][j-1]:
                    f[i][j] = 1
                    self.cnt += 1
        return self.cnt
# @lc code=end

