#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # TC: O(n+n)
        # OC: O(26)=O(1)
        from collections import defaultdict
        ht = defaultdict(int)
        if (ls:=len(s)) != (lt:=len(t)):
            return False
        for char in s:
            ht[char] += 1
        for char in t:
            ht[char] -= 1
        for v in ht.values():
            if v != 0:
                return False

        return True
        
# @lc code=end

