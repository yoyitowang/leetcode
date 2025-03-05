#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # TC: O(n)
        # SC: O(128)=O(1)=O(len(set(s)))
        cnt = Counter()
        ans = 0
        left = 0

        for right, char in enumerate(s):
            cnt[char] += 1
            while cnt[char] > 1:
                cnt[s[left]] -= 1
                left += 1
            ans = max(ans , right-left+1)
            
        return ans      
# @lc code=end

