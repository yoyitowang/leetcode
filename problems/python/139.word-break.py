#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # TC: O(n^2)
        # SC: O(n)
        n = len(wordDict)
        cap = len(s)

        f = [False] * (cap+1)
        f[0] = True
        for i in range(1,cap+1):
            for j in range(i):
                if f[j] and s[j:i] in wordDict:
                    f[i] = True
                    break
        
        return f[cap]
# @lc code=end

