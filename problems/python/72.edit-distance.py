#
# @lc app=leetcode id=72 lang=python3
#
# [72] Edit Distance
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # # TC: O(s*t)
        # # SC: O(s*t)
        # s = len(word1)
        # t = len(word2)
        # # word1[i] == word2[j]: no action -> go to i-1 and j-1 substrings
        # # word1[i] != word2[j]: insert/delete/replace
        # # insert: i, j-1
        # # delete: i-1, j
        # # replace: i-1, j-1
        # @cache
        # def dfs(i, j):
        #     # word1 is empty -> insert j+1 times
        #     if i < 0:
        #         return j + 1
        #     # word2 is empty -> insert i+1 times
        #     if j < 0:
        #         return i + 1
        #     if word1[i] == word2[j]:
        #         return dfs(i-1, j-1)
        #     else:
        #         return min(dfs(i, j-1), dfs(i-1, j), dfs(i-1, j-1)) + 1

        # return dfs(s-1, t-1)     
    

        s = len(word1)
        t = len(word2)

        f = [[0] * (t+1) for _ in range(s+1)]
        # i < 0
        f[0] = list(range(t+1))
        for i, x in enumerate(word1):
            # j < 0
            f[i+1][0] = i + 1
            for j, y in enumerate(word2):
                if x == y:
                    f[i+1][j+1] = f[i][j]
                else:
                    f[i+1][j+1] = min(f[i+1][j], f[i][j+1], f[i][j]) + 1
        
        return f[s][t]
# @lc code=end

