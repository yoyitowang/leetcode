#
# @lc app=leetcode id=151 lang=python3
#
# [151] Reverse Words in a String
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.split()
        left, right = 0, len(l)-1
        while left < right:
            l[left], l[right] = l[right], l[left]
            left += 1
            right -= 1
        return ' '.join(l)
        
# @lc code=end

