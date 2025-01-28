#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # TC: O(n+n)
        # SC: O(n)
        ss = ''.join(char.lower() for char in s if char.isalnum())
        left, right = 0, len(ss)-1
        while left < right:
            if ss[left] != ss[right]:
                return False
            left += 1
            right -= 1
        return True      
# @lc code=end

