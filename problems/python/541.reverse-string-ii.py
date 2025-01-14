#
# @lc app=leetcode id=541 lang=python3
#
# [541] Reverse String II
#

# @lc code=start
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        # TC: O(n)
        # SC: O(n)
        s = list(s)
        for i in range(0, len(s), 2*k):
            left, right = i, i+k-1 if i+k-1 < len(s)-1 else len(s)-1
            while left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
        return ''.join(s)
# @lc code=end

