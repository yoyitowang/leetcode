#
# @lc app=leetcode id=1143 lang=python3
#
# [1143] Longest Common Subsequence
#

# @lc code=start
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # TC: O(s*t)
        # SC: O(t)
        s = len(text1)
        t = len(text2)

        # f[i][j]
        # equal: f[i-1][j-1] + 1
        # not equal: max(f[i-1][j], f[i][j-1])
        f = [0] * (t+1)
        for i, x in enumerate(text1):
            pre = f[0]
            for j, y in enumerate(text2):
                pre, f[j+1] = f[j+1], pre + 1 if x == y else max(f[j], f[j+1])
        
        return f[t]
# @lc code=end

