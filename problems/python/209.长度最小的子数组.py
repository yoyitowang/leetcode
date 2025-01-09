#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        l = len(nums)
        res = float('inf')
        total = 0

        while right < l:
            total += nums[right]
            while total >= target:
                res = min(res, right-left+1)
                total -= nums[left]
                left += 1
            right += 1
        
        return res if res != float('inf') else 0
        
# @lc code=end

