#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # TC: O(s+t)
        # SC: O(s)
        if len(s) != len(t):
            return False

        from collections import defaultdict
        ht = defaultdict(int)
        for char in s:
            ht[char] += 1
        
        for char in t:
            if ht[char] == 0:
                return False
            ht[char] -= 1

        return True             
# @lc code=end

