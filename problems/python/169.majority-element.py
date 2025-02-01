#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # TC: O(n)
        # SC: O(1)
        cnt = 0
        candidate = None

        for num in nums:
            if cnt == 0:
                candidate = num
                cnt = 1
            elif num == candidate:
                cnt += 1
            else:
                cnt -= 1

        return candidate
# @lc code=end

