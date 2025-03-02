#
# @lc app=leetcode id=583 lang=python3
#
# [583] Delete Operation for Two Strings
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # n1, n2 = len(word1), len(word2)

        # @cache
        # def dfs(i, j):
        #     if i < 0:
        #         return j + 1
        #     if j < 0:
        #         return i + 1
            
        #     if word1[i] == word2[j]:
        #         return dfs(i-1, j-1)
        #     return min(dfs(i-1, j)+1, dfs(i, j-1)+1, dfs(i-1, j-1)+2) 

        # return dfs(n1-1, n2-1)

        # # TC: O(n1*n2)
        # # SC: O(n1*n2)
        # n1, n2 = len(word1), len(word2)

        # f = [[0] * (n2+1) for _ in range(n1+1)]
        # for i in range(n1+1):
        #     f[i][0] = i
        # for j in range(n2+1):
        #     f[0][j] = j
        # for i, w1 in enumerate(word1):
        #     for j, w2 in enumerate(word2):
        #         if w1 == w2:
        #             f[i+1][j+1] = f[i][j]
        #         else:
        #             f[i+1][j+1] = min(f[i][j]+2, f[i+1][j]+1, f[i][j+1]+1)

        # return f[n1][n2]

        # TC: O(n1*n2)
        # SC: O(n2)
        n1, n2 = len(word1), len(word2)

        f = [i for i in range(n2+1)]
        for i, w1 in enumerate(word1):
            prev = f[0]
            f[0] = i + 1
            for j, w2 in enumerate(word2):
                tmp = f[j+1]
                if w1 == w2:
                    f[j+1] = prev
                else:
                    f[j+1] = min(prev+2, f[j]+1, f[j+1]+1)
                prev = tmp

        return f[n2]
# @lc code=end

