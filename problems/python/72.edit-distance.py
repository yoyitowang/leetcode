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
    
        # TC: O(n1*n2)
        # SC: O(n2)
        n1, n2 = len(word1), len(word2)
        f = list(range(n2+1))

        for i, w1 in enumerate(word1):
            prev = f[0]
            f[0] = i+1
            for j, w2 in enumerate(word2):
                prev , f[j+1] = f[j+1], prev if w1 == w2 else min(prev, f[j], f[j+1]) + 1
        return f[n2]
# @lc code=end

