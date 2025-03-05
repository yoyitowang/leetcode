#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # TC: O(n)
        # SC: O(26)
        ht = defaultdict(int)
        left = 0
        ans = 0
        max_value = 0 
        for right, char in enumerate(s):
            ht[char] += 1
            max_value = max(max_value, ht[char])
            # calculate if length - max <= k
            while right-left+1 - max_value > k:
                ht[s[left]] -= 1
                left += 1
            ans = max(ans, right-left+1)
        return ans
# @lc code=end

