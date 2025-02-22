#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        _nums = set(nums)
        streak = 0
        res = 0

        for num in _nums:
            if (num-1) not in _nums:
                if (num + res) not in _nums:
                    continue
                    
                tmp = num
                streak = 1
                while (tmp+1) in _nums:
                    streak += 1
                    tmp += 1

                res = max(res, streak)
        return res 

# @lc code=end

