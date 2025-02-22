#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # TC: O(n^2 + n log n)
        # SC: O(1)
        nums.sort()
        ans = []
        for i, num in enumerate(nums):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            left, right = i+1, len(nums)-1
            while left < right:
                total = num + nums[left] + nums[right]

                if total == 0:
                    ans.append([num, nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right]==nums[right-1]:
                        right -= 1
                    right -= 1
                    left += 1
                    
                elif total > 0:
                    right -= 1
                else:
                    left += 1

        return ans
# @lc code=end

