#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for start in range(len(nums)):
            if start > 0 and nums[start-1] == nums[start]:
                continue
            left, right = start+1, len(nums)-1
            while left < right:
                _sum = nums[start]+nums[left]+nums[right]
                if _sum == 0:
                    tmp = [nums[start], nums[left], nums[right]]
                    res.append(tmp)
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1

                    left += 1
                    right -= 1
                elif _sum < 0:
                    left += 1
                else:
                    right -= 1

        return res
                
# @lc code=end

