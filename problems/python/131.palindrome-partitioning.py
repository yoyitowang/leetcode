#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#

# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # TC: O(n*2^n)
        # SC: O(n)
        self.ans = []
        self.backtracking(s, 0, [])
        return self.ans
        
    def backtracking(self, s, start, path):
        if start == len(s):
            self.ans.append(path[:])
            return
        
        for i in range(start, len(s)):
            if self.isPalindrome(s, start, i):
                path.append(s[start: i+1])
                self.backtracking(s, i+1, path)
                path.pop()
        
    def isPalindrome(self, s, start, end):
        left = start
        right = end
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True     
# @lc code=end

