#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # # TC: O(n1|n2)
        # # SC: O(1)
        # n1, n2 = len(s), len(t)
        # left = right = 0

        # while left < n1 and right < n2:
        #     if s[left] == t[right]:
        #         left += 1
        #         right += 1
        #     else:
        #         right += 1

        # return left == n1
    
        # # dfs
        # # TC: O(n2)
        # # SC: O(n2)
        # n1, n2 = len(s), len(t)
        
        # @cache
        # def dfs(i, j):
        #     if i < 0:
        #         return True
        #     if j < 0:
        #         return False
        #     if s[i] == t[j]:
        #         return dfs(i-1, j-1)
        #     return dfs(i, j-1)

        # return dfs(n1-1, n2-1)

        # 2-dim DP
        # TC: O(n2)
        # SC: O(n2)
        n1, n2 = len(s), len(t)
        f = [[False] * (n2+1) for _ in range(n1+1)]
        for i in range(n2):
            f[0][i] = True
        
        for i, x in enumerate(s):
            for j, y in enumerate(t):
                if x == y:
                    f[i+1][j+1] = f[i][j]
                else:
                    f[i+1][j+1] = f[i+1][j]
        return f[n1][n2]
# @lc code=end

