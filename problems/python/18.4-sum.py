#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#

# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        if (n:=len(nums)) < 4:
            return res
        for i in range(n-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, n-2):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                left, right = j+1, n-1
                s = nums[i] + nums[j]
                if (s >= target and nums[left] > 0) or (s <= target and nums[right] < 0):
                    break
                while left < right:
                    _sum = s + nums[left] + nums[right]
                    if _sum == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left+1]: left += 1
                        while left < right and nums[right] == nums[right-1]: right -= 1
                        left += 1
                        right -= 1
                    elif _sum < target:
                        left += 1
                    else:
                        right -= 1

        return res
        
# @lc code=end

