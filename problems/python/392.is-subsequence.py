#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # TC: O(n1|n2)
        # SC: O(1)
        n1, n2 = len(s), len(t)
        left = right = 0

        while left < n1 and right < n2:
            if s[left] == t[right]:
                left += 1
                right += 1
            else:
                right += 1

        return left == n1
# @lc code=end

