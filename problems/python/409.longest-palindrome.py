#
# @lc app=leetcode id=409 lang=python3
#
# [409] Longest Palindrome
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> int:
        # TC: O(n)
        # SC: O(n)
        ht = defaultdict(int)
        cnt = 0
        for char in s:
            ht[char] += 1
            if ht[char] == 2:
                ht[char] = 0
                cnt += 1
        
        res = cnt * 2

        for k, v in ht.items():
            if v >= 1:
                res += 1
                break

        return res     
# @lc code=end

