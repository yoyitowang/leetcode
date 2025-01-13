#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # TC: O(n+m)
        # SC: O(1)

        from collections import Counter
        ht = Counter(i for i in magazine)
        for char in ransomNote:
            if char not in ht or ht[char] <= 0:
                return False
            
            ht[char] -= 1
        
        return True
# @lc code=end

