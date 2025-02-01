#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # TC: O(n)
        # SC: O(n)
        ht = defaultdict(int)
        n = len(nums)
        
        for num in nums:
            ht[num] += 1
            if ht[num] > n/2:
                return num     
# @lc code=end

