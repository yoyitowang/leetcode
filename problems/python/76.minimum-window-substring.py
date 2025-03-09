#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # TC: O(52*m+n)
        # SC: O(m+n)
        cntT = Counter(t)
        cntS = Counter()

        left = right = 0
        ans = ""
        maxL = inf

        left = 0
        for right, c in enumerate(s):
            cntS[c] += 1
            while cntS >= cntT:
                if right-left+1 < maxL:
                    ans = s[left:right+1]
                    maxL = min(maxL, right-left+1)
                cntS[s[left]] -= 1
                left += 1
        
        return ans
# @lc code=end

